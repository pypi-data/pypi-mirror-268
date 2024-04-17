"""OuterSupportTolerance"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.tolerances import _1929
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_SUPPORT_TOLERANCE = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "OuterSupportTolerance"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1916, _1908


__docformat__ = "restructuredtext en"
__all__ = ("OuterSupportTolerance",)


Self = TypeVar("Self", bound="OuterSupportTolerance")


class OuterSupportTolerance(_1929.SupportTolerance):
    """OuterSupportTolerance

    This is a mastapy class.
    """

    TYPE = _OUTER_SUPPORT_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OuterSupportTolerance")

    class _Cast_OuterSupportTolerance:
        """Special nested class for casting OuterSupportTolerance to subclasses."""

        def __init__(
            self: "OuterSupportTolerance._Cast_OuterSupportTolerance",
            parent: "OuterSupportTolerance",
        ):
            self._parent = parent

        @property
        def support_tolerance(
            self: "OuterSupportTolerance._Cast_OuterSupportTolerance",
        ) -> "_1929.SupportTolerance":
            return self._parent._cast(_1929.SupportTolerance)

        @property
        def interference_tolerance(
            self: "OuterSupportTolerance._Cast_OuterSupportTolerance",
        ) -> "_1916.InterferenceTolerance":
            from mastapy.bearings.tolerances import _1916

            return self._parent._cast(_1916.InterferenceTolerance)

        @property
        def bearing_connection_component(
            self: "OuterSupportTolerance._Cast_OuterSupportTolerance",
        ) -> "_1908.BearingConnectionComponent":
            from mastapy.bearings.tolerances import _1908

            return self._parent._cast(_1908.BearingConnectionComponent)

        @property
        def outer_support_tolerance(
            self: "OuterSupportTolerance._Cast_OuterSupportTolerance",
        ) -> "OuterSupportTolerance":
            return self._parent

        def __getattr__(
            self: "OuterSupportTolerance._Cast_OuterSupportTolerance", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OuterSupportTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "OuterSupportTolerance._Cast_OuterSupportTolerance":
        return self._Cast_OuterSupportTolerance(self)
