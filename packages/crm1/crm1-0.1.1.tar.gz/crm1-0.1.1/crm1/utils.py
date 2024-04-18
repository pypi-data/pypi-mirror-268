"""Don't import this module directly."""

from typing import Optional

import hjson
import requests

from . import spec


def fetch_repo_data(address: str, timeout: Optional[int] = None) -> spec.RRepository:
    """Fetches a repository from the given address."""
    response = requests.get(address, timeout=timeout)
    data = hjson.loads(response.text, object_pairs_hook=dict)
    return get_repo_data_from(data)


def get_repo_data_from(data: dict) -> spec.RRepository:
    """Gets the repository data class for a specific specification version."""
    spec_version = data.get("specVersion", 0)
    if spec_version not in spec.supported_spec_versions:
        raise ValueError("Unsupported repository specification version", spec_version)
    return spec.supported_spec_versions[spec_version].RRepository.from_dict(data)
