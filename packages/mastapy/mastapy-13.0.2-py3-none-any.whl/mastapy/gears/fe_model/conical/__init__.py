"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1210 import ConicalGearFEModel
    from ._1211 import ConicalMeshFEModel
    from ._1212 import ConicalSetFEModel
    from ._1213 import FlankDataSource
else:
    import_structure = {
        "_1210": ["ConicalGearFEModel"],
        "_1211": ["ConicalMeshFEModel"],
        "_1212": ["ConicalSetFEModel"],
        "_1213": ["FlankDataSource"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFEModel",
    "ConicalMeshFEModel",
    "ConicalSetFEModel",
    "FlankDataSource",
)
