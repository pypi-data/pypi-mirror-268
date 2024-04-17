"""WindTurbineCertificationReport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.static_loads import _6813
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.load_case_groups import _5672
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WIND_TURBINE_CERTIFICATION_REPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "WindTurbineCertificationReport",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.system_deflections import _2808
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2954,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WindTurbineCertificationReport",)


Self = TypeVar("Self", bound="WindTurbineCertificationReport")


class WindTurbineCertificationReport(_6276.CombinationAnalysis):
    """WindTurbineCertificationReport

    This is a mastapy class.
    """

    TYPE = _WIND_TURBINE_CERTIFICATION_REPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WindTurbineCertificationReport")

    class _Cast_WindTurbineCertificationReport:
        """Special nested class for casting WindTurbineCertificationReport to subclasses."""

        def __init__(
            self: "WindTurbineCertificationReport._Cast_WindTurbineCertificationReport",
            parent: "WindTurbineCertificationReport",
        ):
            self._parent = parent

        @property
        def combination_analysis(
            self: "WindTurbineCertificationReport._Cast_WindTurbineCertificationReport",
        ) -> "_6276.CombinationAnalysis":
            return self._parent._cast(_6276.CombinationAnalysis)

        @property
        def wind_turbine_certification_report(
            self: "WindTurbineCertificationReport._Cast_WindTurbineCertificationReport",
        ) -> "WindTurbineCertificationReport":
            return self._parent

        def __getattr__(
            self: "WindTurbineCertificationReport._Cast_WindTurbineCertificationReport",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WindTurbineCertificationReport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extreme_load_case(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = self.wrapped.ExtremeLoadCase

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @extreme_load_case.setter
    @enforce_parameter_types
    def extreme_load_case(self: Self, value: "_6813.StaticLoadCase"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ExtremeLoadCase = value

    @property
    def ldd(self: Self) -> "list_with_selected_item.ListWithSelectedItem_DutyCycle":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle]"""
        temp = self.wrapped.LDD

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_DutyCycle",
        )(temp)

    @ldd.setter
    @enforce_parameter_types
    def ldd(self: Self, value: "_5672.DutyCycle"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_DutyCycle.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_DutyCycle.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LDD = value

    @property
    def nominal_load_case(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = self.wrapped.NominalLoadCase

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @nominal_load_case.setter
    @enforce_parameter_types
    def nominal_load_case(self: Self, value: "_6813.StaticLoadCase"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.NominalLoadCase = value

    @property
    def design(self: Self) -> "_2481.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def extreme_load_case_static_analysis(
        self: Self,
    ) -> "_2808.RootAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExtremeLoadCaseStaticAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ldd_static_analysis(self: Self) -> "_2954.RootAssemblyCompoundSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.compound.RootAssemblyCompoundSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LDDStaticAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def nominal_load_case_static_analysis(
        self: Self,
    ) -> "_2808.RootAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalLoadCaseStaticAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WindTurbineCertificationReport._Cast_WindTurbineCertificationReport":
        return self._Cast_WindTurbineCertificationReport(self)
