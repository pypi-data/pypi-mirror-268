"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2122 import ANSIABMA112014Results
    from ._2123 import ANSIABMA92015Results
    from ._2124 import ANSIABMAResults
else:
    import_structure = {
        "_2122": ["ANSIABMA112014Results"],
        "_2123": ["ANSIABMA92015Results"],
        "_2124": ["ANSIABMAResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ANSIABMA112014Results",
    "ANSIABMA92015Results",
    "ANSIABMAResults",
)
