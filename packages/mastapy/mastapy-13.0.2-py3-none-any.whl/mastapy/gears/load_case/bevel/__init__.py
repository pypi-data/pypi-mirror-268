"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._894 import BevelLoadCase
    from ._895 import BevelMeshLoadCase
    from ._896 import BevelSetLoadCase
else:
    import_structure = {
        "_894": ["BevelLoadCase"],
        "_895": ["BevelMeshLoadCase"],
        "_896": ["BevelSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelLoadCase",
    "BevelMeshLoadCase",
    "BevelSetLoadCase",
)
