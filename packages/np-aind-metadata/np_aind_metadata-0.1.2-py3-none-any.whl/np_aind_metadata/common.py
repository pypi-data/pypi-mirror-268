"""Models and controlled language for aind-data-schema devices names.
"""

import datetime
import pathlib
import typing

import pydantic

# COMMON Device names

# GALVO_X = "Galvo x"
# GALVO_Y = "Galvo y"
# LASER_0 = "Laser 0"
# LASER_1 = "Laser 1"
# LASER_ASSEMBLY_0 = "Laser Assembly 0"
# LASER_ASSEMBLY_1 = "Laser Assembly 1"
# CAMERA_0 = "Camera 0"
# CAMERA_1 = "Camera 1"
# CAMERA_2 = "Camera 2"


RigName = typing.Literal["NP0", "NP1", "NP2", "NP3"]


class NeuropixelsETLContext(pydantic.BaseModel):
    """Base Context for Neuropixels ETL."""

    source: pathlib.Path


class DynamicRoutingTaskContext(NeuropixelsETLContext):
    """Context for the DynamicRoutingTask ETL."""


class SyncContext(NeuropixelsETLContext):
    """Context for the Sync ETL."""


class MVRCammeraAlias(pydantic.BaseModel):
    """Alias for the camera name in the MVR file."""

    mvr_name: str
    camera_assembly_name: str


class MVRContext(NeuropixelsETLContext):
    """Context for the MVR ETL."""

    mapping: list[MVRCammeraAlias] = [
        MVRCammeraAlias(mvr_name="Camera 1", camera_assembly_name="Side"),
        MVRCammeraAlias(mvr_name="Camera 2", camera_assembly_name="Eye"),
        MVRCammeraAlias(mvr_name="Camera 3", camera_assembly_name="Front"),
    ]


class ManipulatorInfo(pydantic.BaseModel):

    assembly_name: str
    serial_number: str


class OpenEphysContext(pydantic.BaseModel):
    """Context for the OpenEphys ETL."""

    source: list[pathlib.Path] = []
    manipulators: typing.Optional[list[ManipulatorInfo]] = None
    modification_date: typing.Optional[datetime.date] = None


class DynamicRoutingRigDetails(pydantic.BaseModel):
    """Rig model initialization details."""

    rig_name: str
    mon_computer_name: str
    stim_computer_name: str
    sync_computer_name: str
    room_name: typing.Optional[str] = None
    modification_date: datetime.date
    manipulator_infos: list[ManipulatorInfo] = []


class DynamicRoutingTaskUpdateContext(pydantic.BaseModel):
    """Update Context for the DynamicRoutingTask model."""

    source: typing.Union[pathlib.Path]
    updated: typing.Optional[pathlib.Path] = None
    task_context: typing.Optional[DynamicRoutingTaskContext] = None
    open_ephys_context: typing.Optional[OpenEphysContext] = None
    sync_context: typing.Optional[SyncContext] = None
    mvr_context: typing.Optional[MVRContext] = None
