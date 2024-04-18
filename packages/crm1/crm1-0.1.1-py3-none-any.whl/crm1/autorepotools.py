"""Don't import this module directly."""

from typing import Optional

import requests

from .types import Repository

AUTOREPO_URL = "https://crm-repo.jojojux.de"


def get_all_repos(timeout: Optional[int] = None) -> list[Repository]:
    """Fetches all known repositories from the autorepo server."""
    address = f"{AUTOREPO_URL}/repo_mapping.json"
    response = requests.get(address, timeout=timeout).json()
    return [
        Repository.from_address(repo_address)
        for repo_address in response["repos"].values()
    ]
