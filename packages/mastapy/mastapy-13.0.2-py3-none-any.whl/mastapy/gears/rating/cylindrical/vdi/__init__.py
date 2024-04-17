"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._492 import VDI2737InternalGearSingleFlankRating
else:
    import_structure = {
        "_492": ["VDI2737InternalGearSingleFlankRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = ("VDI2737InternalGearSingleFlankRating",)
