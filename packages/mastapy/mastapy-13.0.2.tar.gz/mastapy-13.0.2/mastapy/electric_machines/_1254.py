"""CADMagnetDetails"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_MAGNET_DETAILS = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "CADMagnetDetails"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1289


__docformat__ = "restructuredtext en"
__all__ = ("CADMagnetDetails",)


Self = TypeVar("Self", bound="CADMagnetDetails")


class CADMagnetDetails(_0.APIBase):
    """CADMagnetDetails

    This is a mastapy class.
    """

    TYPE = _CAD_MAGNET_DETAILS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADMagnetDetails")

    class _Cast_CADMagnetDetails:
        """Special nested class for casting CADMagnetDetails to subclasses."""

        def __init__(
            self: "CADMagnetDetails._Cast_CADMagnetDetails", parent: "CADMagnetDetails"
        ):
            self._parent = parent

        @property
        def cad_magnet_details(
            self: "CADMagnetDetails._Cast_CADMagnetDetails",
        ) -> "CADMagnetDetails":
            return self._parent

        def __getattr__(self: "CADMagnetDetails._Cast_CADMagnetDetails", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADMagnetDetails.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def directly_specify_magnetisation_angle(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DirectlySpecifyMagnetisationAngle

        if temp is None:
            return False

        return temp

    @directly_specify_magnetisation_angle.setter
    @enforce_parameter_types
    def directly_specify_magnetisation_angle(self: Self, value: "bool"):
        self.wrapped.DirectlySpecifyMagnetisationAngle = (
            bool(value) if value is not None else False
        )

    @property
    def magnetisation_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MagnetisationAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @magnetisation_angle.setter
    @enforce_parameter_types
    def magnetisation_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MagnetisationAngle = value

    @property
    def magnetisation_direction(self: Self) -> "_1289.MagnetisationDirection":
        """mastapy.electric_machines.MagnetisationDirection"""
        temp = self.wrapped.MagnetisationDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.MagnetisationDirection"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1289", "MagnetisationDirection"
        )(value)

    @magnetisation_direction.setter
    @enforce_parameter_types
    def magnetisation_direction(self: Self, value: "_1289.MagnetisationDirection"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.MagnetisationDirection"
        )
        self.wrapped.MagnetisationDirection = value

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
    def cast_to(self: Self) -> "CADMagnetDetails._Cast_CADMagnetDetails":
        return self._Cast_CADMagnetDetails(self)
