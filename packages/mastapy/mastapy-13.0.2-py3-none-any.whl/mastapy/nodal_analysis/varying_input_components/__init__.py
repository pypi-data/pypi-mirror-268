"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._96 import AbstractVaryingInputComponent
    from ._97 import AngleInputComponent
    from ._98 import ForceInputComponent
    from ._99 import MomentInputComponent
    from ._100 import NonDimensionalInputComponent
    from ._101 import SinglePointSelectionMethod
    from ._102 import VelocityInputComponent
else:
    import_structure = {
        "_96": ["AbstractVaryingInputComponent"],
        "_97": ["AngleInputComponent"],
        "_98": ["ForceInputComponent"],
        "_99": ["MomentInputComponent"],
        "_100": ["NonDimensionalInputComponent"],
        "_101": ["SinglePointSelectionMethod"],
        "_102": ["VelocityInputComponent"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractVaryingInputComponent",
    "AngleInputComponent",
    "ForceInputComponent",
    "MomentInputComponent",
    "NonDimensionalInputComponent",
    "SinglePointSelectionMethod",
    "VelocityInputComponent",
)
