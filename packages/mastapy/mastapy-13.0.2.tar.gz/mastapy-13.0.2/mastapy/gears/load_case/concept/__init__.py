"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._891 import ConceptGearLoadCase
    from ._892 import ConceptGearSetLoadCase
    from ._893 import ConceptMeshLoadCase
else:
    import_structure = {
        "_891": ["ConceptGearLoadCase"],
        "_892": ["ConceptGearSetLoadCase"],
        "_893": ["ConceptMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearLoadCase",
    "ConceptGearSetLoadCase",
    "ConceptMeshLoadCase",
)
