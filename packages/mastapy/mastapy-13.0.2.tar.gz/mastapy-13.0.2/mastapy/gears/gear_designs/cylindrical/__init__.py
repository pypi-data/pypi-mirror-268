"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1002 import AddendumModificationDistributionRule
    from ._1003 import BacklashSpecification
    from ._1004 import BasicRackProfiles
    from ._1005 import CaseHardeningProperties
    from ._1006 import CreateNewSuitableCutterOption
    from ._1007 import CrossedAxisCylindricalGearPair
    from ._1008 import CrossedAxisCylindricalGearPairLineContact
    from ._1009 import CrossedAxisCylindricalGearPairPointContact
    from ._1010 import CylindricalGearAbstractRack
    from ._1011 import CylindricalGearAbstractRackFlank
    from ._1012 import CylindricalGearBasicRack
    from ._1013 import CylindricalGearBasicRackFlank
    from ._1014 import CylindricalGearCuttingOptions
    from ._1015 import CylindricalGearDefaults
    from ._1016 import CylindricalGearDesign
    from ._1017 import CylindricalGearDesignConstraint
    from ._1018 import CylindricalGearDesignConstraints
    from ._1019 import CylindricalGearDesignConstraintsDatabase
    from ._1020 import CylindricalGearDesignConstraintSettings
    from ._1021 import CylindricalGearFlankDesign
    from ._1022 import CylindricalGearMeshDesign
    from ._1023 import CylindricalGearMeshFlankDesign
    from ._1024 import CylindricalGearMicroGeometrySettings
    from ._1025 import CylindricalGearMicroGeometrySettingsDatabase
    from ._1026 import CylindricalGearMicroGeometrySettingsItem
    from ._1027 import CylindricalGearPinionTypeCutter
    from ._1028 import CylindricalGearPinionTypeCutterFlank
    from ._1029 import CylindricalGearProfileMeasurement
    from ._1030 import CylindricalGearProfileMeasurementType
    from ._1031 import CylindricalGearProfileModifications
    from ._1032 import CylindricalGearSetDesign
    from ._1033 import CylindricalGearSetFlankDesign
    from ._1034 import CylindricalGearSetMacroGeometryOptimiser
    from ._1035 import CylindricalGearSetManufacturingConfigurationSelection
    from ._1036 import CylindricalGearSetMicroGeometrySettings
    from ._1037 import CylindricalGearSetOptimisationWrapper
    from ._1038 import CylindricalGearTableMGItemDetail
    from ._1039 import CylindricalGearTableWithMGCharts
    from ._1040 import CylindricalGearToothThicknessSpecification
    from ._1041 import CylindricalMeshAngularBacklash
    from ._1042 import CylindricalMeshedGear
    from ._1043 import CylindricalMeshedGearFlank
    from ._1044 import CylindricalMeshLinearBacklashSpecification
    from ._1045 import CylindricalPlanetaryGearSetDesign
    from ._1046 import CylindricalPlanetGearDesign
    from ._1047 import DIN3967AllowanceSeries
    from ._1048 import DIN3967ToleranceSeries
    from ._1049 import DoubleAxisScaleAndRange
    from ._1050 import FinishToothThicknessDesignSpecification
    from ._1051 import GearFitSystems
    from ._1052 import GearManufacturingConfigSetupViewModel
    from ._1053 import GearSetManufacturingConfigurationSetup
    from ._1054 import GeometrySpecificationType
    from ._1055 import HardenedMaterialProperties
    from ._1056 import HardnessProfileCalculationMethod
    from ._1057 import HeatTreatmentType
    from ._1058 import ISO6336Geometry
    from ._1059 import ISO6336GeometryBase
    from ._1060 import ISO6336GeometryForShapedGears
    from ._1061 import ISO6336GeometryManufactured
    from ._1062 import LinearBacklashSpecification
    from ._1063 import LTCALoadCaseModifiableSettings
    from ._1064 import LTCASettings
    from ._1065 import MicroGeometryConvention
    from ._1066 import MicroGeometryProfileConvention
    from ._1067 import Micropitting
    from ._1068 import MullerResidualStressDefinition
    from ._1069 import NamedPlanetAssemblyIndex
    from ._1070 import NamedPlanetSideBandAmplitudeFactor
    from ._1071 import ReadonlyToothThicknessSpecification
    from ._1072 import RelativeMeasurementViewModel
    from ._1073 import RelativeValuesSpecification
    from ._1074 import ResidualStressCalculationMethod
    from ._1075 import RootStressSurfaceChartOption
    from ._1076 import Scuffing
    from ._1077 import ScuffingCoefficientOfFrictionMethods
    from ._1078 import ScuffingTemperatureMethodsAGMA
    from ._1079 import ScuffingTemperatureMethodsISO
    from ._1080 import ShaperEdgeTypes
    from ._1081 import SpurGearLoadSharingCodes
    from ._1082 import StandardRack
    from ._1083 import StandardRackFlank
    from ._1084 import SurfaceRoughness
    from ._1085 import ThicknessType
    from ._1086 import TiffAnalysisSettings
    from ._1087 import TipAlterationCoefficientMethod
    from ._1088 import TolerancedMetalMeasurements
    from ._1089 import TolerancedValueSpecification
    from ._1090 import ToothFlankFractureAnalysisSettings
    from ._1091 import ToothThicknessSpecification
    from ._1092 import ToothThicknessSpecificationBase
    from ._1093 import TypeOfMechanismHousing
    from ._1094 import Usage
