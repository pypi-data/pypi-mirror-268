"""CutterProcessSimulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUTTER_PROCESS_SIMULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.ProcessSimulation",
    "CutterProcessSimulation",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.process_simulation import _643, _644


__docformat__ = "restructuredtext en"
__all__ = ("CutterProcessSimulation",)


Self = TypeVar("Self", bound="CutterProcessSimulation")


class CutterProcessSimulation(_0.APIBase):
    """CutterProcessSimulation

    This is a mastapy class.
    """

    TYPE = _CUTTER_PROCESS_SIMULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CutterProcessSimulation")

    class _Cast_CutterProcessSimulation:
        """Special nested class for casting CutterProcessSimulation to subclasses."""

        def __init__(
            self: "CutterProcessSimulation._Cast_CutterProcessSimulation",
            parent: "CutterProcessSimulation",
        ):
            self._parent = parent

        @property
        def form_wheel_grinding_process_simulation(
            self: "CutterProcessSimulation._Cast_CutterProcessSimulation",
        ) -> "_643.FormWheelGrindingProcessSimulation":
            from mastapy.gears.manufacturing.cylindrical.process_simulation import _643

            return self._parent._cast(_643.FormWheelGrindingProcessSimulation)

        @property
        def shaping_process_simulation(
            self: "CutterProcessSimulation._Cast_CutterProcessSimulation",
        ) -> "_644.ShapingProcessSimulation":
            from mastapy.gears.manufacturing.cylindrical.process_simulation import _644

            return self._parent._cast(_644.ShapingProcessSimulation)

        @property
        def cutter_process_simulation(
            self: "CutterProcessSimulation._Cast_CutterProcessSimulation",
        ) -> "CutterProcessSimulation":
            return self._parent

        def __getattr__(
            self: "CutterProcessSimulation._Cast_CutterProcessSimulation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CutterProcessSimulation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def end_of_measured_lead(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndOfMeasuredLead

        if temp is None:
            return 0.0

        return temp

    @end_of_measured_lead.setter
    @enforce_parameter_types
    def end_of_measured_lead(self: Self, value: "float"):
        self.wrapped.EndOfMeasuredLead = float(value) if value is not None else 0.0

    @property
    def end_of_measured_profile(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndOfMeasuredProfile

        if temp is None:
            return 0.0

        return temp

    @end_of_measured_profile.setter
    @enforce_parameter_types
    def end_of_measured_profile(self: Self, value: "float"):
        self.wrapped.EndOfMeasuredProfile = float(value) if value is not None else 0.0

    @property
    def lead_distance_per_step(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeadDistancePerStep

        if temp is None:
            return 0.0

        return temp

    @lead_distance_per_step.setter
    @enforce_parameter_types
    def lead_distance_per_step(self: Self, value: "float"):
        self.wrapped.LeadDistancePerStep = float(value) if value is not None else 0.0

    @property
    def number_of_teeth_to_calculate(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeethToCalculate

        if temp is None:
            return 0

        return temp

    @number_of_teeth_to_calculate.setter
    @enforce_parameter_types
    def number_of_teeth_to_calculate(self: Self, value: "int"):
        self.wrapped.NumberOfTeethToCalculate = int(value) if value is not None else 0

    @property
    def rolling_distance_per_step(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollingDistancePerStep

        if temp is None:
            return 0.0

        return temp

    @rolling_distance_per_step.setter
    @enforce_parameter_types
    def rolling_distance_per_step(self: Self, value: "float"):
        self.wrapped.RollingDistancePerStep = float(value) if value is not None else 0.0

    @property
    def start_of_measured_lead(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfMeasuredLead

        if temp is None:
            return 0.0

        return temp

    @start_of_measured_lead.setter
    @enforce_parameter_types
    def start_of_measured_lead(self: Self, value: "float"):
        self.wrapped.StartOfMeasuredLead = float(value) if value is not None else 0.0

    @property
    def start_of_measured_profile(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfMeasuredProfile

        if temp is None:
            return 0.0

        return temp

    @start_of_measured_profile.setter
    @enforce_parameter_types
    def start_of_measured_profile(self: Self, value: "float"):
        self.wrapped.StartOfMeasuredProfile = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "CutterProcessSimulation._Cast_CutterProcessSimulation":
        return self._Cast_CutterProcessSimulation(self)
