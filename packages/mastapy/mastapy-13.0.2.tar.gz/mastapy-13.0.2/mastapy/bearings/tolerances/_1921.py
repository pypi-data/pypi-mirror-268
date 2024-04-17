"""RaceDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.tolerances import _1915
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACE_DETAIL = python_net_import("SMT.MastaAPI.Bearings.Tolerances", "RaceDetail")

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1908


__docformat__ = "restructuredtext en"
__all__ = ("RaceDetail",)


Self = TypeVar("Self", bound="RaceDetail")


class RaceDetail(_1915.InterferenceDetail):
    """RaceDetail

    This is a mastapy class.
    """

    TYPE = _RACE_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RaceDetail")

    class _Cast_RaceDetail:
        """Special nested class for casting RaceDetail to subclasses."""

        def __init__(self: "RaceDetail._Cast_RaceDetail", parent: "RaceDetail"):
            self._parent = parent

        @property
        def interference_detail(
            self: "RaceDetail._Cast_RaceDetail",
        ) -> "_1915.InterferenceDetail":
            return self._parent._cast(_1915.InterferenceDetail)

        @property
        def bearing_connection_component(
            self: "RaceDetail._Cast_RaceDetail",
        ) -> "_1908.BearingConnectionComponent":
            from mastapy.bearings.tolerances import _1908

            return self._parent._cast(_1908.BearingConnectionComponent)

        @property
        def race_detail(self: "RaceDetail._Cast_RaceDetail") -> "RaceDetail":
            return self._parent

        def __getattr__(self: "RaceDetail._Cast_RaceDetail", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RaceDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RaceDetail._Cast_RaceDetail":
        return self._Cast_RaceDetail(self)
