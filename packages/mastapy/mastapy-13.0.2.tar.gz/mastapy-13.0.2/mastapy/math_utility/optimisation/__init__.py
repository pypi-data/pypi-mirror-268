"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1546 import AbstractOptimisable
    from ._1547 import DesignSpaceSearchStrategyDatabase
    from ._1548 import InputSetter
    from ._1549 import Optimisable
    from ._1550 import OptimisationHistory
    from ._1551 import OptimizationInput
    from ._1552 import OptimizationVariable
    from ._1553 import ParetoOptimisationFilter
    from ._1554 import ParetoOptimisationInput
    from ._1555 import ParetoOptimisationOutput
    from ._1556 import ParetoOptimisationStrategy
    from ._1557 import ParetoOptimisationStrategyBars
    from ._1558 import ParetoOptimisationStrategyChartInformation
    from ._1559 import ParetoOptimisationStrategyDatabase
    from ._1560 import ParetoOptimisationVariable
    from ._1561 import ParetoOptimisationVariableBase
    from ._1562 import PropertyTargetForDominantCandidateSearch
    from ._1563 import ReportingOptimizationInput
    from ._1564 import SpecifyOptimisationInputAs
    from ._1565 import TargetingPropertyTo
else:
    import_structure = {
        "_1546": ["AbstractOptimisable"],
        "_1547": ["DesignSpaceSearchStrategyDatabase"],
        "_1548": ["InputSetter"],
        "_1549": ["Optimisable"],
        "_1550": ["OptimisationHistory"],
        "_1551": ["OptimizationInput"],
        "_1552": ["OptimizationVariable"],
        "_1553": ["ParetoOptimisationFilter"],
        "_1554": ["ParetoOptimisationInput"],
        "_1555": ["ParetoOptimisationOutput"],
        "_1556": ["ParetoOptimisationStrategy"],
        "_1557": ["ParetoOptimisationStrategyBars"],
        "_1558": ["ParetoOptimisationStrategyChartInformation"],
        "_1559": ["ParetoOptimisationStrategyDatabase"],
        "_1560": ["ParetoOptimisationVariable"],
        "_1561": ["ParetoOptimisationVariableBase"],
        "_1562": ["PropertyTargetForDominantCandidateSearch"],
        "_1563": ["ReportingOptimizationInput"],
        "_1564": ["SpecifyOptimisationInputAs"],
        "_1565": ["TargetingPropertyTo"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractOptimisable",
    "DesignSpaceSearchStrategyDatabase",
    "InputSetter",
    "Optimisable",
    "OptimisationHistory",
    "OptimizationInput",
    "OptimizationVariable",
    "ParetoOptimisationFilter",
    "ParetoOptimisationInput",
    "ParetoOptimisationOutput",
    "ParetoOptimisationStrategy",
    "ParetoOptimisationStrategyBars",
    "ParetoOptimisationStrategyChartInformation",
    "ParetoOptimisationStrategyDatabase",
    "ParetoOptimisationVariable",
    "ParetoOptimisationVariableBase",
    "PropertyTargetForDominantCandidateSearch",
    "ReportingOptimizationInput",
    "SpecifyOptimisationInputAs",
    "TargetingPropertyTo",
)
