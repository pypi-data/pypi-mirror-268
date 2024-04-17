"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._960 import WormDesign
    from ._961 import WormGearDesign
    from ._962 import WormGearMeshDesign
    from ._963 import WormGearSetDesign
    from ._964 import WormWheelDesign
else:
    import_structure = {
        "_960": ["WormDesign"],
        "_961": ["WormGearDesign"],
        "_962": ["WormGearMeshDesign"],
        "_963": ["WormGearSetDesign"],
        "_964": ["WormWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormDesign",
    "WormGearDesign",
    "WormGearMeshDesign",
    "WormGearSetDesign",
    "WormWheelDesign",
)
