"""BearingConnectionComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_CONNECTION_COMPONENT = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "BearingConnectionComponent"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import (
        _1913,
        _1914,
        _1915,
        _1916,
        _1918,
        _1919,
        _1920,
        _1921,
        _1924,
        _1927,
        _1929,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BearingConnectionComponent",)


Self = TypeVar("Self", bound="BearingConnectionComponent")


class BearingConnectionComponent(_0.APIBase):
    """BearingConnectionComponent

    This is a mastapy class.
    """

    TYPE = _BEARING_CONNECTION_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingConnectionComponent")

    class _Cast_BearingConnectionComponent:
        """Special nested class for casting BearingConnectionComponent to subclasses."""

        def __init__(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
            parent: "BearingConnectionComponent",
        ):
            self._parent = parent

        @property
        def inner_ring_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1913.InnerRingTolerance":
            from mastapy.bearings.tolerances import _1913

            return self._parent._cast(_1913.InnerRingTolerance)

        @property
        def inner_support_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1914.InnerSupportTolerance":
            from mastapy.bearings.tolerances import _1914

            return self._parent._cast(_1914.InnerSupportTolerance)

        @property
        def interference_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1915.InterferenceDetail":
            from mastapy.bearings.tolerances import _1915

            return self._parent._cast(_1915.InterferenceDetail)

        @property
        def interference_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1916.InterferenceTolerance":
            from mastapy.bearings.tolerances import _1916

            return self._parent._cast(_1916.InterferenceTolerance)

        @property
        def mounting_sleeve_diameter_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1918.MountingSleeveDiameterDetail":
            from mastapy.bearings.tolerances import _1918

            return self._parent._cast(_1918.MountingSleeveDiameterDetail)

        @property
        def outer_ring_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1919.OuterRingTolerance":
            from mastapy.bearings.tolerances import _1919

            return self._parent._cast(_1919.OuterRingTolerance)

        @property
        def outer_support_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1920.OuterSupportTolerance":
            from mastapy.bearings.tolerances import _1920

            return self._parent._cast(_1920.OuterSupportTolerance)

        @property
        def race_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1921.RaceDetail":
            from mastapy.bearings.tolerances import _1921

            return self._parent._cast(_1921.RaceDetail)

        @property
        def ring_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1924.RingTolerance":
            from mastapy.bearings.tolerances import _1924

            return self._parent._cast(_1924.RingTolerance)

        @property
        def support_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1927.SupportDetail":
            from mastapy.bearings.tolerances import _1927

            return self._parent._cast(_1927.SupportDetail)

        @property
        def support_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "_1929.SupportTolerance":
            from mastapy.bearings.tolerances import _1929

            return self._parent._cast(_1929.SupportTolerance)

        @property
        def bearing_connection_component(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "BearingConnectionComponent":
            return self._parent

        def __getattr__(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingConnectionComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BearingConnectionComponent._Cast_BearingConnectionComponent":
        return self._Cast_BearingConnectionComponent(self)
