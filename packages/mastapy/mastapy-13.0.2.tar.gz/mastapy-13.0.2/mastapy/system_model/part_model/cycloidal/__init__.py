"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2575 import CycloidalAssembly
    from ._2576 import CycloidalDisc
    from ._2577 import RingPins
else:
    import_structure = {
        "_2575": ["CycloidalAssembly"],
        "_2576": ["CycloidalDisc"],
        "_2577": ["RingPins"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalAssembly",
    "CycloidalDisc",
    "RingPins",
)
