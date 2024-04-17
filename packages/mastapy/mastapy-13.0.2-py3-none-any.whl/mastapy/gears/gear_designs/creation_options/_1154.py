"""HypoidGearSetCreationOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.creation_options import _1153
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_CREATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.CreationOptions", "HypoidGearSetCreationOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCreationOptions",)


Self = TypeVar("Self", bound="HypoidGearSetCreationOptions")


class HypoidGearSetCreationOptions(
    _1153.GearSetCreationOptions["_991.HypoidGearSetDesign"]
):
    """HypoidGearSetCreationOptions

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_CREATION_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetCreationOptions")

    class _Cast_HypoidGearSetCreationOptions:
        """Special nested class for casting HypoidGearSetCreationOptions to subclasses."""

        def __init__(
            self: "HypoidGearSetCreationOptions._Cast_HypoidGearSetCreationOptions",
            parent: "HypoidGearSetCreationOptions",
        ):
            self._parent = parent

        @property
        def gear_set_creation_options(
            self: "HypoidGearSetCreationOptions._Cast_HypoidGearSetCreationOptions",
        ) -> "_1153.GearSetCreationOptions":
            return self._parent._cast(_1153.GearSetCreationOptions)

        @property
        def hypoid_gear_set_creation_options(
            self: "HypoidGearSetCreationOptions._Cast_HypoidGearSetCreationOptions",
        ) -> "HypoidGearSetCreationOptions":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCreationOptions._Cast_HypoidGearSetCreationOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetCreationOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetCreationOptions._Cast_HypoidGearSetCreationOptions":
        return self._Cast_HypoidGearSetCreationOptions(self)
