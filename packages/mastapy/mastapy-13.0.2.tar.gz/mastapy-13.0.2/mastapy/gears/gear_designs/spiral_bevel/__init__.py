"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._973 import SpiralBevelGearDesign
    from ._974 import SpiralBevelGearMeshDesign
    from ._975 import SpiralBevelGearSetDesign
    from ._976 import SpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_973": ["SpiralBevelGearDesign"],
        "_974": ["SpiralBevelGearMeshDesign"],
        "_975": ["SpiralBevelGearSetDesign"],
        "_976": ["SpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpiralBevelGearDesign",
    "SpiralBevelGearMeshDesign",
    "SpiralBevelGearSetDesign",
    "SpiralBevelMeshedGearDesign",
)
