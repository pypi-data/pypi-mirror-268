"""CylindricalGearSetOptimisationWrapper"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_OPTIMISATION_WRAPPER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CylindricalGearSetOptimisationWrapper",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetOptimisationWrapper",)


Self = TypeVar("Self", bound="CylindricalGearSetOptimisationWrapper")


class CylindricalGearSetOptimisationWrapper(_0.APIBase):
    """CylindricalGearSetOptimisationWrapper

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_OPTIMISATION_WRAPPER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetOptimisationWrapper"
    )

    class _Cast_CylindricalGearSetOptimisationWrapper:
        """Special nested class for casting CylindricalGearSetOptimisationWrapper to subclasses."""

        def __init__(
            self: "CylindricalGearSetOptimisationWrapper._Cast_CylindricalGearSetOptimisationWrapper",
            parent: "CylindricalGearSetOptimisationWrapper",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_optimisation_wrapper(
            self: "CylindricalGearSetOptimisationWrapper._Cast_CylindricalGearSetOptimisationWrapper",
        ) -> "CylindricalGearSetOptimisationWrapper":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetOptimisationWrapper._Cast_CylindricalGearSetOptimisationWrapper",
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
        self: Self, instance_to_wrap: "CylindricalGearSetOptimisationWrapper.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def face_width_with_constant_axial_contact_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidthWithConstantAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @face_width_with_constant_axial_contact_ratio.setter
    @enforce_parameter_types
    def face_width_with_constant_axial_contact_ratio(self: Self, value: "float"):
        self.wrapped.FaceWidthWithConstantAxialContactRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    @enforce_parameter_types
    def helix_angle(self: Self, value: "float"):
        self.wrapped.HelixAngle = float(value) if value is not None else 0.0

    @property
    def helix_angle_fixed_transverse_profile(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngleFixedTransverseProfile

        if temp is None:
            return 0.0

        return temp

    @helix_angle_fixed_transverse_profile.setter
    @enforce_parameter_types
    def helix_angle_fixed_transverse_profile(self: Self, value: "float"):
        self.wrapped.HelixAngleFixedTransverseProfile = (
            float(value) if value is not None else 0.0
        )

    @property
    def normal_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @normal_module.setter
    @enforce_parameter_types
    def normal_module(self: Self, value: "float"):
        self.wrapped.NormalModule = float(value) if value is not None else 0.0

    @property
    def normal_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    @enforce_parameter_types
    def normal_pressure_angle(self: Self, value: "float"):
        self.wrapped.NormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def planet_diameter_with_adjusted_face_width_to_maintain_mass(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.PlanetDiameterWithAdjustedFaceWidthToMaintainMass

        if temp is None:
            return 0.0

        return temp

    @planet_diameter_with_adjusted_face_width_to_maintain_mass.setter
    @enforce_parameter_types
    def planet_diameter_with_adjusted_face_width_to_maintain_mass(
        self: Self, value: "float"
    ):
        self.wrapped.PlanetDiameterWithAdjustedFaceWidthToMaintainMass = (
            float(value) if value is not None else 0.0
        )

    @property
    def root_gear_profile_shift_coefficient(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RootGearProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @root_gear_profile_shift_coefficient.setter
    @enforce_parameter_types
    def root_gear_profile_shift_coefficient(self: Self, value: "float"):
        self.wrapped.RootGearProfileShiftCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def root_gear_profile_shift_coefficient_with_fixed_tip_and_root_diameters(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.RootGearProfileShiftCoefficientWithFixedTipAndRootDiameters

        if temp is None:
            return 0.0

        return temp

    @root_gear_profile_shift_coefficient_with_fixed_tip_and_root_diameters.setter
    @enforce_parameter_types
    def root_gear_profile_shift_coefficient_with_fixed_tip_and_root_diameters(
        self: Self, value: "float"
    ):
        self.wrapped.RootGearProfileShiftCoefficientWithFixedTipAndRootDiameters = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetOptimisationWrapper._Cast_CylindricalGearSetOptimisationWrapper":
        return self._Cast_CylindricalGearSetOptimisationWrapper(self)
