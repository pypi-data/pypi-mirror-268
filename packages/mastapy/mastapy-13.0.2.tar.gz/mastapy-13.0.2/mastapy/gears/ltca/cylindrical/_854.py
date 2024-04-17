"""CylindricalGearBendingStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BENDING_STIFFNESS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearBendingStiffness"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _850
    from mastapy.nodal_analysis import _66


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearBendingStiffness",)


Self = TypeVar("Self", bound="CylindricalGearBendingStiffness")


class CylindricalGearBendingStiffness(_836.GearBendingStiffness):
    """CylindricalGearBendingStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BENDING_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearBendingStiffness")

    class _Cast_CylindricalGearBendingStiffness:
        """Special nested class for casting CylindricalGearBendingStiffness to subclasses."""

        def __init__(
            self: "CylindricalGearBendingStiffness._Cast_CylindricalGearBendingStiffness",
            parent: "CylindricalGearBendingStiffness",
        ):
            self._parent = parent

        @property
        def gear_bending_stiffness(
            self: "CylindricalGearBendingStiffness._Cast_CylindricalGearBendingStiffness",
        ) -> "_836.GearBendingStiffness":
            return self._parent._cast(_836.GearBendingStiffness)

        @property
        def gear_stiffness(
            self: "CylindricalGearBendingStiffness._Cast_CylindricalGearBendingStiffness",
        ) -> "_850.GearStiffness":
            from mastapy.gears.ltca import _850

            return self._parent._cast(_850.GearStiffness)

        @property
        def fe_stiffness(
            self: "CylindricalGearBendingStiffness._Cast_CylindricalGearBendingStiffness",
        ) -> "_66.FEStiffness":
            from mastapy.nodal_analysis import _66

            return self._parent._cast(_66.FEStiffness)

        @property
        def cylindrical_gear_bending_stiffness(
            self: "CylindricalGearBendingStiffness._Cast_CylindricalGearBendingStiffness",
        ) -> "CylindricalGearBendingStiffness":
            return self._parent

        def __getattr__(
            self: "CylindricalGearBendingStiffness._Cast_CylindricalGearBendingStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearBendingStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearBendingStiffness._Cast_CylindricalGearBendingStiffness":
        return self._Cast_CylindricalGearBendingStiffness(self)
