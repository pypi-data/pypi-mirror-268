"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2578 import BeltCreationOptions
    from ._2579 import CycloidalAssemblyCreationOptions
    from ._2580 import CylindricalGearLinearTrainCreationOptions
    from ._2581 import PlanetCarrierCreationOptions
    from ._2582 import ShaftCreationOptions
else:
    import_structure = {
        "_2578": ["BeltCreationOptions"],
        "_2579": ["CycloidalAssemblyCreationOptions"],
        "_2580": ["CylindricalGearLinearTrainCreationOptions"],
        "_2581": ["PlanetCarrierCreationOptions"],
        "_2582": ["ShaftCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltCreationOptions",
    "CycloidalAssemblyCreationOptions",
    "CylindricalGearLinearTrainCreationOptions",
    "PlanetCarrierCreationOptions",
    "ShaftCreationOptions",
)
