"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6 import AGMAHardeningType
    from ._7 import CastingFactorCondition
    from ._8 import ConsequenceOfFailure
    from ._9 import DesignShaftSection
    from ._10 import DesignShaftSectionEnd
    from ._11 import FkmMaterialGroup
    from ._12 import FkmSnCurveModel
    from ._13 import FkmVersionOfMinersRule
    from ._14 import GenericStressConcentrationFactor
    from ._15 import ProfilePointFilletStressConcentrationFactors
    from ._16 import ShaftAxialBendingTorsionalComponentValues
    from ._17 import ShaftAxialBendingXBendingYTorsionalComponentValues
    from ._18 import ShaftAxialTorsionalComponentValues
    from ._19 import ShaftDamageResults
    from ._20 import ShaftDamageResultsTableAndChart
    from ._21 import ShaftFeature
    from ._22 import ShaftGroove
    from ._23 import ShaftKey
    from ._24 import ShaftMaterial
    from ._25 import ShaftMaterialDatabase
    from ._26 import ShaftMaterialForReports
    from ._27 import ShaftPointStress
    from ._28 import ShaftPointStressCycle
    from ._29 import ShaftPointStressCycleReporting
    from ._30 import ShaftProfile
    from ._31 import ShaftProfilePoint
    from ._32 import ShaftProfilePointCopy
    from ._33 import ShaftRadialHole
    from ._34 import ShaftRatingMethod
    from ._35 import ShaftSafetyFactorSettings
    from ._36 import ShaftSectionDamageResults
    from ._37 import ShaftSectionEndDamageResults
    from ._38 import ShaftSettings
    from ._39 import ShaftSettingsDatabase
    from ._40 import ShaftSettingsItem
    from ._41 import ShaftSurfaceFinishSection
    from ._42 import ShaftSurfaceRoughness
    from ._43 import SimpleShaftDefinition
    from ._44 import StressMeasurementShaftAxialBendingTorsionalComponentValues
    from ._45 import SurfaceFinishes
else:
    import_structure = {
        "_6": ["AGMAHardeningType"],
        "_7": ["CastingFactorCondition"],
        "_8": ["ConsequenceOfFailure"],
        "_9": ["DesignShaftSection"],
        "_10": ["DesignShaftSectionEnd"],
        "_11": ["FkmMaterialGroup"],
        "_12": ["FkmSnCurveModel"],
        "_13": ["FkmVersionOfMinersRule"],
        "_14": ["GenericStressConcentrationFactor"],
        "_15": ["ProfilePointFilletStressConcentrationFactors"],
        "_16": ["ShaftAxialBendingTorsionalComponentValues"],
        "_17": ["ShaftAxialBendingXBendingYTorsionalComponentValues"],
        "_18": ["ShaftAxialTorsionalComponentValues"],
        "_19": ["ShaftDamageResults"],
        "_20": ["ShaftDamageResultsTableAndChart"],
        "_21": ["ShaftFeature"],
        "_22": ["ShaftGroove"],
        "_23": ["ShaftKey"],
        "_24": ["ShaftMaterial"],
        "_25": ["ShaftMaterialDatabase"],
        "_26": ["ShaftMaterialForReports"],
        "_27": ["ShaftPointStress"],
        "_28": ["ShaftPointStressCycle"],
        "_29": ["ShaftPointStressCycleReporting"],
        "_30": ["ShaftProfile"],
        "_31": ["ShaftProfilePoint"],
        "_32": ["ShaftProfilePointCopy"],
        "_33": ["ShaftRadialHole"],
        "_34": ["ShaftRatingMethod"],
        "_35": ["ShaftSafetyFactorSettings"],
        "_36": ["ShaftSectionDamageResults"],
        "_37": ["ShaftSectionEndDamageResults"],
        "_38": ["ShaftSettings"],
        "_39": ["ShaftSettingsDatabase"],
        "_40": ["ShaftSettingsItem"],
        "_41": ["ShaftSurfaceFinishSection"],
        "_42": ["ShaftSurfaceRoughness"],
        "_43": ["SimpleShaftDefinition"],
        "_44": ["StressMeasurementShaftAxialBendingTorsionalComponentValues"],
        "_45": ["SurfaceFinishes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAHardeningType",
    "CastingFactorCondition",
    "ConsequenceOfFailure",
    "DesignShaftSection",
    "DesignShaftSectionEnd",
    "FkmMaterialGroup",
    "FkmSnCurveModel",
    "FkmVersionOfMinersRule",
    "GenericStressConcentrationFactor",
    "ProfilePointFilletStressConcentrationFactors",
    "ShaftAxialBendingTorsionalComponentValues",
    "ShaftAxialBendingXBendingYTorsionalComponentValues",
    "ShaftAxialTorsionalComponentValues",
    "ShaftDamageResults",
    "ShaftDamageResultsTableAndChart",
    "ShaftFeature",
    "ShaftGroove",
    "ShaftKey",
    "ShaftMaterial",
    "ShaftMaterialDatabase",
    "ShaftMaterialForReports",
    "ShaftPointStress",
    "ShaftPointStressCycle",
    "ShaftPointStressCycleReporting",
    "ShaftProfile",
    "ShaftProfilePoint",
    "ShaftProfilePointCopy",
    "ShaftRadialHole",
    "ShaftRatingMethod",
    "ShaftSafetyFactorSettings",
    "ShaftSectionDamageResults",
    "ShaftSectionEndDamageResults",
    "ShaftSettings",
    "ShaftSettingsDatabase",
    "ShaftSettingsItem",
    "ShaftSurfaceFinishSection",
    "ShaftSurfaceRoughness",
    "SimpleShaftDefinition",
    "StressMeasurementShaftAxialBendingTorsionalComponentValues",
    "SurfaceFinishes",
)
