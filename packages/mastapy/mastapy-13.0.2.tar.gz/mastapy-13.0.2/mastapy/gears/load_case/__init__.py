"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._876 import GearLoadCaseBase
    from ._877 import GearSetLoadCaseBase
    from ._878 import MeshLoadCase
else:
    import_structure = {
        "_876": ["GearLoadCaseBase"],
        "_877": ["GearSetLoadCaseBase"],
        "_878": ["MeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearLoadCaseBase",
    "GearSetLoadCaseBase",
    "MeshLoadCase",
)
