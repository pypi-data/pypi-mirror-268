"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._417 import KlingelnbergConicalMeshSingleFlankRating
    from ._418 import KlingelnbergConicalRateableMesh
    from ._419 import KlingelnbergCycloPalloidConicalGearSingleFlankRating
    from ._420 import KlingelnbergCycloPalloidHypoidGearSingleFlankRating
    from ._421 import KlingelnbergCycloPalloidHypoidMeshSingleFlankRating
    from ._422 import KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating
else:
    import_structure = {
        "_417": ["KlingelnbergConicalMeshSingleFlankRating"],
        "_418": ["KlingelnbergConicalRateableMesh"],
        "_419": ["KlingelnbergCycloPalloidConicalGearSingleFlankRating"],
        "_420": ["KlingelnbergCycloPalloidHypoidGearSingleFlankRating"],
        "_421": ["KlingelnbergCycloPalloidHypoidMeshSingleFlankRating"],
        "_422": ["KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergConicalMeshSingleFlankRating",
    "KlingelnbergConicalRateableMesh",
    "KlingelnbergCycloPalloidConicalGearSingleFlankRating",
    "KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
    "KlingelnbergCycloPalloidHypoidMeshSingleFlankRating",
    "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
)
