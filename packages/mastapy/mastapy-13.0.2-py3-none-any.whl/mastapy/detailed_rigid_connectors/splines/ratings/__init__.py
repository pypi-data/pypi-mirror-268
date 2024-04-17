"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1430 import AGMA6123SplineHalfRating
    from ._1431 import AGMA6123SplineJointRating
    from ._1432 import DIN5466SplineHalfRating
    from ._1433 import DIN5466SplineRating
    from ._1434 import GBT17855SplineHalfRating
    from ._1435 import GBT17855SplineJointRating
    from ._1436 import SAESplineHalfRating
    from ._1437 import SAESplineJointRating
    from ._1438 import SplineHalfRating
    from ._1439 import SplineJointRating
else:
    import_structure = {
        "_1430": ["AGMA6123SplineHalfRating"],
        "_1431": ["AGMA6123SplineJointRating"],
        "_1432": ["DIN5466SplineHalfRating"],
        "_1433": ["DIN5466SplineRating"],
        "_1434": ["GBT17855SplineHalfRating"],
        "_1435": ["GBT17855SplineJointRating"],
        "_1436": ["SAESplineHalfRating"],
        "_1437": ["SAESplineJointRating"],
        "_1438": ["SplineHalfRating"],
        "_1439": ["SplineJointRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineHalfRating",
    "AGMA6123SplineJointRating",
    "DIN5466SplineHalfRating",
    "DIN5466SplineRating",
    "GBT17855SplineHalfRating",
    "GBT17855SplineJointRating",
    "SAESplineHalfRating",
    "SAESplineJointRating",
    "SplineHalfRating",
    "SplineJointRating",
)