else:
    import_structure = {
        "_1002": ["AddendumModificationDistributionRule"],
        "_1003": ["BacklashSpecification"],
        "_1004": ["BasicRackProfiles"],
        "_1005": ["CaseHardeningProperties"],
        "_1006": ["CreateNewSuitableCutterOption"],
        "_1007": ["CrossedAxisCylindricalGearPair"],
        "_1008": ["CrossedAxisCylindricalGearPairLineContact"],
        "_1009": ["CrossedAxisCylindricalGearPairPointContact"],
        "_1010": ["CylindricalGearAbstractRack"],
        "_1011": ["CylindricalGearAbstractRackFlank"],
        "_1012": ["CylindricalGearBasicRack"],
        "_1013": ["CylindricalGearBasicRackFlank"],
        "_1014": ["CylindricalGearCuttingOptions"],
        "_1015": ["CylindricalGearDefaults"],
        "_1016": ["CylindricalGearDesign"],
        "_1017": ["CylindricalGearDesignConstraint"],
        "_1018": ["CylindricalGearDesignConstraints"],
        "_1019": ["CylindricalGearDesignConstraintsDatabase"],
        "_1020": ["CylindricalGearDesignConstraintSettings"],
        "_1021": ["CylindricalGearFlankDesign"],
        "_1022": ["CylindricalGearMeshDesign"],
        "_1023": ["CylindricalGearMeshFlankDesign"],
        "_1024": ["CylindricalGearMicroGeometrySettings"],
        "_1025": ["CylindricalGearMicroGeometrySettingsDatabase"],
        "_1026": ["CylindricalGearMicroGeometrySettingsItem"],
        "_1027": ["CylindricalGearPinionTypeCutter"],
        "_1028": ["CylindricalGearPinionTypeCutterFlank"],
        "_1029": ["CylindricalGearProfileMeasurement"],
        "_1030": ["CylindricalGearProfileMeasurementType"],
        "_1031": ["CylindricalGearProfileModifications"],
        "_1032": ["CylindricalGearSetDesign"],
        "_1033": ["CylindricalGearSetFlankDesign"],
        "_1034": ["CylindricalGearSetMacroGeometryOptimiser"],
        "_1035": ["CylindricalGearSetManufacturingConfigurationSelection"],
        "_1036": ["CylindricalGearSetMicroGeometrySettings"],
        "_1037": ["CylindricalGearSetOptimisationWrapper"],
        "_1038": ["CylindricalGearTableMGItemDetail"],
        "_1039": ["CylindricalGearTableWithMGCharts"],
        "_1040": ["CylindricalGearToothThicknessSpecification"],
        "_1041": ["CylindricalMeshAngularBacklash"],
        "_1042": ["CylindricalMeshedGear"],
        "_1043": ["CylindricalMeshedGearFlank"],
        "_1044": ["CylindricalMeshLinearBacklashSpecification"],
        "_1045": ["CylindricalPlanetaryGearSetDesign"],
        "_1046": ["CylindricalPlanetGearDesign"],
        "_1047": ["DIN3967AllowanceSeries"],
        "_1048": ["DIN3967ToleranceSeries"],
        "_1049": ["DoubleAxisScaleAndRange"],
        "_1050": ["FinishToothThicknessDesignSpecification"],
        "_1051": ["GearFitSystems"],
        "_1052": ["GearManufacturingConfigSetupViewModel"],
        "_1053": ["GearSetManufacturingConfigurationSetup"],
        "_1054": ["GeometrySpecificationType"],
        "_1055": ["HardenedMaterialProperties"],
        "_1056": ["HardnessProfileCalculationMethod"],
        "_1057": ["HeatTreatmentType"],
        "_1058": ["ISO6336Geometry"],
        "_1059": ["ISO6336GeometryBase"],
        "_1060": ["ISO6336GeometryForShapedGears"],
        "_1061": ["ISO6336GeometryManufactured"],
        "_1062": ["LinearBacklashSpecification"],
        "_1063": ["LTCALoadCaseModifiableSettings"],
        "_1064": ["LTCASettings"],
        "_1065": ["MicroGeometryConvention"],
        "_1066": ["MicroGeometryProfileConvention"],
        "_1067": ["Micropitting"],
        "_1068": ["MullerResidualStressDefinition"],
        "_1069": ["NamedPlanetAssemblyIndex"],
        "_1070": ["NamedPlanetSideBandAmplitudeFactor"],
        "_1071": ["ReadonlyToothThicknessSpecification"],
        "_1072": ["RelativeMeasurementViewModel"],
        "_1073": ["RelativeValuesSpecification"],
        "_1074": ["ResidualStressCalculationMethod"],
        "_1075": ["RootStressSurfaceChartOption"],
        "_1076": ["Scuffing"],
        "_1077": ["ScuffingCoefficientOfFrictionMethods"],
        "_1078": ["ScuffingTemperatureMethodsAGMA"],
        "_1079": ["ScuffingTemperatureMethodsISO"],
        "_1080": ["ShaperEdgeTypes"],
        "_1081": ["SpurGearLoadSharingCodes"],
        "_1082": ["StandardRack"],
        "_1083": ["StandardRackFlank"],
        "_1084": ["SurfaceRoughness"],
        "_1085": ["ThicknessType"],
        "_1086": ["TiffAnalysisSettings"],
        "_1087": ["TipAlterationCoefficientMethod"],
        "_1088": ["TolerancedMetalMeasurements"],
        "_1089": ["TolerancedValueSpecification"],
        "_1090": ["ToothFlankFractureAnalysisSettings"],
        "_1091": ["ToothThicknessSpecification"],
        "_1092": ["ToothThicknessSpecificationBase"],
        "_1093": ["TypeOfMechanismHousing"],
        "_1094": ["Usage"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AddendumModificationDistributionRule",
    "BacklashSpecification",
    "BasicRackProfiles",
    "CaseHardeningProperties",
    "CreateNewSuitableCutterOption",
    "CrossedAxisCylindricalGearPair",
    "CrossedAxisCylindricalGearPairLineContact",
    "CrossedAxisCylindricalGearPairPointContact",
    "CylindricalGearAbstractRack",
    "CylindricalGearAbstractRackFlank",
    "CylindricalGearBasicRack",
    "CylindricalGearBasicRackFlank",
    "CylindricalGearCuttingOptions",
    "CylindricalGearDefaults",
    "CylindricalGearDesign",
    "CylindricalGearDesignConstraint",
    "CylindricalGearDesignConstraints",
    "CylindricalGearDesignConstraintsDatabase",
    "CylindricalGearDesignConstraintSettings",
    "CylindricalGearFlankDesign",
    "CylindricalGearMeshDesign",
    "CylindricalGearMeshFlankDesign",
    "CylindricalGearMicroGeometrySettings",
    "CylindricalGearMicroGeometrySettingsDatabase",
    "CylindricalGearMicroGeometrySettingsItem",
    "CylindricalGearPinionTypeCutter",
    "CylindricalGearPinionTypeCutterFlank",
    "CylindricalGearProfileMeasurement",
    "CylindricalGearProfileMeasurementType",
    "CylindricalGearProfileModifications",
    "CylindricalGearSetDesign",
    "CylindricalGearSetFlankDesign",
    "CylindricalGearSetMacroGeometryOptimiser",
    "CylindricalGearSetManufacturingConfigurationSelection",
    "CylindricalGearSetMicroGeometrySettings",
    "CylindricalGearSetOptimisationWrapper",
    "CylindricalGearTableMGItemDetail",
    "CylindricalGearTableWithMGCharts",
    "CylindricalGearToothThicknessSpecification",
    "CylindricalMeshAngularBacklash",
    "CylindricalMeshedGear",
    "CylindricalMeshedGearFlank",
    "CylindricalMeshLinearBacklashSpecification",
    "CylindricalPlanetaryGearSetDesign",
    "CylindricalPlanetGearDesign",
    "DIN3967AllowanceSeries",
    "DIN3967ToleranceSeries",
    "DoubleAxisScaleAndRange",
    "FinishToothThicknessDesignSpecification",
    "GearFitSystems",
    "GearManufacturingConfigSetupViewModel",
    "GearSetManufacturingConfigurationSetup",
    "GeometrySpecificationType",
    "HardenedMaterialProperties",
    "HardnessProfileCalculationMethod",
    "HeatTreatmentType",
    "ISO6336Geometry",
    "ISO6336GeometryBase",
    "ISO6336GeometryForShapedGears",
    "ISO6336GeometryManufactured",
    "LinearBacklashSpecification",
    "LTCALoadCaseModifiableSettings",
    "LTCASettings",
    "MicroGeometryConvention",
    "MicroGeometryProfileConvention",
    "Micropitting",
    "MullerResidualStressDefinition",
    "NamedPlanetAssemblyIndex",
    "NamedPlanetSideBandAmplitudeFactor",
    "ReadonlyToothThicknessSpecification",
    "RelativeMeasurementViewModel",
    "RelativeValuesSpecification",
    "ResidualStressCalculationMethod",
    "RootStressSurfaceChartOption",
    "Scuffing",
    "ScuffingCoefficientOfFrictionMethods",
    "ScuffingTemperatureMethodsAGMA",
    "ScuffingTemperatureMethodsISO",
    "ShaperEdgeTypes",
    "SpurGearLoadSharingCodes",
    "StandardRack",
    "StandardRackFlank",
    "SurfaceRoughness",
    "ThicknessType",
    "TiffAnalysisSettings",
    "TipAlterationCoefficientMethod",
    "TolerancedMetalMeasurements",
    "TolerancedValueSpecification",
    "ToothFlankFractureAnalysisSettings",
    "ToothThicknessSpecification",
    "ToothThicknessSpecificationBase",
    "TypeOfMechanismHousing",
    "Usage",
)
