"""ElectricMachineResultsForConductorTurnAtTimeStep"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_FOR_CONDUCTOR_TURN_AT_TIME_STEP = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results",
    "ElectricMachineResultsForConductorTurnAtTimeStep",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineResultsForConductorTurnAtTimeStep",)


Self = TypeVar("Self", bound="ElectricMachineResultsForConductorTurnAtTimeStep")


class ElectricMachineResultsForConductorTurnAtTimeStep(_0.APIBase):
    """ElectricMachineResultsForConductorTurnAtTimeStep

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_FOR_CONDUCTOR_TURN_AT_TIME_STEP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineResultsForConductorTurnAtTimeStep"
    )

    class _Cast_ElectricMachineResultsForConductorTurnAtTimeStep:
        """Special nested class for casting ElectricMachineResultsForConductorTurnAtTimeStep to subclasses."""

        def __init__(
            self: "ElectricMachineResultsForConductorTurnAtTimeStep._Cast_ElectricMachineResultsForConductorTurnAtTimeStep",
            parent: "ElectricMachineResultsForConductorTurnAtTimeStep",
        ):
            self._parent = parent

        @property
        def electric_machine_results_for_conductor_turn_at_time_step(
            self: "ElectricMachineResultsForConductorTurnAtTimeStep._Cast_ElectricMachineResultsForConductorTurnAtTimeStep",
        ) -> "ElectricMachineResultsForConductorTurnAtTimeStep":
            return self._parent

        def __getattr__(
            self: "ElectricMachineResultsForConductorTurnAtTimeStep._Cast_ElectricMachineResultsForConductorTurnAtTimeStep",
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
        self: Self,
        instance_to_wrap: "ElectricMachineResultsForConductorTurnAtTimeStep.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ac_winding_losses(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ACWindingLosses

        if temp is None:
            return 0.0

        return temp

    @ac_winding_losses.setter
    @enforce_parameter_types
    def ac_winding_losses(self: Self, value: "float"):
        self.wrapped.ACWindingLosses = float(value) if value is not None else 0.0

    @property
    def conductor(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Conductor

        if temp is None:
            return 0

        return temp

    @property
    def dcac_winding_losses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DCACWindingLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def dc_winding_losses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DCWindingLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

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
    ) -> "ElectricMachineResultsForConductorTurnAtTimeStep._Cast_ElectricMachineResultsForConductorTurnAtTimeStep":
        return self._Cast_ElectricMachineResultsForConductorTurnAtTimeStep(self)
