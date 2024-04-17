"""AbstractForceAndDisplacementResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_FORCE_AND_DISPLACEMENT_RESULTS = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredVectors", "AbstractForceAndDisplacementResults"
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_vectors import _1571, _1567, _1568


__docformat__ = "restructuredtext en"
__all__ = ("AbstractForceAndDisplacementResults",)


Self = TypeVar("Self", bound="AbstractForceAndDisplacementResults")


class AbstractForceAndDisplacementResults(_0.APIBase):
    """AbstractForceAndDisplacementResults

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_FORCE_AND_DISPLACEMENT_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractForceAndDisplacementResults")

    class _Cast_AbstractForceAndDisplacementResults:
        """Special nested class for casting AbstractForceAndDisplacementResults to subclasses."""

        def __init__(
            self: "AbstractForceAndDisplacementResults._Cast_AbstractForceAndDisplacementResults",
            parent: "AbstractForceAndDisplacementResults",
        ):
            self._parent = parent

        @property
        def force_and_displacement_results(
            self: "AbstractForceAndDisplacementResults._Cast_AbstractForceAndDisplacementResults",
        ) -> "_1567.ForceAndDisplacementResults":
            from mastapy.math_utility.measured_vectors import _1567

            return self._parent._cast(_1567.ForceAndDisplacementResults)

        @property
        def force_results(
            self: "AbstractForceAndDisplacementResults._Cast_AbstractForceAndDisplacementResults",
        ) -> "_1568.ForceResults":
            from mastapy.math_utility.measured_vectors import _1568

            return self._parent._cast(_1568.ForceResults)

        @property
        def abstract_force_and_displacement_results(
            self: "AbstractForceAndDisplacementResults._Cast_AbstractForceAndDisplacementResults",
        ) -> "AbstractForceAndDisplacementResults":
            return self._parent

        def __getattr__(
            self: "AbstractForceAndDisplacementResults._Cast_AbstractForceAndDisplacementResults",
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
        self: Self, instance_to_wrap: "AbstractForceAndDisplacementResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Node

        if temp is None:
            return ""

        return temp

    @property
    def force(self: Self) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Force

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def location(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Location

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "AbstractForceAndDisplacementResults._Cast_AbstractForceAndDisplacementResults"
    ):
        return self._Cast_AbstractForceAndDisplacementResults(self)
