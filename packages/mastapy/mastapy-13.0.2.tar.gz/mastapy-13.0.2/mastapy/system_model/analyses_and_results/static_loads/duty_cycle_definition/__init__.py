"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6997 import AdditionalForcesObtainedFrom
    from ._6998 import BoostPressureLoadCaseInputOptions
    from ._6999 import DesignStateOptions
    from ._7000 import DestinationDesignState
    from ._7001 import ForceInputOptions
    from ._7002 import GearRatioInputOptions
    from ._7003 import LoadCaseNameOptions
    from ._7004 import MomentInputOptions
    from ._7005 import MultiTimeSeriesDataInputFileOptions
    from ._7006 import PointLoadInputOptions
    from ._7007 import PowerLoadInputOptions
    from ._7008 import RampOrSteadyStateInputOptions
    from ._7009 import SpeedInputOptions
    from ._7010 import TimeSeriesImporter
    from ._7011 import TimeStepInputOptions
    from ._7012 import TorqueInputOptions
    from ._7013 import TorqueValuesObtainedFrom
else:
    import_structure = {
        "_6997": ["AdditionalForcesObtainedFrom"],
        "_6998": ["BoostPressureLoadCaseInputOptions"],
        "_6999": ["DesignStateOptions"],
        "_7000": ["DestinationDesignState"],
        "_7001": ["ForceInputOptions"],
        "_7002": ["GearRatioInputOptions"],
        "_7003": ["LoadCaseNameOptions"],
        "_7004": ["MomentInputOptions"],
        "_7005": ["MultiTimeSeriesDataInputFileOptions"],
        "_7006": ["PointLoadInputOptions"],
        "_7007": ["PowerLoadInputOptions"],
        "_7008": ["RampOrSteadyStateInputOptions"],
        "_7009": ["SpeedInputOptions"],
        "_7010": ["TimeSeriesImporter"],
        "_7011": ["TimeStepInputOptions"],
        "_7012": ["TorqueInputOptions"],
        "_7013": ["TorqueValuesObtainedFrom"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdditionalForcesObtainedFrom",
    "BoostPressureLoadCaseInputOptions",
    "DesignStateOptions",
    "DestinationDesignState",
    "ForceInputOptions",
    "GearRatioInputOptions",
    "LoadCaseNameOptions",
    "MomentInputOptions",
    "MultiTimeSeriesDataInputFileOptions",
    "PointLoadInputOptions",
    "PowerLoadInputOptions",
    "RampOrSteadyStateInputOptions",
    "SpeedInputOptions",
    "TimeSeriesImporter",
    "TimeStepInputOptions",
    "TorqueInputOptions",
    "TorqueValuesObtainedFrom",
)
