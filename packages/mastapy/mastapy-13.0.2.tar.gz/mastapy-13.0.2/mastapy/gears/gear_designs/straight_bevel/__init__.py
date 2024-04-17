"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._965 import StraightBevelGearDesign
    from ._966 import StraightBevelGearMeshDesign
    from ._967 import StraightBevelGearSetDesign
    from ._968 import StraightBevelMeshedGearDesign
else:
    import_structure = {
        "_965": ["StraightBevelGearDesign"],
        "_966": ["StraightBevelGearMeshDesign"],
        "_967": ["StraightBevelGearSetDesign"],
        "_968": ["StraightBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelGearDesign",
    "StraightBevelGearMeshDesign",
    "StraightBevelGearSetDesign",
    "StraightBevelMeshedGearDesign",
)
