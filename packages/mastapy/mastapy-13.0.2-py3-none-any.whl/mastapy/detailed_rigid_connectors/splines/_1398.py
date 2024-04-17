"""DetailedSplineJointSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_SPLINE_JOINT_SETTINGS = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "DetailedSplineJointSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("DetailedSplineJointSettings",)


Self = TypeVar("Self", bound="DetailedSplineJointSettings")


class DetailedSplineJointSettings(_0.APIBase):
    """DetailedSplineJointSettings

    This is a mastapy class.
    """

    TYPE = _DETAILED_SPLINE_JOINT_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DetailedSplineJointSettings")

    class _Cast_DetailedSplineJointSettings:
        """Special nested class for casting DetailedSplineJointSettings to subclasses."""

        def __init__(
            self: "DetailedSplineJointSettings._Cast_DetailedSplineJointSettings",
            parent: "DetailedSplineJointSettings",
        ):
            self._parent = parent

        @property
        def detailed_spline_joint_settings(
            self: "DetailedSplineJointSettings._Cast_DetailedSplineJointSettings",
        ) -> "DetailedSplineJointSettings":
            return self._parent

        def __getattr__(
            self: "DetailedSplineJointSettings._Cast_DetailedSplineJointSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DetailedSplineJointSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def required_safety_factor_for_compressive_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_compressive_stress.setter
    @enforce_parameter_types
    def required_safety_factor_for_compressive_stress(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForCompressiveStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_ring_bursting(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForRingBursting

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_ring_bursting.setter
    @enforce_parameter_types
    def required_safety_factor_for_ring_bursting(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForRingBursting = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_root_bending_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_root_bending_stress.setter
    @enforce_parameter_types
    def required_safety_factor_for_root_bending_stress(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForRootBendingStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_tooth_shearing_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForToothShearingStress

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_tooth_shearing_stress.setter
    @enforce_parameter_types
    def required_safety_factor_for_tooth_shearing_stress(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForToothShearingStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_torsional_failure(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForTorsionalFailure

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_torsional_failure.setter
    @enforce_parameter_types
    def required_safety_factor_for_torsional_failure(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForTorsionalFailure = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_safety_factor_for_wear_and_fretting(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredSafetyFactorForWearAndFretting

        if temp is None:
            return 0.0

        return temp

    @required_safety_factor_for_wear_and_fretting.setter
    @enforce_parameter_types
    def required_safety_factor_for_wear_and_fretting(self: Self, value: "float"):
        self.wrapped.RequiredSafetyFactorForWearAndFretting = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "DetailedSplineJointSettings._Cast_DetailedSplineJointSettings":
        return self._Cast_DetailedSplineJointSettings(self)
