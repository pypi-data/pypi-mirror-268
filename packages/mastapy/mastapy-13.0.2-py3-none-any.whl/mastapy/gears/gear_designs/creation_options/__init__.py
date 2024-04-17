"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1152 import CylindricalGearPairCreationOptions
    from ._1153 import GearSetCreationOptions
    from ._1154 import HypoidGearSetCreationOptions
    from ._1155 import SpiralBevelGearSetCreationOptions
else:
    import_structure = {
        "_1152": ["CylindricalGearPairCreationOptions"],
        "_1153": ["GearSetCreationOptions"],
        "_1154": ["HypoidGearSetCreationOptions"],
        "_1155": ["SpiralBevelGearSetCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearPairCreationOptions",
    "GearSetCreationOptions",
    "HypoidGearSetCreationOptions",
    "SpiralBevelGearSetCreationOptions",
)
