"""PlungeShaverDynamicSettings"""

from __future__ import annotations

from typing import TypeVar, Any, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_DYNAMIC_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "PlungeShaverDynamicSettings",
)


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShaverDynamicSettings",)


Self = TypeVar("Self", bound="PlungeShaverDynamicSettings")


class PlungeShaverDynamicSettings(_0.APIBase):
    """PlungeShaverDynamicSettings

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_DYNAMIC_SETTINGS

    class PlungeShavingDynamicAccuracy(Enum):
        """PlungeShavingDynamicAccuracy is a nested enum."""

        @classmethod
        def type_(cls):
            return _PLUNGE_SHAVER_DYNAMIC_SETTINGS.PlungeShavingDynamicAccuracy

        LOW_ACCURACY = 0
        HIGH_ACCURACY = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    PlungeShavingDynamicAccuracy.__setattr__ = __enum_setattr
    PlungeShavingDynamicAccuracy.__delattr__ = __enum_delattr

    class PlungeShavingDynamicFlank(Enum):
        """PlungeShavingDynamicFlank is a nested enum."""

        @classmethod
        def type_(cls):
            return _PLUNGE_SHAVER_DYNAMIC_SETTINGS.PlungeShavingDynamicFlank

        LEFT_FLANK = 0
        RIGHT_FLANK = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    PlungeShavingDynamicFlank.__setattr__ = __enum_setattr
    PlungeShavingDynamicFlank.__delattr__ = __enum_delattr

    class PlungeShavingDynamicsSection(Enum):
        """PlungeShavingDynamicsSection is a nested enum."""

        @classmethod
        def type_(cls):
            return _PLUNGE_SHAVER_DYNAMIC_SETTINGS.PlungeShavingDynamicsSection

        CENTER_SECTION = 0
        TOPCENTERBOTTOM_SECTION_125_FACE_WIDTH_FROM_TOPBOTTOM_END = 1
        SPECIFIED_ZPLANE = 2

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    PlungeShavingDynamicsSection.__setattr__ = __enum_setattr
    PlungeShavingDynamicsSection.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlungeShaverDynamicSettings")

    class _Cast_PlungeShaverDynamicSettings:
        """Special nested class for casting PlungeShaverDynamicSettings to subclasses."""

        def __init__(
            self: "PlungeShaverDynamicSettings._Cast_PlungeShaverDynamicSettings",
            parent: "PlungeShaverDynamicSettings",
        ):
            self._parent = parent

        @property
        def plunge_shaver_dynamic_settings(
            self: "PlungeShaverDynamicSettings._Cast_PlungeShaverDynamicSettings",
        ) -> "PlungeShaverDynamicSettings":
            return self._parent

        def __getattr__(
            self: "PlungeShaverDynamicSettings._Cast_PlungeShaverDynamicSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlungeShaverDynamicSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculation_accuracy(
        self: Self,
    ) -> "PlungeShaverDynamicSettings.PlungeShavingDynamicAccuracy":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.PlungeShaverDynamicSettings.PlungeShavingDynamicAccuracy"""
        temp = self.wrapped.CalculationAccuracy

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.PlungeShaverDynamicSettings+PlungeShavingDynamicAccuracy",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.PlungeShaverDynamicSettings.PlungeShaverDynamicSettings",
            "PlungeShavingDynamicAccuracy",
        )(value)

    @calculation_accuracy.setter
    @enforce_parameter_types
    def calculation_accuracy(
        self: Self, value: "PlungeShaverDynamicSettings.PlungeShavingDynamicAccuracy"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.PlungeShaverDynamicSettings+PlungeShavingDynamicAccuracy",
        )
        self.wrapped.CalculationAccuracy = value

    @property
    def calculation_flank(
        self: Self,
    ) -> "PlungeShaverDynamicSettings.PlungeShavingDynamicFlank":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.PlungeShaverDynamicSettings.PlungeShavingDynamicFlank"""
        temp = self.wrapped.CalculationFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.PlungeShaverDynamicSettings+PlungeShavingDynamicFlank",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.PlungeShaverDynamicSettings.PlungeShaverDynamicSettings",
            "PlungeShavingDynamicFlank",
        )(value)

    @calculation_flank.setter
    @enforce_parameter_types
    def calculation_flank(
        self: Self, value: "PlungeShaverDynamicSettings.PlungeShavingDynamicFlank"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.PlungeShaverDynamicSettings+PlungeShavingDynamicFlank",
        )
        self.wrapped.CalculationFlank = value

    @property
    def section_locations(
        self: Self,
    ) -> "PlungeShaverDynamicSettings.PlungeShavingDynamicsSection":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.PlungeShaverDynamicSettings.PlungeShavingDynamicsSection"""
        temp = self.wrapped.SectionLocations

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.PlungeShaverDynamicSettings+PlungeShavingDynamicsSection",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.PlungeShaverDynamicSettings.PlungeShaverDynamicSettings",
            "PlungeShavingDynamicsSection",
        )(value)

    @section_locations.setter
    @enforce_parameter_types
    def section_locations(
        self: Self, value: "PlungeShaverDynamicSettings.PlungeShavingDynamicsSection"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.PlungeShaverDynamicSettings+PlungeShavingDynamicsSection",
        )
        self.wrapped.SectionLocations = value

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
    ) -> "PlungeShaverDynamicSettings._Cast_PlungeShaverDynamicSettings":
        return self._Cast_PlungeShaverDynamicSettings(self)
