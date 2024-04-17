"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1247 import ElementPropertyClass
    from ._1248 import MaterialPropertyClass
else:
    import_structure = {
        "_1247": ["ElementPropertyClass"],
        "_1248": ["MaterialPropertyClass"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElementPropertyClass",
    "MaterialPropertyClass",
)
