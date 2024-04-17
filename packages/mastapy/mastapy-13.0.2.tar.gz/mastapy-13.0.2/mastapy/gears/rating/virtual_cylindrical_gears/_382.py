"""BevelVirtualCylindricalGearSetISO10300MethodB1"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _396
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B1 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "BevelVirtualCylindricalGearSetISO10300MethodB1",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _395


__docformat__ = "restructuredtext en"
__all__ = ("BevelVirtualCylindricalGearSetISO10300MethodB1",)


Self = TypeVar("Self", bound="BevelVirtualCylindricalGearSetISO10300MethodB1")


class BevelVirtualCylindricalGearSetISO10300MethodB1(
    _396.VirtualCylindricalGearSetISO10300MethodB1
):
    """BevelVirtualCylindricalGearSetISO10300MethodB1

    This is a mastapy class.
    """

    TYPE = _BEVEL_VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B1
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelVirtualCylindricalGearSetISO10300MethodB1"
    )

    class _Cast_BevelVirtualCylindricalGearSetISO10300MethodB1:
        """Special nested class for casting BevelVirtualCylindricalGearSetISO10300MethodB1 to subclasses."""

        def __init__(
            self: "BevelVirtualCylindricalGearSetISO10300MethodB1._Cast_BevelVirtualCylindricalGearSetISO10300MethodB1",
            parent: "BevelVirtualCylindricalGearSetISO10300MethodB1",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_set_iso10300_method_b1(
            self: "BevelVirtualCylindricalGearSetISO10300MethodB1._Cast_BevelVirtualCylindricalGearSetISO10300MethodB1",
        ) -> "_396.VirtualCylindricalGearSetISO10300MethodB1":
            return self._parent._cast(_396.VirtualCylindricalGearSetISO10300MethodB1)

        @property
        def virtual_cylindrical_gear_set(
            self: "BevelVirtualCylindricalGearSetISO10300MethodB1._Cast_BevelVirtualCylindricalGearSetISO10300MethodB1",
        ) -> "_395.VirtualCylindricalGearSet":
            pass

            from mastapy.gears.rating.virtual_cylindrical_gears import _395

            return self._parent._cast(_395.VirtualCylindricalGearSet)

        @property
        def bevel_virtual_cylindrical_gear_set_iso10300_method_b1(
            self: "BevelVirtualCylindricalGearSetISO10300MethodB1._Cast_BevelVirtualCylindricalGearSetISO10300MethodB1",
        ) -> "BevelVirtualCylindricalGearSetISO10300MethodB1":
            return self._parent

        def __getattr__(
            self: "BevelVirtualCylindricalGearSetISO10300MethodB1._Cast_BevelVirtualCylindricalGearSetISO10300MethodB1",
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
        instance_to_wrap: "BevelVirtualCylindricalGearSetISO10300MethodB1.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelVirtualCylindricalGearSetISO10300MethodB1._Cast_BevelVirtualCylindricalGearSetISO10300MethodB1":
        return self._Cast_BevelVirtualCylindricalGearSetISO10300MethodB1(self)
