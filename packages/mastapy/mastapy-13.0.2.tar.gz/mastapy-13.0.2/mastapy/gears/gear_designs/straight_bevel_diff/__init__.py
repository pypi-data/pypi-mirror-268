"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._969 import StraightBevelDiffGearDesign
    from ._970 import StraightBevelDiffGearMeshDesign
    from ._971 import StraightBevelDiffGearSetDesign
    from ._972 import StraightBevelDiffMeshedGearDesign
else:
    import_structure = {
        "_969": ["StraightBevelDiffGearDesign"],
        "_970": ["StraightBevelDiffGearMeshDesign"],
        "_971": ["StraightBevelDiffGearSetDesign"],
        "_972": ["StraightBevelDiffMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelDiffGearDesign",
    "StraightBevelDiffGearMeshDesign",
    "StraightBevelDiffGearSetDesign",
    "StraightBevelDiffMeshedGearDesign",
)
