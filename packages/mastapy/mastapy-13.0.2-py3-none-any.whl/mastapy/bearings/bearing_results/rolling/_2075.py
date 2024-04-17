"""RingForceAndDisplacement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_FORCE_AND_DISPLACEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "RingForceAndDisplacement"
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_vectors import _1571


__docformat__ = "restructuredtext en"
__all__ = ("RingForceAndDisplacement",)


Self = TypeVar("Self", bound="RingForceAndDisplacement")


class RingForceAndDisplacement(_0.APIBase):
    """RingForceAndDisplacement

    This is a mastapy class.
    """

    TYPE = _RING_FORCE_AND_DISPLACEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingForceAndDisplacement")

    class _Cast_RingForceAndDisplacement:
        """Special nested class for casting RingForceAndDisplacement to subclasses."""

        def __init__(
            self: "RingForceAndDisplacement._Cast_RingForceAndDisplacement",
            parent: "RingForceAndDisplacement",
        ):
            self._parent = parent

        @property
        def ring_force_and_displacement(
            self: "RingForceAndDisplacement._Cast_RingForceAndDisplacement",
        ) -> "RingForceAndDisplacement":
            return self._parent

        def __getattr__(
            self: "RingForceAndDisplacement._Cast_RingForceAndDisplacement", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingForceAndDisplacement.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude_of_misalignment_normal_to_load_direction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagnitudeOfMisalignmentNormalToLoadDirection

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

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
    def cast_to(
        self: Self,
    ) -> "RingForceAndDisplacement._Cast_RingForceAndDisplacement":
        return self._Cast_RingForceAndDisplacement(self)
