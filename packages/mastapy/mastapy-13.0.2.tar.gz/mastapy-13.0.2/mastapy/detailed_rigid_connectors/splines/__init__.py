"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1396 import CustomSplineHalfDesign
    from ._1397 import CustomSplineJointDesign
    from ._1398 import DetailedSplineJointSettings
    from ._1399 import DIN5480SplineHalfDesign
    from ._1400 import DIN5480SplineJointDesign
    from ._1401 import DudleyEffectiveLengthApproximationOption
    from ._1402 import FitTypes
    from ._1403 import GBT3478SplineHalfDesign
    from ._1404 import GBT3478SplineJointDesign
    from ._1405 import HeatTreatmentTypes
    from ._1406 import ISO4156SplineHalfDesign
    from ._1407 import ISO4156SplineJointDesign
    from ._1408 import JISB1603SplineJointDesign
    from ._1409 import ManufacturingTypes
    from ._1410 import Modules
    from ._1411 import PressureAngleTypes
    from ._1412 import RootTypes
    from ._1413 import SAEFatigueLifeFactorTypes
    from ._1414 import SAESplineHalfDesign
    from ._1415 import SAESplineJointDesign
    from ._1416 import SAETorqueCycles
    from ._1417 import SplineDesignTypes
    from ._1418 import FinishingMethods
    from ._1419 import SplineFitClassType
    from ._1420 import SplineFixtureTypes
    from ._1421 import SplineHalfDesign
    from ._1422 import SplineJointDesign
    from ._1423 import SplineMaterial
    from ._1424 import SplineRatingTypes
    from ._1425 import SplineToleranceClassTypes
    from ._1426 import StandardSplineHalfDesign
    from ._1427 import StandardSplineJointDesign
else:
    import_structure = {
        "_1396": ["CustomSplineHalfDesign"],
        "_1397": ["CustomSplineJointDesign"],
        "_1398": ["DetailedSplineJointSettings"],
        "_1399": ["DIN5480SplineHalfDesign"],
        "_1400": ["DIN5480SplineJointDesign"],
        "_1401": ["DudleyEffectiveLengthApproximationOption"],
        "_1402": ["FitTypes"],
        "_1403": ["GBT3478SplineHalfDesign"],
        "_1404": ["GBT3478SplineJointDesign"],
        "_1405": ["HeatTreatmentTypes"],
        "_1406": ["ISO4156SplineHalfDesign"],
        "_1407": ["ISO4156SplineJointDesign"],
        "_1408": ["JISB1603SplineJointDesign"],
        "_1409": ["ManufacturingTypes"],
        "_1410": ["Modules"],
        "_1411": ["PressureAngleTypes"],
        "_1412": ["RootTypes"],
        "_1413": ["SAEFatigueLifeFactorTypes"],
        "_1414": ["SAESplineHalfDesign"],
        "_1415": ["SAESplineJointDesign"],
        "_1416": ["SAETorqueCycles"],
        "_1417": ["SplineDesignTypes"],
        "_1418": ["FinishingMethods"],
        "_1419": ["SplineFitClassType"],
        "_1420": ["SplineFixtureTypes"],
        "_1421": ["SplineHalfDesign"],
        "_1422": ["SplineJointDesign"],
        "_1423": ["SplineMaterial"],
        "_1424": ["SplineRatingTypes"],
        "_1425": ["SplineToleranceClassTypes"],
        "_1426": ["StandardSplineHalfDesign"],
        "_1427": ["StandardSplineJointDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CustomSplineHalfDesign",
    "CustomSplineJointDesign",
    "DetailedSplineJointSettings",
    "DIN5480SplineHalfDesign",
    "DIN5480SplineJointDesign",
    "DudleyEffectiveLengthApproximationOption",
    "FitTypes",
    "GBT3478SplineHalfDesign",
    "GBT3478SplineJointDesign",
    "HeatTreatmentTypes",
    "ISO4156SplineHalfDesign",
    "ISO4156SplineJointDesign",
    "JISB1603SplineJointDesign",
    "ManufacturingTypes",
    "Modules",
    "PressureAngleTypes",
    "RootTypes",
    "SAEFatigueLifeFactorTypes",
    "SAESplineHalfDesign",
    "SAESplineJointDesign",
    "SAETorqueCycles",
    "SplineDesignTypes",
    "FinishingMethods",
    "SplineFitClassType",
    "SplineFixtureTypes",
    "SplineHalfDesign",
    "SplineJointDesign",
    "SplineMaterial",
    "SplineRatingTypes",
    "SplineToleranceClassTypes",
    "StandardSplineHalfDesign",
    "StandardSplineJointDesign",
)
