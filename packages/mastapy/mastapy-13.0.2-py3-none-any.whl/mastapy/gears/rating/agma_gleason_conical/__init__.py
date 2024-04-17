"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._568 import AGMAGleasonConicalGearMeshRating
    from ._569 import AGMAGleasonConicalGearRating
    from ._570 import AGMAGleasonConicalGearSetRating
    from ._571 import AGMAGleasonConicalRateableMesh
else:
    import_structure = {
        "_568": ["AGMAGleasonConicalGearMeshRating"],
        "_569": ["AGMAGleasonConicalGearRating"],
        "_570": ["AGMAGleasonConicalGearSetRating"],
        "_571": ["AGMAGleasonConicalRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMeshRating",
    "AGMAGleasonConicalGearRating",
    "AGMAGleasonConicalGearSetRating",
    "AGMAGleasonConicalRateableMesh",
)
