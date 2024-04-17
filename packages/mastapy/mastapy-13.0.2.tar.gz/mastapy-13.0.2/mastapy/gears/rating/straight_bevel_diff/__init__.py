"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._401 import StraightBevelDiffGearMeshRating
    from ._402 import StraightBevelDiffGearRating
    from ._403 import StraightBevelDiffGearSetRating
    from ._404 import StraightBevelDiffMeshedGearRating
else:
    import_structure = {
        "_401": ["StraightBevelDiffGearMeshRating"],
        "_402": ["StraightBevelDiffGearRating"],
        "_403": ["StraightBevelDiffGearSetRating"],
        "_404": ["StraightBevelDiffMeshedGearRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelDiffGearMeshRating",
    "StraightBevelDiffGearRating",
    "StraightBevelDiffGearSetRating",
    "StraightBevelDiffMeshedGearRating",
)
