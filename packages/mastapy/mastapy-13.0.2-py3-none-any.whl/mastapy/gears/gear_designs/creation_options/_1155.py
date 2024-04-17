"""SpiralBevelGearSetCreationOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.creation_options import _1153
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.CreationOptions",
    "SpiralBevelGearSetCreationOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCreationOptions",)


Self = TypeVar("Self", bound="SpiralBevelGearSetCreationOptions")


class SpiralBevelGearSetCreationOptions(
    _1153.GearSetCreationOptions["_975.SpiralBevelGearSetDesign"]
):
    """SpiralBevelGearSetCreationOptions

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetCreationOptions")

    class _Cast_SpiralBevelGearSetCreationOptions:
        """Special nested class for casting SpiralBevelGearSetCreationOptions to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCreationOptions._Cast_SpiralBevelGearSetCreationOptions",
            parent: "SpiralBevelGearSetCreationOptions",
        ):
            self._parent = parent

        @property
        def gear_set_creation_options(
            self: "SpiralBevelGearSetCreationOptions._Cast_SpiralBevelGearSetCreationOptions",
        ) -> "_1153.GearSetCreationOptions":
            return self._parent._cast(_1153.GearSetCreationOptions)

        @property
        def spiral_bevel_gear_set_creation_options(
            self: "SpiralBevelGearSetCreationOptions._Cast_SpiralBevelGearSetCreationOptions",
        ) -> "SpiralBevelGearSetCreationOptions":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCreationOptions._Cast_SpiralBevelGearSetCreationOptions",
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
        self: Self, instance_to_wrap: "SpiralBevelGearSetCreationOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetCreationOptions._Cast_SpiralBevelGearSetCreationOptions":
        return self._Cast_SpiralBevelGearSetCreationOptions(self)
