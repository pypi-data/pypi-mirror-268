"""FESubstructureWithSelectionForModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.fe import _2397
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_SELECTION_FOR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureWithSelectionForModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _182, _191
    from mastapy.nodal_analysis import _64
    from mastapy.system_model.fe import _2394, _2367


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureWithSelectionForModalAnalysis",)


Self = TypeVar("Self", bound="FESubstructureWithSelectionForModalAnalysis")


class FESubstructureWithSelectionForModalAnalysis(_2397.FESubstructureWithSelection):
    """FESubstructureWithSelectionForModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_WITH_SELECTION_FOR_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FESubstructureWithSelectionForModalAnalysis"
    )

    class _Cast_FESubstructureWithSelectionForModalAnalysis:
        """Special nested class for casting FESubstructureWithSelectionForModalAnalysis to subclasses."""

        def __init__(
            self: "FESubstructureWithSelectionForModalAnalysis._Cast_FESubstructureWithSelectionForModalAnalysis",
            parent: "FESubstructureWithSelectionForModalAnalysis",
        ):
            self._parent = parent

        @property
        def fe_substructure_with_selection(
            self: "FESubstructureWithSelectionForModalAnalysis._Cast_FESubstructureWithSelectionForModalAnalysis",
        ) -> "_2397.FESubstructureWithSelection":
            return self._parent._cast(_2397.FESubstructureWithSelection)

        @property
        def base_fe_with_selection(
            self: "FESubstructureWithSelectionForModalAnalysis._Cast_FESubstructureWithSelectionForModalAnalysis",
        ) -> "_2367.BaseFEWithSelection":
            from mastapy.system_model.fe import _2367

            return self._parent._cast(_2367.BaseFEWithSelection)

        @property
        def fe_substructure_with_selection_for_modal_analysis(
            self: "FESubstructureWithSelectionForModalAnalysis._Cast_FESubstructureWithSelectionForModalAnalysis",
        ) -> "FESubstructureWithSelectionForModalAnalysis":
            return self._parent

        def __getattr__(
            self: "FESubstructureWithSelectionForModalAnalysis._Cast_FESubstructureWithSelectionForModalAnalysis",
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
        self: Self, instance_to_wrap: "FESubstructureWithSelectionForModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def invert_y_axis_of_mac_chart(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.InvertYAxisOfMACChart

        if temp is None:
            return False

        return temp

    @invert_y_axis_of_mac_chart.setter
    @enforce_parameter_types
    def invert_y_axis_of_mac_chart(self: Self, value: "bool"):
        self.wrapped.InvertYAxisOfMACChart = bool(value) if value is not None else False

    @property
    def max_displacement_scaling(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaxDisplacementScaling

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @max_displacement_scaling.setter
    @enforce_parameter_types
    def max_displacement_scaling(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaxDisplacementScaling = value

    @property
    def mode_to_draw(self: Self) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.ModeToDraw

        if temp is None:
            return 0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @mode_to_draw.setter
    @enforce_parameter_types
    def mode_to_draw(self: Self, value: "int"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.ModeToDraw = value

    @property
    def show_full_fe_mode_shapes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowFullFEModeShapes

        if temp is None:
            return False

        return temp

    @show_full_fe_mode_shapes.setter
    @enforce_parameter_types
    def show_full_fe_mode_shapes(self: Self, value: "bool"):
        self.wrapped.ShowFullFEModeShapes = bool(value) if value is not None else False

    @property
    def eigenvalue_options(self: Self) -> "_182.EigenvalueOptions":
        """mastapy.nodal_analysis.dev_tools_analyses.EigenvalueOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EigenvalueOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_draw_style(self: Self) -> "_191.FEModelModalAnalysisDrawStyle":
        """mastapy.nodal_analysis.dev_tools_analyses.FEModelModalAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fe_modal_frequencies(self: Self) -> "List[_64.FEModalFrequencyComparison]":
        """List[mastapy.nodal_analysis.FEModalFrequencyComparison]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEModalFrequencies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def full_fe_mode_shapes_at_condensation_nodes(
        self: Self,
    ) -> "List[_2394.FESubstructureNodeModeShapes]":
        """List[mastapy.system_model.fe.FESubstructureNodeModeShapes]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FullFEModeShapesAtCondensationNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def calculate_full_fe_modes(self: Self):
        """Method does not return."""
        self.wrapped.CalculateFullFEModes()

    @property
    def cast_to(
        self: Self,
    ) -> "FESubstructureWithSelectionForModalAnalysis._Cast_FESubstructureWithSelectionForModalAnalysis":
        return self._Cast_FESubstructureWithSelectionForModalAnalysis(self)
