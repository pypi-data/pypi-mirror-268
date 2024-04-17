"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._398 import StraightBevelGearMeshRating
    from ._399 import StraightBevelGearRating
    from ._400 import StraightBevelGearSetRating
else:
    import_structure = {
        "_398": ["StraightBevelGearMeshRating"],
        "_399": ["StraightBevelGearRating"],
        "_400": ["StraightBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelGearMeshRating",
    "StraightBevelGearRating",
    "StraightBevelGearSetRating",
)
