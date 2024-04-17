"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1443 import ShaftHubConnectionRating
else:
    import_structure = {
        "_1443": ["ShaftHubConnectionRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = ("ShaftHubConnectionRating",)
