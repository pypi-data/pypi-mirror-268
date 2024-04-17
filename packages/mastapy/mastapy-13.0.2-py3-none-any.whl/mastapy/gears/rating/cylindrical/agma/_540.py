"""ThermalReductionFactorFactorsAndExponents"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THERMAL_REDUCTION_FACTOR_FACTORS_AND_EXPONENTS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.AGMA",
    "ThermalReductionFactorFactorsAndExponents",
)


__docformat__ = "restructuredtext en"
__all__ = ("ThermalReductionFactorFactorsAndExponents",)


Self = TypeVar("Self", bound="ThermalReductionFactorFactorsAndExponents")


class ThermalReductionFactorFactorsAndExponents(_0.APIBase):
    """ThermalReductionFactorFactorsAndExponents

    This is a mastapy class.
    """

    TYPE = _THERMAL_REDUCTION_FACTOR_FACTORS_AND_EXPONENTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ThermalReductionFactorFactorsAndExponents"
    )

    class _Cast_ThermalReductionFactorFactorsAndExponents:
        """Special nested class for casting ThermalReductionFactorFactorsAndExponents to subclasses."""

        def __init__(
            self: "ThermalReductionFactorFactorsAndExponents._Cast_ThermalReductionFactorFactorsAndExponents",
            parent: "ThermalReductionFactorFactorsAndExponents",
        ):
            self._parent = parent

        @property
        def thermal_reduction_factor_factors_and_exponents(
            self: "ThermalReductionFactorFactorsAndExponents._Cast_ThermalReductionFactorFactorsAndExponents",
        ) -> "ThermalReductionFactorFactorsAndExponents":
            return self._parent

        def __getattr__(
            self: "ThermalReductionFactorFactorsAndExponents._Cast_ThermalReductionFactorFactorsAndExponents",
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
        self: Self, instance_to_wrap: "ThermalReductionFactorFactorsAndExponents.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def first_exponent(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FirstExponent

        if temp is None:
            return 0.0

        return temp

    @property
    def first_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FirstFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def second_exponent(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SecondExponent

        if temp is None:
            return 0.0

        return temp

    @property
    def second_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SecondFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ThermalReductionFactorFactorsAndExponents._Cast_ThermalReductionFactorFactorsAndExponents":
        return self._Cast_ThermalReductionFactorFactorsAndExponents(self)
