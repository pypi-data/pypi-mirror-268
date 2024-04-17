"""SoundPressureEnclosure"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SOUND_PRESSURE_ENCLOSURE = python_net_import(
    "SMT.MastaAPI.Materials", "SoundPressureEnclosure"
)

if TYPE_CHECKING:
    from mastapy.materials import _287


__docformat__ = "restructuredtext en"
__all__ = ("SoundPressureEnclosure",)


Self = TypeVar("Self", bound="SoundPressureEnclosure")


class SoundPressureEnclosure(_0.APIBase):
    """SoundPressureEnclosure

    This is a mastapy class.
    """

    TYPE = _SOUND_PRESSURE_ENCLOSURE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SoundPressureEnclosure")

    class _Cast_SoundPressureEnclosure:
        """Special nested class for casting SoundPressureEnclosure to subclasses."""

        def __init__(
            self: "SoundPressureEnclosure._Cast_SoundPressureEnclosure",
            parent: "SoundPressureEnclosure",
        ):
            self._parent = parent

        @property
        def sound_pressure_enclosure(
            self: "SoundPressureEnclosure._Cast_SoundPressureEnclosure",
        ) -> "SoundPressureEnclosure":
            return self._parent

        def __getattr__(
            self: "SoundPressureEnclosure._Cast_SoundPressureEnclosure", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SoundPressureEnclosure.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def enclosure_type(self: Self) -> "_287.SoundPressureEnclosureType":
        """mastapy.materials.SoundPressureEnclosureType"""
        temp = self.wrapped.EnclosureType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.SoundPressureEnclosureType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._287", "SoundPressureEnclosureType"
        )(value)

    @enclosure_type.setter
    @enforce_parameter_types
    def enclosure_type(self: Self, value: "_287.SoundPressureEnclosureType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.SoundPressureEnclosureType"
        )
        self.wrapped.EnclosureType = value

    @property
    def measurement_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeasurementRadius

        if temp is None:
            return 0.0

        return temp

    @measurement_radius.setter
    @enforce_parameter_types
    def measurement_radius(self: Self, value: "float"):
        self.wrapped.MeasurementRadius = float(value) if value is not None else 0.0

    @property
    def surface_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceArea

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
    def cast_to(self: Self) -> "SoundPressureEnclosure._Cast_SoundPressureEnclosure":
        return self._Cast_SoundPressureEnclosure(self)
