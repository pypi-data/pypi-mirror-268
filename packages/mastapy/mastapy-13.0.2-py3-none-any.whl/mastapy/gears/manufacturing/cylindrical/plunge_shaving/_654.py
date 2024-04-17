"""PlungeShaverOutputs"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _646
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.gears.manufacturing.cylindrical import _630
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_OUTPUTS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving", "PlungeShaverOutputs"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _652, _657, _660


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShaverOutputs",)


Self = TypeVar("Self", bound="PlungeShaverOutputs")


class PlungeShaverOutputs(_0.APIBase):
    """PlungeShaverOutputs

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_OUTPUTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlungeShaverOutputs")

    class _Cast_PlungeShaverOutputs:
        """Special nested class for casting PlungeShaverOutputs to subclasses."""

        def __init__(
            self: "PlungeShaverOutputs._Cast_PlungeShaverOutputs",
            parent: "PlungeShaverOutputs",
        ):
            self._parent = parent

        @property
        def real_plunge_shaver_outputs(
            self: "PlungeShaverOutputs._Cast_PlungeShaverOutputs",
        ) -> "_657.RealPlungeShaverOutputs":
            from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _657

            return self._parent._cast(_657.RealPlungeShaverOutputs)

        @property
        def virtual_plunge_shaver_outputs(
            self: "PlungeShaverOutputs._Cast_PlungeShaverOutputs",
        ) -> "_660.VirtualPlungeShaverOutputs":
            from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _660

            return self._parent._cast(_660.VirtualPlungeShaverOutputs)

        @property
        def plunge_shaver_outputs(
            self: "PlungeShaverOutputs._Cast_PlungeShaverOutputs",
        ) -> "PlungeShaverOutputs":
            return self._parent

        def __getattr__(
            self: "PlungeShaverOutputs._Cast_PlungeShaverOutputs", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlungeShaverOutputs.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chart(self: Self) -> "enum_with_selected_value.EnumWithSelectedValue_ChartType":
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.plunge_shaving.ChartType]"""
        temp = self.wrapped.Chart

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ChartType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value)

    @chart.setter
    @enforce_parameter_types
    def chart(self: Self, value: "_646.ChartType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ChartType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Chart = value

    @property
    def difference_between_chart_z_plane(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DifferenceBetweenChartZPlane

        if temp is None:
            return 0.0

        return temp

    @difference_between_chart_z_plane.setter
    @enforce_parameter_types
    def difference_between_chart_z_plane(self: Self, value: "float"):
        self.wrapped.DifferenceBetweenChartZPlane = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_modification_on_conjugate_shaver_chart_left_flank(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileModificationOnConjugateShaverChartLeftFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def profile_modification_on_conjugate_shaver_chart_right_flank(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileModificationOnConjugateShaverChartRightFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def selected_flank(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_Flank":
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.Flank]"""
        temp = self.wrapped.SelectedFlank

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_Flank.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value)

    @selected_flank.setter
    @enforce_parameter_types
    def selected_flank(self: Self, value: "_630.Flank"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_Flank.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SelectedFlank = value

    @property
    def shaved_gear_profile_modification_z_plane(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShavedGearProfileModificationZPlane

        if temp is None:
            return 0.0

        return temp

    @shaved_gear_profile_modification_z_plane.setter
    @enforce_parameter_types
    def shaved_gear_profile_modification_z_plane(self: Self, value: "float"):
        self.wrapped.ShavedGearProfileModificationZPlane = (
            float(value) if value is not None else 0.0
        )

    @property
    def shaver_profile_modification_z_plane(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaverProfileModificationZPlane

        if temp is None:
            return 0.0

        return temp

    @shaver_profile_modification_z_plane.setter
    @enforce_parameter_types
    def shaver_profile_modification_z_plane(self: Self, value: "float"):
        self.wrapped.ShaverProfileModificationZPlane = (
            float(value) if value is not None else 0.0
        )

    @property
    def calculation_details(self: Self) -> "_652.PlungeShaverGeneration":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.PlungeShaverGeneration

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculationDetails

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
    def cast_to(self: Self) -> "PlungeShaverOutputs._Cast_PlungeShaverOutputs":
        return self._Cast_PlungeShaverOutputs(self)
