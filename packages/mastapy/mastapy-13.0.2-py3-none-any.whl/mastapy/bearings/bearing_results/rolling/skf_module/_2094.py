"""GreaseLifeAndRelubricationInterval"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GREASE_LIFE_AND_RELUBRICATION_INTERVAL = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule",
    "GreaseLifeAndRelubricationInterval",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import _2093, _2095, _2096


__docformat__ = "restructuredtext en"
__all__ = ("GreaseLifeAndRelubricationInterval",)


Self = TypeVar("Self", bound="GreaseLifeAndRelubricationInterval")


class GreaseLifeAndRelubricationInterval(_2103.SKFCalculationResult):
    """GreaseLifeAndRelubricationInterval

    This is a mastapy class.
    """

    TYPE = _GREASE_LIFE_AND_RELUBRICATION_INTERVAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GreaseLifeAndRelubricationInterval")

    class _Cast_GreaseLifeAndRelubricationInterval:
        """Special nested class for casting GreaseLifeAndRelubricationInterval to subclasses."""

        def __init__(
            self: "GreaseLifeAndRelubricationInterval._Cast_GreaseLifeAndRelubricationInterval",
            parent: "GreaseLifeAndRelubricationInterval",
        ):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "GreaseLifeAndRelubricationInterval._Cast_GreaseLifeAndRelubricationInterval",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def grease_life_and_relubrication_interval(
            self: "GreaseLifeAndRelubricationInterval._Cast_GreaseLifeAndRelubricationInterval",
        ) -> "GreaseLifeAndRelubricationInterval":
            return self._parent

        def __getattr__(
            self: "GreaseLifeAndRelubricationInterval._Cast_GreaseLifeAndRelubricationInterval",
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
        self: Self, instance_to_wrap: "GreaseLifeAndRelubricationInterval.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def grease(self: Self) -> "_2093.Grease":
        """mastapy.bearings.bearing_results.rolling.skf_module.Grease

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Grease

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def grease_quantity(self: Self) -> "_2095.GreaseQuantity":
        """mastapy.bearings.bearing_results.rolling.skf_module.GreaseQuantity

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GreaseQuantity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def initial_fill(self: Self) -> "_2096.InitialFill":
        """mastapy.bearings.bearing_results.rolling.skf_module.InitialFill

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InitialFill

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GreaseLifeAndRelubricationInterval._Cast_GreaseLifeAndRelubricationInterval":
        return self._Cast_GreaseLifeAndRelubricationInterval(self)
