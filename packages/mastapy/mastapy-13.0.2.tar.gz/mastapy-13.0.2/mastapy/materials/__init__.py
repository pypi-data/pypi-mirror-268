"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._239 import AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial
    from ._240 import AcousticRadiationEfficiency
    from ._241 import AcousticRadiationEfficiencyInputType
    from ._242 import AGMALubricantType
    from ._243 import AGMAMaterialApplications
    from ._244 import AGMAMaterialClasses
    from ._245 import AGMAMaterialGrade
    from ._246 import AirProperties
    from ._247 import BearingLubricationCondition
    from ._248 import BearingMaterial
    from ._249 import BearingMaterialDatabase
    from ._250 import BHCurveExtrapolationMethod
    from ._251 import BHCurveSpecification
    from ._252 import ComponentMaterialDatabase
    from ._253 import CompositeFatigueSafetyFactorItem
    from ._254 import CylindricalGearRatingMethods
    from ._255 import DensitySpecificationMethod
    from ._256 import FatigueSafetyFactorItem
    from ._257 import FatigueSafetyFactorItemBase
    from ._258 import GearingTypes
    from ._259 import GeneralTransmissionProperties
    from ._260 import GreaseContaminationOptions
    from ._261 import HardnessType
    from ._262 import ISO76StaticSafetyFactorLimits
    from ._263 import ISOLubricantType
    from ._264 import LubricantDefinition
    from ._265 import LubricantDelivery
    from ._266 import LubricantViscosityClassAGMA
    from ._267 import LubricantViscosityClassification
    from ._268 import LubricantViscosityClassISO
    from ._269 import LubricantViscosityClassSAE
    from ._270 import LubricationDetail
    from ._271 import LubricationDetailDatabase
    from ._272 import Material
    from ._273 import MaterialDatabase
    from ._274 import MaterialsSettings
    from ._275 import MaterialsSettingsDatabase
    from ._276 import MaterialsSettingsItem
    from ._277 import MaterialStandards
    from ._278 import MetalPlasticType
    from ._279 import OilFiltrationOptions
    from ._280 import PressureViscosityCoefficientMethod
    from ._281 import QualityGrade
    from ._282 import SafetyFactorGroup
    from ._283 import SafetyFactorItem
    from ._284 import SNCurve
    from ._285 import SNCurvePoint
    from ._286 import SoundPressureEnclosure
    from ._287 import SoundPressureEnclosureType
    from ._288 import StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial
    from ._289 import StressCyclesDataForTheContactSNCurveOfAPlasticMaterial
    from ._290 import TransmissionApplications
    from ._291 import VDI2736LubricantType
    from ._292 import VehicleDynamicsProperties
    from ._293 import WindTurbineStandards
    from ._294 import WorkingCharacteristics
else:
    import_structure = {
        "_239": ["AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"],
        "_240": ["AcousticRadiationEfficiency"],
        "_241": ["AcousticRadiationEfficiencyInputType"],
        "_242": ["AGMALubricantType"],
        "_243": ["AGMAMaterialApplications"],
        "_244": ["AGMAMaterialClasses"],
        "_245": ["AGMAMaterialGrade"],
        "_246": ["AirProperties"],
        "_247": ["BearingLubricationCondition"],
        "_248": ["BearingMaterial"],
        "_249": ["BearingMaterialDatabase"],
        "_250": ["BHCurveExtrapolationMethod"],
        "_251": ["BHCurveSpecification"],
        "_252": ["ComponentMaterialDatabase"],
        "_253": ["CompositeFatigueSafetyFactorItem"],
        "_254": ["CylindricalGearRatingMethods"],
        "_255": ["DensitySpecificationMethod"],
        "_256": ["FatigueSafetyFactorItem"],
        "_257": ["FatigueSafetyFactorItemBase"],
        "_258": ["GearingTypes"],
        "_259": ["GeneralTransmissionProperties"],
        "_260": ["GreaseContaminationOptions"],
        "_261": ["HardnessType"],
        "_262": ["ISO76StaticSafetyFactorLimits"],
        "_263": ["ISOLubricantType"],
        "_264": ["LubricantDefinition"],
        "_265": ["LubricantDelivery"],
        "_266": ["LubricantViscosityClassAGMA"],
        "_267": ["LubricantViscosityClassification"],
        "_268": ["LubricantViscosityClassISO"],
        "_269": ["LubricantViscosityClassSAE"],
        "_270": ["LubricationDetail"],
        "_271": ["LubricationDetailDatabase"],
        "_272": ["Material"],
        "_273": ["MaterialDatabase"],
        "_274": ["MaterialsSettings"],
        "_275": ["MaterialsSettingsDatabase"],
        "_276": ["MaterialsSettingsItem"],
        "_277": ["MaterialStandards"],
        "_278": ["MetalPlasticType"],
        "_279": ["OilFiltrationOptions"],
        "_280": ["PressureViscosityCoefficientMethod"],
        "_281": ["QualityGrade"],
        "_282": ["SafetyFactorGroup"],
        "_283": ["SafetyFactorItem"],
        "_284": ["SNCurve"],
        "_285": ["SNCurvePoint"],
        "_286": ["SoundPressureEnclosure"],
        "_287": ["SoundPressureEnclosureType"],
        "_288": ["StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial"],
        "_289": ["StressCyclesDataForTheContactSNCurveOfAPlasticMaterial"],
        "_290": ["TransmissionApplications"],
        "_291": ["VDI2736LubricantType"],
        "_292": ["VehicleDynamicsProperties"],
        "_293": ["WindTurbineStandards"],
        "_294": ["WorkingCharacteristics"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
    "AcousticRadiationEfficiency",
    "AcousticRadiationEfficiencyInputType",
    "AGMALubricantType",
    "AGMAMaterialApplications",
    "AGMAMaterialClasses",
    "AGMAMaterialGrade",
    "AirProperties",
    "BearingLubricationCondition",
    "BearingMaterial",
    "BearingMaterialDatabase",
    "BHCurveExtrapolationMethod",
    "BHCurveSpecification",
    "ComponentMaterialDatabase",
    "CompositeFatigueSafetyFactorItem",
    "CylindricalGearRatingMethods",
    "DensitySpecificationMethod",
    "FatigueSafetyFactorItem",
    "FatigueSafetyFactorItemBase",
    "GearingTypes",
    "GeneralTransmissionProperties",
    "GreaseContaminationOptions",
    "HardnessType",
    "ISO76StaticSafetyFactorLimits",
    "ISOLubricantType",
    "LubricantDefinition",
    "LubricantDelivery",
    "LubricantViscosityClassAGMA",
    "LubricantViscosityClassification",
    "LubricantViscosityClassISO",
    "LubricantViscosityClassSAE",
    "LubricationDetail",
    "LubricationDetailDatabase",
    "Material",
    "MaterialDatabase",
    "MaterialsSettings",
    "MaterialsSettingsDatabase",
    "MaterialsSettingsItem",
    "MaterialStandards",
    "MetalPlasticType",
    "OilFiltrationOptions",
    "PressureViscosityCoefficientMethod",
    "QualityGrade",
    "SafetyFactorGroup",
    "SafetyFactorItem",
    "SNCurve",
    "SNCurvePoint",
    "SoundPressureEnclosure",
    "SoundPressureEnclosureType",
    "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
    "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
    "TransmissionApplications",
    "VDI2736LubricantType",
    "VehicleDynamicsProperties",
    "WindTurbineStandards",
    "WorkingCharacteristics",
)
