"""GearBendingStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _850
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_BENDING_STIFFNESS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearBendingStiffness"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _854
    from mastapy.gears.ltca.conical import _866
    from mastapy.nodal_analysis import _66


__docformat__ = "restructuredtext en"
__all__ = ("GearBendingStiffness",)


Self = TypeVar("Self", bound="GearBendingStiffness")


class GearBendingStiffness(_850.GearStiffness):
    """GearBendingStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_BENDING_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearBendingStiffness")

    class _Cast_GearBendingStiffness:
        """Special nested class for casting GearBendingStiffness to subclasses."""

        def __init__(
            self: "GearBendingStiffness._Cast_GearBendingStiffness",
            parent: "GearBendingStiffness",
        ):
            self._parent = parent

        @property
        def gear_stiffness(
            self: "GearBendingStiffness._Cast_GearBendingStiffness",
        ) -> "_850.GearStiffness":
            return self._parent._cast(_850.GearStiffness)

        @property
        def fe_stiffness(
            self: "GearBendingStiffness._Cast_GearBendingStiffness",
        ) -> "_66.FEStiffness":
            from mastapy.nodal_analysis import _66

            return self._parent._cast(_66.FEStiffness)

        @property
        def cylindrical_gear_bending_stiffness(
            self: "GearBendingStiffness._Cast_GearBendingStiffness",
        ) -> "_854.CylindricalGearBendingStiffness":
            from mastapy.gears.ltca.cylindrical import _854

            return self._parent._cast(_854.CylindricalGearBendingStiffness)

        @property
        def conical_gear_bending_stiffness(
            self: "GearBendingStiffness._Cast_GearBendingStiffness",
        ) -> "_866.ConicalGearBendingStiffness":
            from mastapy.gears.ltca.conical import _866

            return self._parent._cast(_866.ConicalGearBendingStiffness)

        @property
        def gear_bending_stiffness(
            self: "GearBendingStiffness._Cast_GearBendingStiffness",
        ) -> "GearBendingStiffness":
            return self._parent

        def __getattr__(
            self: "GearBendingStiffness._Cast_GearBendingStiffness", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearBendingStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearBendingStiffness._Cast_GearBendingStiffness":
        return self._Cast_GearBendingStiffness(self)
