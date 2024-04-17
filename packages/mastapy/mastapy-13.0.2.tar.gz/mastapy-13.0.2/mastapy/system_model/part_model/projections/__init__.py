"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2491 import SpecifiedConcentricPartGroupDrawingOrder
    from ._2492 import SpecifiedParallelPartGroupDrawingOrder
else:
    import_structure = {
        "_2491": ["SpecifiedConcentricPartGroupDrawingOrder"],
        "_2492": ["SpecifiedParallelPartGroupDrawingOrder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpecifiedConcentricPartGroupDrawingOrder",
    "SpecifiedParallelPartGroupDrawingOrder",
)
