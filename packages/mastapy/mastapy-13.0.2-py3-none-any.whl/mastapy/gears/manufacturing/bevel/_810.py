"""PinionHypoidFormateTiltMachineSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.bevel import _809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_HYPOID_FORMATE_TILT_MACHINE_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "PinionHypoidFormateTiltMachineSettings"
)

if TYPE_CHECKING:
    from mastapy.gears import _323


__docformat__ = "restructuredtext en"
__all__ = ("PinionHypoidFormateTiltMachineSettings",)


Self = TypeVar("Self", bound="PinionHypoidFormateTiltMachineSettings")


class PinionHypoidFormateTiltMachineSettings(_809.PinionFinishMachineSettings):
    """PinionHypoidFormateTiltMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_HYPOID_FORMATE_TILT_MACHINE_SETTINGS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PinionHypoidFormateTiltMachineSettings"
    )

    class _Cast_PinionHypoidFormateTiltMachineSettings:
        """Special nested class for casting PinionHypoidFormateTiltMachineSettings to subclasses."""

        def __init__(
            self: "PinionHypoidFormateTiltMachineSettings._Cast_PinionHypoidFormateTiltMachineSettings",
            parent: "PinionHypoidFormateTiltMachineSettings",
        ):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(
            self: "PinionHypoidFormateTiltMachineSettings._Cast_PinionHypoidFormateTiltMachineSettings",
        ) -> "_809.PinionFinishMachineSettings":
            return self._parent._cast(_809.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(
            self: "PinionHypoidFormateTiltMachineSettings._Cast_PinionHypoidFormateTiltMachineSettings",
        ) -> "_323.ConicalGearToothSurface":
            from mastapy.gears import _323

            return self._parent._cast(_323.ConicalGearToothSurface)

        @property
        def pinion_hypoid_formate_tilt_machine_settings(
            self: "PinionHypoidFormateTiltMachineSettings._Cast_PinionHypoidFormateTiltMachineSettings",
        ) -> "PinionHypoidFormateTiltMachineSettings":
            return self._parent

        def __getattr__(
            self: "PinionHypoidFormateTiltMachineSettings._Cast_PinionHypoidFormateTiltMachineSettings",
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
        self: Self, instance_to_wrap: "PinionHypoidFormateTiltMachineSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PinionHypoidFormateTiltMachineSettings._Cast_PinionHypoidFormateTiltMachineSettings":
        return self._Cast_PinionHypoidFormateTiltMachineSettings(self)
