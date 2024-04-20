from datetime import datetime
from typing import Optional

from pydantic import model_validator

from ..base.schema import BaseSchema


class HelloSchema(BaseSchema):
    """
    Schema defining the returned attributes of the  ACROSS API Hello class.
    """

    hello: str


class HelloGetSchema(BaseSchema):
    """
    Schema to validate input parameters of ACROSS API Hello class.
    """

    name: Optional[str] = None


class ResolveSchema(BaseSchema):
    """
    A schema for resolving astronomical coordinates.
    """

    ra: float
    dec: float
    resolver: str


class ResolveGetSchema(BaseSchema):
    """Schema defines required parameters for a GET"""

    name: str


class JobSchema(BaseSchema):
    """Full return of Job Information for ACROSSAPIJobs"""

    jobnumber: Optional[int] = None
    reqtype: str
    apiversion: str
    began: datetime
    created: datetime
    expires: datetime
    params: str
    result: Optional[str] = None
    status: Optional[str] = None


class UserArgSchema(BaseSchema):
    username: Optional[str] = "anonymous"
    api_token: Optional[str] = None

    @model_validator(mode="after")
    def username_requires_api_token(self) -> "UserArgSchema":
        if self.username != "anonymous" and self.api_token is None:
            raise ValueError("api_token required if username is set")
        return self


class ACROSSAPIJobsGetSchema(BaseSchema):
    username: str
    begin: Optional[datetime]
    end: Optional[datetime]
    unexpired_only: bool = True
    reqtype: str
