"""InnerRingTolerance"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.tolerances import _1924
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_RING_TOLERANCE = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "InnerRingTolerance"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1916, _1908


__docformat__ = "restructuredtext en"
__all__ = ("InnerRingTolerance",)


Self = TypeVar("Self", bound="InnerRingTolerance")


class InnerRingTolerance(_1924.RingTolerance):
    """InnerRingTolerance

    This is a mastapy class.
    """

    TYPE = _INNER_RING_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InnerRingTolerance")

    class _Cast_InnerRingTolerance:
        """Special nested class for casting InnerRingTolerance to subclasses."""

        def __init__(
            self: "InnerRingTolerance._Cast_InnerRingTolerance",
            parent: "InnerRingTolerance",
        ):
            self._parent = parent

        @property
        def ring_tolerance(
            self: "InnerRingTolerance._Cast_InnerRingTolerance",
        ) -> "_1924.RingTolerance":
            return self._parent._cast(_1924.RingTolerance)

        @property
        def interference_tolerance(
            self: "InnerRingTolerance._Cast_InnerRingTolerance",
        ) -> "_1916.InterferenceTolerance":
            from mastapy.bearings.tolerances import _1916

            return self._parent._cast(_1916.InterferenceTolerance)

        @property
        def bearing_connection_component(
            self: "InnerRingTolerance._Cast_InnerRingTolerance",
        ) -> "_1908.BearingConnectionComponent":
            from mastapy.bearings.tolerances import _1908

            return self._parent._cast(_1908.BearingConnectionComponent)

        @property
        def inner_ring_tolerance(
            self: "InnerRingTolerance._Cast_InnerRingTolerance",
        ) -> "InnerRingTolerance":
            return self._parent

        def __getattr__(self: "InnerRingTolerance._Cast_InnerRingTolerance", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InnerRingTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InnerRingTolerance._Cast_InnerRingTolerance":
        return self._Cast_InnerRingTolerance(self)
