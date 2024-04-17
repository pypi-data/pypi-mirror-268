"""ISOTR1417922001Results"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _1986
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISOTR1417922001_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "ISOTR1417922001Results"
)


__docformat__ = "restructuredtext en"
__all__ = ("ISOTR1417922001Results",)


Self = TypeVar("Self", bound="ISOTR1417922001Results")


class ISOTR1417922001Results(_1986.ISOTR141792001Results):
    """ISOTR1417922001Results

    This is a mastapy class.
    """

    TYPE = _ISOTR1417922001_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISOTR1417922001Results")

    class _Cast_ISOTR1417922001Results:
        """Special nested class for casting ISOTR1417922001Results to subclasses."""

        def __init__(
            self: "ISOTR1417922001Results._Cast_ISOTR1417922001Results",
            parent: "ISOTR1417922001Results",
        ):
            self._parent = parent

        @property
        def isotr141792001_results(
            self: "ISOTR1417922001Results._Cast_ISOTR1417922001Results",
        ) -> "_1986.ISOTR141792001Results":
            return self._parent._cast(_1986.ISOTR141792001Results)

        @property
        def isotr1417922001_results(
            self: "ISOTR1417922001Results._Cast_ISOTR1417922001Results",
        ) -> "ISOTR1417922001Results":
            return self._parent

        def __getattr__(
            self: "ISOTR1417922001Results._Cast_ISOTR1417922001Results", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISOTR1417922001Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_for_no_load_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientForNoLoadPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ISOTR1417922001Results._Cast_ISOTR1417922001Results":
        return self._Cast_ISOTR1417922001Results(self)
