"""RingPinsDesign"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_DESIGN = python_net_import("SMT.MastaAPI.Cycloidal", "RingPinsDesign")


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsDesign",)


Self = TypeVar("Self", bound="RingPinsDesign")


class RingPinsDesign(_0.APIBase):
    """RingPinsDesign

    This is a mastapy class.
    """

    TYPE = _RING_PINS_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsDesign")

    class _Cast_RingPinsDesign:
        """Special nested class for casting RingPinsDesign to subclasses."""

        def __init__(
            self: "RingPinsDesign._Cast_RingPinsDesign", parent: "RingPinsDesign"
        ):
            self._parent = parent

        @property
        def ring_pins_design(
            self: "RingPinsDesign._Cast_RingPinsDesign",
        ) -> "RingPinsDesign":
            return self._parent

        def __getattr__(self: "RingPinsDesign._Cast_RingPinsDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length_of_pins(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LengthOfPins

        if temp is None:
            return 0.0

        return temp

    @length_of_pins.setter
    @enforce_parameter_types
    def length_of_pins(self: Self, value: "float"):
        self.wrapped.LengthOfPins = float(value) if value is not None else 0.0

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
    def number_of_pins(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPins

        if temp is None:
            return 0

        return temp

    @number_of_pins.setter
    @enforce_parameter_types
    def number_of_pins(self: Self, value: "int"):
        self.wrapped.NumberOfPins = int(value) if value is not None else 0

    @property
    def pin_centre_circle_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinCentreCircleDiameter

        if temp is None:
            return 0.0

        return temp

    @pin_centre_circle_diameter.setter
    @enforce_parameter_types
    def pin_centre_circle_diameter(self: Self, value: "float"):
        self.wrapped.PinCentreCircleDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def pin_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinDiameter

        if temp is None:
            return 0.0

        return temp

    @pin_diameter.setter
    @enforce_parameter_types
    def pin_diameter(self: Self, value: "float"):
        self.wrapped.PinDiameter = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "RingPinsDesign._Cast_RingPinsDesign":
        return self._Cast_RingPinsDesign(self)
