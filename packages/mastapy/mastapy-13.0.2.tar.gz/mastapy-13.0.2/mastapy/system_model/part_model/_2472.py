"""OilLevelSpecification"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model.gears import _2532
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2455
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_LEVEL_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "OilLevelSpecification"
)


__docformat__ = "restructuredtext en"
__all__ = ("OilLevelSpecification",)


Self = TypeVar("Self", bound="OilLevelSpecification")


class OilLevelSpecification(_0.APIBase):
    """OilLevelSpecification

    This is a mastapy class.
    """

    TYPE = _OIL_LEVEL_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilLevelSpecification")

    class _Cast_OilLevelSpecification:
        """Special nested class for casting OilLevelSpecification to subclasses."""

        def __init__(
            self: "OilLevelSpecification._Cast_OilLevelSpecification",
            parent: "OilLevelSpecification",
        ):
            self._parent = parent

        @property
        def oil_level_specification(
            self: "OilLevelSpecification._Cast_OilLevelSpecification",
        ) -> "OilLevelSpecification":
            return self._parent

        def __getattr__(
            self: "OilLevelSpecification._Cast_OilLevelSpecification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilLevelSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_for_oil_level_reference(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_CylindricalGear":
        """ListWithSelectedItem[mastapy.system_model.part_model.gears.CylindricalGear]"""
        temp = self.wrapped.GearForOilLevelReference

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_CylindricalGear",
        )(temp)

    @gear_for_oil_level_reference.setter
    @enforce_parameter_types
    def gear_for_oil_level_reference(self: Self, value: "_2532.CylindricalGear"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGear.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGear.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.GearForOilLevelReference = value

    @property
    def oil_level(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OilLevel

        if temp is None:
            return 0.0

        return temp

    @oil_level.setter
    @enforce_parameter_types
    def oil_level(self: Self, value: "float"):
        self.wrapped.OilLevel = float(value) if value is not None else 0.0

    @property
    def oil_level_reference_datum(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_Datum":
        """ListWithSelectedItem[mastapy.system_model.part_model.Datum]"""
        temp = self.wrapped.OilLevelReferenceDatum

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Datum",
        )(temp)

    @oil_level_reference_datum.setter
    @enforce_parameter_types
    def oil_level_reference_datum(self: Self, value: "_2455.Datum"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Datum.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Datum.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.OilLevelReferenceDatum = value

    @property
    def oil_level_specified(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OilLevelSpecified

        if temp is None:
            return False

        return temp

    @oil_level_specified.setter
    @enforce_parameter_types
    def oil_level_specified(self: Self, value: "bool"):
        self.wrapped.OilLevelSpecified = bool(value) if value is not None else False

    @property
    def use_gear_tip_diameter_for_oil_level_reference(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseGearTipDiameterForOilLevelReference

        if temp is None:
            return False

        return temp

    @use_gear_tip_diameter_for_oil_level_reference.setter
    @enforce_parameter_types
    def use_gear_tip_diameter_for_oil_level_reference(self: Self, value: "bool"):
        self.wrapped.UseGearTipDiameterForOilLevelReference = (
            bool(value) if value is not None else False
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
    def cast_to(self: Self) -> "OilLevelSpecification._Cast_OilLevelSpecification":
        return self._Cast_OilLevelSpecification(self)
