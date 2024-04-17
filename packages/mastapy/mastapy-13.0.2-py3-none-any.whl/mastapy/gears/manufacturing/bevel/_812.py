"""PinionMachineSettingsSMT"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.bevel import _809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_MACHINE_SETTINGS_SMT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "PinionMachineSettingsSMT"
)

if TYPE_CHECKING:
    from mastapy.gears import _323


__docformat__ = "restructuredtext en"
__all__ = ("PinionMachineSettingsSMT",)


Self = TypeVar("Self", bound="PinionMachineSettingsSMT")


class PinionMachineSettingsSMT(_809.PinionFinishMachineSettings):
    """PinionMachineSettingsSMT

    This is a mastapy class.
    """

    TYPE = _PINION_MACHINE_SETTINGS_SMT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PinionMachineSettingsSMT")

    class _Cast_PinionMachineSettingsSMT:
        """Special nested class for casting PinionMachineSettingsSMT to subclasses."""

        def __init__(
            self: "PinionMachineSettingsSMT._Cast_PinionMachineSettingsSMT",
            parent: "PinionMachineSettingsSMT",
        ):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(
            self: "PinionMachineSettingsSMT._Cast_PinionMachineSettingsSMT",
        ) -> "_809.PinionFinishMachineSettings":
            return self._parent._cast(_809.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(
            self: "PinionMachineSettingsSMT._Cast_PinionMachineSettingsSMT",
        ) -> "_323.ConicalGearToothSurface":
            from mastapy.gears import _323

            return self._parent._cast(_323.ConicalGearToothSurface)

        @property
        def pinion_machine_settings_smt(
            self: "PinionMachineSettingsSMT._Cast_PinionMachineSettingsSMT",
        ) -> "PinionMachineSettingsSMT":
            return self._parent

        def __getattr__(
            self: "PinionMachineSettingsSMT._Cast_PinionMachineSettingsSMT", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PinionMachineSettingsSMT.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PinionMachineSettingsSMT._Cast_PinionMachineSettingsSMT":
        return self._Cast_PinionMachineSettingsSMT(self)
