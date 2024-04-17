"""ElectricMachineBasicMechanicalLossSettings"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_BASIC_MECHANICAL_LOSS_SETTINGS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses",
    "ElectricMachineBasicMechanicalLossSettings",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineBasicMechanicalLossSettings",)


Self = TypeVar("Self", bound="ElectricMachineBasicMechanicalLossSettings")


class ElectricMachineBasicMechanicalLossSettings(_0.APIBase):
    """ElectricMachineBasicMechanicalLossSettings

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_BASIC_MECHANICAL_LOSS_SETTINGS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineBasicMechanicalLossSettings"
    )

    class _Cast_ElectricMachineBasicMechanicalLossSettings:
        """Special nested class for casting ElectricMachineBasicMechanicalLossSettings to subclasses."""

        def __init__(
            self: "ElectricMachineBasicMechanicalLossSettings._Cast_ElectricMachineBasicMechanicalLossSettings",
            parent: "ElectricMachineBasicMechanicalLossSettings",
        ):
            self._parent = parent

        @property
        def electric_machine_basic_mechanical_loss_settings(
            self: "ElectricMachineBasicMechanicalLossSettings._Cast_ElectricMachineBasicMechanicalLossSettings",
        ) -> "ElectricMachineBasicMechanicalLossSettings":
            return self._parent

        def __getattr__(
            self: "ElectricMachineBasicMechanicalLossSettings._Cast_ElectricMachineBasicMechanicalLossSettings",
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
        self: Self, instance_to_wrap: "ElectricMachineBasicMechanicalLossSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def friction_loss_exponent(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FrictionLossExponent

        if temp is None:
            return 0.0

        return temp

    @friction_loss_exponent.setter
    @enforce_parameter_types
    def friction_loss_exponent(self: Self, value: "float"):
        self.wrapped.FrictionLossExponent = float(value) if value is not None else 0.0

    @property
    def friction_losses_at_reference_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FrictionLossesAtReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @friction_losses_at_reference_speed.setter
    @enforce_parameter_types
    def friction_losses_at_reference_speed(self: Self, value: "float"):
        self.wrapped.FrictionLossesAtReferenceSpeed = (
            float(value) if value is not None else 0.0
        )

    @property
    def include_basic_mechanical_losses_calculation(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBasicMechanicalLossesCalculation

        if temp is None:
            return False

        return temp

    @include_basic_mechanical_losses_calculation.setter
    @enforce_parameter_types
    def include_basic_mechanical_losses_calculation(self: Self, value: "bool"):
        self.wrapped.IncludeBasicMechanicalLossesCalculation = (
            bool(value) if value is not None else False
        )

    @property
    def reference_speed_for_mechanical_losses(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReferenceSpeedForMechanicalLosses

        if temp is None:
            return 0.0

        return temp

    @reference_speed_for_mechanical_losses.setter
    @enforce_parameter_types
    def reference_speed_for_mechanical_losses(self: Self, value: "float"):
        self.wrapped.ReferenceSpeedForMechanicalLosses = (
            float(value) if value is not None else 0.0
        )

    @property
    def windage_loss_exponent(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WindageLossExponent

        if temp is None:
            return 0.0

        return temp

    @windage_loss_exponent.setter
    @enforce_parameter_types
    def windage_loss_exponent(self: Self, value: "float"):
        self.wrapped.WindageLossExponent = float(value) if value is not None else 0.0

    @property
    def windage_loss_at_reference_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WindageLossAtReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @windage_loss_at_reference_speed.setter
    @enforce_parameter_types
    def windage_loss_at_reference_speed(self: Self, value: "float"):
        self.wrapped.WindageLossAtReferenceSpeed = (
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
    def cast_to(
        self: Self,
    ) -> "ElectricMachineBasicMechanicalLossSettings._Cast_ElectricMachineBasicMechanicalLossSettings":
        return self._Cast_ElectricMachineBasicMechanicalLossSettings(self)
