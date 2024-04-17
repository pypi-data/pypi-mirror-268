"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._541 import ConicalGearDutyCycleRating
    from ._542 import ConicalGearMeshRating
    from ._543 import ConicalGearRating
    from ._544 import ConicalGearSetDutyCycleRating
    from ._545 import ConicalGearSetRating
    from ._546 import ConicalGearSingleFlankRating
    from ._547 import ConicalMeshDutyCycleRating
    from ._548 import ConicalMeshedGearRating
    from ._549 import ConicalMeshSingleFlankRating
    from ._550 import ConicalRateableMesh
else:
    import_structure = {
        "_541": ["ConicalGearDutyCycleRating"],
        "_542": ["ConicalGearMeshRating"],
        "_543": ["ConicalGearRating"],
        "_544": ["ConicalGearSetDutyCycleRating"],
        "_545": ["ConicalGearSetRating"],
        "_546": ["ConicalGearSingleFlankRating"],
        "_547": ["ConicalMeshDutyCycleRating"],
        "_548": ["ConicalMeshedGearRating"],
        "_549": ["ConicalMeshSingleFlankRating"],
        "_550": ["ConicalRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearDutyCycleRating",
    "ConicalGearMeshRating",
    "ConicalGearRating",
    "ConicalGearSetDutyCycleRating",
    "ConicalGearSetRating",
    "ConicalGearSingleFlankRating",
    "ConicalMeshDutyCycleRating",
    "ConicalMeshedGearRating",
    "ConicalMeshSingleFlankRating",
    "ConicalRateableMesh",
)
