from datetime import datetime
from typing import Optional


class ACROSSDateRange:
    """
    Represents a date range in the ACROSS API.

    Parameters
    ----------
    begin : datetime
        The start date of the range.
    end : Optional[datetime], optional
        The end date of the range.

    Attributes
    ----------
    begin : datetime
        The start date of the range.
    end : Optional[datetime]
        The end date of the range.
    _length : Union[float, timedelta, str, None]
        The length of the date range.

    Properties
    ----------
    length : Union[float, timedelta, str, None]
        The length of the date range.

    Methods
    -------
    None
    """

    begin: datetime
    end: Optional[datetime]
