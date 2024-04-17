"""BasicConicalGearMachineSettingsFormate"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _824
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASIC_CONICAL_GEAR_MACHINE_SETTINGS_FORMATE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.BasicMachineSettings",
    "BasicConicalGearMachineSettingsFormate",
)


__docformat__ = "restructuredtext en"
__all__ = ("BasicConicalGearMachineSettingsFormate",)


Self = TypeVar("Self", bound="BasicConicalGearMachineSettingsFormate")


class BasicConicalGearMachineSettingsFormate(_824.BasicConicalGearMachineSettings):
    """BasicConicalGearMachineSettingsFormate

    This is a mastapy class.
    """

    TYPE = _BASIC_CONICAL_GEAR_MACHINE_SETTINGS_FORMATE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BasicConicalGearMachineSettingsFormate"
    )

    class _Cast_BasicConicalGearMachineSettingsFormate:
        """Special nested class for casting BasicConicalGearMachineSettingsFormate to subclasses."""

        def __init__(
            self: "BasicConicalGearMachineSettingsFormate._Cast_BasicConicalGearMachineSettingsFormate",
            parent: "BasicConicalGearMachineSettingsFormate",
        ):
            self._parent = parent

        @property
        def basic_conical_gear_machine_settings(
            self: "BasicConicalGearMachineSettingsFormate._Cast_BasicConicalGearMachineSettingsFormate",
        ) -> "_824.BasicConicalGearMachineSettings":
            return self._parent._cast(_824.BasicConicalGearMachineSettings)

        @property
        def basic_conical_gear_machine_settings_formate(
            self: "BasicConicalGearMachineSettingsFormate._Cast_BasicConicalGearMachineSettingsFormate",
        ) -> "BasicConicalGearMachineSettingsFormate":
            return self._parent

        def __getattr__(
            self: "BasicConicalGearMachineSettingsFormate._Cast_BasicConicalGearMachineSettingsFormate",
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
        self: Self, instance_to_wrap: "BasicConicalGearMachineSettingsFormate.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def horizontal_setting(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HorizontalSetting

        if temp is None:
            return 0.0

        return temp

    @horizontal_setting.setter
    @enforce_parameter_types
    def horizontal_setting(self: Self, value: "float"):
        self.wrapped.HorizontalSetting = float(value) if value is not None else 0.0

    @property
    def vertical_setting(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VerticalSetting

        if temp is None:
            return 0.0

        return temp

    @vertical_setting.setter
    @enforce_parameter_types
    def vertical_setting(self: Self, value: "float"):
        self.wrapped.VerticalSetting = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "BasicConicalGearMachineSettingsFormate._Cast_BasicConicalGearMachineSettingsFormate":
        return self._Cast_BasicConicalGearMachineSettingsFormate(self)
