import pytest
import pathlib
import shutil
from aind_data_schema.core import rig

from np_aind_metadata import np_codeocean, storage


def _copy_resource_files(
    source: pathlib.Path,
    dest: pathlib.Path,
) -> pathlib.Path:
    """Copies all files from source to dest.
    """
    for file in source.iterdir():
        if file.is_dir():
            dest_dir = dest / file.name
            (dest_dir).mkdir()
            _copy_resource_files(file, dest_dir)
        else:
            shutil.copy2(file, dest / file.name)
    return dest


RESOURCES_DIRECTORY = pathlib.Path("tests") / "resources"


@pytest.mark.onprem
def test_update_session_and_rig(tmp_path) -> None:
    """Runs two tests to ensure order is correct.
    """
    np_codeocean.logger.setLevel("DEBUG")
    # setup temporary test directories
    rig_directory_temp = tmp_path / "rig"
    rig_directory_temp.mkdir()
    rig_directory = _copy_resource_files(
        RESOURCES_DIRECTORY / "rig-directory",
        rig_directory_temp,
    )
    session_directory_0_temp = tmp_path / "session-0"
    session_directory_0_temp.mkdir()
    session_directory_0 = _copy_resource_files(
        RESOURCES_DIRECTORY / "session-directory-0",
        session_directory_0_temp,
    )
    session_directory_1_temp = tmp_path / "session-1"
    session_directory_1_temp.mkdir()
    session_directory_1 = _copy_resource_files(
        RESOURCES_DIRECTORY / "session-directory-1",
        session_directory_1_temp,
    )

    def get_current_rig_model() -> rig.Rig:
        return rig.Rig.model_validate_json(
            storage.get_latest_base_rig(
                rig_directory,
                "dynamic_routing",
                "NP3",
            ).read_text()
        )

    initial_rig_model = get_current_rig_model()

    # Test no update
    np_codeocean.update_session_and_rig(
        session_directory_0,
        rig_directory,
        "dynamic_routing",
    )

    non_updated_rig_model = get_current_rig_model()
    assert initial_rig_model == non_updated_rig_model

    # Test update
    np_codeocean.update_session_and_rig(
        session_directory_1,
        rig_directory,
        "dynamic_routing",
    )

    updated_rig_model = get_current_rig_model()
    assert initial_rig_model != updated_rig_model
