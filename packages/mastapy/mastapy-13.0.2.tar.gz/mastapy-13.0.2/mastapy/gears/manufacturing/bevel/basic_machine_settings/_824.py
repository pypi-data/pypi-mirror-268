"""BasicConicalGearMachineSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASIC_CONICAL_GEAR_MACHINE_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.BasicMachineSettings",
    "BasicConicalGearMachineSettings",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel.basic_machine_settings import _825, _826


__docformat__ = "restructuredtext en"
__all__ = ("BasicConicalGearMachineSettings",)


Self = TypeVar("Self", bound="BasicConicalGearMachineSettings")


class BasicConicalGearMachineSettings(_0.APIBase):
    """BasicConicalGearMachineSettings

    This is a mastapy class.
    """

    TYPE = _BASIC_CONICAL_GEAR_MACHINE_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BasicConicalGearMachineSettings")

    class _Cast_BasicConicalGearMachineSettings:
        """Special nested class for casting BasicConicalGearMachineSettings to subclasses."""

        def __init__(
            self: "BasicConicalGearMachineSettings._Cast_BasicConicalGearMachineSettings",
            parent: "BasicConicalGearMachineSettings",
        ):
            self._parent = parent

        @property
        def basic_conical_gear_machine_settings_formate(
            self: "BasicConicalGearMachineSettings._Cast_BasicConicalGearMachineSettings",
        ) -> "_825.BasicConicalGearMachineSettingsFormate":
            from mastapy.gears.manufacturing.bevel.basic_machine_settings import _825

            return self._parent._cast(_825.BasicConicalGearMachineSettingsFormate)

        @property
        def basic_conical_gear_machine_settings_generated(
            self: "BasicConicalGearMachineSettings._Cast_BasicConicalGearMachineSettings",
        ) -> "_826.BasicConicalGearMachineSettingsGenerated":
            from mastapy.gears.manufacturing.bevel.basic_machine_settings import _826

            return self._parent._cast(_826.BasicConicalGearMachineSettingsGenerated)

        @property
        def basic_conical_gear_machine_settings(
            self: "BasicConicalGearMachineSettings._Cast_BasicConicalGearMachineSettings",
        ) -> "BasicConicalGearMachineSettings":
            return self._parent

        def __getattr__(
            self: "BasicConicalGearMachineSettings._Cast_BasicConicalGearMachineSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BasicConicalGearMachineSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def machine_centre_to_back(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MachineCentreToBack

        if temp is None:
            return 0.0

        return temp

    @machine_centre_to_back.setter
    @enforce_parameter_types
    def machine_centre_to_back(self: Self, value: "float"):
        self.wrapped.MachineCentreToBack = float(value) if value is not None else 0.0

    @property
    def machine_root_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MachineRootAngle

        if temp is None:
            return 0.0

        return temp

    @machine_root_angle.setter
    @enforce_parameter_types
    def machine_root_angle(self: Self, value: "float"):
        self.wrapped.MachineRootAngle = float(value) if value is not None else 0.0

    @property
    def sliding_base(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidingBase

        if temp is None:
            return 0.0

        return temp

    @sliding_base.setter
    @enforce_parameter_types
    def sliding_base(self: Self, value: "float"):
        self.wrapped.SlidingBase = float(value) if value is not None else 0.0

    @property
    def swivel_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SwivelAngle

        if temp is None:
            return 0.0

        return temp

    @swivel_angle.setter
    @enforce_parameter_types
    def swivel_angle(self: Self, value: "float"):
        self.wrapped.SwivelAngle = float(value) if value is not None else 0.0

    @property
    def tilt_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltAngle

        if temp is None:
            return 0.0

        return temp

    @tilt_angle.setter
    @enforce_parameter_types
    def tilt_angle(self: Self, value: "float"):
        self.wrapped.TiltAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "BasicConicalGearMachineSettings._Cast_BasicConicalGearMachineSettings":
        return self._Cast_BasicConicalGearMachineSettings(self)
