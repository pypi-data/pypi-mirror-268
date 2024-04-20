import re
import warnings
from datetime import date, datetime, timedelta, timezone
from typing import Optional, Union

import astropy.units as u  # type: ignore
import numpy as np
from astropy.time import Time, TimeDelta  # type: ignore
from astropy.units import Quantity
from dateutil import parser


def tablefy(table: list, header: Optional[list] = None) -> str:
    """Simple HTML table generator

    Parameters
    ----------
    table : list
        Data for table
    header : list, optional
        Headers for table, by default None

    Returns
    -------
    str
        HTML formatted table.
    """

    tab = "<table>"
    if header is not None:
        tab += "<thead>"
        tab += "".join(
            [f"<th style='text-align: left;'>{head}</th>" for head in header]
        )
        tab += "</thead>"

    for row in table:
        tab += "<tr>"
        # Replace any carriage returns with <br>
        row = [f"{col}".replace("\n", "<br>") for col in row]
        tab += "".join([f"<td style='text-align: left;'>{col}</td>" for col in row])
        tab += "</tr>"
    tab += "</table>"
    return tab


# Regex for matching date, time and datetime strings
DATE_REGEX = r"^[0-2]\d{3}-(0?[1-9]|1[012])-([0][1-9]|[1-2][0-9]|3[0-1])?$"
ISO8601_REGEX = r"^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$"
DATETIME_REGEX = r"^[0-2]\d{3}-(0?[1-9]|1[012])-([0][1-9]|[1-2][0-9]|3[0-1])[\sT]([0-9]:|[0-1][0-9]:|2[0-3]:)[0-5][0-9]:[0-5][0-9]+(\.\d+)?$"


def convert_timedelta(
    length: Union[str, float, timedelta, TimeDelta, Quantity, None], units=u.day
) -> timedelta:
    """Convert various timedelta formats to swiftdatetime or datetime

    Parameters
    ----------
    length : Union[str, float, timedelta, TimeDelta, Quantity, None]
        Value to be converted.
    units : astropy.units.Quantity, optional
        Unit to use if float/int given. Default is days.

    Returns
    -------
    datetime.timedelta
        Returned timedelta object.

    Raises
    ------
    TypeError
        Raised if incorrect format is given for conversion.
    """

    if units == u.day:
        divisor = 86400.0
    else:
        divisor = 1.0
    if type(length) is Quantity:
        length = length.to(u.day).value
    elif type(length) is timedelta:
        length = length.total_seconds() / divisor
    elif type(length) is TimeDelta:
        length = length.to_datetime().total_seconds() / divisor  # type: ignore
    else:
        try:
            length = float(length)  # type: ignore
        except ValueError:
            raise TypeError(
                f"Length of time should be given as a datetime.timedelta, astropy TimeDelta, astropy quantity or as a number of {units}"
            )
    return timedelta(days=length)  # type: ignore


def convert_to_dt(value: Union[str, date, datetime, Time]) -> Optional[datetime]:
    """Convert various date formats to datetime

    Parameters
    ----------
    value : Union[str, date, datetime, Time]
        Value to be converted.

    Returns
    -------
    datetime.datetime
        Returned datetime object.

    Raises
    ------
    TypeError
        Raised if incorrect format is given for conversion.
    """
    if value is None:
        return None

    if isinstance(value, (str, np.str_)):
        if re.match(DATETIME_REGEX, value):
            # Remove the rogue T in 2023-10-17T00:00:00 style strings
            value = value.replace("T", " ")
            # Figure out if we have decimal places
            if "." in value:
                # Do this because "fromisoformat" is restricted to 0, 3 or 6
                # decimal plaaces
                dtvalue = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
            else:
                dtvalue = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        elif re.match(DATE_REGEX, value):
            dtvalue = datetime.strptime(f"{value} 00:00:00", "%Y-%m-%d %H:%M:%S")
        elif re.match(ISO8601_REGEX, value):
            dtvalue = parser.parse(value)
            if dtvalue.tzinfo is None:
                warnings.warn(
                    "ISO8601 formatted dates should be supplied with timezone. ISO8601 dates with no timezone will be assumed to be localtime and then converted to UTC."
                )
            dtvalue = dtvalue.astimezone(timezone.utc).replace(tzinfo=None)
        else:
            raise ValueError(
                "Date/time given as string should 'YYYY-MM-DD HH:MM:SS' or ISO8601 format."
            )
    elif type(value) is date:
        dtvalue = datetime.strptime(f"{value} 00:00:00", "%Y-%m-%d %H:%M:%S")
    elif type(value) is datetime:
        if value.tzinfo is not None:
            # Strip out timezone info and convert to UTC
            value = value.astimezone(timezone.utc).replace(tzinfo=None)
        dtvalue = value  # Just pass through un molested
    elif type(value) is Time:
        dtvalue = value.datetime
    else:
        raise TypeError(
            'DateTime should be given as a datetime, astropy Time, or as string of format "YYYY-MM-DD HH:MM:SS"'
        )

    return dtvalue
