"""CradleStyleConicalMachineSettingsGenerated"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CRADLE_STYLE_CONICAL_MACHINE_SETTINGS_GENERATED = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.BasicMachineSettings",
    "CradleStyleConicalMachineSettingsGenerated",
)


__docformat__ = "restructuredtext en"
__all__ = ("CradleStyleConicalMachineSettingsGenerated",)


Self = TypeVar("Self", bound="CradleStyleConicalMachineSettingsGenerated")


class CradleStyleConicalMachineSettingsGenerated(_0.APIBase):
    """CradleStyleConicalMachineSettingsGenerated

    This is a mastapy class.
    """

    TYPE = _CRADLE_STYLE_CONICAL_MACHINE_SETTINGS_GENERATED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CradleStyleConicalMachineSettingsGenerated"
    )

    class _Cast_CradleStyleConicalMachineSettingsGenerated:
        """Special nested class for casting CradleStyleConicalMachineSettingsGenerated to subclasses."""

        def __init__(
            self: "CradleStyleConicalMachineSettingsGenerated._Cast_CradleStyleConicalMachineSettingsGenerated",
            parent: "CradleStyleConicalMachineSettingsGenerated",
        ):
            self._parent = parent

        @property
        def cradle_style_conical_machine_settings_generated(
            self: "CradleStyleConicalMachineSettingsGenerated._Cast_CradleStyleConicalMachineSettingsGenerated",
        ) -> "CradleStyleConicalMachineSettingsGenerated":
            return self._parent

        def __getattr__(
            self: "CradleStyleConicalMachineSettingsGenerated._Cast_CradleStyleConicalMachineSettingsGenerated",
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
        self: Self, instance_to_wrap: "CradleStyleConicalMachineSettingsGenerated.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cradle_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CradleAngle

        if temp is None:
            return 0.0

        return temp

    @cradle_angle.setter
    @enforce_parameter_types
    def cradle_angle(self: Self, value: "float"):
        self.wrapped.CradleAngle = float(value) if value is not None else 0.0

    @property
    def cutter_spindle_rotation_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CutterSpindleRotationAngle

        if temp is None:
            return 0.0

        return temp

    @cutter_spindle_rotation_angle.setter
    @enforce_parameter_types
    def cutter_spindle_rotation_angle(self: Self, value: "float"):
        self.wrapped.CutterSpindleRotationAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def decimal_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DecimalRatio

        if temp is None:
            return 0.0

        return temp

    @decimal_ratio.setter
    @enforce_parameter_types
    def decimal_ratio(self: Self, value: "float"):
        self.wrapped.DecimalRatio = float(value) if value is not None else 0.0

    @property
    def eccentric_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EccentricAngle

        if temp is None:
            return 0.0

        return temp

    @eccentric_angle.setter
    @enforce_parameter_types
    def eccentric_angle(self: Self, value: "float"):
        self.wrapped.EccentricAngle = float(value) if value is not None else 0.0

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
    def cast_to(
        self: Self,
    ) -> "CradleStyleConicalMachineSettingsGenerated._Cast_CradleStyleConicalMachineSettingsGenerated":
        return self._Cast_CradleStyleConicalMachineSettingsGenerated(self)
