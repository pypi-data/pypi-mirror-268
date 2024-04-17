"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._441 import HypoidGearMeshRating
    from ._442 import HypoidGearRating
    from ._443 import HypoidGearSetRating
    from ._444 import HypoidRatingMethod
else:
    import_structure = {
        "_441": ["HypoidGearMeshRating"],
        "_442": ["HypoidGearRating"],
        "_443": ["HypoidGearSetRating"],
        "_444": ["HypoidRatingMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "HypoidGearMeshRating",
    "HypoidGearRating",
    "HypoidGearSetRating",
    "HypoidRatingMethod",
)
