from datetime import datetime
from typing import Any, Optional

from astropy.coordinates import SkyCoord  # type: ignore
from pydantic import BaseModel, ConfigDict, Field, model_validator

from ..functions import convert_to_dt  # type: ignore
from .coords import coord_convert  # type: ignore


class BaseSchema(BaseModel):
    """Base schema for all other schemas"""

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    @property
    def _table(self):
        """Get the table representation of the schema"""
        header = self.model_fields.keys()
        return list(header), [list(self.model_dump().values())]


class CoordSchema(BaseSchema):
    """Schema that defines basic RA/Dec"""

    ra: float = Field(ge=0, lt=360)
    dec: float = Field(ge=-90, le=90)

    @model_validator(mode="before")
    @classmethod
    def convert_coord(cls, data: Any) -> Any:
        """Convert the coordinate data to a specific format"""
        if isinstance(data, dict):
            for key in data.keys():
                if key == "ra" or key == "dec":
                    data[key] = coord_convert(data[key])
        else:
            data.ra = coord_convert(data.ra)
            data.dec = coord_convert(data.dec)
        return data

    @property
    def skycoord(self) -> SkyCoord:
        """Get the SkyCoord representation of the coordinates"""
        return SkyCoord(self.ra, self.dec, unit="deg")


class OptionalCoordSchema(BaseSchema):
    """Schema that defines optional RA/Dec"""

    ra: Optional[float] = Field(ge=0, lt=360, default=None)
    dec: Optional[float] = Field(ge=-90, le=90, default=None)

    @model_validator(mode="before")
    @classmethod
    def coord_convert(cls, data: Any) -> Any:
        """Convert the coordinate data to a specific format"""
        if isinstance(data, dict):
            for key in data.keys():
                if key == "ra" or key == "dec":
                    data[key] = coord_convert(data[key])
        elif hasattr(data, "ra") and hasattr(data, "dec"):
            data.ra = coord_convert(data.ra)
            data.dec = coord_convert(data.dec)
        return data

    @model_validator(mode="after")
    @classmethod
    def check_ra_dec(cls, data: Any) -> Any:
        """Check if RA and Dec are both set or both not set"""
        if data.ra is None or data.dec is None:
            assert data.ra == data.dec, "RA/Dec should both be set, or both not set"
        return data

    @property
    def skycoord(self) -> Optional[SkyCoord]:
        """Get the SkyCoord representation of the coordinates"""
        if self.ra is not None and self.dec is not None:
            return SkyCoord(self.ra, self.dec, unit="deg")
        return None


class OptionalPositionSchema(OptionalCoordSchema):
    """Schema that defines position with error"""

    error_radius: Optional[float] = None


class DateRangeSchema(BaseSchema):
    """Schema that defines date range"""

    begin: datetime
    end: datetime

    @model_validator(mode="before")
    @classmethod
    def convert_date(cls, data: Any) -> datetime:
        """Check if the begin and end dates are both set or both not set"""
        if isinstance(data, dict):
            for key in data.keys():
                if key == "begin" or key == "end":
                    data[key] = convert_to_dt(data[key])
        else:
            data.begin = convert_to_dt(data.begin)
            data.end = convert_to_dt(data.end)
        return data

    @model_validator(mode="after")
    @classmethod
    def check_dates(cls, data: Any) -> Any:
        """Check if the begin and end dates are both set or both not set"""
        assert data.begin <= data.end, "End date should not be before begin."

        return data


class OptionalDateRangeSchema(BaseSchema):
    """Schema that defines optional date range"""

    begin: Optional[datetime] = None
    end: Optional[datetime] = None

    @model_validator(mode="before")
    @classmethod
    def convert_date(cls, data: Any) -> datetime:
        """Check if the begin and end dates are both set or both not set"""
        if isinstance(data, dict):
            for key in data.keys():
                if key == "begin" or key == "end":
                    data[key] = convert_to_dt(data[key])
        else:
            data.begin = convert_to_dt(data.begin)
            data.end = convert_to_dt(data.end)
        return data

    @model_validator(mode="after")
    @classmethod
    def check_dates(cls, data: Any) -> Any:
        """Check if the begin and end dates are both set or both not set"""
        if data.begin is None or data.end is None:
            assert (
                data.begin == data.end
            ), "Begin/End should both be set, or both not set."
        if data.begin is not None and data.end is not None:
            assert data.begin <= data.end, "End date should not be before begin."

        return data
