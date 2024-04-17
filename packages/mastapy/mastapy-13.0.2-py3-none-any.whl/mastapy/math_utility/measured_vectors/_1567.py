"""ForceAndDisplacementResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.math_utility.measured_vectors import _1566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_AND_DISPLACEMENT_RESULTS = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredVectors", "ForceAndDisplacementResults"
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_vectors import _1571


__docformat__ = "restructuredtext en"
__all__ = ("ForceAndDisplacementResults",)


Self = TypeVar("Self", bound="ForceAndDisplacementResults")


class ForceAndDisplacementResults(_1566.AbstractForceAndDisplacementResults):
    """ForceAndDisplacementResults

    This is a mastapy class.
    """

    TYPE = _FORCE_AND_DISPLACEMENT_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ForceAndDisplacementResults")

    class _Cast_ForceAndDisplacementResults:
        """Special nested class for casting ForceAndDisplacementResults to subclasses."""

        def __init__(
            self: "ForceAndDisplacementResults._Cast_ForceAndDisplacementResults",
            parent: "ForceAndDisplacementResults",
        ):
            self._parent = parent

        @property
        def abstract_force_and_displacement_results(
            self: "ForceAndDisplacementResults._Cast_ForceAndDisplacementResults",
        ) -> "_1566.AbstractForceAndDisplacementResults":
            return self._parent._cast(_1566.AbstractForceAndDisplacementResults)

        @property
        def force_and_displacement_results(
            self: "ForceAndDisplacementResults._Cast_ForceAndDisplacementResults",
        ) -> "ForceAndDisplacementResults":
            return self._parent

        def __getattr__(
            self: "ForceAndDisplacementResults._Cast_ForceAndDisplacementResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ForceAndDisplacementResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def displacement(self: Self) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Displacement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ForceAndDisplacementResults._Cast_ForceAndDisplacementResults":
        return self._Cast_ForceAndDisplacementResults(self)
