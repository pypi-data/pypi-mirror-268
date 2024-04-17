"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._985 import KlingelnbergConicalGearDesign
    from ._986 import KlingelnbergConicalGearMeshDesign
    from ._987 import KlingelnbergConicalGearSetDesign
    from ._988 import KlingelnbergConicalMeshedGearDesign
else:
    import_structure = {
        "_985": ["KlingelnbergConicalGearDesign"],
        "_986": ["KlingelnbergConicalGearMeshDesign"],
        "_987": ["KlingelnbergConicalGearSetDesign"],
        "_988": ["KlingelnbergConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergConicalGearDesign",
    "KlingelnbergConicalGearMeshDesign",
    "KlingelnbergConicalGearSetDesign",
    "KlingelnbergConicalMeshedGearDesign",
)
