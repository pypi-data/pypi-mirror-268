"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._408 import KlingelnbergCycloPalloidSpiralBevelGearMeshRating
    from ._409 import KlingelnbergCycloPalloidSpiralBevelGearRating
    from ._410 import KlingelnbergCycloPalloidSpiralBevelGearSetRating
else:
    import_structure = {
        "_408": ["KlingelnbergCycloPalloidSpiralBevelGearMeshRating"],
        "_409": ["KlingelnbergCycloPalloidSpiralBevelGearRating"],
        "_410": ["KlingelnbergCycloPalloidSpiralBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
    "KlingelnbergCycloPalloidSpiralBevelGearRating",
    "KlingelnbergCycloPalloidSpiralBevelGearSetRating",
)
