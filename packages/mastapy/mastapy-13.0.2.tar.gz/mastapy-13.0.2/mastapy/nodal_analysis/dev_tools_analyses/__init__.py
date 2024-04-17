"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._181 import DrawStyleForFE
    from ._182 import EigenvalueOptions
    from ._183 import ElementFaceGroup
    from ._184 import ElementGroup
    from ._185 import FEEntityGroup
    from ._186 import FEEntityGroupInteger
    from ._187 import FEModel
    from ._188 import FEModelComponentDrawStyle
    from ._189 import FEModelHarmonicAnalysisDrawStyle
    from ._190 import FEModelInstanceDrawStyle
    from ._191 import FEModelModalAnalysisDrawStyle
    from ._192 import FEModelPart
    from ._193 import FEModelSetupViewType
    from ._194 import FEModelStaticAnalysisDrawStyle
    from ._195 import FEModelTabDrawStyle
    from ._196 import FEModelTransparencyDrawStyle
    from ._197 import FENodeSelectionDrawStyle
    from ._198 import FESelectionMode
    from ._199 import FESurfaceAndNonDeformedDrawingOption
    from ._200 import FESurfaceDrawingOption
    from ._201 import MassMatrixType
    from ._202 import ModelSplittingMethod
    from ._203 import NodeGroup
    from ._204 import NoneSelectedAllOption
    from ._205 import RigidCouplingType
else:
    import_structure = {
        "_181": ["DrawStyleForFE"],
        "_182": ["EigenvalueOptions"],
        "_183": ["ElementFaceGroup"],
        "_184": ["ElementGroup"],
        "_185": ["FEEntityGroup"],
        "_186": ["FEEntityGroupInteger"],
        "_187": ["FEModel"],
        "_188": ["FEModelComponentDrawStyle"],
        "_189": ["FEModelHarmonicAnalysisDrawStyle"],
        "_190": ["FEModelInstanceDrawStyle"],
        "_191": ["FEModelModalAnalysisDrawStyle"],
        "_192": ["FEModelPart"],
        "_193": ["FEModelSetupViewType"],
        "_194": ["FEModelStaticAnalysisDrawStyle"],
        "_195": ["FEModelTabDrawStyle"],
        "_196": ["FEModelTransparencyDrawStyle"],
        "_197": ["FENodeSelectionDrawStyle"],
        "_198": ["FESelectionMode"],
        "_199": ["FESurfaceAndNonDeformedDrawingOption"],
        "_200": ["FESurfaceDrawingOption"],
        "_201": ["MassMatrixType"],
        "_202": ["ModelSplittingMethod"],
        "_203": ["NodeGroup"],
        "_204": ["NoneSelectedAllOption"],
        "_205": ["RigidCouplingType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DrawStyleForFE",
    "EigenvalueOptions",
    "ElementFaceGroup",
    "ElementGroup",
    "FEEntityGroup",
    "FEEntityGroupInteger",
    "FEModel",
    "FEModelComponentDrawStyle",
    "FEModelHarmonicAnalysisDrawStyle",
    "FEModelInstanceDrawStyle",
    "FEModelModalAnalysisDrawStyle",
    "FEModelPart",
    "FEModelSetupViewType",
    "FEModelStaticAnalysisDrawStyle",
    "FEModelTabDrawStyle",
    "FEModelTransparencyDrawStyle",
    "FENodeSelectionDrawStyle",
    "FESelectionMode",
    "FESurfaceAndNonDeformedDrawingOption",
    "FESurfaceDrawingOption",
    "MassMatrixType",
    "ModelSplittingMethod",
    "NodeGroup",
    "NoneSelectedAllOption",
    "RigidCouplingType",
)
