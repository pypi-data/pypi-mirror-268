"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1458 import ContactSpecification
    from ._1459 import CrowningSpecificationMethod
    from ._1460 import CycloidalAssemblyDesign
    from ._1461 import CycloidalDiscDesign
    from ._1462 import CycloidalDiscDesignExporter
    from ._1463 import CycloidalDiscMaterial
    from ._1464 import CycloidalDiscMaterialDatabase
    from ._1465 import CycloidalDiscModificationsSpecification
    from ._1466 import DirectionOfMeasuredModifications
    from ._1467 import GeometryToExport
    from ._1468 import NamedDiscPhase
    from ._1469 import RingPinsDesign
    from ._1470 import RingPinsMaterial
    from ._1471 import RingPinsMaterialDatabase
else:
    import_structure = {
        "_1458": ["ContactSpecification"],
        "_1459": ["CrowningSpecificationMethod"],
        "_1460": ["CycloidalAssemblyDesign"],
        "_1461": ["CycloidalDiscDesign"],
        "_1462": ["CycloidalDiscDesignExporter"],
        "_1463": ["CycloidalDiscMaterial"],
        "_1464": ["CycloidalDiscMaterialDatabase"],
        "_1465": ["CycloidalDiscModificationsSpecification"],
        "_1466": ["DirectionOfMeasuredModifications"],
        "_1467": ["GeometryToExport"],
        "_1468": ["NamedDiscPhase"],
        "_1469": ["RingPinsDesign"],
        "_1470": ["RingPinsMaterial"],
        "_1471": ["RingPinsMaterialDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactSpecification",
    "CrowningSpecificationMethod",
    "CycloidalAssemblyDesign",
    "CycloidalDiscDesign",
    "CycloidalDiscDesignExporter",
    "CycloidalDiscMaterial",
    "CycloidalDiscMaterialDatabase",
    "CycloidalDiscModificationsSpecification",
    "DirectionOfMeasuredModifications",
    "GeometryToExport",
    "NamedDiscPhase",
    "RingPinsDesign",
    "RingPinsMaterial",
    "RingPinsMaterialDatabase",
)
