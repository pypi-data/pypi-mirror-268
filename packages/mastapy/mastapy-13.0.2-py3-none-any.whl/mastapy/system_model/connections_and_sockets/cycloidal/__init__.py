"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2340 import CycloidalDiscAxialLeftSocket
    from ._2341 import CycloidalDiscAxialRightSocket
    from ._2342 import CycloidalDiscCentralBearingConnection
    from ._2343 import CycloidalDiscInnerSocket
    from ._2344 import CycloidalDiscOuterSocket
    from ._2345 import CycloidalDiscPlanetaryBearingConnection
    from ._2346 import CycloidalDiscPlanetaryBearingSocket
    from ._2347 import RingPinsSocket
    from ._2348 import RingPinsToDiscConnection
else:
    import_structure = {
        "_2340": ["CycloidalDiscAxialLeftSocket"],
        "_2341": ["CycloidalDiscAxialRightSocket"],
        "_2342": ["CycloidalDiscCentralBearingConnection"],
        "_2343": ["CycloidalDiscInnerSocket"],
        "_2344": ["CycloidalDiscOuterSocket"],
        "_2345": ["CycloidalDiscPlanetaryBearingConnection"],
        "_2346": ["CycloidalDiscPlanetaryBearingSocket"],
        "_2347": ["RingPinsSocket"],
        "_2348": ["RingPinsToDiscConnection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalDiscAxialLeftSocket",
    "CycloidalDiscAxialRightSocket",
    "CycloidalDiscCentralBearingConnection",
    "CycloidalDiscInnerSocket",
    "CycloidalDiscOuterSocket",
    "CycloidalDiscPlanetaryBearingConnection",
    "CycloidalDiscPlanetaryBearingSocket",
    "RingPinsSocket",
    "RingPinsToDiscConnection",
)
