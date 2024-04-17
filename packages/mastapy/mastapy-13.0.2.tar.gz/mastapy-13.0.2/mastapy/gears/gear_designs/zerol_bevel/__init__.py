"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._956 import ZerolBevelGearDesign
    from ._957 import ZerolBevelGearMeshDesign
    from ._958 import ZerolBevelGearSetDesign
    from ._959 import ZerolBevelMeshedGearDesign
else:
    import_structure = {
        "_956": ["ZerolBevelGearDesign"],
        "_957": ["ZerolBevelGearMeshDesign"],
        "_958": ["ZerolBevelGearSetDesign"],
        "_959": ["ZerolBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ZerolBevelGearDesign",
    "ZerolBevelGearMeshDesign",
    "ZerolBevelGearSetDesign",
    "ZerolBevelMeshedGearDesign",
)
