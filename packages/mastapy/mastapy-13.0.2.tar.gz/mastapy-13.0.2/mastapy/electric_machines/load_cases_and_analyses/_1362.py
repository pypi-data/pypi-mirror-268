"""ElectricMachineEfficiencyMapSettings"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_EFFICIENCY_MAP_SETTINGS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses",
    "ElectricMachineEfficiencyMapSettings",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineEfficiencyMapSettings",)


Self = TypeVar("Self", bound="ElectricMachineEfficiencyMapSettings")


class ElectricMachineEfficiencyMapSettings(_0.APIBase):
    """ElectricMachineEfficiencyMapSettings

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_EFFICIENCY_MAP_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineEfficiencyMapSettings")

    class _Cast_ElectricMachineEfficiencyMapSettings:
        """Special nested class for casting ElectricMachineEfficiencyMapSettings to subclasses."""

        def __init__(
            self: "ElectricMachineEfficiencyMapSettings._Cast_ElectricMachineEfficiencyMapSettings",
            parent: "ElectricMachineEfficiencyMapSettings",
        ):
            self._parent = parent

        @property
        def electric_machine_efficiency_map_settings(
            self: "ElectricMachineEfficiencyMapSettings._Cast_ElectricMachineEfficiencyMapSettings",
        ) -> "ElectricMachineEfficiencyMapSettings":
            return self._parent

        def __getattr__(
            self: "ElectricMachineEfficiencyMapSettings._Cast_ElectricMachineEfficiencyMapSettings",
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
        self: Self, instance_to_wrap: "ElectricMachineEfficiencyMapSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumSpeed

        if temp is None:
            return 0.0

        return temp

    @maximum_speed.setter
    @enforce_parameter_types
    def maximum_speed(self: Self, value: "float"):
        self.wrapped.MaximumSpeed = float(value) if value is not None else 0.0

    @property
    def minimum_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumSpeed

        if temp is None:
            return 0.0

        return temp

    @minimum_speed.setter
    @enforce_parameter_types
    def minimum_speed(self: Self, value: "float"):
        self.wrapped.MinimumSpeed = float(value) if value is not None else 0.0

    @property
    def minimum_torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumTorque

        if temp is None:
            return 0.0

        return temp

    @minimum_torque.setter
    @enforce_parameter_types
    def minimum_torque(self: Self, value: "float"):
        self.wrapped.MinimumTorque = float(value) if value is not None else 0.0

    @property
    def number_of_speed_values(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSpeedValues

        if temp is None:
            return 0

        return temp

    @number_of_speed_values.setter
    @enforce_parameter_types
    def number_of_speed_values(self: Self, value: "int"):
        self.wrapped.NumberOfSpeedValues = int(value) if value is not None else 0

    @property
    def number_of_torque_values(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTorqueValues

        if temp is None:
            return 0

        return temp

    @number_of_torque_values.setter
    @enforce_parameter_types
    def number_of_torque_values(self: Self, value: "int"):
        self.wrapped.NumberOfTorqueValues = int(value) if value is not None else 0

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
    ) -> "ElectricMachineEfficiencyMapSettings._Cast_ElectricMachineEfficiencyMapSettings":
        return self._Cast_ElectricMachineEfficiencyMapSettings(self)
