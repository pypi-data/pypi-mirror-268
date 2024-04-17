"""StandardRackFlank"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical import _1013
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_RACK_FLANK = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "StandardRackFlank"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1011


__docformat__ = "restructuredtext en"
__all__ = ("StandardRackFlank",)


Self = TypeVar("Self", bound="StandardRackFlank")


class StandardRackFlank(_1013.CylindricalGearBasicRackFlank):
    """StandardRackFlank

    This is a mastapy class.
    """

    TYPE = _STANDARD_RACK_FLANK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StandardRackFlank")

    class _Cast_StandardRackFlank:
        """Special nested class for casting StandardRackFlank to subclasses."""

        def __init__(
            self: "StandardRackFlank._Cast_StandardRackFlank",
            parent: "StandardRackFlank",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_basic_rack_flank(
            self: "StandardRackFlank._Cast_StandardRackFlank",
        ) -> "_1013.CylindricalGearBasicRackFlank":
            return self._parent._cast(_1013.CylindricalGearBasicRackFlank)

        @property
        def cylindrical_gear_abstract_rack_flank(
            self: "StandardRackFlank._Cast_StandardRackFlank",
        ) -> "_1011.CylindricalGearAbstractRackFlank":
            from mastapy.gears.gear_designs.cylindrical import _1011

            return self._parent._cast(_1011.CylindricalGearAbstractRackFlank)

        @property
        def standard_rack_flank(
            self: "StandardRackFlank._Cast_StandardRackFlank",
        ) -> "StandardRackFlank":
            return self._parent

        def __getattr__(self: "StandardRackFlank._Cast_StandardRackFlank", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StandardRackFlank.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StandardRackFlank._Cast_StandardRackFlank":
        return self._Cast_StandardRackFlank(self)
