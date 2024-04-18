import ast
import pathlib
import shutil
import time

from np_aind_metadata import common


def _path_rig_id_sorter(path: pathlib.Path) -> int:
    """"""
    _, mtime_str = path.stem.split("_")[0].split("-")
    return ast.literal_eval(mtime_str)


def get_project_rig_directory(
    rig_directory: pathlib.Path,
    project_name: str,
) -> pathlib.Path:
    """"""
    project_rig_directory = rig_directory / project_name
    if not project_rig_directory.exists():
        raise Exception(f"Project rig directory not found: {project_rig_directory}")

    return project_rig_directory


def get_latest_base_rig(
    rig_directory: pathlib.Path,
    project_name: str,
    rig_name: common.RigName,
) -> pathlib.Path:
    """"""
    base_rigs = list(
        get_project_rig_directory(rig_directory, project_name).glob(
            f"{rig_name}-*_rig.json"
        )
    )
    if not base_rigs:
        raise Exception(f"No base rig found for {rig_name}")

    sorted_base_rigs = sorted(base_rigs, key=_path_rig_id_sorter)
    return sorted_base_rigs[-1]


def update_base_rig(
    rig_directory: pathlib.Path,
    project_name: str,
    rig_name: common.RigName,
    updated_path: pathlib.Path,
) -> None:
    """"""
    shutil.copy2(
        updated_path,
        get_project_rig_directory(rig_directory, project_name)
        / f"{rig_name}-{int(time.time())}_rig.json",
    )
