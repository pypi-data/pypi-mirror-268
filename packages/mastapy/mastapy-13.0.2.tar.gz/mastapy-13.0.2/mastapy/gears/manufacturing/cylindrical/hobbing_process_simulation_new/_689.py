"""ProcessSimulationNew"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROCESS_SIMULATION_NEW = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "ProcessSimulationNew",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _684,
        _685,
        _686,
        _687,
        _691,
        _688,
        _676,
        _703,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ProcessSimulationNew",)


Self = TypeVar("Self", bound="ProcessSimulationNew")
T = TypeVar("T", bound="_688.ProcessSimulationInput")


class ProcessSimulationNew(_0.APIBase, Generic[T]):
    """ProcessSimulationNew

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _PROCESS_SIMULATION_NEW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProcessSimulationNew")

    class _Cast_ProcessSimulationNew:
        """Special nested class for casting ProcessSimulationNew to subclasses."""

        def __init__(
            self: "ProcessSimulationNew._Cast_ProcessSimulationNew",
            parent: "ProcessSimulationNew",
        ):
            self._parent = parent

        @property
        def hobbing_process_simulation_new(
            self: "ProcessSimulationNew._Cast_ProcessSimulationNew",
        ) -> "_676.HobbingProcessSimulationNew":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _676,
            )

            return self._parent._cast(_676.HobbingProcessSimulationNew)

        @property
        def worm_grinding_process_simulation_new(
            self: "ProcessSimulationNew._Cast_ProcessSimulationNew",
        ) -> "_703.WormGrindingProcessSimulationNew":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _703,
            )

            return self._parent._cast(_703.WormGrindingProcessSimulationNew)

        @property
        def process_simulation_new(
            self: "ProcessSimulationNew._Cast_ProcessSimulationNew",
        ) -> "ProcessSimulationNew":
            return self._parent

        def __getattr__(
            self: "ProcessSimulationNew._Cast_ProcessSimulationNew", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProcessSimulationNew.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def achieved_agma20151a01_quality_grade(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AchievedAGMA20151A01QualityGrade

        if temp is None:
            return 0.0

        return temp

    @property
    def achieved_iso132811995e_quality_grade(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AchievedISO132811995EQualityGrade

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_tooth_shape_calculation(self: Self) -> "_684.ProcessGearShape":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessGearShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearToothShapeCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def input(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Input

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_calculation(self: Self) -> "_685.ProcessLeadCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessLeadCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pitch_calculation(self: Self) -> "_686.ProcessPitchCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessPitchCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_calculation(self: Self) -> "_687.ProcessProfileCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessProfileCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_modification_calculation(
        self: Self,
    ) -> "_691.ProcessTotalModificationCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ProcessTotalModificationCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalModificationCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "ProcessSimulationNew._Cast_ProcessSimulationNew":
        return self._Cast_ProcessSimulationNew(self)
