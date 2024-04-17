"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1178 import ConicalGearBiasModification
    from ._1179 import ConicalGearFlankMicroGeometry
    from ._1180 import ConicalGearLeadModification
    from ._1181 import ConicalGearProfileModification
else:
    import_structure = {
        "_1178": ["ConicalGearBiasModification"],
        "_1179": ["ConicalGearFlankMicroGeometry"],
        "_1180": ["ConicalGearLeadModification"],
        "_1181": ["ConicalGearProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBiasModification",
    "ConicalGearFlankMicroGeometry",
    "ConicalGearLeadModification",
    "ConicalGearProfileModification",
)
