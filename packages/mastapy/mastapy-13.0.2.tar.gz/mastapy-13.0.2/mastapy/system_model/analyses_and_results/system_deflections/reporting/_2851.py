"""FlexibleGearChart"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.system_deflections import _2753
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_GEAR_CHART = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting",
    "FlexibleGearChart",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1863


__docformat__ = "restructuredtext en"
__all__ = ("FlexibleGearChart",)


Self = TypeVar("Self", bound="FlexibleGearChart")


class FlexibleGearChart(_0.APIBase):
    """FlexibleGearChart

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_GEAR_CHART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexibleGearChart")

    class _Cast_FlexibleGearChart:
        """Special nested class for casting FlexibleGearChart to subclasses."""

        def __init__(
            self: "FlexibleGearChart._Cast_FlexibleGearChart",
            parent: "FlexibleGearChart",
        ):
            self._parent = parent

        @property
        def flexible_gear_chart(
            self: "FlexibleGearChart._Cast_FlexibleGearChart",
        ) -> "FlexibleGearChart":
            return self._parent

        def __getattr__(self: "FlexibleGearChart._Cast_FlexibleGearChart", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexibleGearChart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planets(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_CylindricalGearSystemDeflection":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection]"""
        temp = self.wrapped.Planets

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_CylindricalGearSystemDeflection",
        )(temp)

    @planets.setter
    @enforce_parameter_types
    def planets(self: Self, value: "_2753.CylindricalGearSystemDeflection"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearSystemDeflection.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearSystemDeflection.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Planets = value

    @property
    def remove_rigid_body_motion(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RemoveRigidBodyMotion

        if temp is None:
            return False

        return temp

    @remove_rigid_body_motion.setter
    @enforce_parameter_types
    def remove_rigid_body_motion(self: Self, value: "bool"):
        self.wrapped.RemoveRigidBodyMotion = bool(value) if value is not None else False

    @property
    def chart(self: Self) -> "_1863.LegacyChartMathChartDefinition":
        """mastapy.utility_gui.charts.LegacyChartMathChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Chart

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
    def cast_to(self: Self) -> "FlexibleGearChart._Cast_FlexibleGearChart":
        return self._Cast_FlexibleGearChart(self)
