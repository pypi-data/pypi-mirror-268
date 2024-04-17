"""Grease"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GREASE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "Grease"
)


__docformat__ = "restructuredtext en"
__all__ = ("Grease",)


Self = TypeVar("Self", bound="Grease")


class Grease(_2103.SKFCalculationResult):
    """Grease

    This is a mastapy class.
    """

    TYPE = _GREASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Grease")

    class _Cast_Grease:
        """Special nested class for casting Grease to subclasses."""

        def __init__(self: "Grease._Cast_Grease", parent: "Grease"):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "Grease._Cast_Grease",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def grease(self: "Grease._Cast_Grease") -> "Grease":
            return self._parent

        def __getattr__(self: "Grease._Cast_Grease", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Grease.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def grease_life(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GreaseLife

        if temp is None:
            return 0.0

        return temp

    @property
    def relubrication_interval(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelubricationInterval

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "Grease._Cast_Grease":
        return self._Cast_Grease(self)
