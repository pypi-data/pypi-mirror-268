"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1572 import GriddedSurfaceAccessor
    from ._1573 import LookupTableBase
    from ._1574 import OnedimensionalFunctionLookupTable
    from ._1575 import TwodimensionalFunctionLookupTable
else:
    import_structure = {
        "_1572": ["GriddedSurfaceAccessor"],
        "_1573": ["LookupTableBase"],
        "_1574": ["OnedimensionalFunctionLookupTable"],
        "_1575": ["TwodimensionalFunctionLookupTable"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GriddedSurfaceAccessor",
    "LookupTableBase",
    "OnedimensionalFunctionLookupTable",
    "TwodimensionalFunctionLookupTable",
)
