"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1182 import ConceptGearDesign
    from ._1183 import ConceptGearMeshDesign
    from ._1184 import ConceptGearSetDesign
else:
    import_structure = {
        "_1182": ["ConceptGearDesign"],
        "_1183": ["ConceptGearMeshDesign"],
        "_1184": ["ConceptGearSetDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearDesign",
    "ConceptGearMeshDesign",
    "ConceptGearSetDesign",
)
