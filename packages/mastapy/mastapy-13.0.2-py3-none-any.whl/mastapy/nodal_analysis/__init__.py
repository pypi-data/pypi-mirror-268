"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._46 import AbstractLinearConnectionProperties
    from ._47 import AbstractNodalMatrix
    from ._48 import AnalysisSettings
    from ._49 import AnalysisSettingsDatabase
    from ._50 import AnalysisSettingsItem
    from ._51 import BarGeometry
    from ._52 import BarModelAnalysisType
    from ._53 import BarModelExportType
    from ._54 import CouplingType
    from ._55 import CylindricalMisalignmentCalculator
    from ._56 import DampingScalingTypeForInitialTransients
    from ._57 import DiagonalNonLinearStiffness
    from ._58 import ElementOrder
    from ._59 import FEMeshElementEntityOption
    from ._60 import FEMeshingOperation
    from ._61 import FEMeshingOptions
    from ._62 import FEMeshingProblem
    from ._63 import FEMeshingProblems
    from ._64 import FEModalFrequencyComparison
    from ._65 import FENodeOption
    from ._66 import FEStiffness
    from ._67 import FEStiffnessNode
    from ._68 import FEUserSettings
    from ._69 import GearMeshContactStatus
    from ._70 import GravityForceSource
    from ._71 import IntegrationMethod
    from ._72 import LinearDampingConnectionProperties
    from ._73 import LinearStiffnessProperties
    from ._74 import LoadingStatus
    from ._75 import LocalNodeInfo
    from ._76 import MeshingDiameterForGear
    from ._77 import MeshingOptions
    from ._78 import ModeInputType
    from ._79 import NodalMatrix
    from ._80 import NodalMatrixEditorWrapper
    from ._81 import NodalMatrixEditorWrapperColumn
    from ._82 import NodalMatrixEditorWrapperConceptCouplingStiffness
    from ._83 import NodalMatrixRow
    from ._84 import RatingTypeForBearingReliability
    from ._85 import RatingTypeForShaftReliability
    from ._86 import ResultLoggingFrequency
    from ._87 import SectionEnd
    from ._88 import ShaftFEMeshingOptions
    from ._89 import SparseNodalMatrix
    from ._90 import StressResultsType
    from ._91 import TransientSolverOptions
    from ._92 import TransientSolverStatus
    from ._93 import TransientSolverToleranceInputMethod
    from ._94 import ValueInputOption
    from ._95 import VolumeElementShape
else:
    import_structure = {
        "_46": ["AbstractLinearConnectionProperties"],
        "_47": ["AbstractNodalMatrix"],
        "_48": ["AnalysisSettings"],
        "_49": ["AnalysisSettingsDatabase"],
        "_50": ["AnalysisSettingsItem"],
        "_51": ["BarGeometry"],
        "_52": ["BarModelAnalysisType"],
        "_53": ["BarModelExportType"],
        "_54": ["CouplingType"],
        "_55": ["CylindricalMisalignmentCalculator"],
        "_56": ["DampingScalingTypeForInitialTransients"],
        "_57": ["DiagonalNonLinearStiffness"],
        "_58": ["ElementOrder"],
        "_59": ["FEMeshElementEntityOption"],
        "_60": ["FEMeshingOperation"],
        "_61": ["FEMeshingOptions"],
        "_62": ["FEMeshingProblem"],
        "_63": ["FEMeshingProblems"],
        "_64": ["FEModalFrequencyComparison"],
        "_65": ["FENodeOption"],
        "_66": ["FEStiffness"],
        "_67": ["FEStiffnessNode"],
        "_68": ["FEUserSettings"],
        "_69": ["GearMeshContactStatus"],
        "_70": ["GravityForceSource"],
        "_71": ["IntegrationMethod"],
        "_72": ["LinearDampingConnectionProperties"],
        "_73": ["LinearStiffnessProperties"],
        "_74": ["LoadingStatus"],
        "_75": ["LocalNodeInfo"],
        "_76": ["MeshingDiameterForGear"],
        "_77": ["MeshingOptions"],
        "_78": ["ModeInputType"],
        "_79": ["NodalMatrix"],
        "_80": ["NodalMatrixEditorWrapper"],
        "_81": ["NodalMatrixEditorWrapperColumn"],
        "_82": ["NodalMatrixEditorWrapperConceptCouplingStiffness"],
        "_83": ["NodalMatrixRow"],
        "_84": ["RatingTypeForBearingReliability"],
        "_85": ["RatingTypeForShaftReliability"],
        "_86": ["ResultLoggingFrequency"],
        "_87": ["SectionEnd"],
        "_88": ["ShaftFEMeshingOptions"],
        "_89": ["SparseNodalMatrix"],
        "_90": ["StressResultsType"],
        "_91": ["TransientSolverOptions"],
        "_92": ["TransientSolverStatus"],
        "_93": ["TransientSolverToleranceInputMethod"],
        "_94": ["ValueInputOption"],
        "_95": ["VolumeElementShape"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractLinearConnectionProperties",
    "AbstractNodalMatrix",
    "AnalysisSettings",
    "AnalysisSettingsDatabase",
    "AnalysisSettingsItem",
    "BarGeometry",
    "BarModelAnalysisType",
    "BarModelExportType",
    "CouplingType",
    "CylindricalMisalignmentCalculator",
    "DampingScalingTypeForInitialTransients",
    "DiagonalNonLinearStiffness",
    "ElementOrder",
    "FEMeshElementEntityOption",
    "FEMeshingOperation",
    "FEMeshingOptions",
    "FEMeshingProblem",
    "FEMeshingProblems",
    "FEModalFrequencyComparison",
    "FENodeOption",
    "FEStiffness",
    "FEStiffnessNode",
    "FEUserSettings",
    "GearMeshContactStatus",
    "GravityForceSource",
    "IntegrationMethod",
    "LinearDampingConnectionProperties",
    "LinearStiffnessProperties",
    "LoadingStatus",
    "LocalNodeInfo",
    "MeshingDiameterForGear",
    "MeshingOptions",
    "ModeInputType",
    "NodalMatrix",
    "NodalMatrixEditorWrapper",
    "NodalMatrixEditorWrapperColumn",
    "NodalMatrixEditorWrapperConceptCouplingStiffness",
    "NodalMatrixRow",
    "RatingTypeForBearingReliability",
    "RatingTypeForShaftReliability",
    "ResultLoggingFrequency",
    "SectionEnd",
    "ShaftFEMeshingOptions",
    "SparseNodalMatrix",
    "StressResultsType",
    "TransientSolverOptions",
    "TransientSolverStatus",
    "TransientSolverToleranceInputMethod",
    "ValueInputOption",
    "VolumeElementShape",
)
