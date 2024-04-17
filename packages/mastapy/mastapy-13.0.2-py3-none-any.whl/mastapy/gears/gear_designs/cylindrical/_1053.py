"""GearSetManufacturingConfigurationSetup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_MANUFACTURING_CONFIGURATION_SETUP = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "GearSetManufacturingConfigurationSetup",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1006, _1052


__docformat__ = "restructuredtext en"
__all__ = ("GearSetManufacturingConfigurationSetup",)


Self = TypeVar("Self", bound="GearSetManufacturingConfigurationSetup")


class GearSetManufacturingConfigurationSetup(_0.APIBase):
    """GearSetManufacturingConfigurationSetup

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_MANUFACTURING_CONFIGURATION_SETUP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetManufacturingConfigurationSetup"
    )

    class _Cast_GearSetManufacturingConfigurationSetup:
        """Special nested class for casting GearSetManufacturingConfigurationSetup to subclasses."""

        def __init__(
            self: "GearSetManufacturingConfigurationSetup._Cast_GearSetManufacturingConfigurationSetup",
            parent: "GearSetManufacturingConfigurationSetup",
        ):
            self._parent = parent

        @property
        def gear_set_manufacturing_configuration_setup(
            self: "GearSetManufacturingConfigurationSetup._Cast_GearSetManufacturingConfigurationSetup",
        ) -> "GearSetManufacturingConfigurationSetup":
            return self._parent

        def __getattr__(
            self: "GearSetManufacturingConfigurationSetup._Cast_GearSetManufacturingConfigurationSetup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "GearSetManufacturingConfigurationSetup.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def create_new_suitable_cutters(
        self: Self,
    ) -> "_1006.CreateNewSuitableCutterOption":
        """mastapy.gears.gear_designs.cylindrical.CreateNewSuitableCutterOption"""
        temp = self.wrapped.CreateNewSuitableCutters

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CreateNewSuitableCutterOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1006",
            "CreateNewSuitableCutterOption",
        )(value)

    @create_new_suitable_cutters.setter
    @enforce_parameter_types
    def create_new_suitable_cutters(
        self: Self, value: "_1006.CreateNewSuitableCutterOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CreateNewSuitableCutterOption",
        )
        self.wrapped.CreateNewSuitableCutters = value

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def use_as_design_mode_geometry(
        self: Self,
    ) -> "_1006.CreateNewSuitableCutterOption":
        """mastapy.gears.gear_designs.cylindrical.CreateNewSuitableCutterOption"""
        temp = self.wrapped.UseAsDesignModeGeometry

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CreateNewSuitableCutterOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1006",
            "CreateNewSuitableCutterOption",
        )(value)

    @use_as_design_mode_geometry.setter
    @enforce_parameter_types
    def use_as_design_mode_geometry(
        self: Self, value: "_1006.CreateNewSuitableCutterOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CreateNewSuitableCutterOption",
        )
        self.wrapped.UseAsDesignModeGeometry = value

    @property
    def gears(self: Self) -> "List[_1052.GearManufacturingConfigSetupViewModel]":
        """List[mastapy.gears.gear_designs.cylindrical.GearManufacturingConfigSetupViewModel]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

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
    ) -> "GearSetManufacturingConfigurationSetup._Cast_GearSetManufacturingConfigurationSetup":
        return self._Cast_GearSetManufacturingConfigurationSetup(self)
