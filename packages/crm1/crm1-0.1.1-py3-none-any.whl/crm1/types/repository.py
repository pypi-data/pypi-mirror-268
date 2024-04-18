"""Don't import this module directly."""

import warnings
from typing import Optional

import hjson

from .. import spec, utils
from .mod import Mod


class Repository:
    """A repository."""

    address: Optional[str]
    """The address of the repository."""
    data: spec.RRepository
    """The raw data of the repository."""
    timeout: Optional[int]
    """The timeout for fetching the repository data."""

    def __init__(
        self,
        address: Optional[str],
        data: spec.RRepository,
        timeout: Optional[int] = None,
    ):
        """Initializes a repository with an address and data."""
        self.address = address
        self.data = data
        self.timeout = timeout

        if not isinstance(self.address, str):
            raise TypeError("Invalid repository address type", type(address))
        if not isinstance(self.data, spec.RRepository):
            raise TypeError("Invalid repository data type", type(self.data))
        if data.spec_version not in spec.supported_spec_versions:
            raise ValueError(
                "Unsupported repository specification version", data.spec_version
            )
        if not isinstance(self.timeout, int) and timeout is not None:
            raise TypeError("Invalid timeout type", type(timeout))

    def get_mod(self, id_: str) -> Optional[Mod]:
        """Gets a mod by its ID."""
        found_mods = self.get_mods(id_)
        if len(found_mods) == 0:
            return None
        if len(found_mods) > 1:
            warnings.warn(
                "Multiple mods with the same ID. "
                "Use .get_mods() to get all matching mods, not only the first one.",
                UserWarning,
            )
        return found_mods[0]

    def get_mods(self, id_: str) -> list[Mod]:
        """Gets all mods with the same ID."""
        return [Mod(mod) for mod in self.data.mods if mod.id == id_]

    def has_mod(self, id_: str) -> bool:
        """Checks if a mod exists in the repository."""
        return bool(self.get_mods(id_))

    def get_spec(self) -> int:
        """The version of the repository specification."""
        return spec.supported_spec_versions[self.data.spec_version]

    def update(self):
        """Updates the repository data."""
        self.data = utils.fetch_repo_data(self.address)

    @classmethod
    def from_address(cls, address: str, timeout: Optional[int] = None) -> "Repository":
        """Creates a repository from an address."""
        if not isinstance(address, str):
            raise TypeError("Invalid repository address type", type(address))
        return cls(address, utils.fetch_repo_data(address), timeout=timeout)

    @classmethod
    def from_dict(
        cls, address: str, data: dict[str, str], timeout: Optional[int] = None
    ) -> "Repository":
        """Creates a repository from a dictionary."""
        if not isinstance(data, dict):
            raise TypeError("Invalid data type", type(data))
        if not isinstance(address, str):
            raise TypeError("Invalid repository address type", type(address))
        spec_version = data.get("specVersion", 0)
        if spec_version not in spec.supported_spec_versions:
            raise ValueError(
                "Unsupported repository specification version", spec_version
            )
        spec_vx = spec.supported_spec_versions[spec_version]
        return cls(address, spec_vx.RRepository.from_dict(data), timeout=timeout)

    @classmethod
    def from_hjson(
        cls, address: str, raw_hjson: str, timeout: Optional[int] = None
    ) -> "Repository":
        """Creates a repository from HJSON."""
        data = hjson.loads(raw_hjson)
        return cls.from_dict(address, data, timeout=timeout)
