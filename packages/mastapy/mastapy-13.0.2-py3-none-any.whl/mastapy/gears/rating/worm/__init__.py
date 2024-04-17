"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._375 import WormGearDutyCycleRating
    from ._376 import WormGearMeshRating
    from ._377 import WormGearRating
    from ._378 import WormGearSetDutyCycleRating
    from ._379 import WormGearSetRating
    from ._380 import WormMeshDutyCycleRating
else:
    import_structure = {
        "_375": ["WormGearDutyCycleRating"],
        "_376": ["WormGearMeshRating"],
        "_377": ["WormGearRating"],
        "_378": ["WormGearSetDutyCycleRating"],
        "_379": ["WormGearSetRating"],
        "_380": ["WormMeshDutyCycleRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormGearDutyCycleRating",
    "WormGearMeshRating",
    "WormGearRating",
    "WormGearSetDutyCycleRating",
    "WormGearSetRating",
    "WormMeshDutyCycleRating",
)
