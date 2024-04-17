"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2562 import BoostPressureInputOptions
    from ._2563 import InputPowerInputOptions
    from ._2564 import PressureRatioInputOptions
    from ._2565 import RotorSetDataInputFileOptions
    from ._2566 import RotorSetMeasuredPoint
    from ._2567 import RotorSpeedInputOptions
    from ._2568 import SuperchargerMap
    from ._2569 import SuperchargerMaps
    from ._2570 import SuperchargerRotorSet
    from ._2571 import SuperchargerRotorSetDatabase
    from ._2572 import YVariableForImportedData
else:
    import_structure = {
        "_2562": ["BoostPressureInputOptions"],
        "_2563": ["InputPowerInputOptions"],
        "_2564": ["PressureRatioInputOptions"],
        "_2565": ["RotorSetDataInputFileOptions"],
        "_2566": ["RotorSetMeasuredPoint"],
        "_2567": ["RotorSpeedInputOptions"],
        "_2568": ["SuperchargerMap"],
        "_2569": ["SuperchargerMaps"],
        "_2570": ["SuperchargerRotorSet"],
        "_2571": ["SuperchargerRotorSetDatabase"],
        "_2572": ["YVariableForImportedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoostPressureInputOptions",
    "InputPowerInputOptions",
    "PressureRatioInputOptions",
    "RotorSetDataInputFileOptions",
    "RotorSetMeasuredPoint",
    "RotorSpeedInputOptions",
    "SuperchargerMap",
    "SuperchargerMaps",
    "SuperchargerRotorSet",
    "SuperchargerRotorSetDatabase",
    "YVariableForImportedData",
)
