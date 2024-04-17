"""PinionFinishMachineSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears import _323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_FINISH_MACHINE_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "PinionFinishMachineSettings"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1177
    from mastapy.gears.manufacturing.bevel import _804, _805, _807, _810, _811, _812


__docformat__ = "restructuredtext en"
__all__ = ("PinionFinishMachineSettings",)


Self = TypeVar("Self", bound="PinionFinishMachineSettings")


class PinionFinishMachineSettings(_323.ConicalGearToothSurface):
    """PinionFinishMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_FINISH_MACHINE_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PinionFinishMachineSettings")

    class _Cast_PinionFinishMachineSettings:
        """Special nested class for casting PinionFinishMachineSettings to subclasses."""

        def __init__(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
            parent: "PinionFinishMachineSettings",
        ):
            self._parent = parent

        @property
        def conical_gear_tooth_surface(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
        ) -> "_323.ConicalGearToothSurface":
            return self._parent._cast(_323.ConicalGearToothSurface)

        @property
        def pinion_bevel_generating_modified_roll_machine_settings(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
        ) -> "_804.PinionBevelGeneratingModifiedRollMachineSettings":
            from mastapy.gears.manufacturing.bevel import _804

            return self._parent._cast(
                _804.PinionBevelGeneratingModifiedRollMachineSettings
            )

        @property
        def pinion_bevel_generating_tilt_machine_settings(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
        ) -> "_805.PinionBevelGeneratingTiltMachineSettings":
            from mastapy.gears.manufacturing.bevel import _805

            return self._parent._cast(_805.PinionBevelGeneratingTiltMachineSettings)

        @property
        def pinion_conical_machine_settings_specified(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
        ) -> "_807.PinionConicalMachineSettingsSpecified":
            from mastapy.gears.manufacturing.bevel import _807

            return self._parent._cast(_807.PinionConicalMachineSettingsSpecified)

        @property
        def pinion_hypoid_formate_tilt_machine_settings(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
        ) -> "_810.PinionHypoidFormateTiltMachineSettings":
            from mastapy.gears.manufacturing.bevel import _810

            return self._parent._cast(_810.PinionHypoidFormateTiltMachineSettings)

        @property
        def pinion_hypoid_generating_tilt_machine_settings(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
        ) -> "_811.PinionHypoidGeneratingTiltMachineSettings":
            from mastapy.gears.manufacturing.bevel import _811

            return self._parent._cast(_811.PinionHypoidGeneratingTiltMachineSettings)

        @property
        def pinion_machine_settings_smt(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
        ) -> "_812.PinionMachineSettingsSMT":
            from mastapy.gears.manufacturing.bevel import _812

            return self._parent._cast(_812.PinionMachineSettingsSMT)

        @property
        def pinion_finish_machine_settings(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
        ) -> "PinionFinishMachineSettings":
            return self._parent

        def __getattr__(
            self: "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PinionFinishMachineSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def blade_edge_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BladeEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def cc_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CCAngle

        if temp is None:
            return 0.0

        return temp

    @cc_angle.setter
    @enforce_parameter_types
    def cc_angle(self: Self, value: "float"):
        self.wrapped.CCAngle = float(value) if value is not None else 0.0

    @property
    def cutter_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CutterRadius

        if temp is None:
            return 0.0

        return temp

    @cutter_radius.setter
    @enforce_parameter_types
    def cutter_radius(self: Self, value: "float"):
        self.wrapped.CutterRadius = float(value) if value is not None else 0.0

    @property
    def ease_off_at_heel_root(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EaseOffAtHeelRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def ease_off_at_heel_tip(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EaseOffAtHeelTip

        if temp is None:
            return 0.0

        return temp

    @property
    def ease_off_at_toe_root(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EaseOffAtToeRoot

        if temp is None:
            return 0.0

        return temp

    @property
    def ease_off_at_toe_tip(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EaseOffAtToeTip

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_cutter_blade_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionCutterBladeAngle

        if temp is None:
            return 0.0

        return temp

    @pinion_cutter_blade_angle.setter
    @enforce_parameter_types
    def pinion_cutter_blade_angle(self: Self, value: "float"):
        self.wrapped.PinionCutterBladeAngle = float(value) if value is not None else 0.0

    @property
    def toprem_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TopremAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def toprem_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TopremLength

        if temp is None:
            return 0.0

        return temp

    @property
    def toprem_letter(self: Self) -> "_1177.TopremLetter":
        """mastapy.gears.gear_designs.conical.TopremLetter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TopremLetter

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.TopremLetter"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1177", "TopremLetter"
        )(value)

    @property
    def cast_to(
        self: Self,
    ) -> "PinionFinishMachineSettings._Cast_PinionFinishMachineSettings":
        return self._Cast_PinionFinishMachineSettings(self)
