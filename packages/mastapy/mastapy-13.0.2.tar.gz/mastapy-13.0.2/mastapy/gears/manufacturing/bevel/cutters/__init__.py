"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._816 import PinionFinishCutter
    from ._817 import PinionRoughCutter
    from ._818 import WheelFinishCutter
    from ._819 import WheelRoughCutter
else:
    import_structure = {
        "_816": ["PinionFinishCutter"],
        "_817": ["PinionRoughCutter"],
        "_818": ["WheelFinishCutter"],
        "_819": ["WheelRoughCutter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "PinionFinishCutter",
    "PinionRoughCutter",
    "WheelFinishCutter",
    "WheelRoughCutter",
)
