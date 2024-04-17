"""MountingSleeveDiameterDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.tolerances import _1915
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTING_SLEEVE_DIAMETER_DETAIL = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "MountingSleeveDiameterDetail"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1908


__docformat__ = "restructuredtext en"
__all__ = ("MountingSleeveDiameterDetail",)


Self = TypeVar("Self", bound="MountingSleeveDiameterDetail")


class MountingSleeveDiameterDetail(_1915.InterferenceDetail):
    """MountingSleeveDiameterDetail

    This is a mastapy class.
    """

    TYPE = _MOUNTING_SLEEVE_DIAMETER_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountingSleeveDiameterDetail")

    class _Cast_MountingSleeveDiameterDetail:
        """Special nested class for casting MountingSleeveDiameterDetail to subclasses."""

        def __init__(
            self: "MountingSleeveDiameterDetail._Cast_MountingSleeveDiameterDetail",
            parent: "MountingSleeveDiameterDetail",
        ):
            self._parent = parent

        @property
        def interference_detail(
            self: "MountingSleeveDiameterDetail._Cast_MountingSleeveDiameterDetail",
        ) -> "_1915.InterferenceDetail":
            return self._parent._cast(_1915.InterferenceDetail)

        @property
        def bearing_connection_component(
            self: "MountingSleeveDiameterDetail._Cast_MountingSleeveDiameterDetail",
        ) -> "_1908.BearingConnectionComponent":
            from mastapy.bearings.tolerances import _1908

            return self._parent._cast(_1908.BearingConnectionComponent)

        @property
        def mounting_sleeve_diameter_detail(
            self: "MountingSleeveDiameterDetail._Cast_MountingSleeveDiameterDetail",
        ) -> "MountingSleeveDiameterDetail":
            return self._parent

        def __getattr__(
            self: "MountingSleeveDiameterDetail._Cast_MountingSleeveDiameterDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountingSleeveDiameterDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MountingSleeveDiameterDetail._Cast_MountingSleeveDiameterDetail":
        return self._Cast_MountingSleeveDiameterDetail(self)
