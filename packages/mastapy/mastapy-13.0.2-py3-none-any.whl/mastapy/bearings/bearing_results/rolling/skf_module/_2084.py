"""AdjustmentFactors"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADJUSTMENT_FACTORS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "AdjustmentFactors"
)


__docformat__ = "restructuredtext en"
__all__ = ("AdjustmentFactors",)


Self = TypeVar("Self", bound="AdjustmentFactors")


class AdjustmentFactors(_0.APIBase):
    """AdjustmentFactors

    This is a mastapy class.
    """

    TYPE = _ADJUSTMENT_FACTORS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AdjustmentFactors")

    class _Cast_AdjustmentFactors:
        """Special nested class for casting AdjustmentFactors to subclasses."""

        def __init__(
            self: "AdjustmentFactors._Cast_AdjustmentFactors",
            parent: "AdjustmentFactors",
        ):
            self._parent = parent

        @property
        def adjustment_factors(
            self: "AdjustmentFactors._Cast_AdjustmentFactors",
        ) -> "AdjustmentFactors":
            return self._parent

        def __getattr__(self: "AdjustmentFactors._Cast_AdjustmentFactors", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AdjustmentFactors.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def for_bearing_load_p(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForBearingLoadP

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_viscosity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "AdjustmentFactors._Cast_AdjustmentFactors":
        return self._Cast_AdjustmentFactors(self)
