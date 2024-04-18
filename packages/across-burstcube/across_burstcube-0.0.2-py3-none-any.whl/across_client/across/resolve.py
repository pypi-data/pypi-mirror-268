from typing import Optional

from ..base.common import ACROSSBase
from .schema import ResolveGetSchema, ResolveSchema


class Resolve(ACROSSBase):
    """
    Represents a resolver for resolving celestial object coordinates.

    Attributes
    ----------
    name : Optional[str]
        The name of the celestial object.
    ra : Optional[float]
        The right ascension of the celestial object.
    dec : Optional[float]
        The declination of the celestial object.
    resolver : Optional[str]
        The resolver used for resolving the coordinates.
    """

    # Type hints
    name: Optional[str] = None
    ra: Optional[float] = None
    dec: Optional[float] = None
    resolver: Optional[str] = None

    _mission = "ACROSS"
    _api_name = "Resolve"
    _schema = ResolveSchema
    _get_schema = ResolveGetSchema

    def __init__(self, name: Optional[str] = None, **kwargs):
        self.name = name
        for k, a in kwargs.items():
            setattr(self, k, a)


class ACROSSResolveName:
    """_summary_

    Returns
    -------
    _type_
        _description_
    """

    ra: Optional[float]
    dec: Optional[float]
    _name: str

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, targname: str):
        """Set name

        Parameters
        ----------
        targname : str
            Target name that can be resolved by the Resolve class
        """
        self._name = targname
        if hasattr(self, "ra") is False or self.ra is None:
            r = Resolve(name=targname)
            r.get()
            self.ra = r.ra
            self.dec = r.dec


def resolve(name: str) -> Resolve:
    """Resolve a target name to coordinates

    Parameters
    ----------
    name : str
        Target name that can be resolved by the Resolve class

    Returns
    -------
    Resolve
        A Resolve object with the coordinates of the target
    """
    r = Resolve(name=name)
    r.get()
    return r
