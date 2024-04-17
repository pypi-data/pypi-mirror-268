"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._356 import AbstractGearMeshRating
    from ._357 import AbstractGearRating
    from ._358 import AbstractGearSetRating
    from ._359 import BendingAndContactReportingObject
    from ._360 import FlankLoadingState
    from ._361 import GearDutyCycleRating
    from ._362 import GearFlankRating
    from ._363 import GearMeshRating
    from ._364 import GearRating
    from ._365 import GearSetDutyCycleRating
    from ._366 import GearSetRating
    from ._367 import GearSingleFlankRating
    from ._368 import MeshDutyCycleRating
    from ._369 import MeshSingleFlankRating
    from ._370 import RateableMesh
    from ._371 import SafetyFactorResults
else:
    import_structure = {
        "_356": ["AbstractGearMeshRating"],
        "_357": ["AbstractGearRating"],
        "_358": ["AbstractGearSetRating"],
        "_359": ["BendingAndContactReportingObject"],
        "_360": ["FlankLoadingState"],
        "_361": ["GearDutyCycleRating"],
        "_362": ["GearFlankRating"],
        "_363": ["GearMeshRating"],
        "_364": ["GearRating"],
        "_365": ["GearSetDutyCycleRating"],
        "_366": ["GearSetRating"],
        "_367": ["GearSingleFlankRating"],
        "_368": ["MeshDutyCycleRating"],
        "_369": ["MeshSingleFlankRating"],
        "_370": ["RateableMesh"],
        "_371": ["SafetyFactorResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearMeshRating",
    "AbstractGearRating",
    "AbstractGearSetRating",
    "BendingAndContactReportingObject",
    "FlankLoadingState",
    "GearDutyCycleRating",
    "GearFlankRating",
    "GearMeshRating",
    "GearRating",
    "GearSetDutyCycleRating",
    "GearSetRating",
    "GearSingleFlankRating",
    "MeshDutyCycleRating",
    "MeshSingleFlankRating",
    "RateableMesh",
    "SafetyFactorResults",
)
