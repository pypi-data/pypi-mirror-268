"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4034 import RotorDynamicsDrawStyle
    from ._4035 import ShaftComplexShape
    from ._4036 import ShaftForcedComplexShape
    from ._4037 import ShaftModalComplexShape
    from ._4038 import ShaftModalComplexShapeAtSpeeds
    from ._4039 import ShaftModalComplexShapeAtStiffness
else:
    import_structure = {
        "_4034": ["RotorDynamicsDrawStyle"],
        "_4035": ["ShaftComplexShape"],
        "_4036": ["ShaftForcedComplexShape"],
        "_4037": ["ShaftModalComplexShape"],
        "_4038": ["ShaftModalComplexShapeAtSpeeds"],
        "_4039": ["ShaftModalComplexShapeAtStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "RotorDynamicsDrawStyle",
    "ShaftComplexShape",
    "ShaftForcedComplexShape",
    "ShaftModalComplexShape",
    "ShaftModalComplexShapeAtSpeeds",
    "ShaftModalComplexShapeAtStiffness",
)
