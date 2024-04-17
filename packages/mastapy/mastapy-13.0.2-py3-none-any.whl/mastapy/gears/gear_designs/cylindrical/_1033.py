"""CylindricalGearSetFlankDesign"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_FLANK_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearSetFlankDesign"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetFlankDesign",)


Self = TypeVar("Self", bound="CylindricalGearSetFlankDesign")


class CylindricalGearSetFlankDesign(_0.APIBase):
    """CylindricalGearSetFlankDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_FLANK_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetFlankDesign")

    class _Cast_CylindricalGearSetFlankDesign:
        """Special nested class for casting CylindricalGearSetFlankDesign to subclasses."""

        def __init__(
            self: "CylindricalGearSetFlankDesign._Cast_CylindricalGearSetFlankDesign",
            parent: "CylindricalGearSetFlankDesign",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_flank_design(
            self: "CylindricalGearSetFlankDesign._Cast_CylindricalGearSetFlankDesign",
        ) -> "CylindricalGearSetFlankDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetFlankDesign._Cast_CylindricalGearSetFlankDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetFlankDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BaseHelixAngle

        if temp is None:
            return 0.0

        return temp

    @base_helix_angle.setter
    @enforce_parameter_types
    def base_helix_angle(self: Self, value: "float"):
        self.wrapped.BaseHelixAngle = float(value) if value is not None else 0.0

    @property
    def flank_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankName

        if temp is None:
            return ""

        return temp

    @property
    def minimum_total_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumTotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_transverse_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_base_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_base_pitch_set_by_changing_normal_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalBasePitchSetByChangingNormalModule

        if temp is None:
            return 0.0

        return temp

    @normal_base_pitch_set_by_changing_normal_module.setter
    @enforce_parameter_types
    def normal_base_pitch_set_by_changing_normal_module(self: Self, value: "float"):
        self.wrapped.NormalBasePitchSetByChangingNormalModule = (
            float(value) if value is not None else 0.0
        )

    @property
    def normal_base_pitch_set_by_changing_normal_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalBasePitchSetByChangingNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_base_pitch_set_by_changing_normal_pressure_angle.setter
    @enforce_parameter_types
    def normal_base_pitch_set_by_changing_normal_pressure_angle(
        self: Self, value: "float"
    ):
        self.wrapped.NormalBasePitchSetByChangingNormalPressureAngle = (
            float(value) if value is not None else 0.0
        )

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
    def transverse_base_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle_normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransversePressureAngleNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetFlankDesign._Cast_CylindricalGearSetFlankDesign":
        return self._Cast_CylindricalGearSetFlankDesign(self)
