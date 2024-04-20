import io
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Union

from pydantic import FilePath

from ..across.resolve import ACROSSResolveName
from ..base.common import ACROSSBase
from .constants import MISSION
from .schema import (
    BurstCubeTOOGetSchema,
    BurstCubeTOOPostSchema,
    BurstCubeTOOPutSchema,
    BurstCubeTOORequestsGetSchema,
    BurstCubeTOORequestsSchema,
    BurstCubeTOOSchema,
    BurstCubeTriggerInfo,
    TOOReason,
    TOOStatus,
)


@dataclass
class TOO(ACROSSBase, ACROSSResolveName):
    """
    Class representing a Target of Opportunity (TOO) request.

    Parameters:
    ----------
    api_token: str
        The api_token for login (optional).
    trigger_time : datetime
        The time of the trigger.
    ra : Optional[float]
        The right ascension of the target (optional).
    dec : Optional[float]
        The declination of the target (optional).
    begin : datetime
        The start time of the TOO observation.
    end : datetime
        The end time of the TOO observation.
    exposure : float
        The exposure time for the TOO observation.
    offset : float
        The offset for the TOO observation.
    healpix_filename : Optional[FilePath]
        The healpix filename that represents the object localization for the TOO. This should be a file
        on disk.
    healpix_file : Union[io.BytesIO, io.BufferedReader, None]
        The healpix file handle for the TOO observation, takes a file like object.
    trigger_info : BurstCubeTriggerInfo
        The trigger information for the TOO observation.
    too_info : str
        The information about the TOO observation.
    status : str
        The status of the TOO request.
    id : id
        The ID of the TOO request.


    Attributes:
    ----------
    created_on : datetime
        The time at which the TOO request was made.
    created_by : str
        The user who made the TOO request.
    modified_on : datetime
        The time at which the TOO request was last modified.
    modified_by : str
        The user who modified the TOO request.
    reject_reason : str
        The reason for the TOO request being rejected.
    status : str
        The status of the TOO request.
    too_info : str
        The information about the TOO request.
    id : str
        The ID of the TOO request.
    """

    api_token: Optional[str] = None
    id: Optional[int] = None
    trigger_time: Optional[datetime] = None
    created_by: Optional[str] = None
    created_on: Optional[datetime] = None
    modified_by: Optional[str] = None
    modified_on: Optional[datetime] = None
    trigger_info: BurstCubeTriggerInfo = field(default_factory=BurstCubeTriggerInfo)
    exposure: float = 200
    offset: float = -50
    too_info: str = ""
    ra: Optional[float] = None
    dec: Optional[float] = None
    error_radius: Optional[float] = None
    healpix_filename: Optional[FilePath] = None
    healpix_file: Union[io.BytesIO, io.BufferedReader, None] = None
    reject_reason: TOOReason = TOOReason.none
    status: TOOStatus = TOOStatus.requested
    version: Optional[int] = None

    # API definitions
    _mission = MISSION
    _api_name = "TOO"
    _schema = BurstCubeTOOSchema
    _put_schema = BurstCubeTOOPutSchema
    _post_schema = BurstCubeTOOPostSchema
    _get_schema = BurstCubeTOOGetSchema
    _del_schema = BurstCubeTOOGetSchema

    @classmethod
    def submit_too(cls, **kwargs):
        """
        Submit a TOO request.
        """
        for k, a in kwargs.items():
            if k in cls._post_schema.model_fields.keys():
                setattr(cls, k, a)

        if cls.validate_post():
            cls.post()

    @property
    def _table(self):
        return (
            [
                "TOO ID",
                "Submitted",
                "Submitter",
                "Trigger Time",
                "Mission",
                "Instrument",
                "ID",
                "Status",
                "Reason",
            ],
            [
                [
                    self.id,
                    self.created_on,
                    self.created_by,
                    self.trigger_time,
                    self.trigger_info.trigger_mission,
                    self.trigger_info.trigger_instrument,
                    self.trigger_info.trigger_id,
                    self.status.value,
                    self.reject_reason.value,
                ]
            ],
        )


class TOORequests(ACROSSBase):
    """
    Represents a Targer of Opportunity (TOO) request.

    Attributes
    ----------
    begin : datetime
        The start time of the observation.
    end : datetime
        The end time of the observation.
    limit : int
        The maximum number of entries for the observation.
    trigger_time : datetime
        The time at which the observation should be triggered.
    entries : list
        The list of entries for the observation.
    """

    _mission = MISSION
    _api_name = "TOO"
    _schema = BurstCubeTOORequestsSchema
    _get_schema = BurstCubeTOORequestsGetSchema

    def __init__(self, **kwargs):
        self.entries = []
        self.begin = None
        self.end = None
        self.limit = None
        for k, a in kwargs.items():
            if k in self._get_schema.model_fields.keys():
                setattr(self, k, a)

        # As this is a GET only class, we can validate and get the data
        if self.validate_get():
            self.get()

        # Convert the entries to a list of TOO objects
        self.entries = [TOO(**entry.__dict__) for entry in self.entries]

    def by_id(self, id):
        """
        Get a TOO request by ID.
        """
        for entry in self.entries:
            if entry.id == id:
                return entry

    @property
    def _table(self):
        return (
            [
                "TOO ID",
                "Submitted",
                "Submitter",
                "Trigger Time",
                "Mission",
                "Instrument",
                "ID",
                "Status",
                "Reason",
            ],
            [
                [
                    entry.id,
                    entry.created_on,
                    entry.created_by,
                    entry.trigger_time,
                    entry.trigger_info.trigger_mission,
                    entry.trigger_info.trigger_instrument,
                    entry.trigger_info.trigger_id,
                    entry.status.value,
                    entry.reject_reason.value,
                ]
                for entry in self.entries
            ],
        )


# Alias
BurstCubeTOO = TOO
BurstCubeTOORequests = TOORequests
submit_too = TOO.submit_too
burstcube_submit_too = TOO.submit_too
