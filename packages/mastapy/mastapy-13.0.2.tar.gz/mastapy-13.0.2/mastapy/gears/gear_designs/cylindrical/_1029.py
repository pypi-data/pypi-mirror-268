"""CylindricalGearProfileMeasurement"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PROFILE_MEASUREMENT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearProfileMeasurement"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearProfileMeasurement",)


Self = TypeVar("Self", bound="CylindricalGearProfileMeasurement")


class CylindricalGearProfileMeasurement(_0.APIBase):
    """CylindricalGearProfileMeasurement

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PROFILE_MEASUREMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearProfileMeasurement")

    class _Cast_CylindricalGearProfileMeasurement:
        """Special nested class for casting CylindricalGearProfileMeasurement to subclasses."""

        def __init__(
            self: "CylindricalGearProfileMeasurement._Cast_CylindricalGearProfileMeasurement",
            parent: "CylindricalGearProfileMeasurement",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_profile_measurement(
            self: "CylindricalGearProfileMeasurement._Cast_CylindricalGearProfileMeasurement",
        ) -> "CylindricalGearProfileMeasurement":
            return self._parent

        def __getattr__(
            self: "CylindricalGearProfileMeasurement._Cast_CylindricalGearProfileMeasurement",
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
        self: Self, instance_to_wrap: "CylindricalGearProfileMeasurement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def auto_diameter_show_depending_on_settings(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AutoDiameterShowDependingOnSettings

        if temp is None:
            return 0.0

        return temp

    @auto_diameter_show_depending_on_settings.setter
    @enforce_parameter_types
    def auto_diameter_show_depending_on_settings(self: Self, value: "float"):
        self.wrapped.AutoDiameterShowDependingOnSettings = (
            float(value) if value is not None else 0.0
        )

    @property
    def auto_radius_show_depending_on_settings(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AutoRadiusShowDependingOnSettings

        if temp is None:
            return 0.0

        return temp

    @auto_radius_show_depending_on_settings.setter
    @enforce_parameter_types
    def auto_radius_show_depending_on_settings(self: Self, value: "float"):
        self.wrapped.AutoRadiusShowDependingOnSettings = (
            float(value) if value is not None else 0.0
        )

    @property
    def auto_roll_angle_show_depending_on_settings(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AutoRollAngleShowDependingOnSettings

        if temp is None:
            return 0.0

        return temp

    @auto_roll_angle_show_depending_on_settings.setter
    @enforce_parameter_types
    def auto_roll_angle_show_depending_on_settings(self: Self, value: "float"):
        self.wrapped.AutoRollAngleShowDependingOnSettings = (
            float(value) if value is not None else 0.0
        )

    @property
    def auto_rolling_distance_show_depending_on_settings(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AutoRollingDistanceShowDependingOnSettings

        if temp is None:
            return 0.0

        return temp

    @auto_rolling_distance_show_depending_on_settings.setter
    @enforce_parameter_types
    def auto_rolling_distance_show_depending_on_settings(self: Self, value: "float"):
        self.wrapped.AutoRollingDistanceShowDependingOnSettings = (
            float(value) if value is not None else 0.0
        )

    @property
    def diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "float"):
        self.wrapped.Diameter = float(value) if value is not None else 0.0

    @property
    def radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "float"):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def roll_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollAngle

        if temp is None:
            return 0.0

        return temp

    @roll_angle.setter
    @enforce_parameter_types
    def roll_angle(self: Self, value: "float"):
        self.wrapped.RollAngle = float(value) if value is not None else 0.0

    @property
    def rolling_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollingDistance

        if temp is None:
            return 0.0

        return temp

    @rolling_distance.setter
    @enforce_parameter_types
    def rolling_distance(self: Self, value: "float"):
        self.wrapped.RollingDistance = float(value) if value is not None else 0.0

    @property
    def signed_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SignedDiameter

        if temp is None:
            return 0.0

        return temp

    @signed_diameter.setter
    @enforce_parameter_types
    def signed_diameter(self: Self, value: "float"):
        self.wrapped.SignedDiameter = float(value) if value is not None else 0.0

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
    ) -> "CylindricalGearProfileMeasurement._Cast_CylindricalGearProfileMeasurement":
        return self._Cast_CylindricalGearProfileMeasurement(self)
