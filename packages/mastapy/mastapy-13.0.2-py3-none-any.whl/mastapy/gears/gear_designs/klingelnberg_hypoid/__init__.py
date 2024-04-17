"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._981 import KlingelnbergCycloPalloidHypoidGearDesign
    from ._982 import KlingelnbergCycloPalloidHypoidGearMeshDesign
    from ._983 import KlingelnbergCycloPalloidHypoidGearSetDesign
    from ._984 import KlingelnbergCycloPalloidHypoidMeshedGearDesign
else:
    import_structure = {
        "_981": ["KlingelnbergCycloPalloidHypoidGearDesign"],
        "_982": ["KlingelnbergCycloPalloidHypoidGearMeshDesign"],
        "_983": ["KlingelnbergCycloPalloidHypoidGearSetDesign"],
        "_984": ["KlingelnbergCycloPalloidHypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidHypoidGearDesign",
    "KlingelnbergCycloPalloidHypoidGearMeshDesign",
    "KlingelnbergCycloPalloidHypoidGearSetDesign",
    "KlingelnbergCycloPalloidHypoidMeshedGearDesign",
)
