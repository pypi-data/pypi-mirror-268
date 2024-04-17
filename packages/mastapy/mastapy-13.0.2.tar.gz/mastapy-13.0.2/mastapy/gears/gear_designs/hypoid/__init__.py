"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._989 import HypoidGearDesign
    from ._990 import HypoidGearMeshDesign
    from ._991 import HypoidGearSetDesign
    from ._992 import HypoidMeshedGearDesign
else:
    import_structure = {
        "_989": ["HypoidGearDesign"],
        "_990": ["HypoidGearMeshDesign"],
        "_991": ["HypoidGearSetDesign"],
        "_992": ["HypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "HypoidGearDesign",
    "HypoidGearMeshDesign",
    "HypoidGearSetDesign",
    "HypoidMeshedGearDesign",
)
