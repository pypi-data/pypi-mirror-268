"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2573 import GearMaterialExpertSystemMaterialDetails
    from ._2574 import GearMaterialExpertSystemMaterialOptions
else:
    import_structure = {
        "_2573": ["GearMaterialExpertSystemMaterialDetails"],
        "_2574": ["GearMaterialExpertSystemMaterialOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMaterialExpertSystemMaterialDetails",
    "GearMaterialExpertSystemMaterialOptions",
)
