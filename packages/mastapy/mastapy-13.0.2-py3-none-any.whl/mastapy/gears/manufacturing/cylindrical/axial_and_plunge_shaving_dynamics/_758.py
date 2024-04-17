"""PlungeShaverDynamics"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _768,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_DYNAMICS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "PlungeShaverDynamics",
)


__docformat__ = "restructuredtext en"
__all__ = ("PlungeShaverDynamics",)


Self = TypeVar("Self", bound="PlungeShaverDynamics")


class PlungeShaverDynamics(_768.ShavingDynamics):
    """PlungeShaverDynamics

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_DYNAMICS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlungeShaverDynamics")

    class _Cast_PlungeShaverDynamics:
        """Special nested class for casting PlungeShaverDynamics to subclasses."""

        def __init__(
            self: "PlungeShaverDynamics._Cast_PlungeShaverDynamics",
            parent: "PlungeShaverDynamics",
        ):
            self._parent = parent

        @property
        def shaving_dynamics(
            self: "PlungeShaverDynamics._Cast_PlungeShaverDynamics",
        ) -> "_768.ShavingDynamics":
            return self._parent._cast(_768.ShavingDynamics)

        @property
        def plunge_shaver_dynamics(
            self: "PlungeShaverDynamics._Cast_PlungeShaverDynamics",
        ) -> "PlungeShaverDynamics":
            return self._parent

        def __getattr__(
            self: "PlungeShaverDynamics._Cast_PlungeShaverDynamics", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlungeShaverDynamics.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_gear_teeth_passed_per_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfGearTeethPassedPerFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "PlungeShaverDynamics._Cast_PlungeShaverDynamics":
        return self._Cast_PlungeShaverDynamics(self)
