"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._178 import Data
    from ._179 import Data1D
    from ._180 import Data3D
else:
    import_structure = {
        "_178": ["Data"],
        "_179": ["Data1D"],
        "_180": ["Data3D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Data",
    "Data1D",
    "Data3D",
)
