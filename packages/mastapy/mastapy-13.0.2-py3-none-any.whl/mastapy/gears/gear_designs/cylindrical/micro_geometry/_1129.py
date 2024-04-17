"""MicroGeometryViewingOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.ltca import _830
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.nodal_analysis import _90
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_VIEWING_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "MicroGeometryViewingOptions",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1118


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryViewingOptions",)


Self = TypeVar("Self", bound="MicroGeometryViewingOptions")


class MicroGeometryViewingOptions(_0.APIBase):
    """MicroGeometryViewingOptions

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_VIEWING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MicroGeometryViewingOptions")

    class _Cast_MicroGeometryViewingOptions:
        """Special nested class for casting MicroGeometryViewingOptions to subclasses."""

        def __init__(
            self: "MicroGeometryViewingOptions._Cast_MicroGeometryViewingOptions",
            parent: "MicroGeometryViewingOptions",
        ):
            self._parent = parent

        @property
        def micro_geometry_viewing_options(
            self: "MicroGeometryViewingOptions._Cast_MicroGeometryViewingOptions",
        ) -> "MicroGeometryViewingOptions":
            return self._parent

        def __getattr__(
            self: "MicroGeometryViewingOptions._Cast_MicroGeometryViewingOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MicroGeometryViewingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_results(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ContactResultType":
        """EnumWithSelectedValue[mastapy.gears.ltca.ContactResultType]"""
        temp = self.wrapped.ContactResults

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ContactResultType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @contact_results.setter
    @enforce_parameter_types
    def contact_results(self: Self, value: "_830.ContactResultType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ContactResultType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ContactResults = value

    @property
    def gear_option(self: Self) -> "_1118.DrawDefiningGearOrBoth":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.DrawDefiningGearOrBoth"""
        temp = self.wrapped.GearOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry.DrawDefiningGearOrBoth",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical.micro_geometry._1118",
            "DrawDefiningGearOrBoth",
        )(value)

    @gear_option.setter
    @enforce_parameter_types
    def gear_option(self: Self, value: "_1118.DrawDefiningGearOrBoth"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry.DrawDefiningGearOrBoth",
        )
        self.wrapped.GearOption = value

    @property
    def root_stress_results_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_StressResultsType":
        """EnumWithSelectedValue[mastapy.nodal_analysis.StressResultsType]"""
        temp = self.wrapped.RootStressResultsType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_StressResultsType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @root_stress_results_type.setter
    @enforce_parameter_types
    def root_stress_results_type(self: Self, value: "_90.StressResultsType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_StressResultsType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RootStressResultsType = value

    @property
    def show_contact_chart(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowContactChart

        if temp is None:
            return False

        return temp

    @show_contact_chart.setter
    @enforce_parameter_types
    def show_contact_chart(self: Self, value: "bool"):
        self.wrapped.ShowContactChart = bool(value) if value is not None else False

    @property
    def show_contact_points(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowContactPoints

        if temp is None:
            return False

        return temp

    @show_contact_points.setter
    @enforce_parameter_types
    def show_contact_points(self: Self, value: "bool"):
        self.wrapped.ShowContactPoints = bool(value) if value is not None else False

    @property
    def show_force_arrows(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowForceArrows

        if temp is None:
            return False

        return temp

    @show_force_arrows.setter
    @enforce_parameter_types
    def show_force_arrows(self: Self, value: "bool"):
        self.wrapped.ShowForceArrows = bool(value) if value is not None else False

    @property
    def show_root_stress_chart(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowRootStressChart

        if temp is None:
            return False

        return temp

    @show_root_stress_chart.setter
    @enforce_parameter_types
    def show_root_stress_chart(self: Self, value: "bool"):
        self.wrapped.ShowRootStressChart = bool(value) if value is not None else False

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
    ) -> "MicroGeometryViewingOptions._Cast_MicroGeometryViewingOptions":
        return self._Cast_MicroGeometryViewingOptions(self)
