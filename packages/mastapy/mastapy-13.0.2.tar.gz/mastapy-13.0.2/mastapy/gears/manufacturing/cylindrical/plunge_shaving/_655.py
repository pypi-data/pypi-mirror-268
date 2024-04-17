"""PlungeShaverSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving", "PlungeShaverSettings"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _648


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShaverSettings",)


Self = TypeVar("Self", bound="PlungeShaverSettings")


class PlungeShaverSettings(_0.APIBase):
    """PlungeShaverSettings

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlungeShaverSettings")

    class _Cast_PlungeShaverSettings:
        """Special nested class for casting PlungeShaverSettings to subclasses."""

        def __init__(
            self: "PlungeShaverSettings._Cast_PlungeShaverSettings",
            parent: "PlungeShaverSettings",
        ):
            self._parent = parent

        @property
        def plunge_shaver_settings(
            self: "PlungeShaverSettings._Cast_PlungeShaverSettings",
        ) -> "PlungeShaverSettings":
            return self._parent

        def __getattr__(
            self: "PlungeShaverSettings._Cast_PlungeShaverSettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlungeShaverSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extend_gear_surface_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ExtendGearSurfaceFactor

        if temp is None:
            return 0.0

        return temp

    @extend_gear_surface_factor.setter
    @enforce_parameter_types
    def extend_gear_surface_factor(self: Self, value: "float"):
        self.wrapped.ExtendGearSurfaceFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def lead_display_method(self: Self) -> "_648.MicroGeometryDefinitionMethod":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod"""
        temp = self.wrapped.LeadDisplayMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.plunge_shaving._648",
            "MicroGeometryDefinitionMethod",
        )(value)

    @lead_display_method.setter
    @enforce_parameter_types
    def lead_display_method(self: Self, value: "_648.MicroGeometryDefinitionMethod"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )
        self.wrapped.LeadDisplayMethod = value

    @property
    def number_of_cutter_transverse_planes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfCutterTransversePlanes

        if temp is None:
            return 0

        return temp

    @number_of_cutter_transverse_planes.setter
    @enforce_parameter_types
    def number_of_cutter_transverse_planes(self: Self, value: "int"):
        self.wrapped.NumberOfCutterTransversePlanes = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_gear_tip_transverse_planes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfGearTipTransversePlanes

        if temp is None:
            return 0

        return temp

    @number_of_gear_tip_transverse_planes.setter
    @enforce_parameter_types
    def number_of_gear_tip_transverse_planes(self: Self, value: "int"):
        self.wrapped.NumberOfGearTipTransversePlanes = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_points_on_each_shaver_transverse_plane(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsOnEachShaverTransversePlane

        if temp is None:
            return 0

        return temp

    @number_of_points_on_each_shaver_transverse_plane.setter
    @enforce_parameter_types
    def number_of_points_on_each_shaver_transverse_plane(self: Self, value: "int"):
        self.wrapped.NumberOfPointsOnEachShaverTransversePlane = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_points_on_the_input_gear_involute(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsOnTheInputGearInvolute

        if temp is None:
            return 0

        return temp

    @number_of_points_on_the_input_gear_involute.setter
    @enforce_parameter_types
    def number_of_points_on_the_input_gear_involute(self: Self, value: "int"):
        self.wrapped.NumberOfPointsOnTheInputGearInvolute = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_points_on_the_tip(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPointsOnTheTip

        if temp is None:
            return 0

        return temp

    @number_of_points_on_the_tip.setter
    @enforce_parameter_types
    def number_of_points_on_the_tip(self: Self, value: "int"):
        self.wrapped.NumberOfPointsOnTheTip = int(value) if value is not None else 0

    @property
    def number_of_solver_initial_guesses(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSolverInitialGuesses

        if temp is None:
            return 0

        return temp

    @number_of_solver_initial_guesses.setter
    @enforce_parameter_types
    def number_of_solver_initial_guesses(self: Self, value: "int"):
        self.wrapped.NumberOfSolverInitialGuesses = (
            int(value) if value is not None else 0
        )

    @property
    def profile_display_method(self: Self) -> "_648.MicroGeometryDefinitionMethod":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod"""
        temp = self.wrapped.ProfileDisplayMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.plunge_shaving._648",
            "MicroGeometryDefinitionMethod",
        )(value)

    @profile_display_method.setter
    @enforce_parameter_types
    def profile_display_method(self: Self, value: "_648.MicroGeometryDefinitionMethod"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )
        self.wrapped.ProfileDisplayMethod = value

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
    def cast_to(self: Self) -> "PlungeShaverSettings._Cast_PlungeShaverSettings":
        return self._Cast_PlungeShaverSettings(self)
