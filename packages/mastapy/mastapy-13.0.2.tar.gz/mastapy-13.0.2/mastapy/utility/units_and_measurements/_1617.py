"""Unit"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNIT = python_net_import("SMT.MastaAPI.Utility.UnitsAndMeasurements", "Unit")

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import (
        _1609,
        _1610,
        _1611,
        _1615,
        _1616,
        _1618,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Unit",)


Self = TypeVar("Self", bound="Unit")


class Unit(_0.APIBase):
    """Unit

    This is a mastapy class.
    """

    TYPE = _UNIT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Unit")

    class _Cast_Unit:
        """Special nested class for casting Unit to subclasses."""

        def __init__(self: "Unit._Cast_Unit", parent: "Unit"):
            self._parent = parent

        @property
        def degrees_minutes_seconds(
            self: "Unit._Cast_Unit",
        ) -> "_1609.DegreesMinutesSeconds":
            from mastapy.utility.units_and_measurements import _1609

            return self._parent._cast(_1609.DegreesMinutesSeconds)

        @property
        def enum_unit(self: "Unit._Cast_Unit") -> "_1610.EnumUnit":
            from mastapy.utility.units_and_measurements import _1610

            return self._parent._cast(_1610.EnumUnit)

        @property
        def inverse_unit(self: "Unit._Cast_Unit") -> "_1611.InverseUnit":
            from mastapy.utility.units_and_measurements import _1611

            return self._parent._cast(_1611.InverseUnit)

        @property
        def safety_factor_unit(self: "Unit._Cast_Unit") -> "_1615.SafetyFactorUnit":
            from mastapy.utility.units_and_measurements import _1615

            return self._parent._cast(_1615.SafetyFactorUnit)

        @property
        def time_unit(self: "Unit._Cast_Unit") -> "_1616.TimeUnit":
            from mastapy.utility.units_and_measurements import _1616

            return self._parent._cast(_1616.TimeUnit)

        @property
        def unit_gradient(self: "Unit._Cast_Unit") -> "_1618.UnitGradient":
            from mastapy.utility.units_and_measurements import _1618

            return self._parent._cast(_1618.UnitGradient)

        @property
        def unit(self: "Unit._Cast_Unit") -> "Unit":
            return self._parent

        def __getattr__(self: "Unit._Cast_Unit", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Unit.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def html_symbol(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HTMLSymbol

        if temp is None:
            return ""

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def offset(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @property
    def scale(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Scale

        if temp is None:
            return 0.0

        return temp

    @property
    def symbol(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Symbol

        if temp is None:
            return ""

        return temp

    @enforce_parameter_types
    def convert_from_si_unit(self: Self, d: "float") -> "float":
        """float

        Args:
            d (float)
        """
        d = float(d)
        method_result = self.wrapped.ConvertFromSIUnit(d if d else 0.0)
        return method_result

    @enforce_parameter_types
    def convert_to_si_unit(self: Self, d: "float") -> "float":
        """float

        Args:
            d (float)
        """
        d = float(d)
        method_result = self.wrapped.ConvertToSIUnit(d if d else 0.0)
        return method_result

    @property
    def cast_to(self: Self) -> "Unit._Cast_Unit":
        return self._Cast_Unit(self)
