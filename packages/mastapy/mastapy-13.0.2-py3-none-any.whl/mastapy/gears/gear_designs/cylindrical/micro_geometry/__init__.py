"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1099 import CylindricalGearBiasModification
    from ._1100 import CylindricalGearCommonFlankMicroGeometry
    from ._1101 import CylindricalGearFlankMicroGeometry
    from ._1102 import CylindricalGearLeadModification
    from ._1103 import CylindricalGearLeadModificationAtProfilePosition
    from ._1104 import CylindricalGearMeshMicroGeometry
    from ._1105 import CylindricalGearMeshMicroGeometryDutyCycle
    from ._1106 import CylindricalGearMicroGeometry
    from ._1107 import CylindricalGearMicroGeometryBase
    from ._1108 import CylindricalGearMicroGeometryDutyCycle
    from ._1109 import CylindricalGearMicroGeometryMap
    from ._1110 import CylindricalGearMicroGeometryPerTooth
    from ._1111 import CylindricalGearProfileModification
    from ._1112 import CylindricalGearProfileModificationAtFaceWidthPosition
    from ._1113 import CylindricalGearSetMicroGeometry
    from ._1114 import CylindricalGearSetMicroGeometryDutyCycle
    from ._1115 import CylindricalGearToothMicroGeometry
    from ._1116 import CylindricalGearTriangularEndModification
    from ._1117 import CylindricalGearTriangularEndModificationAtOrientation
    from ._1118 import DrawDefiningGearOrBoth
    from ._1119 import GearAlignment
    from ._1120 import LeadFormReliefWithDeviation
    from ._1121 import LeadReliefWithDeviation
    from ._1122 import LeadSlopeReliefWithDeviation
    from ._1123 import LinearCylindricalGearTriangularEndModification
    from ._1124 import MeasuredMapDataTypes
    from ._1125 import MeshAlignment
    from ._1126 import MeshedCylindricalGearFlankMicroGeometry
    from ._1127 import MeshedCylindricalGearMicroGeometry
    from ._1128 import MicroGeometryLeadToleranceChartView
    from ._1129 import MicroGeometryViewingOptions
    from ._1130 import ParabolicCylindricalGearTriangularEndModification
    from ._1131 import ProfileFormReliefWithDeviation
    from ._1132 import ProfileReliefWithDeviation
    from ._1133 import ProfileSlopeReliefWithDeviation
    from ._1134 import ReliefWithDeviation
    from ._1135 import SingleCylindricalGearTriangularEndModification
    from ._1136 import TotalLeadReliefWithDeviation
    from ._1137 import TotalProfileReliefWithDeviation
else:
    import_structure = {
        "_1099": ["CylindricalGearBiasModification"],
        "_1100": ["CylindricalGearCommonFlankMicroGeometry"],
        "_1101": ["CylindricalGearFlankMicroGeometry"],
        "_1102": ["CylindricalGearLeadModification"],
        "_1103": ["CylindricalGearLeadModificationAtProfilePosition"],
        "_1104": ["CylindricalGearMeshMicroGeometry"],
        "_1105": ["CylindricalGearMeshMicroGeometryDutyCycle"],
        "_1106": ["CylindricalGearMicroGeometry"],
        "_1107": ["CylindricalGearMicroGeometryBase"],
        "_1108": ["CylindricalGearMicroGeometryDutyCycle"],
        "_1109": ["CylindricalGearMicroGeometryMap"],
        "_1110": ["CylindricalGearMicroGeometryPerTooth"],
        "_1111": ["CylindricalGearProfileModification"],
        "_1112": ["CylindricalGearProfileModificationAtFaceWidthPosition"],
        "_1113": ["CylindricalGearSetMicroGeometry"],
        "_1114": ["CylindricalGearSetMicroGeometryDutyCycle"],
        "_1115": ["CylindricalGearToothMicroGeometry"],
        "_1116": ["CylindricalGearTriangularEndModification"],
        "_1117": ["CylindricalGearTriangularEndModificationAtOrientation"],
        "_1118": ["DrawDefiningGearOrBoth"],
        "_1119": ["GearAlignment"],
        "_1120": ["LeadFormReliefWithDeviation"],
        "_1121": ["LeadReliefWithDeviation"],
        "_1122": ["LeadSlopeReliefWithDeviation"],
        "_1123": ["LinearCylindricalGearTriangularEndModification"],
        "_1124": ["MeasuredMapDataTypes"],
        "_1125": ["MeshAlignment"],
        "_1126": ["MeshedCylindricalGearFlankMicroGeometry"],
        "_1127": ["MeshedCylindricalGearMicroGeometry"],
        "_1128": ["MicroGeometryLeadToleranceChartView"],
        "_1129": ["MicroGeometryViewingOptions"],
        "_1130": ["ParabolicCylindricalGearTriangularEndModification"],
        "_1131": ["ProfileFormReliefWithDeviation"],
        "_1132": ["ProfileReliefWithDeviation"],
        "_1133": ["ProfileSlopeReliefWithDeviation"],
        "_1134": ["ReliefWithDeviation"],
        "_1135": ["SingleCylindricalGearTriangularEndModification"],
        "_1136": ["TotalLeadReliefWithDeviation"],
        "_1137": ["TotalProfileReliefWithDeviation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBiasModification",
    "CylindricalGearCommonFlankMicroGeometry",
    "CylindricalGearFlankMicroGeometry",
    "CylindricalGearLeadModification",
    "CylindricalGearLeadModificationAtProfilePosition",
    "CylindricalGearMeshMicroGeometry",
    "CylindricalGearMeshMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometry",
    "CylindricalGearMicroGeometryBase",
    "CylindricalGearMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometryMap",
    "CylindricalGearMicroGeometryPerTooth",
    "CylindricalGearProfileModification",
    "CylindricalGearProfileModificationAtFaceWidthPosition",
    "CylindricalGearSetMicroGeometry",
    "CylindricalGearSetMicroGeometryDutyCycle",
    "CylindricalGearToothMicroGeometry",
    "CylindricalGearTriangularEndModification",
    "CylindricalGearTriangularEndModificationAtOrientation",
    "DrawDefiningGearOrBoth",
    "GearAlignment",
    "LeadFormReliefWithDeviation",
    "LeadReliefWithDeviation",
    "LeadSlopeReliefWithDeviation",
    "LinearCylindricalGearTriangularEndModification",
    "MeasuredMapDataTypes",
    "MeshAlignment",
    "MeshedCylindricalGearFlankMicroGeometry",
    "MeshedCylindricalGearMicroGeometry",
    "MicroGeometryLeadToleranceChartView",
    "MicroGeometryViewingOptions",
    "ParabolicCylindricalGearTriangularEndModification",
    "ProfileFormReliefWithDeviation",
    "ProfileReliefWithDeviation",
    "ProfileSlopeReliefWithDeviation",
    "ReliefWithDeviation",
    "SingleCylindricalGearTriangularEndModification",
    "TotalLeadReliefWithDeviation",
    "TotalProfileReliefWithDeviation",
)
