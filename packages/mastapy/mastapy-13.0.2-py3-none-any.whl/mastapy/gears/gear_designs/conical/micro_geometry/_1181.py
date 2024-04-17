"""ConicalGearProfileModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.micro_geometry import _585
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_PROFILE_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry",
    "ConicalGearProfileModification",
)

if TYPE_CHECKING:
    from mastapy.gears.micro_geometry import _582


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearProfileModification",)


Self = TypeVar("Self", bound="ConicalGearProfileModification")


class ConicalGearProfileModification(_585.ProfileModification):
    """ConicalGearProfileModification

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_PROFILE_MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearProfileModification")

    class _Cast_ConicalGearProfileModification:
        """Special nested class for casting ConicalGearProfileModification to subclasses."""

        def __init__(
            self: "ConicalGearProfileModification._Cast_ConicalGearProfileModification",
            parent: "ConicalGearProfileModification",
        ):
            self._parent = parent

        @property
        def profile_modification(
            self: "ConicalGearProfileModification._Cast_ConicalGearProfileModification",
        ) -> "_585.ProfileModification":
            return self._parent._cast(_585.ProfileModification)

        @property
        def modification(
            self: "ConicalGearProfileModification._Cast_ConicalGearProfileModification",
        ) -> "_582.Modification":
            from mastapy.gears.micro_geometry import _582

            return self._parent._cast(_582.Modification)

        @property
        def conical_gear_profile_modification(
            self: "ConicalGearProfileModification._Cast_ConicalGearProfileModification",
        ) -> "ConicalGearProfileModification":
            return self._parent

        def __getattr__(
            self: "ConicalGearProfileModification._Cast_ConicalGearProfileModification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearProfileModification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearProfileModification._Cast_ConicalGearProfileModification":
        return self._Cast_ConicalGearProfileModification(self)
