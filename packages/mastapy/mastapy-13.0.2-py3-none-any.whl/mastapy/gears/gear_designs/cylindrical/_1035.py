"""CylindricalGearSetManufacturingConfigurationSelection"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.gears.manufacturing.cylindrical import _628
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MANUFACTURING_CONFIGURATION_SELECTION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CylindricalGearSetManufacturingConfigurationSelection",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetManufacturingConfigurationSelection",)


Self = TypeVar("Self", bound="CylindricalGearSetManufacturingConfigurationSelection")


class CylindricalGearSetManufacturingConfigurationSelection(_0.APIBase):
    """CylindricalGearSetManufacturingConfigurationSelection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MANUFACTURING_CONFIGURATION_SELECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetManufacturingConfigurationSelection"
    )

    class _Cast_CylindricalGearSetManufacturingConfigurationSelection:
        """Special nested class for casting CylindricalGearSetManufacturingConfigurationSelection to subclasses."""

        def __init__(
            self: "CylindricalGearSetManufacturingConfigurationSelection._Cast_CylindricalGearSetManufacturingConfigurationSelection",
            parent: "CylindricalGearSetManufacturingConfigurationSelection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_manufacturing_configuration_selection(
            self: "CylindricalGearSetManufacturingConfigurationSelection._Cast_CylindricalGearSetManufacturingConfigurationSelection",
        ) -> "CylindricalGearSetManufacturingConfigurationSelection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetManufacturingConfigurationSelection._Cast_CylindricalGearSetManufacturingConfigurationSelection",
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
        self: Self,
        instance_to_wrap: "CylindricalGearSetManufacturingConfigurationSelection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def manufacturing_configuration(
        self: Self,
    ) -> (
        "list_with_selected_item.ListWithSelectedItem_CylindricalSetManufacturingConfig"
    ):
        """ListWithSelectedItem[mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig]"""
        temp = self.wrapped.ManufacturingConfiguration

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_CylindricalSetManufacturingConfig",
        )(temp)

    @manufacturing_configuration.setter
    @enforce_parameter_types
    def manufacturing_configuration(
        self: Self, value: "_628.CylindricalSetManufacturingConfig"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalSetManufacturingConfig.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalSetManufacturingConfig.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ManufacturingConfiguration = value

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
    ) -> "CylindricalGearSetManufacturingConfigurationSelection._Cast_CylindricalGearSetManufacturingConfigurationSelection":
        return self._Cast_CylindricalGearSetManufacturingConfigurationSelection(self)
