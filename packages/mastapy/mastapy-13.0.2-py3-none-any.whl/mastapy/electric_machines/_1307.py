"""StatorCutOutSpecification"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_CUT_OUT_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "StatorCutOutSpecification"
)


__docformat__ = "restructuredtext en"
__all__ = ("StatorCutOutSpecification",)


Self = TypeVar("Self", bound="StatorCutOutSpecification")


class StatorCutOutSpecification(_0.APIBase):
    """StatorCutOutSpecification

    This is a mastapy class.
    """

    TYPE = _STATOR_CUT_OUT_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StatorCutOutSpecification")

    class _Cast_StatorCutOutSpecification:
        """Special nested class for casting StatorCutOutSpecification to subclasses."""

        def __init__(
            self: "StatorCutOutSpecification._Cast_StatorCutOutSpecification",
            parent: "StatorCutOutSpecification",
        ):
            self._parent = parent

        @property
        def stator_cut_out_specification(
            self: "StatorCutOutSpecification._Cast_StatorCutOutSpecification",
        ) -> "StatorCutOutSpecification":
            return self._parent

        def __getattr__(
            self: "StatorCutOutSpecification._Cast_StatorCutOutSpecification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StatorCutOutSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_to_first_cut_out(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngleToFirstCutOut

        if temp is None:
            return 0.0

        return temp

    @angle_to_first_cut_out.setter
    @enforce_parameter_types
    def angle_to_first_cut_out(self: Self, value: "float"):
        self.wrapped.AngleToFirstCutOut = float(value) if value is not None else 0.0

    @property
    def corner_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CornerRadius

        if temp is None:
            return 0.0

        return temp

    @corner_radius.setter
    @enforce_parameter_types
    def corner_radius(self: Self, value: "float"):
        self.wrapped.CornerRadius = float(value) if value is not None else 0.0

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

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
    def number_of_cut_outs(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfCutOuts

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_cut_outs.setter
    @enforce_parameter_types
    def number_of_cut_outs(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfCutOuts = value

    @property
    def radial_position(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialPosition

        if temp is None:
            return 0.0

        return temp

    @radial_position.setter
    @enforce_parameter_types
    def radial_position(self: Self, value: "float"):
        self.wrapped.RadialPosition = float(value) if value is not None else 0.0

    @property
    def rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Rotation

        if temp is None:
            return 0.0

        return temp

    @rotation.setter
    @enforce_parameter_types
    def rotation(self: Self, value: "float"):
        self.wrapped.Rotation = float(value) if value is not None else 0.0

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

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
    ) -> "StatorCutOutSpecification._Cast_StatorCutOutSpecification":
        return self._Cast_StatorCutOutSpecification(self)
