"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._445 import GleasonHypoidGearSingleFlankRating
    from ._446 import GleasonHypoidMeshSingleFlankRating
    from ._447 import HypoidRateableMesh
else:
    import_structure = {
        "_445": ["GleasonHypoidGearSingleFlankRating"],
        "_446": ["GleasonHypoidMeshSingleFlankRating"],
        "_447": ["HypoidRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GleasonHypoidGearSingleFlankRating",
    "GleasonHypoidMeshSingleFlankRating",
    "HypoidRateableMesh",
)
