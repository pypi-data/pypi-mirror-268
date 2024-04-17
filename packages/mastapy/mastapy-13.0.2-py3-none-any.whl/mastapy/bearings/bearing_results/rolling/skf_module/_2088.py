"""Frequencies"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FREQUENCIES = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "Frequencies"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import _2089, _2101


__docformat__ = "restructuredtext en"
__all__ = ("Frequencies",)


Self = TypeVar("Self", bound="Frequencies")


class Frequencies(_2103.SKFCalculationResult):
    """Frequencies

    This is a mastapy class.
    """

    TYPE = _FREQUENCIES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Frequencies")

    class _Cast_Frequencies:
        """Special nested class for casting Frequencies to subclasses."""

        def __init__(self: "Frequencies._Cast_Frequencies", parent: "Frequencies"):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "Frequencies._Cast_Frequencies",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def frequencies(self: "Frequencies._Cast_Frequencies") -> "Frequencies":
            return self._parent

        def __getattr__(self: "Frequencies._Cast_Frequencies", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Frequencies.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequency_of_over_rolling(self: Self) -> "_2089.FrequencyOfOverRolling":
        """mastapy.bearings.bearing_results.rolling.skf_module.FrequencyOfOverRolling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOfOverRolling

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rotational_frequency(self: Self) -> "_2101.RotationalFrequency":
        """mastapy.bearings.bearing_results.rolling.skf_module.RotationalFrequency

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotationalFrequency

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Frequencies._Cast_Frequencies":
        return self._Cast_Frequencies(self)
