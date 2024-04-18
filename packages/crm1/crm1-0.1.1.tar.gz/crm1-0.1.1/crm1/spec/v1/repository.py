"""Don't import this module directly."""

from dataclasses import dataclass

from dataclasses_hjson import DataClassHjsonMixin

from .mod import RMod


@dataclass
class RRepository(DataClassHjsonMixin):
    """Raw repository data. This is used for deserialization."""

    last_updated: int
    """The timestamp of the last update of the repository."""
    root_id: str
    """The root ID of the repository."""
    mods: list[RMod]
    """A list of mods in the repository."""
    spec_version: int = 1
    """The version of the repository specification."""
