"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._448 import FaceGearDutyCycleRating
    from ._449 import FaceGearMeshDutyCycleRating
    from ._450 import FaceGearMeshRating
    from ._451 import FaceGearRating
    from ._452 import FaceGearSetDutyCycleRating
    from ._453 import FaceGearSetRating
else:
    import_structure = {
        "_448": ["FaceGearDutyCycleRating"],
        "_449": ["FaceGearMeshDutyCycleRating"],
        "_450": ["FaceGearMeshRating"],
        "_451": ["FaceGearRating"],
        "_452": ["FaceGearSetDutyCycleRating"],
        "_453": ["FaceGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearDutyCycleRating",
    "FaceGearMeshDutyCycleRating",
    "FaceGearMeshRating",
    "FaceGearRating",
    "FaceGearSetDutyCycleRating",
    "FaceGearSetRating",
)
