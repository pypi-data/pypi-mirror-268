from typing import Optional, Union

from astropy.coordinates import SkyCoord  # type: ignore
from astropy.coordinates import Latitude, Longitude  # type: ignore
from astropy.units import Quantity, deg  # type: ignore


def coord_convert(
    coord: Union[float, int, str, Quantity, Longitude, None],
) -> Optional[float]:
    """Convert coordinates of various types either string, integer,
    astropy Longitude or astropy "deg" unit, to a float.

    Parameters
    ----------
    coord : Union[float, str, int, Quantity, Longitude, None]
        Coordinate in one of the types

    Returns
    -------
    float | None
        Coordinate expressed as a float. Just pass through a None.
    """
    if coord is None:
        return None
    if type(coord) is Quantity:
        return coord.to(deg).value
    if type(coord) is Longitude or type(coord) is Latitude:
        return coord.value
    # Universal translator
    return float(coord)


class ACROSSSkyCoord:
    ra: float
    dec: float

    @property
    def skycoord(self) -> SkyCoord:
        """Returns a string representation of the skycoord."""
        if self.ra is None or self.dec is None:
            return None
        else:
            return SkyCoord(self.ra, self.dec, unit="deg")

    @skycoord.setter
    def skycoord(self, coord: SkyCoord):
        """Sets the ra and dec from a SkyCoord."""
        self.ra = coord.icrs.ra.deg
        self.dec = coord.icrs.dec.deg
