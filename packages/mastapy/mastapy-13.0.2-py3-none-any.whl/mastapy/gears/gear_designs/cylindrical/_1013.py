"""CylindricalGearBasicRackFlank"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical import _1011
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BASIC_RACK_FLANK = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearBasicRackFlank"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1083


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearBasicRackFlank",)


Self = TypeVar("Self", bound="CylindricalGearBasicRackFlank")


class CylindricalGearBasicRackFlank(_1011.CylindricalGearAbstractRackFlank):
    """CylindricalGearBasicRackFlank

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BASIC_RACK_FLANK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearBasicRackFlank")

    class _Cast_CylindricalGearBasicRackFlank:
        """Special nested class for casting CylindricalGearBasicRackFlank to subclasses."""

        def __init__(
            self: "CylindricalGearBasicRackFlank._Cast_CylindricalGearBasicRackFlank",
            parent: "CylindricalGearBasicRackFlank",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_abstract_rack_flank(
            self: "CylindricalGearBasicRackFlank._Cast_CylindricalGearBasicRackFlank",
        ) -> "_1011.CylindricalGearAbstractRackFlank":
            return self._parent._cast(_1011.CylindricalGearAbstractRackFlank)

        @property
        def standard_rack_flank(
            self: "CylindricalGearBasicRackFlank._Cast_CylindricalGearBasicRackFlank",
        ) -> "_1083.StandardRackFlank":
            from mastapy.gears.gear_designs.cylindrical import _1083

            return self._parent._cast(_1083.StandardRackFlank)

        @property
        def cylindrical_gear_basic_rack_flank(
            self: "CylindricalGearBasicRackFlank._Cast_CylindricalGearBasicRackFlank",
        ) -> "CylindricalGearBasicRackFlank":
            return self._parent

        def __getattr__(
            self: "CylindricalGearBasicRackFlank._Cast_CylindricalGearBasicRackFlank",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearBasicRackFlank.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearBasicRackFlank._Cast_CylindricalGearBasicRackFlank":
        return self._Cast_CylindricalGearBasicRackFlank(self)
