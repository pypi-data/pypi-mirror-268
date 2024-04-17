"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1933 import ISO2812007BallBearingDynamicEquivalentLoadCalculator
else:
    import_structure = {
        "_1933": ["ISO2812007BallBearingDynamicEquivalentLoadCalculator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = ("ISO2812007BallBearingDynamicEquivalentLoadCalculator",)
