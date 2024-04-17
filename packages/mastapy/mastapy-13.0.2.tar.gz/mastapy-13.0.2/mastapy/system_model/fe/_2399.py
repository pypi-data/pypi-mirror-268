"""FESubstructureWithSelectionForHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.fe import _2397
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_SELECTION_FOR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureWithSelectionForHarmonicAnalysis"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _189
    from mastapy.system_model.fe import _2407, _2367


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureWithSelectionForHarmonicAnalysis",)


Self = TypeVar("Self", bound="FESubstructureWithSelectionForHarmonicAnalysis")


class FESubstructureWithSelectionForHarmonicAnalysis(_2397.FESubstructureWithSelection):
    """FESubstructureWithSelectionForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_WITH_SELECTION_FOR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FESubstructureWithSelectionForHarmonicAnalysis"
    )

    class _Cast_FESubstructureWithSelectionForHarmonicAnalysis:
        """Special nested class for casting FESubstructureWithSelectionForHarmonicAnalysis to subclasses."""

        def __init__(
            self: "FESubstructureWithSelectionForHarmonicAnalysis._Cast_FESubstructureWithSelectionForHarmonicAnalysis",
            parent: "FESubstructureWithSelectionForHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def fe_substructure_with_selection(
            self: "FESubstructureWithSelectionForHarmonicAnalysis._Cast_FESubstructureWithSelectionForHarmonicAnalysis",
        ) -> "_2397.FESubstructureWithSelection":
            return self._parent._cast(_2397.FESubstructureWithSelection)

        @property
        def base_fe_with_selection(
            self: "FESubstructureWithSelectionForHarmonicAnalysis._Cast_FESubstructureWithSelectionForHarmonicAnalysis",
        ) -> "_2367.BaseFEWithSelection":
            from mastapy.system_model.fe import _2367

            return self._parent._cast(_2367.BaseFEWithSelection)

        @property
        def fe_substructure_with_selection_for_harmonic_analysis(
            self: "FESubstructureWithSelectionForHarmonicAnalysis._Cast_FESubstructureWithSelectionForHarmonicAnalysis",
        ) -> "FESubstructureWithSelectionForHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "FESubstructureWithSelectionForHarmonicAnalysis._Cast_FESubstructureWithSelectionForHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "FESubstructureWithSelectionForHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def alpha_damping_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AlphaDampingValue

        if temp is None:
            return 0.0

        return temp

    @alpha_damping_value.setter
    @enforce_parameter_types
    def alpha_damping_value(self: Self, value: "float"):
        self.wrapped.AlphaDampingValue = float(value) if value is not None else 0.0

    @property
    def beta_damping_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BetaDampingValue

        if temp is None:
            return 0.0

        return temp

    @beta_damping_value.setter
    @enforce_parameter_types
    def beta_damping_value(self: Self, value: "float"):
        self.wrapped.BetaDampingValue = float(value) if value is not None else 0.0

    @property
    def frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Frequency

        if temp is None:
            return 0.0

        return temp

    @frequency.setter
    @enforce_parameter_types
    def frequency(self: Self, value: "float"):
        self.wrapped.Frequency = float(value) if value is not None else 0.0

    @property
    def harmonic_draw_style(self: Self) -> "_189.FEModelHarmonicAnalysisDrawStyle":
        """mastapy.nodal_analysis.dev_tools_analyses.FEModelHarmonicAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def boundary_conditions_all_nodes(
        self: Self,
    ) -> "List[_2407.NodeBoundaryConditionStaticAnalysis]":
        """List[mastapy.system_model.fe.NodeBoundaryConditionStaticAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoundaryConditionsAllNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def export_velocity_to_file(self: Self):
        """Method does not return."""
        self.wrapped.ExportVelocityToFile()

    def solve_for_current_inputs(self: Self):
        """Method does not return."""
        self.wrapped.SolveForCurrentInputs()

    @property
    def cast_to(
        self: Self,
    ) -> "FESubstructureWithSelectionForHarmonicAnalysis._Cast_FESubstructureWithSelectionForHarmonicAnalysis":
        return self._Cast_FESubstructureWithSelectionForHarmonicAnalysis(self)
