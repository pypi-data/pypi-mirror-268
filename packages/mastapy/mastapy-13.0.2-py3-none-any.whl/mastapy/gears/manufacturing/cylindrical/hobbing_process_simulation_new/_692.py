"""RackManufactureError"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACK_MANUFACTURE_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "RackManufactureError",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _679,
        _694,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RackManufactureError",)


Self = TypeVar("Self", bound="RackManufactureError")


class RackManufactureError(_0.APIBase):
    """RackManufactureError

    This is a mastapy class.
    """

    TYPE = _RACK_MANUFACTURE_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RackManufactureError")

    class _Cast_RackManufactureError:
        """Special nested class for casting RackManufactureError to subclasses."""

        def __init__(
            self: "RackManufactureError._Cast_RackManufactureError",
            parent: "RackManufactureError",
        ):
            self._parent = parent

        @property
        def hob_manufacture_error(
            self: "RackManufactureError._Cast_RackManufactureError",
        ) -> "_679.HobManufactureError":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _679,
            )

            return self._parent._cast(_679.HobManufactureError)

        @property
        def worm_grinder_manufacture_error(
            self: "RackManufactureError._Cast_RackManufactureError",
        ) -> "_694.WormGrinderManufactureError":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _694,
            )

            return self._parent._cast(_694.WormGrinderManufactureError)

        @property
        def rack_manufacture_error(
            self: "RackManufactureError._Cast_RackManufactureError",
        ) -> "RackManufactureError":
            return self._parent

        def __getattr__(
            self: "RackManufactureError._Cast_RackManufactureError", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RackManufactureError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_pressure_angle_error_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeftFlankPressureAngleErrorLength

        if temp is None:
            return 0.0

        return temp

    @left_flank_pressure_angle_error_length.setter
    @enforce_parameter_types
    def left_flank_pressure_angle_error_length(self: Self, value: "float"):
        self.wrapped.LeftFlankPressureAngleErrorLength = (
            float(value) if value is not None else 0.0
        )

    @property
    def left_flank_pressure_angle_error_reading(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeftFlankPressureAngleErrorReading

        if temp is None:
            return 0.0

        return temp

    @left_flank_pressure_angle_error_reading.setter
    @enforce_parameter_types
    def left_flank_pressure_angle_error_reading(self: Self, value: "float"):
        self.wrapped.LeftFlankPressureAngleErrorReading = (
            float(value) if value is not None else 0.0
        )

    @property
    def right_flank_pressure_angle_error_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RightFlankPressureAngleErrorLength

        if temp is None:
            return 0.0

        return temp

    @right_flank_pressure_angle_error_length.setter
    @enforce_parameter_types
    def right_flank_pressure_angle_error_length(self: Self, value: "float"):
        self.wrapped.RightFlankPressureAngleErrorLength = (
            float(value) if value is not None else 0.0
        )

    @property
    def right_flank_pressure_angle_error_reading(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RightFlankPressureAngleErrorReading

        if temp is None:
            return 0.0

        return temp

    @right_flank_pressure_angle_error_reading.setter
    @enforce_parameter_types
    def right_flank_pressure_angle_error_reading(self: Self, value: "float"):
        self.wrapped.RightFlankPressureAngleErrorReading = (
            float(value) if value is not None else 0.0
        )

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
    def cast_to(self: Self) -> "RackManufactureError._Cast_RackManufactureError":
        return self._Cast_RackManufactureError(self)
