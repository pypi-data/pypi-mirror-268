"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1207 import CylindricalGearFEModel
    from ._1208 import CylindricalGearMeshFEModel
    from ._1209 import CylindricalGearSetFEModel
else:
    import_structure = {
        "_1207": ["CylindricalGearFEModel"],
        "_1208": ["CylindricalGearMeshFEModel"],
        "_1209": ["CylindricalGearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearFEModel",
    "CylindricalGearMeshFEModel",
    "CylindricalGearSetFEModel",
)
