"""ShaverPointCalculationError"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _645
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVER_POINT_CALCULATION_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "ShaverPointCalculationError",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaverPointCalculationError",)


Self = TypeVar("Self", bound="ShaverPointCalculationError")


class ShaverPointCalculationError(_645.CalculationError):
    """ShaverPointCalculationError

    This is a mastapy class.
    """

    TYPE = _SHAVER_POINT_CALCULATION_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaverPointCalculationError")

    class _Cast_ShaverPointCalculationError:
        """Special nested class for casting ShaverPointCalculationError to subclasses."""

        def __init__(
            self: "ShaverPointCalculationError._Cast_ShaverPointCalculationError",
            parent: "ShaverPointCalculationError",
        ):
            self._parent = parent

        @property
        def calculation_error(
            self: "ShaverPointCalculationError._Cast_ShaverPointCalculationError",
        ) -> "_645.CalculationError":
            return self._parent._cast(_645.CalculationError)

        @property
        def shaver_point_calculation_error(
            self: "ShaverPointCalculationError._Cast_ShaverPointCalculationError",
        ) -> "ShaverPointCalculationError":
            return self._parent

        def __getattr__(
            self: "ShaverPointCalculationError._Cast_ShaverPointCalculationError",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaverPointCalculationError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def achieved_shaver_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AchievedShaverRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def achieved_shaver_z_plane(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AchievedShaverZPlane

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_z_plane(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaverZPlane

        if temp is None:
            return 0.0

        return temp

    @property
    def total_error(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalError

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ShaverPointCalculationError._Cast_ShaverPointCalculationError":
        return self._Cast_ShaverPointCalculationError(self)
