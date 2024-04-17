"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._103 import BackwardEulerAccelerationStepHalvingTransientSolver
    from ._104 import BackwardEulerTransientSolver
    from ._105 import DenseStiffnessSolver
    from ._106 import DynamicSolver
    from ._107 import InternalTransientSolver
    from ._108 import LobattoIIIATransientSolver
    from ._109 import LobattoIIICTransientSolver
    from ._110 import NewmarkAccelerationTransientSolver
    from ._111 import NewmarkTransientSolver
    from ._112 import SemiImplicitTransientSolver
    from ._113 import SimpleAccelerationBasedStepHalvingTransientSolver
    from ._114 import SimpleVelocityBasedStepHalvingTransientSolver
    from ._115 import SingularDegreeOfFreedomAnalysis
    from ._116 import SingularValuesAnalysis
    from ._117 import SingularVectorAnalysis
    from ._118 import Solver
    from ._119 import StepHalvingTransientSolver
    from ._120 import StiffnessSolver
    from ._121 import TransientSolver
    from ._122 import WilsonThetaTransientSolver
else:
    import_structure = {
        "_103": ["BackwardEulerAccelerationStepHalvingTransientSolver"],
        "_104": ["BackwardEulerTransientSolver"],
        "_105": ["DenseStiffnessSolver"],
        "_106": ["DynamicSolver"],
        "_107": ["InternalTransientSolver"],
        "_108": ["LobattoIIIATransientSolver"],
        "_109": ["LobattoIIICTransientSolver"],
        "_110": ["NewmarkAccelerationTransientSolver"],
        "_111": ["NewmarkTransientSolver"],
        "_112": ["SemiImplicitTransientSolver"],
        "_113": ["SimpleAccelerationBasedStepHalvingTransientSolver"],
        "_114": ["SimpleVelocityBasedStepHalvingTransientSolver"],
        "_115": ["SingularDegreeOfFreedomAnalysis"],
        "_116": ["SingularValuesAnalysis"],
        "_117": ["SingularVectorAnalysis"],
        "_118": ["Solver"],
        "_119": ["StepHalvingTransientSolver"],
        "_120": ["StiffnessSolver"],
        "_121": ["TransientSolver"],
        "_122": ["WilsonThetaTransientSolver"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BackwardEulerAccelerationStepHalvingTransientSolver",
    "BackwardEulerTransientSolver",
    "DenseStiffnessSolver",
    "DynamicSolver",
    "InternalTransientSolver",
    "LobattoIIIATransientSolver",
    "LobattoIIICTransientSolver",
    "NewmarkAccelerationTransientSolver",
    "NewmarkTransientSolver",
    "SemiImplicitTransientSolver",
    "SimpleAccelerationBasedStepHalvingTransientSolver",
    "SimpleVelocityBasedStepHalvingTransientSolver",
    "SingularDegreeOfFreedomAnalysis",
    "SingularValuesAnalysis",
    "SingularVectorAnalysis",
    "Solver",
    "StepHalvingTransientSolver",
    "StiffnessSolver",
    "TransientSolver",
    "WilsonThetaTransientSolver",
)
