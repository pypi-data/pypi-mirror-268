"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2108 import BallISO2812007Results
    from ._2109 import BallISOTS162812008Results
    from ._2110 import ISO2812007Results
    from ._2111 import ISO762006Results
    from ._2112 import ISOResults
    from ._2113 import ISOTS162812008Results
    from ._2114 import RollerISO2812007Results
    from ._2115 import RollerISOTS162812008Results
    from ._2116 import StressConcentrationMethod
else:
    import_structure = {
        "_2108": ["BallISO2812007Results"],
        "_2109": ["BallISOTS162812008Results"],
        "_2110": ["ISO2812007Results"],
        "_2111": ["ISO762006Results"],
        "_2112": ["ISOResults"],
        "_2113": ["ISOTS162812008Results"],
        "_2114": ["RollerISO2812007Results"],
        "_2115": ["RollerISOTS162812008Results"],
        "_2116": ["StressConcentrationMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallISO2812007Results",
    "BallISOTS162812008Results",
    "ISO2812007Results",
    "ISO762006Results",
    "ISOResults",
    "ISOTS162812008Results",
    "RollerISO2812007Results",
    "RollerISOTS162812008Results",
    "StressConcentrationMethod",
)
