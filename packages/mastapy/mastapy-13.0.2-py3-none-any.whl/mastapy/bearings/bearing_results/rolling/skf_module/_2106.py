"""StaticSafetyFactors"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATIC_SAFETY_FACTORS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "StaticSafetyFactors"
)


__docformat__ = "restructuredtext en"
__all__ = ("StaticSafetyFactors",)


Self = TypeVar("Self", bound="StaticSafetyFactors")


class StaticSafetyFactors(_2103.SKFCalculationResult):
    """StaticSafetyFactors

    This is a mastapy class.
    """

    TYPE = _STATIC_SAFETY_FACTORS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StaticSafetyFactors")

    class _Cast_StaticSafetyFactors:
        """Special nested class for casting StaticSafetyFactors to subclasses."""

        def __init__(
            self: "StaticSafetyFactors._Cast_StaticSafetyFactors",
            parent: "StaticSafetyFactors",
        ):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "StaticSafetyFactors._Cast_StaticSafetyFactors",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def static_safety_factors(
            self: "StaticSafetyFactors._Cast_StaticSafetyFactors",
        ) -> "StaticSafetyFactors":
            return self._parent

        def __getattr__(
            self: "StaticSafetyFactors._Cast_StaticSafetyFactors", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StaticSafetyFactors.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equivalent_static_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentStaticLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def static_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "StaticSafetyFactors._Cast_StaticSafetyFactors":
        return self._Cast_StaticSafetyFactors(self)
