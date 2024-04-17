"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._726 import CutterShapeDefinition
    from ._727 import CylindricalGearFormedWheelGrinderTangible
    from ._728 import CylindricalGearHobShape
    from ._729 import CylindricalGearShaperTangible
    from ._730 import CylindricalGearShaverTangible
    from ._731 import CylindricalGearWormGrinderShape
    from ._732 import NamedPoint
    from ._733 import RackShape
else:
    import_structure = {
        "_726": ["CutterShapeDefinition"],
        "_727": ["CylindricalGearFormedWheelGrinderTangible"],
        "_728": ["CylindricalGearHobShape"],
        "_729": ["CylindricalGearShaperTangible"],
        "_730": ["CylindricalGearShaverTangible"],
        "_731": ["CylindricalGearWormGrinderShape"],
        "_732": ["NamedPoint"],
        "_733": ["RackShape"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterShapeDefinition",
    "CylindricalGearFormedWheelGrinderTangible",
    "CylindricalGearHobShape",
    "CylindricalGearShaperTangible",
    "CylindricalGearShaverTangible",
    "CylindricalGearWormGrinderShape",
    "NamedPoint",
    "RackShape",
)
