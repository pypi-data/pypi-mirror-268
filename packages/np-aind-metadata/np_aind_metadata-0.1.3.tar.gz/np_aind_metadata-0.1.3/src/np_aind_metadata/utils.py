import logging
from pathlib import Path
from typing import Any, Union

from h5py import Dataset, File

logger = logging.getLogger(__name__)


def load_hdf5(h5_path: Path) -> File:
    """Load hdf5 file from path."""
    return File(h5_path, "r")


def extract_hdf5_value(h5_file: File, path: list[str]) -> Union[Any, None]:
    """Extract value from hdf5 file using a path. Path is a list of property
    names that are used to traverse the hdf5 file. A path of length greater
    than 1 is expected to point to a nested property.
    """
    try:
        value = None
        for part in path:
            value = h5_file[part]
    except KeyError as e:
        logger.warning(f"Key not found: {e}")
        return None

    if isinstance(value, Dataset):
        return value[()]
    else:
        return value


def find_replace_or_append(
    iterable: list[Any],
    filters: list[tuple[str, Any]],
    update: Any,
) -> None:
    """Find an item in a list of items that matches the filters and replace it.
    If no item is found, append.
    """
    for idx, obj in enumerate(iterable):
        if all(
            getattr(obj, prop_name, None) == prop_value
            for prop_name, prop_value in filters
        ):
            iterable[idx] = update
            break
    else:
        iterable.append(update)


def fix_allen_path(path: Path) -> Path:
    """Fix Allen path for Windows."""
    if path.parts[0] == "\x07llen":
        logger.debug(f"Fixing Allen path: {path}")
        return Path(r"\\allen", *path.parts[1:])
    return path
