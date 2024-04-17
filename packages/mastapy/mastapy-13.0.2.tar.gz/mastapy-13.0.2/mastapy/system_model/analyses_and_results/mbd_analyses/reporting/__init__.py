"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5531 import AbstractMeasuredDynamicResponseAtTime
    from ._5532 import DynamicForceResultAtTime
    from ._5533 import DynamicForceVector3DResult
    from ._5534 import DynamicTorqueResultAtTime
    from ._5535 import DynamicTorqueVector3DResult
else:
    import_structure = {
        "_5531": ["AbstractMeasuredDynamicResponseAtTime"],
        "_5532": ["DynamicForceResultAtTime"],
        "_5533": ["DynamicForceVector3DResult"],
        "_5534": ["DynamicTorqueResultAtTime"],
        "_5535": ["DynamicTorqueVector3DResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractMeasuredDynamicResponseAtTime",
    "DynamicForceResultAtTime",
    "DynamicForceVector3DResult",
    "DynamicTorqueResultAtTime",
    "DynamicTorqueVector3DResult",
)
