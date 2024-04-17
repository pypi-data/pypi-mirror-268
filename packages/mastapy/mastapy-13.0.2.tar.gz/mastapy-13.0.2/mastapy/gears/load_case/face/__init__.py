"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._882 import FaceGearLoadCase
    from ._883 import FaceGearSetLoadCase
    from ._884 import FaceMeshLoadCase
else:
    import_structure = {
        "_882": ["FaceGearLoadCase"],
        "_883": ["FaceGearSetLoadCase"],
        "_884": ["FaceMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearLoadCase",
    "FaceGearSetLoadCase",
    "FaceMeshLoadCase",
)
