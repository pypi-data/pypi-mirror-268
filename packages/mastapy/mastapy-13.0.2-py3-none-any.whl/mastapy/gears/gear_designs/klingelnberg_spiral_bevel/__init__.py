"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._977 import KlingelnbergCycloPalloidSpiralBevelGearDesign
    from ._978 import KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
    from ._979 import KlingelnbergCycloPalloidSpiralBevelGearSetDesign
    from ._980 import KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_977": ["KlingelnbergCycloPalloidSpiralBevelGearDesign"],
        "_978": ["KlingelnbergCycloPalloidSpiralBevelGearMeshDesign"],
        "_979": ["KlingelnbergCycloPalloidSpiralBevelGearSetDesign"],
        "_980": ["KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearSetDesign",
    "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
)
