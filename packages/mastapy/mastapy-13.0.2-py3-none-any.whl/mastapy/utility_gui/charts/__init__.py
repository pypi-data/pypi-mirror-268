"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1859 import BubbleChartDefinition
    from ._1860 import ConstantLine
    from ._1861 import CustomLineChart
    from ._1862 import CustomTableAndChart
    from ._1863 import LegacyChartMathChartDefinition
    from ._1864 import MatrixVisualisationDefinition
    from ._1865 import ModeConstantLine
    from ._1866 import NDChartDefinition
    from ._1867 import ParallelCoordinatesChartDefinition
    from ._1868 import PointsForSurface
    from ._1869 import ScatterChartDefinition
    from ._1870 import Series2D
    from ._1871 import SMTAxis
    from ._1872 import ThreeDChartDefinition
    from ._1873 import ThreeDVectorChartDefinition
    from ._1874 import TwoDChartDefinition
else:
    import_structure = {
        "_1859": ["BubbleChartDefinition"],
        "_1860": ["ConstantLine"],
        "_1861": ["CustomLineChart"],
        "_1862": ["CustomTableAndChart"],
        "_1863": ["LegacyChartMathChartDefinition"],
        "_1864": ["MatrixVisualisationDefinition"],
        "_1865": ["ModeConstantLine"],
        "_1866": ["NDChartDefinition"],
        "_1867": ["ParallelCoordinatesChartDefinition"],
        "_1868": ["PointsForSurface"],
        "_1869": ["ScatterChartDefinition"],
        "_1870": ["Series2D"],
        "_1871": ["SMTAxis"],
        "_1872": ["ThreeDChartDefinition"],
        "_1873": ["ThreeDVectorChartDefinition"],
        "_1874": ["TwoDChartDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BubbleChartDefinition",
    "ConstantLine",
    "CustomLineChart",
    "CustomTableAndChart",
    "LegacyChartMathChartDefinition",
    "MatrixVisualisationDefinition",
    "ModeConstantLine",
    "NDChartDefinition",
    "ParallelCoordinatesChartDefinition",
    "PointsForSurface",
    "ScatterChartDefinition",
    "Series2D",
    "SMTAxis",
    "ThreeDChartDefinition",
    "ThreeDVectorChartDefinition",
    "TwoDChartDefinition",
)
