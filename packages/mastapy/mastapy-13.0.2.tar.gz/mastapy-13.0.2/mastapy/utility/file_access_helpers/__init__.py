"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1824 import ColumnTitle
    from ._1825 import TextFileDelimiterOptions
else:
    import_structure = {
        "_1824": ["ColumnTitle"],
        "_1825": ["TextFileDelimiterOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ColumnTitle",
    "TextFileDelimiterOptions",
)
