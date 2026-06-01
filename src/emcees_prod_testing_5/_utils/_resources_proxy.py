from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `emcees_prod_testing_5.resources` module.

    This is used so that we can lazily import `emcees_prod_testing_5.resources` only when
    needed *and* so that users can just import `emcees_prod_testing_5` and reference `emcees_prod_testing_5.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("emcees_prod_testing_5.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
