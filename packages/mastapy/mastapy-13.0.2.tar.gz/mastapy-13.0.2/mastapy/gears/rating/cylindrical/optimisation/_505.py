"""OptimisationResultsPair"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMISATION_RESULTS_PAIR = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation", "OptimisationResultsPair"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.optimisation import _506, _507


__docformat__ = "restructuredtext en"
__all__ = ("OptimisationResultsPair",)


Self = TypeVar("Self", bound="OptimisationResultsPair")
T = TypeVar("T", bound="_507.SafetyFactorOptimisationStepResult")


class OptimisationResultsPair(_0.APIBase, Generic[T]):
    """OptimisationResultsPair

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _OPTIMISATION_RESULTS_PAIR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OptimisationResultsPair")

    class _Cast_OptimisationResultsPair:
        """Special nested class for casting OptimisationResultsPair to subclasses."""

        def __init__(
            self: "OptimisationResultsPair._Cast_OptimisationResultsPair",
            parent: "OptimisationResultsPair",
        ):
            self._parent = parent

        @property
        def optimisation_results_pair(
            self: "OptimisationResultsPair._Cast_OptimisationResultsPair",
        ) -> "OptimisationResultsPair":
            return self._parent

        def __getattr__(
            self: "OptimisationResultsPair._Cast_OptimisationResultsPair", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OptimisationResultsPair.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def results(self: Self) -> "_506.SafetyFactorOptimisationResults[T]":
        """mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationResults[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp)

    @property
    def results_without_warnings(
        self: Self,
    ) -> "_506.SafetyFactorOptimisationResults[T]":
        """mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationResults[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsWithoutWarnings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp)

    @property
    def cast_to(self: Self) -> "OptimisationResultsPair._Cast_OptimisationResultsPair":
        return self._Cast_OptimisationResultsPair(self)
