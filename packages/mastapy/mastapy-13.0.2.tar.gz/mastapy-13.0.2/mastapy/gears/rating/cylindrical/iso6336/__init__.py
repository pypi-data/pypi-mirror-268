"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._511 import CylindricalGearToothFatigueFractureResults
    from ._512 import CylindricalGearToothFatigueFractureResultsN1457
    from ._513 import HelicalGearMicroGeometryOption
    from ._514 import ISO63361996GearSingleFlankRating
    from ._515 import ISO63361996MeshSingleFlankRating
    from ._516 import ISO63362006GearSingleFlankRating
    from ._517 import ISO63362006MeshSingleFlankRating
    from ._518 import ISO63362019GearSingleFlankRating
    from ._519 import ISO63362019MeshSingleFlankRating
    from ._520 import ISO6336AbstractGearSingleFlankRating
    from ._521 import ISO6336AbstractMeshSingleFlankRating
    from ._522 import ISO6336AbstractMetalGearSingleFlankRating
    from ._523 import ISO6336AbstractMetalMeshSingleFlankRating
    from ._524 import ISO6336MeanStressInfluenceFactor
    from ._525 import ISO6336MetalRateableMesh
    from ._526 import ISO6336RateableMesh
    from ._527 import ToothFlankFractureAnalysisContactPoint
    from ._528 import ToothFlankFractureAnalysisContactPointCommon
    from ._529 import ToothFlankFractureAnalysisContactPointMethodA
    from ._530 import ToothFlankFractureAnalysisContactPointN1457
    from ._531 import ToothFlankFractureAnalysisPoint
    from ._532 import ToothFlankFractureAnalysisPointN1457
    from ._533 import ToothFlankFractureAnalysisRowN1457
    from ._534 import ToothFlankFractureStressStepAtAnalysisPointN1457
else:
    import_structure = {
        "_511": ["CylindricalGearToothFatigueFractureResults"],
        "_512": ["CylindricalGearToothFatigueFractureResultsN1457"],
        "_513": ["HelicalGearMicroGeometryOption"],
        "_514": ["ISO63361996GearSingleFlankRating"],
        "_515": ["ISO63361996MeshSingleFlankRating"],
        "_516": ["ISO63362006GearSingleFlankRating"],
        "_517": ["ISO63362006MeshSingleFlankRating"],
        "_518": ["ISO63362019GearSingleFlankRating"],
        "_519": ["ISO63362019MeshSingleFlankRating"],
        "_520": ["ISO6336AbstractGearSingleFlankRating"],
        "_521": ["ISO6336AbstractMeshSingleFlankRating"],
        "_522": ["ISO6336AbstractMetalGearSingleFlankRating"],
        "_523": ["ISO6336AbstractMetalMeshSingleFlankRating"],
        "_524": ["ISO6336MeanStressInfluenceFactor"],
        "_525": ["ISO6336MetalRateableMesh"],
        "_526": ["ISO6336RateableMesh"],
        "_527": ["ToothFlankFractureAnalysisContactPoint"],
        "_528": ["ToothFlankFractureAnalysisContactPointCommon"],
        "_529": ["ToothFlankFractureAnalysisContactPointMethodA"],
        "_530": ["ToothFlankFractureAnalysisContactPointN1457"],
        "_531": ["ToothFlankFractureAnalysisPoint"],
        "_532": ["ToothFlankFractureAnalysisPointN1457"],
        "_533": ["ToothFlankFractureAnalysisRowN1457"],
        "_534": ["ToothFlankFractureStressStepAtAnalysisPointN1457"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearToothFatigueFractureResults",
    "CylindricalGearToothFatigueFractureResultsN1457",
    "HelicalGearMicroGeometryOption",
    "ISO63361996GearSingleFlankRating",
    "ISO63361996MeshSingleFlankRating",
    "ISO63362006GearSingleFlankRating",
    "ISO63362006MeshSingleFlankRating",
    "ISO63362019GearSingleFlankRating",
    "ISO63362019MeshSingleFlankRating",
    "ISO6336AbstractGearSingleFlankRating",
    "ISO6336AbstractMeshSingleFlankRating",
    "ISO6336AbstractMetalGearSingleFlankRating",
    "ISO6336AbstractMetalMeshSingleFlankRating",
    "ISO6336MeanStressInfluenceFactor",
    "ISO6336MetalRateableMesh",
    "ISO6336RateableMesh",
    "ToothFlankFractureAnalysisContactPoint",
    "ToothFlankFractureAnalysisContactPointCommon",
    "ToothFlankFractureAnalysisContactPointMethodA",
    "ToothFlankFractureAnalysisContactPointN1457",
    "ToothFlankFractureAnalysisPoint",
    "ToothFlankFractureAnalysisPointN1457",
    "ToothFlankFractureAnalysisRowN1457",
    "ToothFlankFractureStressStepAtAnalysisPointN1457",
)
