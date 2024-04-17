"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5862 import AbstractSingleWhineAnalysisResultsPropertyAccessor
    from ._5863 import DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic
    from ._5864 import DataPointForResponseOfANodeAtAFrequencyToAHarmonic
    from ._5865 import FEPartHarmonicAnalysisResultsPropertyAccessor
    from ._5866 import FEPartSingleWhineAnalysisResultsPropertyAccessor
    from ._5867 import HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
    from ._5868 import HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
    from ._5869 import HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic
    from ._5870 import HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
    from ._5871 import HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
    from ._5872 import HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
    from ._5873 import HarmonicAnalysisResultsPropertyAccessor
    from ._5874 import ResultsForMultipleOrders
    from ._5875 import ResultsForMultipleOrdersForFESurface
    from ._5876 import ResultsForMultipleOrdersForGroups
    from ._5877 import ResultsForOrder
    from ._5878 import ResultsForOrderIncludingGroups
    from ._5879 import ResultsForOrderIncludingNodes
    from ._5880 import ResultsForOrderIncludingSurfaces
    from ._5881 import ResultsForResponseOfAComponentOrSurfaceInAHarmonic
    from ._5882 import ResultsForResponseOfANodeOnAHarmonic
    from ._5883 import ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic
    from ._5884 import RootAssemblyHarmonicAnalysisResultsPropertyAccessor
    from ._5885 import RootAssemblySingleWhineAnalysisResultsPropertyAccessor
    from ._5886 import SingleWhineAnalysisResultsPropertyAccessor
else:
    import_structure = {
        "_5862": ["AbstractSingleWhineAnalysisResultsPropertyAccessor"],
        "_5863": ["DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic"],
        "_5864": ["DataPointForResponseOfANodeAtAFrequencyToAHarmonic"],
        "_5865": ["FEPartHarmonicAnalysisResultsPropertyAccessor"],
        "_5866": ["FEPartSingleWhineAnalysisResultsPropertyAccessor"],
        "_5867": ["HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic"],
        "_5868": ["HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic"],
        "_5869": ["HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic"],
        "_5870": ["HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic"],
        "_5871": ["HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic"],
        "_5872": ["HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic"],
        "_5873": ["HarmonicAnalysisResultsPropertyAccessor"],
        "_5874": ["ResultsForMultipleOrders"],
        "_5875": ["ResultsForMultipleOrdersForFESurface"],
        "_5876": ["ResultsForMultipleOrdersForGroups"],
        "_5877": ["ResultsForOrder"],
        "_5878": ["ResultsForOrderIncludingGroups"],
        "_5879": ["ResultsForOrderIncludingNodes"],
        "_5880": ["ResultsForOrderIncludingSurfaces"],
        "_5881": ["ResultsForResponseOfAComponentOrSurfaceInAHarmonic"],
        "_5882": ["ResultsForResponseOfANodeOnAHarmonic"],
        "_5883": ["ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic"],
        "_5884": ["RootAssemblyHarmonicAnalysisResultsPropertyAccessor"],
        "_5885": ["RootAssemblySingleWhineAnalysisResultsPropertyAccessor"],
        "_5886": ["SingleWhineAnalysisResultsPropertyAccessor"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractSingleWhineAnalysisResultsPropertyAccessor",
    "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
    "DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
    "FEPartHarmonicAnalysisResultsPropertyAccessor",
    "FEPartSingleWhineAnalysisResultsPropertyAccessor",
    "HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
    "HarmonicAnalysisResultsPropertyAccessor",
    "ResultsForMultipleOrders",
    "ResultsForMultipleOrdersForFESurface",
    "ResultsForMultipleOrdersForGroups",
    "ResultsForOrder",
    "ResultsForOrderIncludingGroups",
    "ResultsForOrderIncludingNodes",
    "ResultsForOrderIncludingSurfaces",
    "ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
    "ResultsForResponseOfANodeOnAHarmonic",
    "ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic",
    "RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
    "RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
    "SingleWhineAnalysisResultsPropertyAccessor",
)
