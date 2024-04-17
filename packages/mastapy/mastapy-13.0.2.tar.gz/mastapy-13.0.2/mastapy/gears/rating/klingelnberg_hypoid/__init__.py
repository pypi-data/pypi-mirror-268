"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._411 import KlingelnbergCycloPalloidHypoidGearMeshRating
    from ._412 import KlingelnbergCycloPalloidHypoidGearRating
    from ._413 import KlingelnbergCycloPalloidHypoidGearSetRating
else:
    import_structure = {
        "_411": ["KlingelnbergCycloPalloidHypoidGearMeshRating"],
        "_412": ["KlingelnbergCycloPalloidHypoidGearRating"],
        "_413": ["KlingelnbergCycloPalloidHypoidGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidHypoidGearMeshRating",
    "KlingelnbergCycloPalloidHypoidGearRating",
    "KlingelnbergCycloPalloidHypoidGearSetRating",
)
