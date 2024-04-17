"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._572 import BiasModification
    from ._573 import FlankMicroGeometry
    from ._574 import FlankSide
    from ._575 import LeadModification
    from ._576 import LocationOfEvaluationLowerLimit
    from ._577 import LocationOfEvaluationUpperLimit
    from ._578 import LocationOfRootReliefEvaluation
    from ._579 import LocationOfTipReliefEvaluation
    from ._580 import MainProfileReliefEndsAtTheStartOfRootReliefOption
    from ._581 import MainProfileReliefEndsAtTheStartOfTipReliefOption
    from ._582 import Modification
    from ._583 import ParabolicRootReliefStartsTangentToMainProfileRelief
    from ._584 import ParabolicTipReliefStartsTangentToMainProfileRelief
    from ._585 import ProfileModification
else:
    import_structure = {
        "_572": ["BiasModification"],
        "_573": ["FlankMicroGeometry"],
        "_574": ["FlankSide"],
        "_575": ["LeadModification"],
        "_576": ["LocationOfEvaluationLowerLimit"],
        "_577": ["LocationOfEvaluationUpperLimit"],
        "_578": ["LocationOfRootReliefEvaluation"],
        "_579": ["LocationOfTipReliefEvaluation"],
        "_580": ["MainProfileReliefEndsAtTheStartOfRootReliefOption"],
        "_581": ["MainProfileReliefEndsAtTheStartOfTipReliefOption"],
        "_582": ["Modification"],
        "_583": ["ParabolicRootReliefStartsTangentToMainProfileRelief"],
        "_584": ["ParabolicTipReliefStartsTangentToMainProfileRelief"],
        "_585": ["ProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BiasModification",
    "FlankMicroGeometry",
    "FlankSide",
    "LeadModification",
    "LocationOfEvaluationLowerLimit",
    "LocationOfEvaluationUpperLimit",
    "LocationOfRootReliefEvaluation",
    "LocationOfTipReliefEvaluation",
    "MainProfileReliefEndsAtTheStartOfRootReliefOption",
    "MainProfileReliefEndsAtTheStartOfTipReliefOption",
    "Modification",
    "ParabolicRootReliefStartsTangentToMainProfileRelief",
    "ParabolicTipReliefStartsTangentToMainProfileRelief",
    "ProfileModification",
)
