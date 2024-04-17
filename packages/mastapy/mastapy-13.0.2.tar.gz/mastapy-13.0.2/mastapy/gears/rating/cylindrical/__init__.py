"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._454 import AGMAScuffingResultsRow
    from ._455 import CylindricalGearDesignAndRatingSettings
    from ._456 import CylindricalGearDesignAndRatingSettingsDatabase
    from ._457 import CylindricalGearDesignAndRatingSettingsItem
    from ._458 import CylindricalGearDutyCycleRating
    from ._459 import CylindricalGearFlankDutyCycleRating
    from ._460 import CylindricalGearFlankRating
    from ._461 import CylindricalGearMeshRating
    from ._462 import CylindricalGearMicroPittingResults
    from ._463 import CylindricalGearRating
    from ._464 import CylindricalGearRatingGeometryDataSource
    from ._465 import CylindricalGearScuffingResults
    from ._466 import CylindricalGearSetDutyCycleRating
    from ._467 import CylindricalGearSetRating
    from ._468 import CylindricalGearSingleFlankRating
    from ._469 import CylindricalMeshDutyCycleRating
    from ._470 import CylindricalMeshSingleFlankRating
    from ._471 import CylindricalPlasticGearRatingSettings
    from ._472 import CylindricalPlasticGearRatingSettingsDatabase
    from ._473 import CylindricalPlasticGearRatingSettingsItem
    from ._474 import CylindricalRateableMesh
    from ._475 import DynamicFactorMethods
    from ._476 import GearBlankFactorCalculationOptions
    from ._477 import ISOScuffingResultsRow
    from ._478 import MeshRatingForReports
    from ._479 import MicropittingRatingMethod
    from ._480 import MicroPittingResultsRow
    from ._481 import MisalignmentContactPatternEnhancements
    from ._482 import RatingMethod
    from ._483 import ReducedCylindricalGearSetDutyCycleRating
    from ._484 import ScuffingFlashTemperatureRatingMethod
    from ._485 import ScuffingIntegralTemperatureRatingMethod
    from ._486 import ScuffingMethods
    from ._487 import ScuffingResultsRow
    from ._488 import ScuffingResultsRowGear
    from ._489 import TipReliefScuffingOptions
    from ._490 import ToothThicknesses
    from ._491 import VDI2737SafetyFactorReportingObject
else:
    import_structure = {
        "_454": ["AGMAScuffingResultsRow"],
        "_455": ["CylindricalGearDesignAndRatingSettings"],
        "_456": ["CylindricalGearDesignAndRatingSettingsDatabase"],
        "_457": ["CylindricalGearDesignAndRatingSettingsItem"],
        "_458": ["CylindricalGearDutyCycleRating"],
        "_459": ["CylindricalGearFlankDutyCycleRating"],
        "_460": ["CylindricalGearFlankRating"],
        "_461": ["CylindricalGearMeshRating"],
        "_462": ["CylindricalGearMicroPittingResults"],
        "_463": ["CylindricalGearRating"],
        "_464": ["CylindricalGearRatingGeometryDataSource"],
        "_465": ["CylindricalGearScuffingResults"],
        "_466": ["CylindricalGearSetDutyCycleRating"],
        "_467": ["CylindricalGearSetRating"],
        "_468": ["CylindricalGearSingleFlankRating"],
        "_469": ["CylindricalMeshDutyCycleRating"],
        "_470": ["CylindricalMeshSingleFlankRating"],
        "_471": ["CylindricalPlasticGearRatingSettings"],
        "_472": ["CylindricalPlasticGearRatingSettingsDatabase"],
        "_473": ["CylindricalPlasticGearRatingSettingsItem"],
        "_474": ["CylindricalRateableMesh"],
        "_475": ["DynamicFactorMethods"],
        "_476": ["GearBlankFactorCalculationOptions"],
        "_477": ["ISOScuffingResultsRow"],
        "_478": ["MeshRatingForReports"],
        "_479": ["MicropittingRatingMethod"],
        "_480": ["MicroPittingResultsRow"],
        "_481": ["MisalignmentContactPatternEnhancements"],
        "_482": ["RatingMethod"],
        "_483": ["ReducedCylindricalGearSetDutyCycleRating"],
        "_484": ["ScuffingFlashTemperatureRatingMethod"],
        "_485": ["ScuffingIntegralTemperatureRatingMethod"],
        "_486": ["ScuffingMethods"],
        "_487": ["ScuffingResultsRow"],
        "_488": ["ScuffingResultsRowGear"],
        "_489": ["TipReliefScuffingOptions"],
        "_490": ["ToothThicknesses"],
        "_491": ["VDI2737SafetyFactorReportingObject"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAScuffingResultsRow",
    "CylindricalGearDesignAndRatingSettings",
    "CylindricalGearDesignAndRatingSettingsDatabase",
    "CylindricalGearDesignAndRatingSettingsItem",
    "CylindricalGearDutyCycleRating",
    "CylindricalGearFlankDutyCycleRating",
    "CylindricalGearFlankRating",
    "CylindricalGearMeshRating",
    "CylindricalGearMicroPittingResults",
    "CylindricalGearRating",
    "CylindricalGearRatingGeometryDataSource",
    "CylindricalGearScuffingResults",
    "CylindricalGearSetDutyCycleRating",
    "CylindricalGearSetRating",
    "CylindricalGearSingleFlankRating",
    "CylindricalMeshDutyCycleRating",
    "CylindricalMeshSingleFlankRating",
    "CylindricalPlasticGearRatingSettings",
    "CylindricalPlasticGearRatingSettingsDatabase",
    "CylindricalPlasticGearRatingSettingsItem",
    "CylindricalRateableMesh",
    "DynamicFactorMethods",
    "GearBlankFactorCalculationOptions",
    "ISOScuffingResultsRow",
    "MeshRatingForReports",
    "MicropittingRatingMethod",
    "MicroPittingResultsRow",
    "MisalignmentContactPatternEnhancements",
    "RatingMethod",
    "ReducedCylindricalGearSetDutyCycleRating",
    "ScuffingFlashTemperatureRatingMethod",
    "ScuffingIntegralTemperatureRatingMethod",
    "ScuffingMethods",
    "ScuffingResultsRow",
    "ScuffingResultsRowGear",
    "TipReliefScuffingOptions",
    "ToothThicknesses",
    "VDI2737SafetyFactorReportingObject",
)
