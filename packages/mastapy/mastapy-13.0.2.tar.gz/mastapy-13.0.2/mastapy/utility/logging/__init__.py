"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1815 import Logger
    from ._1816 import Message
else:
    import_structure = {
        "_1815": ["Logger"],
        "_1816": ["Message"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Logger",
    "Message",
)
