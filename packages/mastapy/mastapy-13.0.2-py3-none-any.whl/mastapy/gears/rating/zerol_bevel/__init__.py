"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._372 import ZerolBevelGearMeshRating
    from ._373 import ZerolBevelGearRating
    from ._374 import ZerolBevelGearSetRating
else:
    import_structure = {
        "_372": ["ZerolBevelGearMeshRating"],
        "_373": ["ZerolBevelGearRating"],
        "_374": ["ZerolBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ZerolBevelGearMeshRating",
    "ZerolBevelGearRating",
    "ZerolBevelGearSetRating",
)
