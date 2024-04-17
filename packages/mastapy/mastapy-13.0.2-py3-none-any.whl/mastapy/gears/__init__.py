"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._317 import AccuracyGrades
    from ._318 import AGMAToleranceStandard
    from ._319 import BevelHypoidGearDesignSettings
    from ._320 import BevelHypoidGearRatingSettings
    from ._321 import CentreDistanceChangeMethod
    from ._322 import CoefficientOfFrictionCalculationMethod
    from ._323 import ConicalGearToothSurface
    from ._324 import ContactRatioDataSource
    from ._325 import ContactRatioRequirements
    from ._326 import CylindricalFlanks
    from ._327 import CylindricalMisalignmentDataSource
    from ._328 import DeflectionFromBendingOption
    from ._329 import GearFlanks
    from ._330 import GearNURBSSurface
    from ._331 import GearSetDesignGroup
    from ._332 import GearSetModes
    from ._333 import GearSetOptimisationResult
    from ._334 import GearSetOptimisationResults
    from ._335 import GearSetOptimiser
    from ._336 import Hand
    from ._337 import ISOToleranceStandard
    from ._338 import LubricationMethods
    from ._339 import MicroGeometryInputTypes
    from ._340 import MicroGeometryModel
    from ._341 import MicropittingCoefficientOfFrictionCalculationMethod
    from ._342 import NamedPlanetAngle
    from ._343 import PlanetaryDetail
    from ._344 import PlanetaryRatingLoadSharingOption
    from ._345 import PocketingPowerLossCoefficients
    from ._346 import PocketingPowerLossCoefficientsDatabase
    from ._347 import QualityGradeTypes
    from ._348 import SafetyRequirementsAGMA
    from ._349 import SpecificationForTheEffectOfOilKinematicViscosity
    from ._350 import SpiralBevelRootLineTilt
    from ._351 import SpiralBevelToothTaper
    from ._352 import TESpecificationType
    from ._353 import WormAddendumFactor
    from ._354 import WormType
    from ._355 import ZerolBevelGleasonToothTaperOption
else:
    import_structure = {
        "_317": ["AccuracyGrades"],
        "_318": ["AGMAToleranceStandard"],
        "_319": ["BevelHypoidGearDesignSettings"],
        "_320": ["BevelHypoidGearRatingSettings"],
        "_321": ["CentreDistanceChangeMethod"],
        "_322": ["CoefficientOfFrictionCalculationMethod"],
        "_323": ["ConicalGearToothSurface"],
        "_324": ["ContactRatioDataSource"],
        "_325": ["ContactRatioRequirements"],
        "_326": ["CylindricalFlanks"],
        "_327": ["CylindricalMisalignmentDataSource"],
        "_328": ["DeflectionFromBendingOption"],
        "_329": ["GearFlanks"],
        "_330": ["GearNURBSSurface"],
        "_331": ["GearSetDesignGroup"],
        "_332": ["GearSetModes"],
        "_333": ["GearSetOptimisationResult"],
        "_334": ["GearSetOptimisationResults"],
        "_335": ["GearSetOptimiser"],
        "_336": ["Hand"],
        "_337": ["ISOToleranceStandard"],
        "_338": ["LubricationMethods"],
        "_339": ["MicroGeometryInputTypes"],
        "_340": ["MicroGeometryModel"],
        "_341": ["MicropittingCoefficientOfFrictionCalculationMethod"],
        "_342": ["NamedPlanetAngle"],
        "_343": ["PlanetaryDetail"],
        "_344": ["PlanetaryRatingLoadSharingOption"],
        "_345": ["PocketingPowerLossCoefficients"],
        "_346": ["PocketingPowerLossCoefficientsDatabase"],
        "_347": ["QualityGradeTypes"],
        "_348": ["SafetyRequirementsAGMA"],
        "_349": ["SpecificationForTheEffectOfOilKinematicViscosity"],
        "_350": ["SpiralBevelRootLineTilt"],
        "_351": ["SpiralBevelToothTaper"],
        "_352": ["TESpecificationType"],
        "_353": ["WormAddendumFactor"],
        "_354": ["WormType"],
        "_355": ["ZerolBevelGleasonToothTaperOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AccuracyGrades",
    "AGMAToleranceStandard",
    "BevelHypoidGearDesignSettings",
    "BevelHypoidGearRatingSettings",
    "CentreDistanceChangeMethod",
    "CoefficientOfFrictionCalculationMethod",
    "ConicalGearToothSurface",
    "ContactRatioDataSource",
    "ContactRatioRequirements",
    "CylindricalFlanks",
    "CylindricalMisalignmentDataSource",
    "DeflectionFromBendingOption",
    "GearFlanks",
    "GearNURBSSurface",
    "GearSetDesignGroup",
    "GearSetModes",
    "GearSetOptimisationResult",
    "GearSetOptimisationResults",
    "GearSetOptimiser",
    "Hand",
    "ISOToleranceStandard",
    "LubricationMethods",
    "MicroGeometryInputTypes",
    "MicroGeometryModel",
    "MicropittingCoefficientOfFrictionCalculationMethod",
    "NamedPlanetAngle",
    "PlanetaryDetail",
    "PlanetaryRatingLoadSharingOption",
    "PocketingPowerLossCoefficients",
    "PocketingPowerLossCoefficientsDatabase",
    "QualityGradeTypes",
    "SafetyRequirementsAGMA",
    "SpecificationForTheEffectOfOilKinematicViscosity",
    "SpiralBevelRootLineTilt",
    "SpiralBevelToothTaper",
    "TESpecificationType",
    "WormAddendumFactor",
    "WormType",
    "ZerolBevelGleasonToothTaperOption",
)
