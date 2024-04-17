"""SafetyFactorUnit"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_UNIT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements", "SafetyFactorUnit"
)


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorUnit",)


Self = TypeVar("Self", bound="SafetyFactorUnit")


class SafetyFactorUnit(_1617.Unit):
    """SafetyFactorUnit

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_UNIT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SafetyFactorUnit")

    class _Cast_SafetyFactorUnit:
        """Special nested class for casting SafetyFactorUnit to subclasses."""

        def __init__(
            self: "SafetyFactorUnit._Cast_SafetyFactorUnit", parent: "SafetyFactorUnit"
        ):
            self._parent = parent

        @property
        def unit(self: "SafetyFactorUnit._Cast_SafetyFactorUnit") -> "_1617.Unit":
            return self._parent._cast(_1617.Unit)

        @property
        def safety_factor_unit(
            self: "SafetyFactorUnit._Cast_SafetyFactorUnit",
        ) -> "SafetyFactorUnit":
            return self._parent

        def __getattr__(self: "SafetyFactorUnit._Cast_SafetyFactorUnit", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SafetyFactorUnit.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SafetyFactorUnit._Cast_SafetyFactorUnit":
        return self._Cast_SafetyFactorUnit(self)
