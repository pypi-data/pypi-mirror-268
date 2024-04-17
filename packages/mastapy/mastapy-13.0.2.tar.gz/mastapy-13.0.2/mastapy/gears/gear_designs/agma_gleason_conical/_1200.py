"""AGMAGleasonConicalGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.conical import _1175, _1161
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical",
    "AGMAGleasonConicalGearMeshDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.iso_10300 import _424, _437, _439, _440
    from mastapy.gears.gear_designs.zerol_bevel import _957
    from mastapy.gears.gear_designs.straight_bevel import _966
    from mastapy.gears.gear_designs.straight_bevel_diff import _970
    from mastapy.gears.gear_designs.spiral_bevel import _974
    from mastapy.gears.gear_designs.hypoid import _990
    from mastapy.gears.gear_designs.bevel import _1187
    from mastapy.gears.gear_designs import _953, _952


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshDesign",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshDesign")


class AGMAGleasonConicalGearMeshDesign(_1161.ConicalGearMeshDesign):
    """AGMAGleasonConicalGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshDesign")

    class _Cast_AGMAGleasonConicalGearMeshDesign:
        """Special nested class for casting AGMAGleasonConicalGearMeshDesign to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
            parent: "AGMAGleasonConicalGearMeshDesign",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_design(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "_1161.ConicalGearMeshDesign":
            return self._parent._cast(_1161.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            from mastapy.gears.gear_designs import _953

            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_gear_mesh_design(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "_957.ZerolBevelGearMeshDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _957

            return self._parent._cast(_957.ZerolBevelGearMeshDesign)

        @property
        def straight_bevel_gear_mesh_design(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "_966.StraightBevelGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel import _966

            return self._parent._cast(_966.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "_970.StraightBevelDiffGearMeshDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _970

            return self._parent._cast(_970.StraightBevelDiffGearMeshDesign)

        @property
        def spiral_bevel_gear_mesh_design(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "_974.SpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _974

            return self._parent._cast(_974.SpiralBevelGearMeshDesign)

        @property
        def hypoid_gear_mesh_design(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "_990.HypoidGearMeshDesign":
            from mastapy.gears.gear_designs.hypoid import _990

            return self._parent._cast(_990.HypoidGearMeshDesign)

        @property
        def bevel_gear_mesh_design(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "_1187.BevelGearMeshDesign":
            from mastapy.gears.gear_designs.bevel import _1187

            return self._parent._cast(_1187.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
        ) -> "AGMAGleasonConicalGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowned(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Crowned

        if temp is None:
            return False

        return temp

    @crowned.setter
    @enforce_parameter_types
    def crowned(self: Self, value: "bool"):
        self.wrapped.Crowned = bool(value) if value is not None else False

    @property
    def crowning_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CrowningFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @crowning_factor.setter
    @enforce_parameter_types
    def crowning_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CrowningFactor = value

    @property
    def dynamic_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DynamicFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dynamic_factor.setter
    @enforce_parameter_types
    def dynamic_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DynamicFactor = value

    @property
    def hardness_ratio_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HardnessRatioFactor

        if temp is None:
            return 0.0

        return temp

    @hardness_ratio_factor.setter
    @enforce_parameter_types
    def hardness_ratio_factor(self: Self, value: "float"):
        self.wrapped.HardnessRatioFactor = float(value) if value is not None else 0.0

    @property
    def iso10300_gear_set_finishing_methods(
        self: Self,
    ) -> "_424.Iso10300FinishingMethods":
        """mastapy.gears.rating.isoIso10300FinishingMethods"""
        temp = self.wrapped.ISO10300GearSetFinishingMethods

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.Iso10300FinishingMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._424", "Iso10300FinishingMethods"
        )(value)

    @iso10300_gear_set_finishing_methods.setter
    @enforce_parameter_types
    def iso10300_gear_set_finishing_methods(
        self: Self, value: "_424.Iso10300FinishingMethods"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.Iso10300FinishingMethods"
        )
        self.wrapped.ISO10300GearSetFinishingMethods = value

    @property
    def load_distribution_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @load_distribution_factor.setter
    @enforce_parameter_types
    def load_distribution_factor(self: Self, value: "float"):
        self.wrapped.LoadDistributionFactor = float(value) if value is not None else 0.0

    @property
    def load_distribution_factor_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LoadDistributionFactorMethods":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.conical.LoadDistributionFactorMethods]"""
        temp = self.wrapped.LoadDistributionFactorMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LoadDistributionFactorMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @load_distribution_factor_method.setter
    @enforce_parameter_types
    def load_distribution_factor_method(
        self: Self, value: "_1175.LoadDistributionFactorMethods"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LoadDistributionFactorMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LoadDistributionFactorMethod = value

    @property
    def mounting_conditions_of_pinion_and_wheel(
        self: Self,
    ) -> "_437.MountingConditionsOfPinionAndWheel":
        """mastapy.gears.rating.isoMountingConditionsOfPinionAndWheel"""
        temp = self.wrapped.MountingConditionsOfPinionAndWheel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Iso10300.MountingConditionsOfPinionAndWheel",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._437", "MountingConditionsOfPinionAndWheel"
        )(value)

    @mounting_conditions_of_pinion_and_wheel.setter
    @enforce_parameter_types
    def mounting_conditions_of_pinion_and_wheel(
        self: Self, value: "_437.MountingConditionsOfPinionAndWheel"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Iso10300.MountingConditionsOfPinionAndWheel",
        )
        self.wrapped.MountingConditionsOfPinionAndWheel = value

    @property
    def net_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NetFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_face_width_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionFaceWidthOffset

        if temp is None:
            return 0.0

        return temp

    @pinion_face_width_offset.setter
    @enforce_parameter_types
    def pinion_face_width_offset(self: Self, value: "float"):
        self.wrapped.PinionFaceWidthOffset = float(value) if value is not None else 0.0

    @property
    def profile_crowning_setting(self: Self) -> "_439.ProfileCrowningSetting":
        """mastapy.gears.rating.isoProfileCrowningSetting"""
        temp = self.wrapped.ProfileCrowningSetting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.ProfileCrowningSetting"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._439", "ProfileCrowningSetting"
        )(value)

    @profile_crowning_setting.setter
    @enforce_parameter_types
    def profile_crowning_setting(self: Self, value: "_439.ProfileCrowningSetting"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.ProfileCrowningSetting"
        )
        self.wrapped.ProfileCrowningSetting = value

    @property
    def size_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SizeFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @size_factor_bending.setter
    @enforce_parameter_types
    def size_factor_bending(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SizeFactorBending = value

    @property
    def size_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SizeFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @size_factor_contact.setter
    @enforce_parameter_types
    def size_factor_contact(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SizeFactorContact = value

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
    def temperature_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TemperatureFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @temperature_factor.setter
    @enforce_parameter_types
    def temperature_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TemperatureFactor = value

    @property
    def tooth_lengthwise_curvature_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToothLengthwiseCurvatureFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tooth_lengthwise_curvature_factor.setter
    @enforce_parameter_types
    def tooth_lengthwise_curvature_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToothLengthwiseCurvatureFactor = value

    @property
    def verification_of_contact_pattern(
        self: Self,
    ) -> "_440.VerificationOfContactPattern":
        """mastapy.gears.rating.isoVerificationOfContactPattern"""
        temp = self.wrapped.VerificationOfContactPattern

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.VerificationOfContactPattern"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._440", "VerificationOfContactPattern"
        )(value)

    @verification_of_contact_pattern.setter
    @enforce_parameter_types
    def verification_of_contact_pattern(
        self: Self, value: "_440.VerificationOfContactPattern"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.VerificationOfContactPattern"
        )
        self.wrapped.VerificationOfContactPattern = value

    @property
    def wheel_effective_face_width_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelEffectiveFaceWidthFactor

        if temp is None:
            return 0.0

        return temp

    @wheel_effective_face_width_factor.setter
    @enforce_parameter_types
    def wheel_effective_face_width_factor(self: Self, value: "float"):
        self.wrapped.WheelEffectiveFaceWidthFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshDesign._Cast_AGMAGleasonConicalGearMeshDesign":
        return self._Cast_AGMAGleasonConicalGearMeshDesign(self)
