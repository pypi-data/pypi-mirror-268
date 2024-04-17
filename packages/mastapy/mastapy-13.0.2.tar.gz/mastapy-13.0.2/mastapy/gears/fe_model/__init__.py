"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1203 import GearFEModel
    from ._1204 import GearMeshFEModel
    from ._1205 import GearMeshingElementOptions
    from ._1206 import GearSetFEModel
else:
    import_structure = {
        "_1203": ["GearFEModel"],
        "_1204": ["GearMeshFEModel"],
        "_1205": ["GearMeshingElementOptions"],
        "_1206": ["GearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearFEModel",
    "GearMeshFEModel",
    "GearMeshingElementOptions",
    "GearSetFEModel",
)
