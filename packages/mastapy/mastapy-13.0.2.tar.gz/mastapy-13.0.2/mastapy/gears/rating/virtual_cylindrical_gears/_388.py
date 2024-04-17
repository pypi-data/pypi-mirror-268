"""KlingelnbergSpiralBevelVirtualCylindricalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _389
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_SPIRAL_BEVEL_VIRTUAL_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "KlingelnbergSpiralBevelVirtualCylindricalGear",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _391, _392


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergSpiralBevelVirtualCylindricalGear",)


Self = TypeVar("Self", bound="KlingelnbergSpiralBevelVirtualCylindricalGear")


class KlingelnbergSpiralBevelVirtualCylindricalGear(
    _389.KlingelnbergVirtualCylindricalGear
):
    """KlingelnbergSpiralBevelVirtualCylindricalGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_SPIRAL_BEVEL_VIRTUAL_CYLINDRICAL_GEAR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergSpiralBevelVirtualCylindricalGear"
    )

    class _Cast_KlingelnbergSpiralBevelVirtualCylindricalGear:
        """Special nested class for casting KlingelnbergSpiralBevelVirtualCylindricalGear to subclasses."""

        def __init__(
            self: "KlingelnbergSpiralBevelVirtualCylindricalGear._Cast_KlingelnbergSpiralBevelVirtualCylindricalGear",
            parent: "KlingelnbergSpiralBevelVirtualCylindricalGear",
        ):
            self._parent = parent

        @property
        def klingelnberg_virtual_cylindrical_gear(
            self: "KlingelnbergSpiralBevelVirtualCylindricalGear._Cast_KlingelnbergSpiralBevelVirtualCylindricalGear",
        ) -> "_389.KlingelnbergVirtualCylindricalGear":
            return self._parent._cast(_389.KlingelnbergVirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear(
            self: "KlingelnbergSpiralBevelVirtualCylindricalGear._Cast_KlingelnbergSpiralBevelVirtualCylindricalGear",
        ) -> "_391.VirtualCylindricalGear":
            from mastapy.gears.rating.virtual_cylindrical_gears import _391

            return self._parent._cast(_391.VirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_basic(
            self: "KlingelnbergSpiralBevelVirtualCylindricalGear._Cast_KlingelnbergSpiralBevelVirtualCylindricalGear",
        ) -> "_392.VirtualCylindricalGearBasic":
            from mastapy.gears.rating.virtual_cylindrical_gears import _392

            return self._parent._cast(_392.VirtualCylindricalGearBasic)

        @property
        def klingelnberg_spiral_bevel_virtual_cylindrical_gear(
            self: "KlingelnbergSpiralBevelVirtualCylindricalGear._Cast_KlingelnbergSpiralBevelVirtualCylindricalGear",
        ) -> "KlingelnbergSpiralBevelVirtualCylindricalGear":
            return self._parent

        def __getattr__(
            self: "KlingelnbergSpiralBevelVirtualCylindricalGear._Cast_KlingelnbergSpiralBevelVirtualCylindricalGear",
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
        instance_to_wrap: "KlingelnbergSpiralBevelVirtualCylindricalGear.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergSpiralBevelVirtualCylindricalGear._Cast_KlingelnbergSpiralBevelVirtualCylindricalGear":
        return self._Cast_KlingelnbergSpiralBevelVirtualCylindricalGear(self)
