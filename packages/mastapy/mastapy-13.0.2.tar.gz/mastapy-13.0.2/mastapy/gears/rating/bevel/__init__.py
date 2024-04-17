"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._557 import BevelGearMeshRating
    from ._558 import BevelGearRating
    from ._559 import BevelGearSetRating
else:
    import_structure = {
        "_557": ["BevelGearMeshRating"],
        "_558": ["BevelGearRating"],
        "_559": ["BevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelGearMeshRating",
    "BevelGearRating",
    "BevelGearSetRating",
)
