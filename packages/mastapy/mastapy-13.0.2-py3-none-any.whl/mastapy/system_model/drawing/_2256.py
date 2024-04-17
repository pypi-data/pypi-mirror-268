"""HarmonicAnalysisViewable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687, _5778
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.math_utility import _1536
from mastapy.system_model.analyses_and_results.system_deflections import _2767
from mastapy.system_model.drawing.options import _2269
from mastapy.system_model.drawing import _2255
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "HarmonicAnalysisViewable"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338
    from mastapy.system_model.drawing import _2260


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisViewable",)


Self = TypeVar("Self", bound="HarmonicAnalysisViewable")


class HarmonicAnalysisViewable(_2255.DynamicAnalysisViewable):
    """HarmonicAnalysisViewable

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicAnalysisViewable")

    class _Cast_HarmonicAnalysisViewable:
        """Special nested class for casting HarmonicAnalysisViewable to subclasses."""

        def __init__(
            self: "HarmonicAnalysisViewable._Cast_HarmonicAnalysisViewable",
            parent: "HarmonicAnalysisViewable",
        ):
            self._parent = parent

        @property
        def dynamic_analysis_viewable(
            self: "HarmonicAnalysisViewable._Cast_HarmonicAnalysisViewable",
        ) -> "_2255.DynamicAnalysisViewable":
            return self._parent._cast(_2255.DynamicAnalysisViewable)

        @property
        def part_analysis_case_with_contour_viewable(
            self: "HarmonicAnalysisViewable._Cast_HarmonicAnalysisViewable",
        ) -> "_2260.PartAnalysisCaseWithContourViewable":
            from mastapy.system_model.drawing import _2260

            return self._parent._cast(_2260.PartAnalysisCaseWithContourViewable)

        @property
        def harmonic_analysis_viewable(
            self: "HarmonicAnalysisViewable._Cast_HarmonicAnalysisViewable",
        ) -> "HarmonicAnalysisViewable":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisViewable._Cast_HarmonicAnalysisViewable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicAnalysisViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation(
        self: Self,
    ) -> (
        "list_with_selected_item.ListWithSelectedItem_AbstractPeriodicExcitationDetail"
    ):
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractPeriodicExcitationDetail]"""
        temp = self.wrapped.Excitation

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_AbstractPeriodicExcitationDetail",
        )(temp)

    @excitation.setter
    @enforce_parameter_types
    def excitation(self: Self, value: "_5687.AbstractPeriodicExcitationDetail"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_AbstractPeriodicExcitationDetail.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_AbstractPeriodicExcitationDetail.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Excitation = value

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
    def harmonic(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Harmonic

        if temp is None:
            return 0

        return temp

    @harmonic.setter
    @enforce_parameter_types
    def harmonic(self: Self, value: "int"):
        self.wrapped.Harmonic = int(value) if value is not None else 0

    @property
    def harmonic_analysis_with_varying_stiffness_step(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase]"""
        temp = self.wrapped.HarmonicAnalysisWithVaryingStiffnessStep

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
        )(temp)

    @harmonic_analysis_with_varying_stiffness_step.setter
    @enforce_parameter_types
    def harmonic_analysis_with_varying_stiffness_step(
        self: Self, value: "_5778.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.HarmonicAnalysisWithVaryingStiffnessStep = value

    @property
    def order(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_RoundedOrder":
        """ListWithSelectedItem[mastapy.math_utility.RoundedOrder]"""
        temp = self.wrapped.Order

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_RoundedOrder",
        )(temp)

    @order.setter
    @enforce_parameter_types
    def order(self: Self, value: "_1536.RoundedOrder"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_RoundedOrder.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_RoundedOrder.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Order = value

    @property
    def reference_power_load_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReferencePowerLoadSpeed

        if temp is None:
            return 0.0

        return temp

    @reference_power_load_speed.setter
    @enforce_parameter_types
    def reference_power_load_speed(self: Self, value: "float"):
        self.wrapped.ReferencePowerLoadSpeed = (
            float(value) if value is not None else 0.0
        )

    @property
    def uncoupled_mesh(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_GearMeshSystemDeflection":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection]"""
        temp = self.wrapped.UncoupledMesh

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_GearMeshSystemDeflection",
        )(temp)

    @uncoupled_mesh.setter
    @enforce_parameter_types
    def uncoupled_mesh(self: Self, value: "_2767.GearMeshSystemDeflection"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_GearMeshSystemDeflection.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_GearMeshSystemDeflection.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.UncoupledMesh = value

    @property
    def view_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ExcitationAnalysisViewOption":
        """EnumWithSelectedValue[mastapy.system_model.drawing.options.ExcitationAnalysisViewOption]"""
        temp = self.wrapped.ViewType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ExcitationAnalysisViewOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @view_type.setter
    @enforce_parameter_types
    def view_type(self: Self, value: "_2269.ExcitationAnalysisViewOption"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ExcitationAnalysisViewOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ViewType = value

    @property
    def dynamic_analysis_draw_style(self: Self) -> "_6338.DynamicAnalysisDrawStyle":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.DynamicAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisViewable._Cast_HarmonicAnalysisViewable":
        return self._Cast_HarmonicAnalysisViewable(self)
