"""Don't import this module directly."""

from typing import Union

from ..spec import v1, v2

CommonModExt = Union[v1.CommonModExt, v2.CommonModExt]
RDependency = Union[v1.RDependency, v2.RDependency]
RMod = Union[v1.RMod, v2.RMod]
RRepository = Union[v1.RRepository, v2.RRepository]


class __ModuleMockV1:
    CommonModExt = v1.CommonModExt
    RDependency = v1.RDependency
    RMod = v1.RMod
    RRepository = v1.RRepository


class __ModuleMockV2:
    CommonModExt = v2.CommonModExt
    RDependency = v2.RDependency
    RMod = v2.RMod
    RRepository = v2.RRepository


supported_spec_versions: dict[int, Union[__ModuleMockV1, __ModuleMockV2]] = {
    1: v1,
    2: v2,
}
