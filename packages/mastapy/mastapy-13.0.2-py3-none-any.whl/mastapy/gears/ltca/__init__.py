"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._828 import ConicalGearFilletStressResults
    from ._829 import ConicalGearRootFilletStressResults
    from ._830 import ContactResultType
    from ._831 import CylindricalGearFilletNodeStressResults
    from ._832 import CylindricalGearFilletNodeStressResultsColumn
    from ._833 import CylindricalGearFilletNodeStressResultsRow
    from ._834 import CylindricalGearRootFilletStressResults
    from ._835 import CylindricalMeshedGearLoadDistributionAnalysis
    from ._836 import GearBendingStiffness
    from ._837 import GearBendingStiffnessNode
    from ._838 import GearContactStiffness
    from ._839 import GearContactStiffnessNode
    from ._840 import GearFilletNodeStressResults
    from ._841 import GearFilletNodeStressResultsColumn
    from ._842 import GearFilletNodeStressResultsRow
    from ._843 import GearLoadDistributionAnalysis
    from ._844 import GearMeshLoadDistributionAnalysis
    from ._845 import GearMeshLoadDistributionAtRotation
    from ._846 import GearMeshLoadedContactLine
    from ._847 import GearMeshLoadedContactPoint
    from ._848 import GearRootFilletStressResults
    from ._849 import GearSetLoadDistributionAnalysis
    from ._850 import GearStiffness
    from ._851 import GearStiffnessNode
    from ._852 import MeshedGearLoadDistributionAnalysisAtRotation
    from ._853 import UseAdvancedLTCAOptions
else:
    import_structure = {
        "_828": ["ConicalGearFilletStressResults"],
        "_829": ["ConicalGearRootFilletStressResults"],
        "_830": ["ContactResultType"],
        "_831": ["CylindricalGearFilletNodeStressResults"],
        "_832": ["CylindricalGearFilletNodeStressResultsColumn"],
        "_833": ["CylindricalGearFilletNodeStressResultsRow"],
        "_834": ["CylindricalGearRootFilletStressResults"],
        "_835": ["CylindricalMeshedGearLoadDistributionAnalysis"],
        "_836": ["GearBendingStiffness"],
        "_837": ["GearBendingStiffnessNode"],
        "_838": ["GearContactStiffness"],
        "_839": ["GearContactStiffnessNode"],
        "_840": ["GearFilletNodeStressResults"],
        "_841": ["GearFilletNodeStressResultsColumn"],
        "_842": ["GearFilletNodeStressResultsRow"],
        "_843": ["GearLoadDistributionAnalysis"],
        "_844": ["GearMeshLoadDistributionAnalysis"],
        "_845": ["GearMeshLoadDistributionAtRotation"],
        "_846": ["GearMeshLoadedContactLine"],
        "_847": ["GearMeshLoadedContactPoint"],
        "_848": ["GearRootFilletStressResults"],
        "_849": ["GearSetLoadDistributionAnalysis"],
        "_850": ["GearStiffness"],
        "_851": ["GearStiffnessNode"],
        "_852": ["MeshedGearLoadDistributionAnalysisAtRotation"],
        "_853": ["UseAdvancedLTCAOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFilletStressResults",
    "ConicalGearRootFilletStressResults",
    "ContactResultType",
    "CylindricalGearFilletNodeStressResults",
    "CylindricalGearFilletNodeStressResultsColumn",
    "CylindricalGearFilletNodeStressResultsRow",
    "CylindricalGearRootFilletStressResults",
    "CylindricalMeshedGearLoadDistributionAnalysis",
    "GearBendingStiffness",
    "GearBendingStiffnessNode",
    "GearContactStiffness",
    "GearContactStiffnessNode",
    "GearFilletNodeStressResults",
    "GearFilletNodeStressResultsColumn",
    "GearFilletNodeStressResultsRow",
    "GearLoadDistributionAnalysis",
    "GearMeshLoadDistributionAnalysis",
    "GearMeshLoadDistributionAtRotation",
    "GearMeshLoadedContactLine",
    "GearMeshLoadedContactPoint",
    "GearRootFilletStressResults",
    "GearSetLoadDistributionAnalysis",
    "GearStiffness",
    "GearStiffnessNode",
    "MeshedGearLoadDistributionAnalysisAtRotation",
    "UseAdvancedLTCAOptions",
)
