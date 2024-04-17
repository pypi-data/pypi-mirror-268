"""ElectricMachineResultsTimeStepAtLocation"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_TIME_STEP_AT_LOCATION = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "ElectricMachineResultsTimeStepAtLocation"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineResultsTimeStepAtLocation",)


Self = TypeVar("Self", bound="ElectricMachineResultsTimeStepAtLocation")


class ElectricMachineResultsTimeStepAtLocation(_0.APIBase):
    """ElectricMachineResultsTimeStepAtLocation

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_TIME_STEP_AT_LOCATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineResultsTimeStepAtLocation"
    )

    class _Cast_ElectricMachineResultsTimeStepAtLocation:
        """Special nested class for casting ElectricMachineResultsTimeStepAtLocation to subclasses."""

        def __init__(
            self: "ElectricMachineResultsTimeStepAtLocation._Cast_ElectricMachineResultsTimeStepAtLocation",
            parent: "ElectricMachineResultsTimeStepAtLocation",
        ):
            self._parent = parent

        @property
        def electric_machine_results_time_step_at_location(
            self: "ElectricMachineResultsTimeStepAtLocation._Cast_ElectricMachineResultsTimeStepAtLocation",
        ) -> "ElectricMachineResultsTimeStepAtLocation":
            return self._parent

        def __getattr__(
            self: "ElectricMachineResultsTimeStepAtLocation._Cast_ElectricMachineResultsTimeStepAtLocation",
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
        self: Self, instance_to_wrap: "ElectricMachineResultsTimeStepAtLocation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flux_density_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FluxDensityMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def location(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Location

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def magnetic_vector_potential(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagneticVectorPotential

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
    def radial_flux_density(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialFluxDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_flux_density(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialFluxDensity

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
    ) -> "ElectricMachineResultsTimeStepAtLocation._Cast_ElectricMachineResultsTimeStepAtLocation":
        return self._Cast_ElectricMachineResultsTimeStepAtLocation(self)
