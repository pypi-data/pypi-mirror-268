import ast
import datetime
import logging
import pathlib
import shutil
import tempfile
import typing

from aind_data_schema.core import rig

from np_aind_metadata import common
from np_aind_metadata.init import dynamic_routing_task as dynamic_routing_task_init
from np_aind_metadata.update import dynamic_routing_task as dynamic_routing_task_update

logger = logging.getLogger(__name__)

try:
    import np_config
    import np_session
except Exception:
    logger.error("Failed to import neuropixels-related dependencies.", exc_info=True)


RigName = typing.Literal["NP0", "NP1", "NP2", "NP3"]


def get_rig_room(rig_name: RigName) -> typing.Union[str, None]:
    rig_to_room = {
        "NP0": "325",
        "NP1": "325",
        "NP2": "327",
        "NP3": "342",
    }
    try:
        return rig_to_room[rig_name]
    except KeyError:
        logger.debug("No room found for rig: %s" % rig_name)
        return None


# cannot type hint due to np import failing in github actions
def _get_rig_config(rig_name: RigName):
    return np_config.Rig(ast.literal_eval(rig_name[-1]))


def get_manipulator_infos(
    rig_name: RigName,
) -> list[common.ManipulatorInfo]:
    return [
        common.ManipulatorInfo(
            assembly_name=f"Ephys Assembly {key}",
            serial_number=value,
        )
        for key, value in _get_rig_config(rig_name)
        .config["services"]["NewScaleCoordinateRecorder"]["probe_to_serial_number"]
        .items()
    ]


def is_session_exp_dir(path: pathlib.Path) -> bool:
    try:
        np_session.Session(path.stem)
        return True
    except Exception:
        return False


# cannot type hint due to np import failing in github actions
def init_rig_from_np_config(
    rig_name: RigName,
    modification_date: datetime.date,
    output_directory: pathlib.Path,
) -> pathlib.Path:
    rig_config = _get_rig_config(rig_name)
    rig_details = common.DynamicRoutingRigDetails(
        rig_name=rig_name,
        mon_computer_name=rig_config.Mon,
        stim_computer_name=rig_config.Stim,
        sync_computer_name=rig_config.Sync,
        room_name=get_rig_room(rig_name),
        modification_date=modification_date,
        manipulator_infos=get_manipulator_infos(rig_name),
    )
    return dynamic_routing_task_init.init(rig_details, output_directory)


def _fix_modification_date(prev: pathlib.Path, new: pathlib.Path) -> None:
    """Fixes an unintentional bug introduced with neuropixels etls."""
    prev_rig = rig.Rig.model_validate_json(prev.read_text())
    new_rig = rig.Rig.model_validate_json(new.read_text())
    prev_probe_serial_numbers = [
        ephys_assembly.probes[0].serial_number
        for ephys_assembly in prev_rig.ephys_assemblies
    ]
    new_probe_serial_numbers = [
        ephys_assembly.probes[0].serial_number
        for ephys_assembly in new_rig.ephys_assemblies
    ]
    if prev_probe_serial_numbers != new_probe_serial_numbers:
        logger.debug("Probe serial numbers changed. Not reverting modification date.")
        logger.debug(f"Previous: {prev_probe_serial_numbers}")
        logger.debug(f"New: {new_probe_serial_numbers}")
        return

    logger.debug("Probe serial numbers match.")
    logger.debug("Reverting modification date.")
    with tempfile.TemporaryDirectory() as temp_dir:
        new_rig.rig_id = prev_rig.rig_id
        new_rig.modification_date = prev_rig.modification_date
        new_rig.write_standard_file(temp_dir)
        shutil.copy2(pathlib.Path(temp_dir) / "rig.json", new)


def update_rig_from_session_dir(
    rig_path: pathlib.Path,
    session_dir: pathlib.Path,
    output_dir: pathlib.Path = pathlib.Path("./"),
    include: typing.Optional[list[str]] = None,
) -> common.DynamicRoutingTaskUpdateContext:
    context = common.DynamicRoutingTaskUpdateContext(
        source=rig_path,
    )
    context = dynamic_routing_task_update.scrape_update_context(session_dir, context)
    logger.debug("Scraped context: %s" % context.model_dump_json())
    output_path = output_dir / "rig.json"
    updated = dynamic_routing_task_update.update_rig(
        context,
        output_path=output_path,
        modification_date=datetime.date.today(),
        include=include,
    )
    _fix_modification_date(updated.source, output_path)
    return updated


# using typing.Any due to np_session import failing in github actions
def get_session_dirs(
    npexp_path_root: pathlib.Path,
) -> typing.Generator[pathlib.Path, None, None]:
    for path in np_config.utils.normalize_path(npexp_path_root).iterdir():
        if is_session_exp_dir(path):
            yield path


def get_sorted_session_dirs(
    *session_path_roots: pathlib.Path,
) -> list[pathlib.Path]:
    all_session_dirs = []
    for session_path_root in session_path_roots:
        all_session_dirs.extend(list(get_session_dirs(session_path_root)))

    def get_session_dir_sort_key(path: pathlib.Path) -> datetime.date:
        return np_session.Session(path.stem).date

    return sorted(all_session_dirs, key=get_session_dir_sort_key)
