"""FEModalFrequencyComparison"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODAL_FREQUENCY_COMPARISON = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "FEModalFrequencyComparison"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEModalFrequencyComparison",)


Self = TypeVar("Self", bound="FEModalFrequencyComparison")


class FEModalFrequencyComparison(_0.APIBase):
    """FEModalFrequencyComparison

    This is a mastapy class.
    """

    TYPE = _FE_MODAL_FREQUENCY_COMPARISON
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEModalFrequencyComparison")

    class _Cast_FEModalFrequencyComparison:
        """Special nested class for casting FEModalFrequencyComparison to subclasses."""

        def __init__(
            self: "FEModalFrequencyComparison._Cast_FEModalFrequencyComparison",
            parent: "FEModalFrequencyComparison",
        ):
            self._parent = parent

        @property
        def fe_modal_frequency_comparison(
            self: "FEModalFrequencyComparison._Cast_FEModalFrequencyComparison",
        ) -> "FEModalFrequencyComparison":
            return self._parent

        def __getattr__(
            self: "FEModalFrequencyComparison._Cast_FEModalFrequencyComparison",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEModalFrequencyComparison.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def difference_in_frequencies(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DifferenceInFrequencies

        if temp is None:
            return 0.0

        return temp

    @property
    def full_model_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FullModelFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def mode(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mode

        if temp is None:
            return 0

        return temp

    @property
    def percentage_error(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageError

        if temp is None:
            return 0.0

        return temp

    @property
    def reduced_model_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReducedModelFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "FEModalFrequencyComparison._Cast_FEModalFrequencyComparison":
        return self._Cast_FEModalFrequencyComparison(self)
