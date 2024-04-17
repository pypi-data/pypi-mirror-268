"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._879 import WormGearLoadCase
    from ._880 import WormGearSetLoadCase
    from ._881 import WormMeshLoadCase
else:
    import_structure = {
        "_879": ["WormGearLoadCase"],
        "_880": ["WormGearSetLoadCase"],
        "_881": ["WormMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormGearLoadCase",
    "WormGearSetLoadCase",
    "WormMeshLoadCase",
)
