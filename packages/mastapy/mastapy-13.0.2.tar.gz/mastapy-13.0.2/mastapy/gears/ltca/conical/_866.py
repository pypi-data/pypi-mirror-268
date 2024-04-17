"""ConicalGearBendingStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_BENDING_STIFFNESS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalGearBendingStiffness"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _850
    from mastapy.nodal_analysis import _66


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearBendingStiffness",)


Self = TypeVar("Self", bound="ConicalGearBendingStiffness")


class ConicalGearBendingStiffness(_836.GearBendingStiffness):
    """ConicalGearBendingStiffness

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_BENDING_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearBendingStiffness")

    class _Cast_ConicalGearBendingStiffness:
        """Special nested class for casting ConicalGearBendingStiffness to subclasses."""

        def __init__(
            self: "ConicalGearBendingStiffness._Cast_ConicalGearBendingStiffness",
            parent: "ConicalGearBendingStiffness",
        ):
            self._parent = parent

        @property
        def gear_bending_stiffness(
            self: "ConicalGearBendingStiffness._Cast_ConicalGearBendingStiffness",
        ) -> "_836.GearBendingStiffness":
            return self._parent._cast(_836.GearBendingStiffness)

        @property
        def gear_stiffness(
            self: "ConicalGearBendingStiffness._Cast_ConicalGearBendingStiffness",
        ) -> "_850.GearStiffness":
            from mastapy.gears.ltca import _850

            return self._parent._cast(_850.GearStiffness)

        @property
        def fe_stiffness(
            self: "ConicalGearBendingStiffness._Cast_ConicalGearBendingStiffness",
        ) -> "_66.FEStiffness":
            from mastapy.nodal_analysis import _66

            return self._parent._cast(_66.FEStiffness)

        @property
        def conical_gear_bending_stiffness(
            self: "ConicalGearBendingStiffness._Cast_ConicalGearBendingStiffness",
        ) -> "ConicalGearBendingStiffness":
            return self._parent

        def __getattr__(
            self: "ConicalGearBendingStiffness._Cast_ConicalGearBendingStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearBendingStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearBendingStiffness._Cast_ConicalGearBendingStiffness":
        return self._Cast_ConicalGearBendingStiffness(self)
