"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._405 import SpiralBevelGearMeshRating
    from ._406 import SpiralBevelGearRating
    from ._407 import SpiralBevelGearSetRating
else:
    import_structure = {
        "_405": ["SpiralBevelGearMeshRating"],
        "_406": ["SpiralBevelGearRating"],
        "_407": ["SpiralBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpiralBevelGearMeshRating",
    "SpiralBevelGearRating",
    "SpiralBevelGearSetRating",
)
