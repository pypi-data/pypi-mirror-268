"""BasicConicalGearMachineSettingsGenerated"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _824
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASIC_CONICAL_GEAR_MACHINE_SETTINGS_GENERATED = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.BasicMachineSettings",
    "BasicConicalGearMachineSettingsGenerated",
)


__docformat__ = "restructuredtext en"
__all__ = ("BasicConicalGearMachineSettingsGenerated",)


Self = TypeVar("Self", bound="BasicConicalGearMachineSettingsGenerated")


class BasicConicalGearMachineSettingsGenerated(_824.BasicConicalGearMachineSettings):
    """BasicConicalGearMachineSettingsGenerated

    This is a mastapy class.
    """

    TYPE = _BASIC_CONICAL_GEAR_MACHINE_SETTINGS_GENERATED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BasicConicalGearMachineSettingsGenerated"
    )

    class _Cast_BasicConicalGearMachineSettingsGenerated:
        """Special nested class for casting BasicConicalGearMachineSettingsGenerated to subclasses."""

        def __init__(
            self: "BasicConicalGearMachineSettingsGenerated._Cast_BasicConicalGearMachineSettingsGenerated",
            parent: "BasicConicalGearMachineSettingsGenerated",
        ):
            self._parent = parent

        @property
        def basic_conical_gear_machine_settings(
            self: "BasicConicalGearMachineSettingsGenerated._Cast_BasicConicalGearMachineSettingsGenerated",
        ) -> "_824.BasicConicalGearMachineSettings":
            return self._parent._cast(_824.BasicConicalGearMachineSettings)

        @property
        def basic_conical_gear_machine_settings_generated(
            self: "BasicConicalGearMachineSettingsGenerated._Cast_BasicConicalGearMachineSettingsGenerated",
        ) -> "BasicConicalGearMachineSettingsGenerated":
            return self._parent

        def __getattr__(
            self: "BasicConicalGearMachineSettingsGenerated._Cast_BasicConicalGearMachineSettingsGenerated",
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
        self: Self, instance_to_wrap: "BasicConicalGearMachineSettingsGenerated.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_cradle_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BasicCradleAngle

        if temp is None:
            return 0.0

        return temp

    @basic_cradle_angle.setter
    @enforce_parameter_types
    def basic_cradle_angle(self: Self, value: "float"):
        self.wrapped.BasicCradleAngle = float(value) if value is not None else 0.0

    @property
    def blank_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BlankOffset

        if temp is None:
            return 0.0

        return temp

    @blank_offset.setter
    @enforce_parameter_types
    def blank_offset(self: Self, value: "float"):
        self.wrapped.BlankOffset = float(value) if value is not None else 0.0

    @property
    def modified_roll_coefficient_c(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModifiedRollCoefficientC

        if temp is None:
            return 0.0

        return temp

    @modified_roll_coefficient_c.setter
    @enforce_parameter_types
    def modified_roll_coefficient_c(self: Self, value: "float"):
        self.wrapped.ModifiedRollCoefficientC = (
            float(value) if value is not None else 0.0
        )

    @property
    def modified_roll_coefficient_d(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModifiedRollCoefficientD

        if temp is None:
            return 0.0

        return temp

    @modified_roll_coefficient_d.setter
    @enforce_parameter_types
    def modified_roll_coefficient_d(self: Self, value: "float"):
        self.wrapped.ModifiedRollCoefficientD = (
            float(value) if value is not None else 0.0
        )

    @property
    def radial_setting(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialSetting

        if temp is None:
            return 0.0

        return temp

    @radial_setting.setter
    @enforce_parameter_types
    def radial_setting(self: Self, value: "float"):
        self.wrapped.RadialSetting = float(value) if value is not None else 0.0

    @property
    def ratio_of_roll(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RatioOfRoll

        if temp is None:
            return 0.0

        return temp

    @ratio_of_roll.setter
    @enforce_parameter_types
    def ratio_of_roll(self: Self, value: "float"):
        self.wrapped.RatioOfRoll = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "BasicConicalGearMachineSettingsGenerated._Cast_BasicConicalGearMachineSettingsGenerated":
        return self._Cast_BasicConicalGearMachineSettingsGenerated(self)
