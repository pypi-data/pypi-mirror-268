"""PinionBevelGeneratingModifiedRollMachineSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.bevel import _809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_BEVEL_GENERATING_MODIFIED_ROLL_MACHINE_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel",
    "PinionBevelGeneratingModifiedRollMachineSettings",
)

if TYPE_CHECKING:
    from mastapy.gears import _323


__docformat__ = "restructuredtext en"
__all__ = ("PinionBevelGeneratingModifiedRollMachineSettings",)


Self = TypeVar("Self", bound="PinionBevelGeneratingModifiedRollMachineSettings")


class PinionBevelGeneratingModifiedRollMachineSettings(
    _809.PinionFinishMachineSettings
):
    """PinionBevelGeneratingModifiedRollMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_BEVEL_GENERATING_MODIFIED_ROLL_MACHINE_SETTINGS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PinionBevelGeneratingModifiedRollMachineSettings"
    )

    class _Cast_PinionBevelGeneratingModifiedRollMachineSettings:
        """Special nested class for casting PinionBevelGeneratingModifiedRollMachineSettings to subclasses."""

        def __init__(
            self: "PinionBevelGeneratingModifiedRollMachineSettings._Cast_PinionBevelGeneratingModifiedRollMachineSettings",
            parent: "PinionBevelGeneratingModifiedRollMachineSettings",
        ):
            self._parent = parent

        @property
        def pinion_finish_machine_settings(
            self: "PinionBevelGeneratingModifiedRollMachineSettings._Cast_PinionBevelGeneratingModifiedRollMachineSettings",
        ) -> "_809.PinionFinishMachineSettings":
            return self._parent._cast(_809.PinionFinishMachineSettings)

        @property
        def conical_gear_tooth_surface(
            self: "PinionBevelGeneratingModifiedRollMachineSettings._Cast_PinionBevelGeneratingModifiedRollMachineSettings",
        ) -> "_323.ConicalGearToothSurface":
            from mastapy.gears import _323

            return self._parent._cast(_323.ConicalGearToothSurface)

        @property
        def pinion_bevel_generating_modified_roll_machine_settings(
            self: "PinionBevelGeneratingModifiedRollMachineSettings._Cast_PinionBevelGeneratingModifiedRollMachineSettings",
        ) -> "PinionBevelGeneratingModifiedRollMachineSettings":
            return self._parent

        def __getattr__(
            self: "PinionBevelGeneratingModifiedRollMachineSettings._Cast_PinionBevelGeneratingModifiedRollMachineSettings",
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
        self: Self,
        instance_to_wrap: "PinionBevelGeneratingModifiedRollMachineSettings.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PinionBevelGeneratingModifiedRollMachineSettings._Cast_PinionBevelGeneratingModifiedRollMachineSettings":
        return self._Cast_PinionBevelGeneratingModifiedRollMachineSettings(self)
