"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1609 import DegreesMinutesSeconds
    from ._1610 import EnumUnit
    from ._1611 import InverseUnit
    from ._1612 import MeasurementBase
    from ._1613 import MeasurementSettings
    from ._1614 import MeasurementSystem
    from ._1615 import SafetyFactorUnit
    from ._1616 import TimeUnit
    from ._1617 import Unit
    from ._1618 import UnitGradient
else:
    import_structure = {
        "_1609": ["DegreesMinutesSeconds"],
        "_1610": ["EnumUnit"],
        "_1611": ["InverseUnit"],
        "_1612": ["MeasurementBase"],
        "_1613": ["MeasurementSettings"],
        "_1614": ["MeasurementSystem"],
        "_1615": ["SafetyFactorUnit"],
        "_1616": ["TimeUnit"],
        "_1617": ["Unit"],
        "_1618": ["UnitGradient"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DegreesMinutesSeconds",
    "EnumUnit",
    "InverseUnit",
    "MeasurementBase",
    "MeasurementSettings",
    "MeasurementSystem",
    "SafetyFactorUnit",
    "TimeUnit",
    "Unit",
    "UnitGradient",
)
