"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1495 import LicenceServer
    from ._7580 import LicenceServerDetails
    from ._7581 import ModuleDetails
    from ._7582 import ModuleLicenceStatus
else:
    import_structure = {
        "_1495": ["LicenceServer"],
        "_7580": ["LicenceServerDetails"],
        "_7581": ["ModuleDetails"],
        "_7582": ["ModuleLicenceStatus"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LicenceServer",
    "LicenceServerDetails",
    "ModuleDetails",
    "ModuleLicenceStatus",
)
