"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1198 import AGMAGleasonConicalAccuracyGrades
    from ._1199 import AGMAGleasonConicalGearDesign
    from ._1200 import AGMAGleasonConicalGearMeshDesign
    from ._1201 import AGMAGleasonConicalGearSetDesign
    from ._1202 import AGMAGleasonConicalMeshedGearDesign
else:
    import_structure = {
        "_1198": ["AGMAGleasonConicalAccuracyGrades"],
        "_1199": ["AGMAGleasonConicalGearDesign"],
        "_1200": ["AGMAGleasonConicalGearMeshDesign"],
        "_1201": ["AGMAGleasonConicalGearSetDesign"],
        "_1202": ["AGMAGleasonConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalAccuracyGrades",
    "AGMAGleasonConicalGearDesign",
    "AGMAGleasonConicalGearMeshDesign",
    "AGMAGleasonConicalGearSetDesign",
    "AGMAGleasonConicalMeshedGearDesign",
)
