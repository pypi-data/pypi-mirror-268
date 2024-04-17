"""MountingError"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTING_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "MountingError",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _668,
        _693,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountingError",)


Self = TypeVar("Self", bound="MountingError")


class MountingError(_0.APIBase):
    """MountingError

    This is a mastapy class.
    """

    TYPE = _MOUNTING_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountingError")

    class _Cast_MountingError:
        """Special nested class for casting MountingError to subclasses."""

        def __init__(
            self: "MountingError._Cast_MountingError", parent: "MountingError"
        ):
            self._parent = parent

        @property
        def gear_mounting_error(
            self: "MountingError._Cast_MountingError",
        ) -> "_668.GearMountingError":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _668,
            )

            return self._parent._cast(_668.GearMountingError)

        @property
        def rack_mounting_error(
            self: "MountingError._Cast_MountingError",
        ) -> "_693.RackMountingError":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _693,
            )

            return self._parent._cast(_693.RackMountingError)

        @property
        def mounting_error(
            self: "MountingError._Cast_MountingError",
        ) -> "MountingError":
            return self._parent

        def __getattr__(self: "MountingError._Cast_MountingError", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountingError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_between_two_sections(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceBetweenTwoSections

        if temp is None:
            return 0.0

        return temp

    @distance_between_two_sections.setter
    @enforce_parameter_types
    def distance_between_two_sections(self: Self, value: "float"):
        self.wrapped.DistanceBetweenTwoSections = (
            float(value) if value is not None else 0.0
        )

    @property
    def first_section_phase_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstSectionPhaseAngle

        if temp is None:
            return 0.0

        return temp

    @first_section_phase_angle.setter
    @enforce_parameter_types
    def first_section_phase_angle(self: Self, value: "float"):
        self.wrapped.FirstSectionPhaseAngle = float(value) if value is not None else 0.0

    @property
    def first_section_radial_runout(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstSectionRadialRunout

        if temp is None:
            return 0.0

        return temp

    @first_section_radial_runout.setter
    @enforce_parameter_types
    def first_section_radial_runout(self: Self, value: "float"):
        self.wrapped.FirstSectionRadialRunout = (
            float(value) if value is not None else 0.0
        )

    @property
    def second_section_phase_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SecondSectionPhaseAngle

        if temp is None:
            return 0.0

        return temp

    @second_section_phase_angle.setter
    @enforce_parameter_types
    def second_section_phase_angle(self: Self, value: "float"):
        self.wrapped.SecondSectionPhaseAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def second_section_radial_runout(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SecondSectionRadialRunout

        if temp is None:
            return 0.0

        return temp

    @second_section_radial_runout.setter
    @enforce_parameter_types
    def second_section_radial_runout(self: Self, value: "float"):
        self.wrapped.SecondSectionRadialRunout = (
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
    def cast_to(self: Self) -> "MountingError._Cast_MountingError":
        return self._Cast_MountingError(self)
