"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._493 import MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
    from ._494 import PlasticGearVDI2736AbstractGearSingleFlankRating
    from ._495 import PlasticGearVDI2736AbstractMeshSingleFlankRating
    from ._496 import PlasticGearVDI2736AbstractRateableMesh
    from ._497 import PlasticPlasticVDI2736MeshSingleFlankRating
    from ._498 import PlasticSNCurveForTheSpecifiedOperatingConditions
    from ._499 import (
        PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh,
    )
    from ._500 import PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh
    from ._501 import VDI2736MetalPlasticRateableMesh
    from ._502 import VDI2736PlasticMetalRateableMesh
    from ._503 import VDI2736PlasticPlasticRateableMesh
else:
    import_structure = {
        "_493": ["MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating"],
        "_494": ["PlasticGearVDI2736AbstractGearSingleFlankRating"],
        "_495": ["PlasticGearVDI2736AbstractMeshSingleFlankRating"],
        "_496": ["PlasticGearVDI2736AbstractRateableMesh"],
        "_497": ["PlasticPlasticVDI2736MeshSingleFlankRating"],
        "_498": ["PlasticSNCurveForTheSpecifiedOperatingConditions"],
        "_499": [
            "PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh"
        ],
        "_500": ["PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh"],
        "_501": ["VDI2736MetalPlasticRateableMesh"],
        "_502": ["VDI2736PlasticMetalRateableMesh"],
        "_503": ["VDI2736PlasticPlasticRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
    "PlasticGearVDI2736AbstractGearSingleFlankRating",
    "PlasticGearVDI2736AbstractMeshSingleFlankRating",
    "PlasticGearVDI2736AbstractRateableMesh",
    "PlasticPlasticVDI2736MeshSingleFlankRating",
    "PlasticSNCurveForTheSpecifiedOperatingConditions",
    "PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh",
    "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
    "VDI2736MetalPlasticRateableMesh",
    "VDI2736PlasticMetalRateableMesh",
    "VDI2736PlasticPlasticRateableMesh",
)
