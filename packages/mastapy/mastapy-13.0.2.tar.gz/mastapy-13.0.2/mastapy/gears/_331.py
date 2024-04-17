"""GearSetDesignGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears import _340
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_GEAR_SET_DESIGN_GROUP = python_net_import("SMT.MastaAPI.Gears", "GearSetDesignGroup")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1088, _1018
    from mastapy.gears.rating.cylindrical import _481, _457
    from mastapy.materials import _259


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDesignGroup",)


Self = TypeVar("Self", bound="GearSetDesignGroup")


class GearSetDesignGroup(_0.APIBase):
    """GearSetDesignGroup

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DESIGN_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDesignGroup")

    class _Cast_GearSetDesignGroup:
        """Special nested class for casting GearSetDesignGroup to subclasses."""

        def __init__(
            self: "GearSetDesignGroup._Cast_GearSetDesignGroup",
            parent: "GearSetDesignGroup",
        ):
            self._parent = parent

        @property
        def gear_set_design_group(
            self: "GearSetDesignGroup._Cast_GearSetDesignGroup",
        ) -> "GearSetDesignGroup":
            return self._parent

        def __getattr__(self: "GearSetDesignGroup._Cast_GearSetDesignGroup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDesignGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def default_cylindrical_gear_material_agma(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DefaultCylindricalGearMaterialAGMA.SelectedItemName

        if temp is None:
            return ""

        return temp

    @default_cylindrical_gear_material_agma.setter
    @enforce_parameter_types
    def default_cylindrical_gear_material_agma(self: Self, value: "str"):
        self.wrapped.DefaultCylindricalGearMaterialAGMA.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def default_cylindrical_gear_material_iso(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DefaultCylindricalGearMaterialISO.SelectedItemName

        if temp is None:
            return ""

        return temp

    @default_cylindrical_gear_material_iso.setter
    @enforce_parameter_types
    def default_cylindrical_gear_material_iso(self: Self, value: "str"):
        self.wrapped.DefaultCylindricalGearMaterialISO.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def default_rough_toleranced_metal_measurement(
        self: Self,
    ) -> "_1088.TolerancedMetalMeasurements":
        """mastapy.gears.gear_designs.cylindrical.TolerancedMetalMeasurements"""
        temp = self.wrapped.DefaultRoughTolerancedMetalMeasurement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TolerancedMetalMeasurements",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1088",
            "TolerancedMetalMeasurements",
        )(value)

    @default_rough_toleranced_metal_measurement.setter
    @enforce_parameter_types
    def default_rough_toleranced_metal_measurement(
        self: Self, value: "_1088.TolerancedMetalMeasurements"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TolerancedMetalMeasurements",
        )
        self.wrapped.DefaultRoughTolerancedMetalMeasurement = value

    @property
    def extra_backlash_for_all_gears(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ExtraBacklashForAllGears

        if temp is None:
            return 0.0

        return temp

    @extra_backlash_for_all_gears.setter
    @enforce_parameter_types
    def extra_backlash_for_all_gears(self: Self, value: "float"):
        self.wrapped.ExtraBacklashForAllGears = (
            float(value) if value is not None else 0.0
        )

    @property
    def hunting_ratio_required(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HuntingRatioRequired

        if temp is None:
            return False

        return temp

    @hunting_ratio_required.setter
    @enforce_parameter_types
    def hunting_ratio_required(self: Self, value: "bool"):
        self.wrapped.HuntingRatioRequired = bool(value) if value is not None else False

    @property
    def limit_dynamic_factor_if_not_in_main_resonance_range(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LimitDynamicFactorIfNotInMainResonanceRange

        if temp is None:
            return False

        return temp

    @limit_dynamic_factor_if_not_in_main_resonance_range.setter
    @enforce_parameter_types
    def limit_dynamic_factor_if_not_in_main_resonance_range(self: Self, value: "bool"):
        self.wrapped.LimitDynamicFactorIfNotInMainResonanceRange = (
            bool(value) if value is not None else False
        )

    @property
    def limit_micro_geometry_factor_for_the_dynamic_load(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LimitMicroGeometryFactorForTheDynamicLoad

        if temp is None:
            return False

        return temp

    @limit_micro_geometry_factor_for_the_dynamic_load.setter
    @enforce_parameter_types
    def limit_micro_geometry_factor_for_the_dynamic_load(self: Self, value: "bool"):
        self.wrapped.LimitMicroGeometryFactorForTheDynamicLoad = (
            bool(value) if value is not None else False
        )

    @property
    def maximum_number_of_planets(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfPlanets

        if temp is None:
            return 0

        return temp

    @maximum_number_of_planets.setter
    @enforce_parameter_types
    def maximum_number_of_planets(self: Self, value: "int"):
        self.wrapped.MaximumNumberOfPlanets = int(value) if value is not None else 0

    @property
    def micro_geometry_model_in_system_deflection(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_MicroGeometryModel":
        """EnumWithSelectedValue[mastapy.gears.MicroGeometryModel]"""
        temp = self.wrapped.MicroGeometryModelInSystemDeflection

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_MicroGeometryModel.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @micro_geometry_model_in_system_deflection.setter
    @enforce_parameter_types
    def micro_geometry_model_in_system_deflection(
        self: Self, value: "_340.MicroGeometryModel"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_MicroGeometryModel.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MicroGeometryModelInSystemDeflection = value

    @property
    def minimum_factor_of_safety_for_tooth_fatigue_fracture(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumFactorOfSafetyForToothFatigueFracture

        if temp is None:
            return 0.0

        return temp

    @minimum_factor_of_safety_for_tooth_fatigue_fracture.setter
    @enforce_parameter_types
    def minimum_factor_of_safety_for_tooth_fatigue_fracture(self: Self, value: "float"):
        self.wrapped.MinimumFactorOfSafetyForToothFatigueFracture = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_power_for_gear_mesh_to_be_loaded(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumPowerForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return temp

    @minimum_power_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_power_for_gear_mesh_to_be_loaded(self: Self, value: "float"):
        self.wrapped.MinimumPowerForGearMeshToBeLoaded = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_torque_for_gear_mesh_to_be_loaded(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumTorqueForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return temp

    @minimum_torque_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_torque_for_gear_mesh_to_be_loaded(self: Self, value: "float"):
        self.wrapped.MinimumTorqueForGearMeshToBeLoaded = (
            float(value) if value is not None else 0.0
        )

    @property
    def misalignment_contact_pattern_enhancement(
        self: Self,
    ) -> "_481.MisalignmentContactPatternEnhancements":
        """mastapy.gears.rating.cylindrical.MisalignmentContactPatternEnhancements"""
        temp = self.wrapped.MisalignmentContactPatternEnhancement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.MisalignmentContactPatternEnhancements",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._481",
            "MisalignmentContactPatternEnhancements",
        )(value)

    @misalignment_contact_pattern_enhancement.setter
    @enforce_parameter_types
    def misalignment_contact_pattern_enhancement(
        self: Self, value: "_481.MisalignmentContactPatternEnhancements"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.MisalignmentContactPatternEnhancements",
        )
        self.wrapped.MisalignmentContactPatternEnhancement = value

    @property
    def planet_carrier_space_required(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PlanetCarrierSpaceRequired

        if temp is None:
            return 0.0

        return temp

    @planet_carrier_space_required.setter
    @enforce_parameter_types
    def planet_carrier_space_required(self: Self, value: "float"):
        self.wrapped.PlanetCarrierSpaceRequired = (
            float(value) if value is not None else 0.0
        )

    @property
    def relative_tolerance_for_convergence(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RelativeToleranceForConvergence

        if temp is None:
            return 0.0

        return temp

    @relative_tolerance_for_convergence.setter
    @enforce_parameter_types
    def relative_tolerance_for_convergence(self: Self, value: "float"):
        self.wrapped.RelativeToleranceForConvergence = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_bending(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForBending

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_bending.setter
    @enforce_parameter_types
    def required_safety_factor_for_bending(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_contact(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForContact

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_contact.setter
    @enforce_parameter_types
    def required_safety_factor_for_contact(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForContact = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_crack_initiation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForCrackInitiation

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_crack_initiation.setter
    @enforce_parameter_types
    def required_safety_factor_for_crack_initiation(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForCrackInitiation = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_micropitting(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForMicropitting

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_micropitting.setter
    @enforce_parameter_types
    def required_safety_factor_for_micropitting(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForMicropitting = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_scuffing(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForScuffing

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_scuffing.setter
    @enforce_parameter_types
    def required_safety_factor_for_scuffing(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForScuffing = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_static_bending(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForStaticBending

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_static_bending.setter
    @enforce_parameter_types
    def required_safety_factor_for_static_bending(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForStaticBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_static_contact(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForStaticContact

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_static_contact.setter
    @enforce_parameter_types
    def required_safety_factor_for_static_contact(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForStaticContact = (
            float(value) if value is not None else 0.0
        )

    @property
    def cylindrical_gear_design_constraint_settings(
        self: Self,
    ) -> "_1018.CylindricalGearDesignConstraints":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesignConstraints

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignConstraintSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def general_transmission_properties(
        self: Self,
    ) -> "_259.GeneralTransmissionProperties":
        """mastapy.materials.GeneralTransmissionProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeneralTransmissionProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def settings(self: Self) -> "_457.CylindricalGearDesignAndRatingSettingsItem":
        """mastapy.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Settings

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
    def cast_to(self: Self) -> "GearSetDesignGroup._Cast_GearSetDesignGroup":
        return self._Cast_GearSetDesignGroup(self)
