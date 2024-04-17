"""GearPointCalculationError"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _645
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_POINT_CALCULATION_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "GearPointCalculationError",
)


__docformat__ = "restructuredtext en"
__all__ = ("GearPointCalculationError",)


Self = TypeVar("Self", bound="GearPointCalculationError")


class GearPointCalculationError(_645.CalculationError):
    """GearPointCalculationError

    This is a mastapy class.
    """

    TYPE = _GEAR_POINT_CALCULATION_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearPointCalculationError")

    class _Cast_GearPointCalculationError:
        """Special nested class for casting GearPointCalculationError to subclasses."""

        def __init__(
            self: "GearPointCalculationError._Cast_GearPointCalculationError",
            parent: "GearPointCalculationError",
        ):
            self._parent = parent

        @property
        def calculation_error(
            self: "GearPointCalculationError._Cast_GearPointCalculationError",
        ) -> "_645.CalculationError":
            return self._parent._cast(_645.CalculationError)

        @property
        def gear_point_calculation_error(
            self: "GearPointCalculationError._Cast_GearPointCalculationError",
        ) -> "GearPointCalculationError":
            return self._parent

        def __getattr__(
            self: "GearPointCalculationError._Cast_GearPointCalculationError", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearPointCalculationError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearPointCalculationError._Cast_GearPointCalculationError":
        return self._Cast_GearPointCalculationError(self)
