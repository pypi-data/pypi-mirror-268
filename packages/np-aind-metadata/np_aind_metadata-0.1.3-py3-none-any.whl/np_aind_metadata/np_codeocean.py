"""Utilities for interacting with NP Code Ocean."""

import logging
import pathlib
import shutil

from aind_data_schema.core import rig, session

from np_aind_metadata import storage
from np_aind_metadata.np import dynamic_routing_task as dynamic_routing_task_np

logger = logging.getLogger(__name__)


def update_session_and_rig(
    session_directory: pathlib.Path,
    rig_directory: pathlib.Path,
    project_name: str,
) -> None:
    """Update the session and rig metadata in the given directories."""
    try:
        session_path = next(session_directory.glob("**/*session.json"))
    except StopIteration as err:
        raise Exception("No session.json found in directory.") from err
    logger.debug("Scraped session model path: %s" % session_path)
    session_model = session.Session.model_validate_json(session_path.read_text())
    rig_name = session_model.rig_id.split("_")[-2]

    rig_path = storage.get_latest_base_rig(
        rig_directory,
        project_name,
        rig_name,
    )
    logger.debug("Base rig model path: %s" % rig_path)
    original_rig_id = rig.Rig.model_validate_json(rig_path.read_text()).rig_id

    update_context = dynamic_routing_task_np.update_rig_from_session_dir(
        rig_path,
        session_directory,
        output_dir=session_directory,
        include=["open_ephys_context"],
    )
    if not update_context.updated:
        logger.debug("Failed to update rig json. Using current base rig.")
        shutil.copy2(
            rig_path,
            session_directory / "rig.json",
        )
        return

    updated_rig_id = rig.Rig.model_validate_json(
        update_context.updated.read_text()
    ).rig_id

    if original_rig_id != updated_rig_id:
        logger.debug("Rig id updated. Updating session.")
        session_model.rig_id = updated_rig_id
        session_model.write_standard_file(
            session_path.parent,
        )
        logger.debug("Rig json updated. Updating base rig.")
        storage.update_base_rig(
            rig_directory,
            project_name,
            rig_name,
            update_context.updated,
        )
