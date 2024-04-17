"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._309 import ClippingPlane
    from ._310 import DrawStyle
    from ._311 import DrawStyleBase
    from ._312 import PackagingLimits
else:
    import_structure = {
        "_309": ["ClippingPlane"],
        "_310": ["DrawStyle"],
        "_311": ["DrawStyleBase"],
        "_312": ["PackagingLimits"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClippingPlane",
    "DrawStyle",
    "DrawStyleBase",
    "PackagingLimits",
)
