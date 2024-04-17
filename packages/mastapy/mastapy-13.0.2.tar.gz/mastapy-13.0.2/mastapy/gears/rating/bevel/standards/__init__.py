"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._560 import AGMASpiralBevelGearSingleFlankRating
    from ._561 import AGMASpiralBevelMeshSingleFlankRating
    from ._562 import GleasonSpiralBevelGearSingleFlankRating
    from ._563 import GleasonSpiralBevelMeshSingleFlankRating
    from ._564 import SpiralBevelGearSingleFlankRating
    from ._565 import SpiralBevelMeshSingleFlankRating
    from ._566 import SpiralBevelRateableGear
    from ._567 import SpiralBevelRateableMesh
else:
    import_structure = {
        "_560": ["AGMASpiralBevelGearSingleFlankRating"],
        "_561": ["AGMASpiralBevelMeshSingleFlankRating"],
        "_562": ["GleasonSpiralBevelGearSingleFlankRating"],
        "_563": ["GleasonSpiralBevelMeshSingleFlankRating"],
        "_564": ["SpiralBevelGearSingleFlankRating"],
        "_565": ["SpiralBevelMeshSingleFlankRating"],
        "_566": ["SpiralBevelRateableGear"],
        "_567": ["SpiralBevelRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMASpiralBevelGearSingleFlankRating",
    "AGMASpiralBevelMeshSingleFlankRating",
    "GleasonSpiralBevelGearSingleFlankRating",
    "GleasonSpiralBevelMeshSingleFlankRating",
    "SpiralBevelGearSingleFlankRating",
    "SpiralBevelMeshSingleFlankRating",
    "SpiralBevelRateableGear",
    "SpiralBevelRateableMesh",
)
