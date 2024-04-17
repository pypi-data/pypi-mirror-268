"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._866 import ConicalGearBendingStiffness
    from ._867 import ConicalGearBendingStiffnessNode
    from ._868 import ConicalGearContactStiffness
    from ._869 import ConicalGearContactStiffnessNode
    from ._870 import ConicalGearLoadDistributionAnalysis
    from ._871 import ConicalGearSetLoadDistributionAnalysis
    from ._872 import ConicalMeshedGearLoadDistributionAnalysis
    from ._873 import ConicalMeshLoadDistributionAnalysis
    from ._874 import ConicalMeshLoadDistributionAtRotation
    from ._875 import ConicalMeshLoadedContactLine
else:
    import_structure = {
        "_866": ["ConicalGearBendingStiffness"],
        "_867": ["ConicalGearBendingStiffnessNode"],
        "_868": ["ConicalGearContactStiffness"],
        "_869": ["ConicalGearContactStiffnessNode"],
        "_870": ["ConicalGearLoadDistributionAnalysis"],
        "_871": ["ConicalGearSetLoadDistributionAnalysis"],
        "_872": ["ConicalMeshedGearLoadDistributionAnalysis"],
        "_873": ["ConicalMeshLoadDistributionAnalysis"],
        "_874": ["ConicalMeshLoadDistributionAtRotation"],
        "_875": ["ConicalMeshLoadedContactLine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBendingStiffness",
    "ConicalGearBendingStiffnessNode",
    "ConicalGearContactStiffness",
    "ConicalGearContactStiffnessNode",
    "ConicalGearLoadDistributionAnalysis",
    "ConicalGearSetLoadDistributionAnalysis",
    "ConicalMeshedGearLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAtRotation",
    "ConicalMeshLoadedContactLine",
)
