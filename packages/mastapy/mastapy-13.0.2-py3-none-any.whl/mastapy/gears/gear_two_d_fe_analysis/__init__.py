"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._897 import CylindricalGearMeshTIFFAnalysis
    from ._898 import CylindricalGearMeshTIFFAnalysisDutyCycle
    from ._899 import CylindricalGearSetTIFFAnalysis
    from ._900 import CylindricalGearSetTIFFAnalysisDutyCycle
    from ._901 import CylindricalGearTIFFAnalysis
    from ._902 import CylindricalGearTIFFAnalysisDutyCycle
    from ._903 import CylindricalGearTwoDimensionalFEAnalysis
    from ._904 import FindleyCriticalPlaneAnalysis
else:
    import_structure = {
        "_897": ["CylindricalGearMeshTIFFAnalysis"],
        "_898": ["CylindricalGearMeshTIFFAnalysisDutyCycle"],
        "_899": ["CylindricalGearSetTIFFAnalysis"],
        "_900": ["CylindricalGearSetTIFFAnalysisDutyCycle"],
        "_901": ["CylindricalGearTIFFAnalysis"],
        "_902": ["CylindricalGearTIFFAnalysisDutyCycle"],
        "_903": ["CylindricalGearTwoDimensionalFEAnalysis"],
        "_904": ["FindleyCriticalPlaneAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshTIFFAnalysis",
    "CylindricalGearMeshTIFFAnalysisDutyCycle",
    "CylindricalGearSetTIFFAnalysis",
    "CylindricalGearSetTIFFAnalysisDutyCycle",
    "CylindricalGearTIFFAnalysis",
    "CylindricalGearTIFFAnalysisDutyCycle",
    "CylindricalGearTwoDimensionalFEAnalysis",
    "FindleyCriticalPlaneAnalysis",
)
