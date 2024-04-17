"""CycloidalAssemblyDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_DESIGN = python_net_import(
    "SMT.MastaAPI.Cycloidal", "CycloidalAssemblyDesign"
)

if TYPE_CHECKING:
    from mastapy.cycloidal import _1469, _1468, _1461


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyDesign",)


Self = TypeVar("Self", bound="CycloidalAssemblyDesign")


class CycloidalAssemblyDesign(_0.APIBase):
    """CycloidalAssemblyDesign

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalAssemblyDesign")

    class _Cast_CycloidalAssemblyDesign:
        """Special nested class for casting CycloidalAssemblyDesign to subclasses."""

        def __init__(
            self: "CycloidalAssemblyDesign._Cast_CycloidalAssemblyDesign",
            parent: "CycloidalAssemblyDesign",
        ):
            self._parent = parent

        @property
        def cycloidal_assembly_design(
            self: "CycloidalAssemblyDesign._Cast_CycloidalAssemblyDesign",
        ) -> "CycloidalAssemblyDesign":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyDesign._Cast_CycloidalAssemblyDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalAssemblyDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def eccentricity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Eccentricity

        if temp is None:
            return 0.0

        return temp

    @eccentricity.setter
    @enforce_parameter_types
    def eccentricity(self: Self, value: "float"):
        self.wrapped.Eccentricity = float(value) if value is not None else 0.0

    @property
    def first_disc_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstDiscAngle

        if temp is None:
            return 0.0

        return temp

    @first_disc_angle.setter
    @enforce_parameter_types
    def first_disc_angle(self: Self, value: "float"):
        self.wrapped.FirstDiscAngle = float(value) if value is not None else 0.0

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
    def number_of_lobes(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfLobes

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_lobes.setter
    @enforce_parameter_types
    def number_of_lobes(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfLobes = value

    @property
    def ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Ratio

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_symmetry_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothSymmetryAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def ring_pins(self: Self) -> "_1469.RingPinsDesign":
        """mastapy.cycloidal.RingPinsDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPins

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def disc_phases(self: Self) -> "List[_1468.NamedDiscPhase]":
        """List[mastapy.cycloidal.NamedDiscPhase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiscPhases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def discs(self: Self) -> "List[_1461.CycloidalDiscDesign]":
        """List[mastapy.cycloidal.CycloidalDiscDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Discs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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

    def duplicate(self: Self) -> "CycloidalAssemblyDesign":
        """mastapy.cycloidal.CycloidalAssemblyDesign"""
        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

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
    def cast_to(self: Self) -> "CycloidalAssemblyDesign._Cast_CycloidalAssemblyDesign":
        return self._Cast_CycloidalAssemblyDesign(self)
