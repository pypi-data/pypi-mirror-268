"""ForceResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility.measured_vectors import _1566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_RESULTS = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredVectors", "ForceResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("ForceResults",)


Self = TypeVar("Self", bound="ForceResults")


class ForceResults(_1566.AbstractForceAndDisplacementResults):
    """ForceResults

    This is a mastapy class.
    """

    TYPE = _FORCE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ForceResults")

    class _Cast_ForceResults:
        """Special nested class for casting ForceResults to subclasses."""

        def __init__(self: "ForceResults._Cast_ForceResults", parent: "ForceResults"):
            self._parent = parent

        @property
        def abstract_force_and_displacement_results(
            self: "ForceResults._Cast_ForceResults",
        ) -> "_1566.AbstractForceAndDisplacementResults":
            return self._parent._cast(_1566.AbstractForceAndDisplacementResults)

        @property
        def force_results(self: "ForceResults._Cast_ForceResults") -> "ForceResults":
            return self._parent

        def __getattr__(self: "ForceResults._Cast_ForceResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ForceResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ForceResults._Cast_ForceResults":
        return self._Cast_ForceResults(self)
