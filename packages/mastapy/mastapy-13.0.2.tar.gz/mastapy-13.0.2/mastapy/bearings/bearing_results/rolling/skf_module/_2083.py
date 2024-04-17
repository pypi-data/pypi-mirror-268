"""AdjustedSpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADJUSTED_SPEED = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "AdjustedSpeed"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import _2084


__docformat__ = "restructuredtext en"
__all__ = ("AdjustedSpeed",)


Self = TypeVar("Self", bound="AdjustedSpeed")


class AdjustedSpeed(_2103.SKFCalculationResult):
    """AdjustedSpeed

    This is a mastapy class.
    """

    TYPE = _ADJUSTED_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AdjustedSpeed")

    class _Cast_AdjustedSpeed:
        """Special nested class for casting AdjustedSpeed to subclasses."""

        def __init__(
            self: "AdjustedSpeed._Cast_AdjustedSpeed", parent: "AdjustedSpeed"
        ):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "AdjustedSpeed._Cast_AdjustedSpeed",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def adjusted_speed(
            self: "AdjustedSpeed._Cast_AdjustedSpeed",
        ) -> "AdjustedSpeed":
            return self._parent

        def __getattr__(self: "AdjustedSpeed._Cast_AdjustedSpeed", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AdjustedSpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjusted_reference_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def adjustment_factors(self: Self) -> "_2084.AdjustmentFactors":
        """mastapy.bearings.bearing_results.rolling.skf_module.AdjustmentFactors

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustmentFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "AdjustedSpeed._Cast_AdjustedSpeed":
        return self._Cast_AdjustedSpeed(self)
