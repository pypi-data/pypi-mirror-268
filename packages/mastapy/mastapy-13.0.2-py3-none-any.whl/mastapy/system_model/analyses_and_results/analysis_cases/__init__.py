"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7543 import AnalysisCase
    from ._7544 import AbstractAnalysisOptions
    from ._7545 import CompoundAnalysisCase
    from ._7546 import ConnectionAnalysisCase
    from ._7547 import ConnectionCompoundAnalysis
    from ._7548 import ConnectionFEAnalysis
    from ._7549 import ConnectionStaticLoadAnalysisCase
    from ._7550 import ConnectionTimeSeriesLoadAnalysisCase
    from ._7551 import DesignEntityCompoundAnalysis
    from ._7552 import FEAnalysis
    from ._7553 import PartAnalysisCase
    from ._7554 import PartCompoundAnalysis
    from ._7555 import PartFEAnalysis
    from ._7556 import PartStaticLoadAnalysisCase
    from ._7557 import PartTimeSeriesLoadAnalysisCase
    from ._7558 import StaticLoadAnalysisCase
    from ._7559 import TimeSeriesLoadAnalysisCase
else:
    import_structure = {
        "_7543": ["AnalysisCase"],
        "_7544": ["AbstractAnalysisOptions"],
        "_7545": ["CompoundAnalysisCase"],
        "_7546": ["ConnectionAnalysisCase"],
        "_7547": ["ConnectionCompoundAnalysis"],
        "_7548": ["ConnectionFEAnalysis"],
        "_7549": ["ConnectionStaticLoadAnalysisCase"],
        "_7550": ["ConnectionTimeSeriesLoadAnalysisCase"],
        "_7551": ["DesignEntityCompoundAnalysis"],
        "_7552": ["FEAnalysis"],
        "_7553": ["PartAnalysisCase"],
        "_7554": ["PartCompoundAnalysis"],
        "_7555": ["PartFEAnalysis"],
        "_7556": ["PartStaticLoadAnalysisCase"],
        "_7557": ["PartTimeSeriesLoadAnalysisCase"],
        "_7558": ["StaticLoadAnalysisCase"],
        "_7559": ["TimeSeriesLoadAnalysisCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AnalysisCase",
    "AbstractAnalysisOptions",
    "CompoundAnalysisCase",
    "ConnectionAnalysisCase",
    "ConnectionCompoundAnalysis",
    "ConnectionFEAnalysis",
    "ConnectionStaticLoadAnalysisCase",
    "ConnectionTimeSeriesLoadAnalysisCase",
    "DesignEntityCompoundAnalysis",
    "FEAnalysis",
    "PartAnalysisCase",
    "PartCompoundAnalysis",
    "PartFEAnalysis",
    "PartStaticLoadAnalysisCase",
    "PartTimeSeriesLoadAnalysisCase",
    "StaticLoadAnalysisCase",
    "TimeSeriesLoadAnalysisCase",
)
