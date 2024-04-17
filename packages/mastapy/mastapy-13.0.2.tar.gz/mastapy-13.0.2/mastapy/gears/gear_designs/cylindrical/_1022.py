"""CylindricalGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears import _338
from mastapy.gears.gear_designs import _953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears import _321
    from mastapy.gears.gear_designs.cylindrical import (
        _1031,
        _1093,
        _1003,
        _1032,
        _1023,
        _1016,
        _1042,
    )
    from mastapy.math_utility import _1496
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshDesign",)


Self = TypeVar("Self", bound="CylindricalGearMeshDesign")


class CylindricalGearMeshDesign(_953.GearMeshDesign):
    """CylindricalGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshDesign")

    class _Cast_CylindricalGearMeshDesign:
        """Special nested class for casting CylindricalGearMeshDesign to subclasses."""

        def __init__(
            self: "CylindricalGearMeshDesign._Cast_CylindricalGearMeshDesign",
            parent: "CylindricalGearMeshDesign",
        ):
            self._parent = parent

        @property
        def gear_mesh_design(
            self: "CylindricalGearMeshDesign._Cast_CylindricalGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "CylindricalGearMeshDesign._Cast_CylindricalGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def cylindrical_gear_mesh_design(
            self: "CylindricalGearMeshDesign._Cast_CylindricalGearMeshDesign",
        ) -> "CylindricalGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshDesign._Cast_CylindricalGearMeshDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def bearing_span(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BearingSpan

        if temp is None:
            return 0.0

        return temp

    @bearing_span.setter
    @enforce_parameter_types
    def bearing_span(self: Self, value: "float"):
        self.wrapped.BearingSpan = float(value) if value is not None else 0.0

    @property
    def centre_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @centre_distance.setter
    @enforce_parameter_types
    def centre_distance(self: Self, value: "float"):
        self.wrapped.CentreDistance = float(value) if value is not None else 0.0

    @property
    def centre_distance_calculating_gear_teeth_numbers(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreDistanceCalculatingGearTeethNumbers

        if temp is None:
            return 0.0

        return temp

    @centre_distance_calculating_gear_teeth_numbers.setter
    @enforce_parameter_types
    def centre_distance_calculating_gear_teeth_numbers(self: Self, value: "float"):
        self.wrapped.CentreDistanceCalculatingGearTeethNumbers = (
            float(value) if value is not None else 0.0
        )

    @property
    def centre_distance_change_method(self: Self) -> "_321.CentreDistanceChangeMethod":
        """mastapy.gears.CentreDistanceChangeMethod"""
        temp = self.wrapped.CentreDistanceChangeMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.CentreDistanceChangeMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._321", "CentreDistanceChangeMethod"
        )(value)

    @centre_distance_change_method.setter
    @enforce_parameter_types
    def centre_distance_change_method(
        self: Self, value: "_321.CentreDistanceChangeMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.CentreDistanceChangeMethod"
        )
        self.wrapped.CentreDistanceChangeMethod = value

    @property
    def centre_distance_at_tight_mesh_maximum_metal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreDistanceAtTightMeshMaximumMetal

        if temp is None:
            return 0.0

        return temp

    @property
    def centre_distance_at_tight_mesh_minimum_metal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreDistanceAtTightMeshMinimumMetal

        if temp is None:
            return 0.0

        return temp

    @property
    def centre_distance_with_normal_module_adjustment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreDistanceWithNormalModuleAdjustment

        if temp is None:
            return 0.0

        return temp

    @centre_distance_with_normal_module_adjustment.setter
    @enforce_parameter_types
    def centre_distance_with_normal_module_adjustment(self: Self, value: "float"):
        self.wrapped.CentreDistanceWithNormalModuleAdjustment = (
            float(value) if value is not None else 0.0
        )

    @property
    def coefficient_of_friction(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @coefficient_of_friction.setter
    @enforce_parameter_types
    def coefficient_of_friction(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CoefficientOfFriction = value

    @property
    def effective_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_factor_for_extended_tip_contact(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FaceWidthFactorForExtendedTipContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @face_width_factor_for_extended_tip_contact.setter
    @enforce_parameter_types
    def face_width_factor_for_extended_tip_contact(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FaceWidthFactorForExtendedTipContact = value

    @property
    def filter_cutoff_wavelength(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FilterCutoffWavelength

        if temp is None:
            return 0.0

        return temp

    @filter_cutoff_wavelength.setter
    @enforce_parameter_types
    def filter_cutoff_wavelength(self: Self, value: "float"):
        self.wrapped.FilterCutoffWavelength = float(value) if value is not None else 0.0

    @property
    def gear_mesh_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def heat_dissipating_surface_of_housing(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HeatDissipatingSurfaceOfHousing

        if temp is None:
            return 0.0

        return temp

    @heat_dissipating_surface_of_housing.setter
    @enforce_parameter_types
    def heat_dissipating_surface_of_housing(self: Self, value: "float"):
        self.wrapped.HeatDissipatingSurfaceOfHousing = (
            float(value) if value is not None else 0.0
        )

    @property
    def heat_transfer_resistance_of_housing(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.HeatTransferResistanceOfHousing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @heat_transfer_resistance_of_housing.setter
    @enforce_parameter_types
    def heat_transfer_resistance_of_housing(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.HeatTransferResistanceOfHousing = value

    @property
    def is_asymmetric(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsAsymmetric

        if temp is None:
            return False

        return temp

    @property
    def lubrication_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LubricationMethods":
        """EnumWithSelectedValue[mastapy.gears.LubricationMethods]"""
        temp = self.wrapped.LubricationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LubricationMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @lubrication_method.setter
    @enforce_parameter_types
    def lubrication_method(self: Self, value: "_338.LubricationMethods"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LubricationMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricationMethod = value

    @property
    def parameter_for_calculating_tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterForCalculatingToothTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_of_openings_in_the_housing_surface(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PercentageOfOpeningsInTheHousingSurface

        if temp is None:
            return 0.0

        return temp

    @percentage_of_openings_in_the_housing_surface.setter
    @enforce_parameter_types
    def percentage_of_openings_in_the_housing_surface(self: Self, value: "float"):
        self.wrapped.PercentageOfOpeningsInTheHousingSurface = (
            float(value) if value is not None else 0.0
        )

    @property
    def pinion_offset_from_bearing(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionOffsetFromBearing

        if temp is None:
            return 0.0

        return temp

    @pinion_offset_from_bearing.setter
    @enforce_parameter_types
    def pinion_offset_from_bearing(self: Self, value: "float"):
        self.wrapped.PinionOffsetFromBearing = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_modification(self: Self) -> "_1031.CylindricalGearProfileModifications":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileModifications"""
        temp = self.wrapped.ProfileModification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileModifications",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1031",
            "CylindricalGearProfileModifications",
        )(value)

    @profile_modification.setter
    @enforce_parameter_types
    def profile_modification(
        self: Self, value: "_1031.CylindricalGearProfileModifications"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileModifications",
        )
        self.wrapped.ProfileModification = value

    @property
    def ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Ratio

        if temp is None:
            return 0.0

        return temp

    @ratio.setter
    @enforce_parameter_types
    def ratio(self: Self, value: "float"):
        self.wrapped.Ratio = float(value) if value is not None else 0.0

    @property
    def reference_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_tooth_engagement_time(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RelativeToothEngagementTime

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @relative_tooth_engagement_time.setter
    @enforce_parameter_types
    def relative_tooth_engagement_time(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RelativeToothEngagementTime = value

    @property
    def sum_of_profile_shift_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_condition_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SurfaceConditionFactor

        if temp is None:
            return 0.0

        return temp

    @surface_condition_factor.setter
    @enforce_parameter_types
    def surface_condition_factor(self: Self, value: "float"):
        self.wrapped.SurfaceConditionFactor = float(value) if value is not None else 0.0

    @property
    def type_of_mechanism_housing(self: Self) -> "_1093.TypeOfMechanismHousing":
        """mastapy.gears.gear_designs.cylindrical.TypeOfMechanismHousing"""
        temp = self.wrapped.TypeOfMechanismHousing

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TypeOfMechanismHousing"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1093", "TypeOfMechanismHousing"
        )(value)

    @type_of_mechanism_housing.setter
    @enforce_parameter_types
    def type_of_mechanism_housing(self: Self, value: "_1093.TypeOfMechanismHousing"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TypeOfMechanismHousing"
        )
        self.wrapped.TypeOfMechanismHousing = value

    @property
    def user_specified_coefficient_of_friction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedCoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @user_specified_coefficient_of_friction.setter
    @enforce_parameter_types
    def user_specified_coefficient_of_friction(self: Self, value: "float"):
        self.wrapped.UserSpecifiedCoefficientOfFriction = (
            float(value) if value is not None else 0.0
        )

    @property
    def valid_normal_module_range(self: Self) -> "_1496.Range":
        """mastapy.math_utility.Range

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ValidNormalModuleRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wear_coefficient_for_a_driven_pinion(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WearCoefficientForADrivenPinion

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @wear_coefficient_for_a_driven_pinion.setter
    @enforce_parameter_types
    def wear_coefficient_for_a_driven_pinion(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WearCoefficientForADrivenPinion = value

    @property
    def wear_coefficient_for_a_driving_pinion(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WearCoefficientForADrivingPinion

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @wear_coefficient_for_a_driving_pinion.setter
    @enforce_parameter_types
    def wear_coefficient_for_a_driving_pinion(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WearCoefficientForADrivingPinion = value

    @property
    def working_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def working_helix_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingHelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def backlash_specification(self: Self) -> "_1003.BacklashSpecification":
        """mastapy.gears.gear_designs.cylindrical.BacklashSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BacklashSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set(self: Self) -> "_1032.CylindricalGearSetDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank(self: Self) -> "_1023.CylindricalGearMeshFlankDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshFlankDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_1023.CylindricalGearMeshFlankDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshFlankDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears(self: Self) -> "List[_1016.CylindricalGearDesign]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshed_gear(self: Self) -> "List[_1042.CylindricalMeshedGear]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalMeshedGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshedGear

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flanks(self: Self) -> "List[_1023.CylindricalGearMeshFlankDesign]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshFlankDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def both_flanks(self: Self) -> "_1023.CylindricalGearMeshFlankDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshFlankDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BothFlanks

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_a(self: Self) -> "_1016.CylindricalGearDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_1016.CylindricalGearDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def center_distance_for(
        self: Self,
        helix_angle: "float",
        pressure_angle: "float",
        sum_of_adden_mod: "float",
        sum_of_number_of_teeth: "float",
        normal_module: "float",
    ) -> "float":
        """float

        Args:
            helix_angle (float)
            pressure_angle (float)
            sum_of_adden_mod (float)
            sum_of_number_of_teeth (float)
            normal_module (float)
        """
        helix_angle = float(helix_angle)
        pressure_angle = float(pressure_angle)
        sum_of_adden_mod = float(sum_of_adden_mod)
        sum_of_number_of_teeth = float(sum_of_number_of_teeth)
        normal_module = float(normal_module)
        method_result = self.wrapped.CenterDistanceFor(
            helix_angle if helix_angle else 0.0,
            pressure_angle if pressure_angle else 0.0,
            sum_of_adden_mod if sum_of_adden_mod else 0.0,
            sum_of_number_of_teeth if sum_of_number_of_teeth else 0.0,
            normal_module if normal_module else 0.0,
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshDesign._Cast_CylindricalGearMeshDesign":
        return self._Cast_CylindricalGearMeshDesign(self)
