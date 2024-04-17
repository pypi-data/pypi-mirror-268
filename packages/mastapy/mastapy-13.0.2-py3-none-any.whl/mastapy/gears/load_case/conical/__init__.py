"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._888 import ConicalGearLoadCase
    from ._889 import ConicalGearSetLoadCase
    from ._890 import ConicalMeshLoadCase
else:
    import_structure = {
        "_888": ["ConicalGearLoadCase"],
        "_889": ["ConicalGearSetLoadCase"],
        "_890": ["ConicalMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearLoadCase",
    "ConicalGearSetLoadCase",
    "ConicalMeshLoadCase",
)
