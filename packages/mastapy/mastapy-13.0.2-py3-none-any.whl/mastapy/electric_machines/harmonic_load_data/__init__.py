"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1385 import ElectricMachineHarmonicLoadDataBase
    from ._1386 import ForceDisplayOption
    from ._1387 import HarmonicLoadDataBase
    from ._1388 import HarmonicLoadDataControlExcitationOptionBase
    from ._1389 import HarmonicLoadDataType
    from ._1390 import SpeedDependentHarmonicLoadData
    from ._1391 import StatorToothInterpolator
    from ._1392 import StatorToothLoadInterpolator
    from ._1393 import StatorToothMomentInterpolator
else:
    import_structure = {
        "_1385": ["ElectricMachineHarmonicLoadDataBase"],
        "_1386": ["ForceDisplayOption"],
        "_1387": ["HarmonicLoadDataBase"],
        "_1388": ["HarmonicLoadDataControlExcitationOptionBase"],
        "_1389": ["HarmonicLoadDataType"],
        "_1390": ["SpeedDependentHarmonicLoadData"],
        "_1391": ["StatorToothInterpolator"],
        "_1392": ["StatorToothLoadInterpolator"],
        "_1393": ["StatorToothMomentInterpolator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElectricMachineHarmonicLoadDataBase",
    "ForceDisplayOption",
    "HarmonicLoadDataBase",
    "HarmonicLoadDataControlExcitationOptionBase",
    "HarmonicLoadDataType",
    "SpeedDependentHarmonicLoadData",
    "StatorToothInterpolator",
    "StatorToothLoadInterpolator",
    "StatorToothMomentInterpolator",
)
