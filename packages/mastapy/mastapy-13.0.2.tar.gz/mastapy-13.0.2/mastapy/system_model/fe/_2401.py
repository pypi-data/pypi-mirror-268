"""FESubstructureWithSelectionForStaticAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.utility.enums import _1828
from mastapy.system_model.fe import _2397
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_SELECTION_FOR_STATIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureWithSelectionForStaticAnalysis"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.component_mode_synthesis import _238
    from mastapy.nodal_analysis.dev_tools_analyses import _194
    from mastapy.system_model.fe import _2407, _2367
    from mastapy.math_utility.measured_vectors import _1571


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureWithSelectionForStaticAnalysis",)


Self = TypeVar("Self", bound="FESubstructureWithSelectionForStaticAnalysis")


class FESubstructureWithSelectionForStaticAnalysis(_2397.FESubstructureWithSelection):
    """FESubstructureWithSelectionForStaticAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_WITH_SELECTION_FOR_STATIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FESubstructureWithSelectionForStaticAnalysis"
    )

    class _Cast_FESubstructureWithSelectionForStaticAnalysis:
        """Special nested class for casting FESubstructureWithSelectionForStaticAnalysis to subclasses."""

        def __init__(
            self: "FESubstructureWithSelectionForStaticAnalysis._Cast_FESubstructureWithSelectionForStaticAnalysis",
            parent: "FESubstructureWithSelectionForStaticAnalysis",
        ):
            self._parent = parent

        @property
        def fe_substructure_with_selection(
            self: "FESubstructureWithSelectionForStaticAnalysis._Cast_FESubstructureWithSelectionForStaticAnalysis",
        ) -> "_2397.FESubstructureWithSelection":
            return self._parent._cast(_2397.FESubstructureWithSelection)

        @property
        def base_fe_with_selection(
            self: "FESubstructureWithSelectionForStaticAnalysis._Cast_FESubstructureWithSelectionForStaticAnalysis",
        ) -> "_2367.BaseFEWithSelection":
            from mastapy.system_model.fe import _2367

            return self._parent._cast(_2367.BaseFEWithSelection)

        @property
        def fe_substructure_with_selection_for_static_analysis(
            self: "FESubstructureWithSelectionForStaticAnalysis._Cast_FESubstructureWithSelectionForStaticAnalysis",
        ) -> "FESubstructureWithSelectionForStaticAnalysis":
            return self._parent

        def __getattr__(
            self: "FESubstructureWithSelectionForStaticAnalysis._Cast_FESubstructureWithSelectionForStaticAnalysis",
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
        instance_to_wrap: "FESubstructureWithSelectionForStaticAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_stress_to_nodes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AverageStressToNodes

        if temp is None:
            return False

        return temp

    @average_stress_to_nodes.setter
    @enforce_parameter_types
    def average_stress_to_nodes(self: Self, value: "bool"):
        self.wrapped.AverageStressToNodes = bool(value) if value is not None else False

    @property
    def contour_option(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOption":
        """EnumWithSelectedValue[mastapy.utility.enums.ThreeDViewContourOption]"""
        temp = self.wrapped.ContourOption

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @contour_option.setter
    @enforce_parameter_types
    def contour_option(self: Self, value: "_1828.ThreeDViewContourOption"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ContourOption = value

    @property
    def temperature_change_from_nominal(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TemperatureChangeFromNominal

        if temp is None:
            return 0.0

        return temp

    @temperature_change_from_nominal.setter
    @enforce_parameter_types
    def temperature_change_from_nominal(self: Self, value: "float"):
        self.wrapped.TemperatureChangeFromNominal = (
            float(value) if value is not None else 0.0
        )

    @property
    def full_fe_results(self: Self) -> "_238.StaticCMSResults":
        """mastapy.nodal_analysis.component_mode_synthesis.StaticCMSResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FullFEResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_draw_style(self: Self) -> "_194.FEModelStaticAnalysisDrawStyle":
        """mastapy.nodal_analysis.dev_tools_analyses.FEModelStaticAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticDrawStyle

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

    @property
    def boundary_conditions_selected_nodes(
        self: Self,
    ) -> "List[_2407.NodeBoundaryConditionStaticAnalysis]":
        """List[mastapy.system_model.fe.NodeBoundaryConditionStaticAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoundaryConditionsSelectedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def displacement_results(
        self: Self,
    ) -> "List[_1571.VectorWithLinearAndAngularComponents]":
        """List[mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def force_results(self: Self) -> "List[_1571.VectorWithLinearAndAngularComponents]":
        """List[mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def reset_displacements(self: Self):
        """Method does not return."""
        self.wrapped.ResetDisplacements()

    def reset_forces(self: Self):
        """Method does not return."""
        self.wrapped.ResetForces()

    def solve(self: Self):
        """Method does not return."""
        self.wrapped.Solve()

    def torque_transfer_check(self: Self):
        """Method does not return."""
        self.wrapped.TorqueTransferCheck()

    @property
    def cast_to(
        self: Self,
    ) -> "FESubstructureWithSelectionForStaticAnalysis._Cast_FESubstructureWithSelectionForStaticAnalysis":
        return self._Cast_FESubstructureWithSelectionForStaticAnalysis(self)
