"""PartAnalysisCaseWithContourViewable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.utility.enums import _1829, _1830
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_ANALYSIS_CASE_WITH_CONTOUR_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "PartAnalysisCaseWithContourViewable"
)

if TYPE_CHECKING:
    from mastapy.system_model.drawing import (
        _2253,
        _2250,
        _2251,
        _2255,
        _2256,
        _2258,
        _2267,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartAnalysisCaseWithContourViewable",)


Self = TypeVar("Self", bound="PartAnalysisCaseWithContourViewable")


class PartAnalysisCaseWithContourViewable(_0.APIBase):
    """PartAnalysisCaseWithContourViewable

    This is a mastapy class.
    """

    TYPE = _PART_ANALYSIS_CASE_WITH_CONTOUR_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartAnalysisCaseWithContourViewable")

    class _Cast_PartAnalysisCaseWithContourViewable:
        """Special nested class for casting PartAnalysisCaseWithContourViewable to subclasses."""

        def __init__(
            self: "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable",
            parent: "PartAnalysisCaseWithContourViewable",
        ):
            self._parent = parent

        @property
        def abstract_system_deflection_viewable(
            self: "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable",
        ) -> "_2250.AbstractSystemDeflectionViewable":
            from mastapy.system_model.drawing import _2250

            return self._parent._cast(_2250.AbstractSystemDeflectionViewable)

        @property
        def advanced_system_deflection_viewable(
            self: "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable",
        ) -> "_2251.AdvancedSystemDeflectionViewable":
            from mastapy.system_model.drawing import _2251

            return self._parent._cast(_2251.AdvancedSystemDeflectionViewable)

        @property
        def dynamic_analysis_viewable(
            self: "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable",
        ) -> "_2255.DynamicAnalysisViewable":
            from mastapy.system_model.drawing import _2255

            return self._parent._cast(_2255.DynamicAnalysisViewable)

        @property
        def harmonic_analysis_viewable(
            self: "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable",
        ) -> "_2256.HarmonicAnalysisViewable":
            from mastapy.system_model.drawing import _2256

            return self._parent._cast(_2256.HarmonicAnalysisViewable)

        @property
        def modal_analysis_viewable(
            self: "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable",
        ) -> "_2258.ModalAnalysisViewable":
            from mastapy.system_model.drawing import _2258

            return self._parent._cast(_2258.ModalAnalysisViewable)

        @property
        def system_deflection_viewable(
            self: "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable",
        ) -> "_2267.SystemDeflectionViewable":
            from mastapy.system_model.drawing import _2267

            return self._parent._cast(_2267.SystemDeflectionViewable)

        @property
        def part_analysis_case_with_contour_viewable(
            self: "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable",
        ) -> "PartAnalysisCaseWithContourViewable":
            return self._parent

        def __getattr__(
            self: "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable",
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
        self: Self, instance_to_wrap: "PartAnalysisCaseWithContourViewable.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection":
        """EnumWithSelectedValue[mastapy.utility.enums.ThreeDViewContourOptionFirstSelection]"""
        temp = self.wrapped.Contour

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @contour.setter
    @enforce_parameter_types
    def contour(self: Self, value: "_1829.ThreeDViewContourOptionFirstSelection"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Contour = value

    @property
    def contour_secondary(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection":
        """EnumWithSelectedValue[mastapy.utility.enums.ThreeDViewContourOptionSecondSelection]"""
        temp = self.wrapped.ContourSecondary

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @contour_secondary.setter
    @enforce_parameter_types
    def contour_secondary(
        self: Self, value: "_1830.ThreeDViewContourOptionSecondSelection"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ContourSecondary = value

    @property
    def contour_draw_style(self: Self) -> "_2253.ContourDrawStyle":
        """mastapy.system_model.drawing.ContourDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> (
        "PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable"
    ):
        return self._Cast_PartAnalysisCaseWithContourViewable(self)
