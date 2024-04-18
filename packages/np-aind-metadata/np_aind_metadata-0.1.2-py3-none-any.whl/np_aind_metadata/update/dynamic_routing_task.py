import datetime
import json
import logging
import pathlib
import shutil
import tempfile
import typing

from aind_data_schema.core import rig
from aind_metadata_mapper.neuropixels import (
    mvr_rig,
    neuropixels_rig,
    open_ephys_rig,
    sync_rig,
)

from np_aind_metadata import common
from np_aind_metadata.update.dynamic_routing_task_etl import DynamicRoutingTaskRigEtl

logger = logging.getLogger(__name__)


def _run_neuropixels_rig_etl(
    etl_class: neuropixels_rig.NeuropixelsRigEtl,
    input_source: rig.Rig,
    output_dir: pathlib.Path,
    *etl_args,
    **etl_kwargs,
) -> pathlib.Path:
    """Utility for running a neuropixels rig ETL and continuing on error."""
    try:
        etl = etl_class(input_source, output_dir, *etl_args, **etl_kwargs)
        etl.run_job()
        return output_dir / "rig.json"
    except Exception:
        logger.debug("Error calling: %s" % etl_class, exc_info=True)
        return input_source


# cannot type hint due to np import failing in github actions
def scrape_update_context(
    path: pathlib.Path,
    context: common.DynamicRoutingTaskUpdateContext,
    manipulators: typing.Optional[list[common.ManipulatorInfo]] = None,
) -> common.DynamicRoutingTaskUpdateContext:
    """Scrapes the given directory for relevant files and updates
    UpdateContext.
    """
    # dr task
    try:
        task_source = next(path.glob("**/Dynamic*.hdf5"))
        context.task_context = common.DynamicRoutingTaskContext(
            source=task_source,
        )
    except StopIteration:
        logger.debug("No task output found.")

    # sync
    try:
        sync_source = next(path.glob("**/sync.yml"))
        context.sync_context = common.SyncContext(
            source=sync_source,
        )
    except StopIteration:
        logger.debug("No sync config found.")

    # mvr
    try:
        mvr_source = next(path.glob("**/mvr.ini"))
        context.mvr_context = common.MVRContext(
            source=mvr_source,
        )
    except StopIteration:
        logger.debug("No mvr config found.")

    # open ephys
    settings_sources = list(path.glob("**/settings.xml"))
    if len(settings_sources) < 1:
        logger.debug("No open ephys settings found.")

    context.open_ephys_context = common.OpenEphysContext(
        source=settings_sources,
        manipulators=manipulators,
    )

    return context


def update_rig(
    context: common.DynamicRoutingTaskUpdateContext,
    output_path: pathlib.Path = pathlib.Path("rig.json"),
    modification_date: typing.Optional[datetime.date] = None,
    include: typing.Optional[list[str]] = None,
) -> common.DynamicRoutingTaskUpdateContext:
    """Generates a new rig json file with the metadata from the given sources.

    Notes
    -----
    - If rig_source is None, the rig will be initialized with the default
     values.
    - *_source, if present will update various values in the rig model.
    """
    # build model in a temporary directory
    build_dir = pathlib.Path(tempfile.mkdtemp())
    build_source = build_dir / "rig.json"
    shutil.copy(context.source, build_source)
    if include:
        logger.debug("Including only: %s" % json.dumps(include))
        context = common.DynamicRoutingTaskUpdateContext(
            source=context.source, **{k: getattr(context, k) for k in include}
        )
        logger.debug("Updated context: %s" % context.model_dump_json())

    rig_model = rig.Rig.model_validate_json(build_source.read_text())

    if context.task_context:
        logger.debug("Updating rig model with dynamic routing task context.")
        _run_neuropixels_rig_etl(
            DynamicRoutingTaskRigEtl,
            build_source,
            build_dir,
            task_source=context.task_context.source,
            sound_calibration_date=rig_model.modification_date,
            reward_calibration_date=rig_model.modification_date,
        )

    if context.open_ephys_context:
        logger.debug("Updating rig model with open ephys context.")
        if context.open_ephys_context.manipulators:
            manipulators = [
                (
                    m.assembly_name,
                    m.serial_number,
                )
                for m in context.open_ephys_context.manipulators
            ]
        else:
            manipulators = []
        _run_neuropixels_rig_etl(
            open_ephys_rig.OpenEphysRigEtl,
            build_source,
            build_dir,
            open_ephys_settings_sources=context.open_ephys_context.source,
            probe_manipulator_serial_numbers=manipulators,
            modification_date=modification_date,
        )

    if context.sync_context:
        logger.debug("Updating rig model with sync source file.")
        _run_neuropixels_rig_etl(
            sync_rig.SyncRigEtl,
            build_source,
            build_dir,
            config_source=context.sync_context.source,
        )

    if context.mvr_context:
        logger.debug("Updating rig model with mvr source file.")
        if context.mvr_context.mapping:
            camera_aliases = {
                m.mvr_name: m.camera_assembly_name for m in context.mvr_context.mapping
            }
        else:
            camera_aliases = None
        _run_neuropixels_rig_etl(
            mvr_rig.MvrRigEtl,
            build_source,
            build_dir,
            mvr_config_source=context.mvr_context.source,
            mvr_mapping=camera_aliases,
        )

    shutil.copy2(build_source, output_path)
    context.updated = output_path
    return context


if __name__ == "__main__":
    import doctest

    doctest.testmod(
        optionflags=(doctest.IGNORE_EXCEPTION_DETAIL | doctest.NORMALIZE_WHITESPACE)
    )
