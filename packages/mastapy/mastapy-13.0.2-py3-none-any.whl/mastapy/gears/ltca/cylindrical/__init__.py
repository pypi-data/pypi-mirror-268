"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._854 import CylindricalGearBendingStiffness
    from ._855 import CylindricalGearBendingStiffnessNode
    from ._856 import CylindricalGearContactStiffness
    from ._857 import CylindricalGearContactStiffnessNode
    from ._858 import CylindricalGearFESettings
    from ._859 import CylindricalGearLoadDistributionAnalysis
    from ._860 import CylindricalGearMeshLoadDistributionAnalysis
    from ._861 import CylindricalGearMeshLoadedContactLine
    from ._862 import CylindricalGearMeshLoadedContactPoint
    from ._863 import CylindricalGearSetLoadDistributionAnalysis
    from ._864 import CylindricalMeshLoadDistributionAtRotation
    from ._865 import FaceGearSetLoadDistributionAnalysis
else:
    import_structure = {
        "_854": ["CylindricalGearBendingStiffness"],
        "_855": ["CylindricalGearBendingStiffnessNode"],
        "_856": ["CylindricalGearContactStiffness"],
        "_857": ["CylindricalGearContactStiffnessNode"],
        "_858": ["CylindricalGearFESettings"],
        "_859": ["CylindricalGearLoadDistributionAnalysis"],
        "_860": ["CylindricalGearMeshLoadDistributionAnalysis"],
        "_861": ["CylindricalGearMeshLoadedContactLine"],
        "_862": ["CylindricalGearMeshLoadedContactPoint"],
        "_863": ["CylindricalGearSetLoadDistributionAnalysis"],
        "_864": ["CylindricalMeshLoadDistributionAtRotation"],
        "_865": ["FaceGearSetLoadDistributionAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBendingStiffness",
    "CylindricalGearBendingStiffnessNode",
    "CylindricalGearContactStiffness",
    "CylindricalGearContactStiffnessNode",
    "CylindricalGearFESettings",
    "CylindricalGearLoadDistributionAnalysis",
    "CylindricalGearMeshLoadDistributionAnalysis",
    "CylindricalGearMeshLoadedContactLine",
    "CylindricalGearMeshLoadedContactPoint",
    "CylindricalGearSetLoadDistributionAnalysis",
    "CylindricalMeshLoadDistributionAtRotation",
    "FaceGearSetLoadDistributionAnalysis",
)
