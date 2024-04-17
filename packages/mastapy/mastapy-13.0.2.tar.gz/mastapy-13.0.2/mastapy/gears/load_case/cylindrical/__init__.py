"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._885 import CylindricalGearLoadCase
    from ._886 import CylindricalGearSetLoadCase
    from ._887 import CylindricalMeshLoadCase
else:
    import_structure = {
        "_885": ["CylindricalGearLoadCase"],
        "_886": ["CylindricalGearSetLoadCase"],
        "_887": ["CylindricalMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLoadCase",
    "CylindricalGearSetLoadCase",
    "CylindricalMeshLoadCase",
)
