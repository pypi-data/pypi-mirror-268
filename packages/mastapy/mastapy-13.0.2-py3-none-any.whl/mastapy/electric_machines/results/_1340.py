"""ElectricMachineResultsForStatorToothAtTimeStep"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_FOR_STATOR_TOOTH_AT_TIME_STEP = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results",
    "ElectricMachineResultsForStatorToothAtTimeStep",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineResultsForStatorToothAtTimeStep",)


Self = TypeVar("Self", bound="ElectricMachineResultsForStatorToothAtTimeStep")


class ElectricMachineResultsForStatorToothAtTimeStep(_0.APIBase):
    """ElectricMachineResultsForStatorToothAtTimeStep

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_FOR_STATOR_TOOTH_AT_TIME_STEP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineResultsForStatorToothAtTimeStep"
    )

    class _Cast_ElectricMachineResultsForStatorToothAtTimeStep:
        """Special nested class for casting ElectricMachineResultsForStatorToothAtTimeStep to subclasses."""

        def __init__(
            self: "ElectricMachineResultsForStatorToothAtTimeStep._Cast_ElectricMachineResultsForStatorToothAtTimeStep",
            parent: "ElectricMachineResultsForStatorToothAtTimeStep",
        ):
            self._parent = parent

        @property
        def electric_machine_results_for_stator_tooth_at_time_step(
            self: "ElectricMachineResultsForStatorToothAtTimeStep._Cast_ElectricMachineResultsForStatorToothAtTimeStep",
        ) -> "ElectricMachineResultsForStatorToothAtTimeStep":
            return self._parent

        def __getattr__(
            self: "ElectricMachineResultsForStatorToothAtTimeStep._Cast_ElectricMachineResultsForStatorToothAtTimeStep",
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
        instance_to_wrap: "ElectricMachineResultsForStatorToothAtTimeStep.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def stator_tooth_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorToothIndex

        if temp is None:
            return 0

        return temp

    @property
    def tangential_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForce

        if temp is None:
            return 0.0

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
    ) -> "ElectricMachineResultsForStatorToothAtTimeStep._Cast_ElectricMachineResultsForStatorToothAtTimeStep":
        return self._Cast_ElectricMachineResultsForStatorToothAtTimeStep(self)
