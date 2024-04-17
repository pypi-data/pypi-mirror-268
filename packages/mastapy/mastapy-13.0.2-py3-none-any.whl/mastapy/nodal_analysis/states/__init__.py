"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._123 import ElementScalarState
    from ._124 import ElementVectorState
    from ._125 import EntityVectorState
    from ._126 import NodeScalarState
    from ._127 import NodeVectorState
else:
    import_structure = {
        "_123": ["ElementScalarState"],
        "_124": ["ElementVectorState"],
        "_125": ["EntityVectorState"],
        "_126": ["NodeScalarState"],
        "_127": ["NodeVectorState"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElementScalarState",
    "ElementVectorState",
    "EntityVectorState",
    "NodeScalarState",
    "NodeVectorState",
)
