"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._171 import ContactType
    from ._172 import ElectricMachineAnalysisPeriod
    from ._173 import ElmerResults
    from ._174 import ElmerResultsFromElectroMagneticAnalysis
    from ._175 import ElmerResultsViewable
    from ._176 import ElmerResultType
    from ._177 import MechanicalContactSpecification
else:
    import_structure = {
        "_171": ["ContactType"],
        "_172": ["ElectricMachineAnalysisPeriod"],
        "_173": ["ElmerResults"],
        "_174": ["ElmerResultsFromElectroMagneticAnalysis"],
        "_175": ["ElmerResultsViewable"],
        "_176": ["ElmerResultType"],
        "_177": ["MechanicalContactSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactType",
    "ElectricMachineAnalysisPeriod",
    "ElmerResults",
    "ElmerResultsFromElectroMagneticAnalysis",
    "ElmerResultsViewable",
    "ElmerResultType",
    "MechanicalContactSpecification",
)
