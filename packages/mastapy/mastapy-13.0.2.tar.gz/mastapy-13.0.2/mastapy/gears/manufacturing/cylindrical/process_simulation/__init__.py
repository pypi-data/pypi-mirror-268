"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._642 import CutterProcessSimulation
    from ._643 import FormWheelGrindingProcessSimulation
    from ._644 import ShapingProcessSimulation
else:
    import_structure = {
        "_642": ["CutterProcessSimulation"],
        "_643": ["FormWheelGrindingProcessSimulation"],
        "_644": ["ShapingProcessSimulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterProcessSimulation",
    "FormWheelGrindingProcessSimulation",
    "ShapingProcessSimulation",
)
