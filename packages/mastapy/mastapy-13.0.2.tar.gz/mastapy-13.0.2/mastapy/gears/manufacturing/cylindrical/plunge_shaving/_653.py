"""PlungeShaverInputsAndMicroGeometry"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _648, _649
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_INPUTS_AND_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "PlungeShaverInputsAndMicroGeometry",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _656


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShaverInputsAndMicroGeometry",)


Self = TypeVar("Self", bound="PlungeShaverInputsAndMicroGeometry")


class PlungeShaverInputsAndMicroGeometry(_0.APIBase):
    """PlungeShaverInputsAndMicroGeometry

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_INPUTS_AND_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlungeShaverInputsAndMicroGeometry")

    class _Cast_PlungeShaverInputsAndMicroGeometry:
        """Special nested class for casting PlungeShaverInputsAndMicroGeometry to subclasses."""

        def __init__(
            self: "PlungeShaverInputsAndMicroGeometry._Cast_PlungeShaverInputsAndMicroGeometry",
            parent: "PlungeShaverInputsAndMicroGeometry",
        ):
            self._parent = parent

        @property
        def plunge_shaver_inputs_and_micro_geometry(
            self: "PlungeShaverInputsAndMicroGeometry._Cast_PlungeShaverInputsAndMicroGeometry",
        ) -> "PlungeShaverInputsAndMicroGeometry":
            return self._parent

        def __getattr__(
            self: "PlungeShaverInputsAndMicroGeometry._Cast_PlungeShaverInputsAndMicroGeometry",
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
        self: Self, instance_to_wrap: "PlungeShaverInputsAndMicroGeometry.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def do_both_flanks_have_the_same_micro_geometry(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DoBothFlanksHaveTheSameMicroGeometry

        if temp is None:
            return False

        return temp

    @do_both_flanks_have_the_same_micro_geometry.setter
    @enforce_parameter_types
    def do_both_flanks_have_the_same_micro_geometry(self: Self, value: "bool"):
        self.wrapped.DoBothFlanksHaveTheSameMicroGeometry = (
            bool(value) if value is not None else False
        )

    @property
    def lead_measurement_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_MicroGeometryDefinitionMethod":
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod]"""
        temp = self.wrapped.LeadMeasurementMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_MicroGeometryDefinitionMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @lead_measurement_method.setter
    @enforce_parameter_types
    def lead_measurement_method(
        self: Self, value: "_648.MicroGeometryDefinitionMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_MicroGeometryDefinitionMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LeadMeasurementMethod = value

    @property
    def micro_geometry_source(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_MicroGeometryDefinitionType":
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionType]"""
        temp = self.wrapped.MicroGeometrySource

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_MicroGeometryDefinitionType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @micro_geometry_source.setter
    @enforce_parameter_types
    def micro_geometry_source(self: Self, value: "_649.MicroGeometryDefinitionType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_MicroGeometryDefinitionType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MicroGeometrySource = value

    @property
    def number_of_points_of_interest(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsOfInterest

        if temp is None:
            return 0

        return temp

    @number_of_points_of_interest.setter
    @enforce_parameter_types
    def number_of_points_of_interest(self: Self, value: "int"):
        self.wrapped.NumberOfPointsOfInterest = int(value) if value is not None else 0

    @property
    def profile_measurement_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_MicroGeometryDefinitionMethod":
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod]"""
        temp = self.wrapped.ProfileMeasurementMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_MicroGeometryDefinitionMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @profile_measurement_method.setter
    @enforce_parameter_types
    def profile_measurement_method(
        self: Self, value: "_648.MicroGeometryDefinitionMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_MicroGeometryDefinitionMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ProfileMeasurementMethod = value

    @property
    def points_of_interest_left_flank(self: Self) -> "List[_656.PointOfInterest]":
        """List[mastapy.gears.manufacturing.cylindrical.plunge_shaving.PointOfInterest]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointsOfInterestLeftFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def points_of_interest_right_flank(self: Self) -> "List[_656.PointOfInterest]":
        """List[mastapy.gears.manufacturing.cylindrical.plunge_shaving.PointOfInterest]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointsOfInterestRightFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    ) -> "PlungeShaverInputsAndMicroGeometry._Cast_PlungeShaverInputsAndMicroGeometry":
        return self._Cast_PlungeShaverInputsAndMicroGeometry(self)
