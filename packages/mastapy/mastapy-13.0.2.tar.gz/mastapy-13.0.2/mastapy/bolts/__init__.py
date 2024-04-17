"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1472 import AxialLoadType
    from ._1473 import BoltedJointMaterial
    from ._1474 import BoltedJointMaterialDatabase
    from ._1475 import BoltGeometry
    from ._1476 import BoltGeometryDatabase
    from ._1477 import BoltMaterial
    from ._1478 import BoltMaterialDatabase
    from ._1479 import BoltSection
    from ._1480 import BoltShankType
    from ._1481 import BoltTypes
    from ._1482 import ClampedSection
    from ._1483 import ClampedSectionMaterialDatabase
    from ._1484 import DetailedBoltDesign
    from ._1485 import DetailedBoltedJointDesign
    from ._1486 import HeadCapTypes
    from ._1487 import JointGeometries
    from ._1488 import JointTypes
    from ._1489 import LoadedBolt
    from ._1490 import RolledBeforeOrAfterHeatTreatment
    from ._1491 import StandardSizes
    from ._1492 import StrengthGrades
    from ._1493 import ThreadTypes
    from ._1494 import TighteningTechniques
else:
    import_structure = {
        "_1472": ["AxialLoadType"],
        "_1473": ["BoltedJointMaterial"],
        "_1474": ["BoltedJointMaterialDatabase"],
        "_1475": ["BoltGeometry"],
        "_1476": ["BoltGeometryDatabase"],
        "_1477": ["BoltMaterial"],
        "_1478": ["BoltMaterialDatabase"],
        "_1479": ["BoltSection"],
        "_1480": ["BoltShankType"],
        "_1481": ["BoltTypes"],
        "_1482": ["ClampedSection"],
        "_1483": ["ClampedSectionMaterialDatabase"],
        "_1484": ["DetailedBoltDesign"],
        "_1485": ["DetailedBoltedJointDesign"],
        "_1486": ["HeadCapTypes"],
        "_1487": ["JointGeometries"],
        "_1488": ["JointTypes"],
        "_1489": ["LoadedBolt"],
        "_1490": ["RolledBeforeOrAfterHeatTreatment"],
        "_1491": ["StandardSizes"],
        "_1492": ["StrengthGrades"],
        "_1493": ["ThreadTypes"],
        "_1494": ["TighteningTechniques"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialLoadType",
    "BoltedJointMaterial",
    "BoltedJointMaterialDatabase",
    "BoltGeometry",
    "BoltGeometryDatabase",
    "BoltMaterial",
    "BoltMaterialDatabase",
    "BoltSection",
    "BoltShankType",
    "BoltTypes",
    "ClampedSection",
    "ClampedSectionMaterialDatabase",
    "DetailedBoltDesign",
    "DetailedBoltedJointDesign",
    "HeadCapTypes",
    "JointGeometries",
    "JointTypes",
    "LoadedBolt",
    "RolledBeforeOrAfterHeatTreatment",
    "StandardSizes",
    "StrengthGrades",
    "ThreadTypes",
    "TighteningTechniques",
)
