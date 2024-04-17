"""DesignSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy.utility import _1592
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_DESIGN_SETTINGS = python_net_import("SMT.MastaAPI.SystemModel", "DesignSettings")

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _50
    from mastapy.bearings import _1888
    from mastapy.gears.gear_designs import _945, _947, _950
    from mastapy.gears.gear_designs.cylindrical import _1018, _1026
    from mastapy.gears.rating.cylindrical import _457
    from mastapy.materials import _276
    from mastapy.shafts import _40


__docformat__ = "restructuredtext en"
__all__ = ("DesignSettings",)


Self = TypeVar("Self", bound="DesignSettings")


class DesignSettings(_0.APIBase, _1592.IHaveAllSettings):
    """DesignSettings

    This is a mastapy class.
    """

    TYPE = _DESIGN_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignSettings")

    class _Cast_DesignSettings:
        """Special nested class for casting DesignSettings to subclasses."""

        def __init__(
            self: "DesignSettings._Cast_DesignSettings", parent: "DesignSettings"
        ):
            self._parent = parent

        @property
        def design_settings(
            self: "DesignSettings._Cast_DesignSettings",
        ) -> "DesignSettings":
            return self._parent

        def __getattr__(self: "DesignSettings._Cast_DesignSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_settings_database_item(self: Self) -> "str":
        """str"""
        temp = self.wrapped.AnalysisSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ""

        return temp

    @analysis_settings_database_item.setter
    @enforce_parameter_types
    def analysis_settings_database_item(self: Self, value: "str"):
        self.wrapped.AnalysisSettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def analysis_settings_for_new_designs(self: Self) -> "str":
        """str"""
        temp = self.wrapped.AnalysisSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ""

        return temp

    @analysis_settings_for_new_designs.setter
    @enforce_parameter_types
    def analysis_settings_for_new_designs(self: Self, value: "str"):
        self.wrapped.AnalysisSettingsForNewDesigns.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def bearing_settings_database_item(self: Self) -> "str":
        """str"""
        temp = self.wrapped.BearingSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ""

        return temp

    @bearing_settings_database_item.setter
    @enforce_parameter_types
    def bearing_settings_database_item(self: Self, value: "str"):
        self.wrapped.BearingSettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def bearing_settings_for_new_designs(self: Self) -> "str":
        """str"""
        temp = self.wrapped.BearingSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ""

        return temp

    @bearing_settings_for_new_designs.setter
    @enforce_parameter_types
    def bearing_settings_for_new_designs(self: Self, value: "str"):
        self.wrapped.BearingSettingsForNewDesigns.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def bevel_hypoid_gear_design_settings_database_item(self: Self) -> "str":
        """str"""
        temp = self.wrapped.BevelHypoidGearDesignSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ""

        return temp

    @bevel_hypoid_gear_design_settings_database_item.setter
    @enforce_parameter_types
    def bevel_hypoid_gear_design_settings_database_item(self: Self, value: "str"):
        self.wrapped.BevelHypoidGearDesignSettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def bevel_hypoid_gear_design_settings_for_new_designs_database_item(
        self: Self,
    ) -> "str":
        """str"""
        temp = (
            self.wrapped.BevelHypoidGearDesignSettingsForNewDesignsDatabaseItem.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @bevel_hypoid_gear_design_settings_for_new_designs_database_item.setter
    @enforce_parameter_types
    def bevel_hypoid_gear_design_settings_for_new_designs_database_item(
        self: Self, value: "str"
    ):
        self.wrapped.BevelHypoidGearDesignSettingsForNewDesignsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def bevel_hypoid_gear_rating_settings_database_item(self: Self) -> "str":
        """str"""
        temp = self.wrapped.BevelHypoidGearRatingSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ""

        return temp

    @bevel_hypoid_gear_rating_settings_database_item.setter
    @enforce_parameter_types
    def bevel_hypoid_gear_rating_settings_database_item(self: Self, value: "str"):
        self.wrapped.BevelHypoidGearRatingSettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def bevel_hypoid_gear_rating_settings_for_new_designs_database_item(
        self: Self,
    ) -> "str":
        """str"""
        temp = (
            self.wrapped.BevelHypoidGearRatingSettingsForNewDesignsDatabaseItem.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @bevel_hypoid_gear_rating_settings_for_new_designs_database_item.setter
    @enforce_parameter_types
    def bevel_hypoid_gear_rating_settings_for_new_designs_database_item(
        self: Self, value: "str"
    ):
        self.wrapped.BevelHypoidGearRatingSettingsForNewDesignsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def cylindrical_gear_design_constraints_settings_database_item(self: Self) -> "str":
        """str"""
        temp = (
            self.wrapped.CylindricalGearDesignConstraintsSettingsDatabaseItem.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @cylindrical_gear_design_constraints_settings_database_item.setter
    @enforce_parameter_types
    def cylindrical_gear_design_constraints_settings_database_item(
        self: Self, value: "str"
    ):
        self.wrapped.CylindricalGearDesignConstraintsSettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def cylindrical_gear_design_constraints_settings_for_new_designs(
        self: Self,
    ) -> "str":
        """str"""
        temp = (
            self.wrapped.CylindricalGearDesignConstraintsSettingsForNewDesigns.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @cylindrical_gear_design_constraints_settings_for_new_designs.setter
    @enforce_parameter_types
    def cylindrical_gear_design_constraints_settings_for_new_designs(
        self: Self, value: "str"
    ):
        self.wrapped.CylindricalGearDesignConstraintsSettingsForNewDesigns.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def cylindrical_gear_design_and_rating_settings_database_item(self: Self) -> "str":
        """str"""
        temp = (
            self.wrapped.CylindricalGearDesignAndRatingSettingsDatabaseItem.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @cylindrical_gear_design_and_rating_settings_database_item.setter
    @enforce_parameter_types
    def cylindrical_gear_design_and_rating_settings_database_item(
        self: Self, value: "str"
    ):
        self.wrapped.CylindricalGearDesignAndRatingSettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def cylindrical_gear_design_and_rating_settings_for_new_designs(
        self: Self,
    ) -> "str":
        """str"""
        temp = (
            self.wrapped.CylindricalGearDesignAndRatingSettingsForNewDesigns.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @cylindrical_gear_design_and_rating_settings_for_new_designs.setter
    @enforce_parameter_types
    def cylindrical_gear_design_and_rating_settings_for_new_designs(
        self: Self, value: "str"
    ):
        self.wrapped.CylindricalGearDesignAndRatingSettingsForNewDesigns.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def cylindrical_gear_micro_geometry_settings_database_item(self: Self) -> "str":
        """str"""
        temp = (
            self.wrapped.CylindricalGearMicroGeometrySettingsDatabaseItem.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @cylindrical_gear_micro_geometry_settings_database_item.setter
    @enforce_parameter_types
    def cylindrical_gear_micro_geometry_settings_database_item(
        self: Self, value: "str"
    ):
        self.wrapped.CylindricalGearMicroGeometrySettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def cylindrical_gear_micro_geometry_settings_for_new_designs(self: Self) -> "str":
        """str"""
        temp = (
            self.wrapped.CylindricalGearMicroGeometrySettingsForNewDesigns.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @cylindrical_gear_micro_geometry_settings_for_new_designs.setter
    @enforce_parameter_types
    def cylindrical_gear_micro_geometry_settings_for_new_designs(
        self: Self, value: "str"
    ):
        self.wrapped.CylindricalGearMicroGeometrySettingsForNewDesigns.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def design_constraints_settings_database_item(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignConstraintsSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ""

        return temp

    @design_constraints_settings_database_item.setter
    @enforce_parameter_types
    def design_constraints_settings_database_item(self: Self, value: "str"):
        self.wrapped.DesignConstraintsSettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def design_constraints_settings_for_new_designs(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignConstraintsSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ""

        return temp

    @design_constraints_settings_for_new_designs.setter
    @enforce_parameter_types
    def design_constraints_settings_for_new_designs(self: Self, value: "str"):
        self.wrapped.DesignConstraintsSettingsForNewDesigns.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def materials_settings_database_item(self: Self) -> "str":
        """str"""
        temp = self.wrapped.MaterialsSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ""

        return temp

    @materials_settings_database_item.setter
    @enforce_parameter_types
    def materials_settings_database_item(self: Self, value: "str"):
        self.wrapped.MaterialsSettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def materials_settings_for_new_designs(self: Self) -> "str":
        """str"""
        temp = self.wrapped.MaterialsSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ""

        return temp

    @materials_settings_for_new_designs.setter
    @enforce_parameter_types
    def materials_settings_for_new_designs(self: Self, value: "str"):
        self.wrapped.MaterialsSettingsForNewDesigns.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def shaft_settings_database_item(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ShaftSettingsDatabaseItem.SelectedItemName

        if temp is None:
            return ""

        return temp

    @shaft_settings_database_item.setter
    @enforce_parameter_types
    def shaft_settings_database_item(self: Self, value: "str"):
        self.wrapped.ShaftSettingsDatabaseItem.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def shaft_settings_for_new_designs(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ShaftSettingsForNewDesigns.SelectedItemName

        if temp is None:
            return ""

        return temp

    @shaft_settings_for_new_designs.setter
    @enforce_parameter_types
    def shaft_settings_for_new_designs(self: Self, value: "str"):
        self.wrapped.ShaftSettingsForNewDesigns.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def analysis_settings(self: Self) -> "_50.AnalysisSettingsItem":
        """mastapy.nodal_analysis.AnalysisSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_settings(self: Self) -> "_1888.BearingSettingsItem":
        """mastapy.bearings.BearingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_hypoid_gear_design_settings(
        self: Self,
    ) -> "_945.BevelHypoidGearDesignSettingsItem":
        """mastapy.gears.gear_designs.BevelHypoidGearDesignSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearDesignSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_hypoid_gear_rating_settings(
        self: Self,
    ) -> "_947.BevelHypoidGearRatingSettingsItem":
        """mastapy.gears.gear_designs.BevelHypoidGearRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_constraints_settings(
        self: Self,
    ) -> "_1018.CylindricalGearDesignConstraints":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesignConstraints

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignConstraintsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_and_rating_settings(
        self: Self,
    ) -> "_457.CylindricalGearDesignAndRatingSettingsItem":
        """mastapy.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignAndRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_micro_geometry_settings(
        self: Self,
    ) -> "_1026.CylindricalGearMicroGeometrySettingsItem":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMicroGeometrySettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMicroGeometrySettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_constraints_settings(self: Self) -> "_950.DesignConstraintsCollection":
        """mastapy.gears.gear_designs.DesignConstraintsCollection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignConstraintsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def materials_settings(self: Self) -> "_276.MaterialsSettingsItem":
        """mastapy.materials.MaterialsSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_settings(self: Self) -> "_40.ShaftSettingsItem":
        """mastapy.shafts.ShaftSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def copy_settings_from_file(self: Self, file_name: "str"):
        """Method does not return.

        Args:
            file_name (str)
        """
        file_name = str(file_name)
        self.wrapped.CopySettingsFromFile(file_name if file_name else "")

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
    def cast_to(self: Self) -> "DesignSettings._Cast_DesignSettings":
        return self._Cast_DesignSettings(self)
