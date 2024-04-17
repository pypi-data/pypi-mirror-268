"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._414 import KlingelnbergCycloPalloidConicalGearMeshRating
    from ._415 import KlingelnbergCycloPalloidConicalGearRating
    from ._416 import KlingelnbergCycloPalloidConicalGearSetRating
else:
    import_structure = {
        "_414": ["KlingelnbergCycloPalloidConicalGearMeshRating"],
        "_415": ["KlingelnbergCycloPalloidConicalGearRating"],
        "_416": ["KlingelnbergCycloPalloidConicalGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidConicalGearMeshRating",
    "KlingelnbergCycloPalloidConicalGearRating",
    "KlingelnbergCycloPalloidConicalGearSetRating",
)
