"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1214 import CylindricalGearLTCAContactChartDataAsTextFile
    from ._1215 import CylindricalGearLTCAContactCharts
    from ._1216 import CylindricalGearWorstLTCAContactChartDataAsTextFile
    from ._1217 import CylindricalGearWorstLTCAContactCharts
    from ._1218 import GearLTCAContactChartDataAsTextFile
    from ._1219 import GearLTCAContactCharts
    from ._1220 import PointsWithWorstResults
else:
    import_structure = {
        "_1214": ["CylindricalGearLTCAContactChartDataAsTextFile"],
        "_1215": ["CylindricalGearLTCAContactCharts"],
        "_1216": ["CylindricalGearWorstLTCAContactChartDataAsTextFile"],
        "_1217": ["CylindricalGearWorstLTCAContactCharts"],
        "_1218": ["GearLTCAContactChartDataAsTextFile"],
        "_1219": ["GearLTCAContactCharts"],
        "_1220": ["PointsWithWorstResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLTCAContactChartDataAsTextFile",
    "CylindricalGearLTCAContactCharts",
    "CylindricalGearWorstLTCAContactChartDataAsTextFile",
    "CylindricalGearWorstLTCAContactCharts",
    "GearLTCAContactChartDataAsTextFile",
    "GearLTCAContactCharts",
    "PointsWithWorstResults",
)
