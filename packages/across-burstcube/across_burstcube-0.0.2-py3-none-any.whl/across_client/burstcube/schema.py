from datetime import datetime
from enum import Enum
from io import IOBase
from typing import List, Optional

from pydantic import ConfigDict  # type: ignore

from ..base.schema import BaseSchema, OptionalDateRangeSchema, OptionalPositionSchema


class TOOReason(str, Enum):
    """
    Reasons for rejecting TOO observations

    Attributes
    ----------
    saa
        In SAA
    earth_occult
        Earth occulted
    moon_occult
        Moon occulted
    sun_occult
        Sun occulted
    too_old
        Too old
    other
        Other
    none
        None
    """

    saa = "In SAA"
    earth_occult = "Earth occulted"
    moon_occult = "Moon occulted"
    sun_occult = "Sun occulted"
    too_old = "Too old"
    other = "Other"
    none = "None"


class TOOStatus(str, Enum):
    """
    Enumeration class representing the status of a Target of Opportunity (TOO) request.

    Attributes:
    requested
        The TOO request has been submitted.
    rejected
        The TOO request has been rejected.
    declined
        The TOO request has been declined.
    approved
        The TOO request has been approved.
    executed
        The TOO request has been executed.
    other
        The TOO request has a status other than the predefined ones.
    """

    requested = "Requested"
    rejected = "Rejected"
    declined = "Declined"
    approved = "Approved"
    executed = "Executed"
    deleted = "Deleted"
    other = "Other"


class BurstCubeTriggerInfo(BaseSchema):
    """
    Metadata schema for the BurstCube Target of Opportunity (TOO) request. Note
    that this schema is not strictly defined, keys are only suggested, and
    additional keys can be added as needed.
    """

    trigger_name: Optional[str] = None
    trigger_mission: Optional[str] = None
    trigger_instrument: Optional[str] = None
    trigger_id: Optional[str] = None
    trigger_duration: Optional[float] = None
    classification: Optional[str] = None
    justification: Optional[str] = None

    model_config = ConfigDict(extra="allow")


class BurstCubeTOOSchema(OptionalPositionSchema):
    """
    Schema describing a BurstCube TOO Request.
    """

    id: Optional[int] = None
    created_by: str
    created_on: datetime
    modified_by: Optional[str] = None
    modified_on: Optional[datetime] = None
    trigger_time: datetime
    trigger_info: BurstCubeTriggerInfo
    exposure: int
    offset: int
    reject_reason: TOOReason = TOOReason.none
    status: TOOStatus = TOOStatus.requested
    too_info: str = ""
    healpix_filename: Optional[str] = None
    version: int


class BurstCubeTOODelSchema(BaseSchema):
    """
    Schema for BurstCubeTOO DELETE API call.

    Attributes
    ----------
    id
        The ID of the BurstCubeTOODel object.
    """

    id: int


class BurstCubeTOOPostSchema(OptionalPositionSchema):
    """
    Schema to submit a TOO request for BurstCube.
    """

    trigger_time: datetime
    trigger_info: BurstCubeTriggerInfo
    exposure: int = 200
    offset: int = -50
    healpix_file: Optional[IOBase] = None


class BurstCubeTOOGetSchema(BaseSchema):
    """
    Schema for BurstCubeTOO GET request.
    """

    id: int


class BurstCubeTOOPutSchema(BurstCubeTOOPostSchema):
    """
    Schema for BurstCubeTOO PUT request.
    """

    id: int
    trigger_time: datetime
    trigger_info: BurstCubeTriggerInfo
    exposure: int = 200
    offset: int = -50
    status: TOOStatus
    healpix_file: Optional[IOBase] = None


class BurstCubeTOORequestsGetSchema(OptionalDateRangeSchema):
    """
    Schema for GET requests to retrieve BurstCube Target of Opportunity (TOO) requests.
    """

    duration: Optional[float] = None
    limit: Optional[int] = None
    offset: Optional[int] = None


class BurstCubeTOORequestsSchema(BaseSchema):
    """
    Schema for BurstCube TOO requests.
    """

    entries: List[BurstCubeTOOSchema]
