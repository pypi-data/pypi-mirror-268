"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2232 import PerformRegressionTestFromMASTAOptions
else:
    import_structure = {
        "_2232": ["PerformRegressionTestFromMASTAOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = ("PerformRegressionTestFromMASTAOptions",)
