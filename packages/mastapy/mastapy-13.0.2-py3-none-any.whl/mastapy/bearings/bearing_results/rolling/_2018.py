"""LoadedDeepGrooveBallBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2007
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_DEEP_GROOVE_BALL_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedDeepGrooveBallBearingElement"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedDeepGrooveBallBearingElement",)


Self = TypeVar("Self", bound="LoadedDeepGrooveBallBearingElement")


class LoadedDeepGrooveBallBearingElement(_2007.LoadedBallBearingElement):
    """LoadedDeepGrooveBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_DEEP_GROOVE_BALL_BEARING_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedDeepGrooveBallBearingElement")

    class _Cast_LoadedDeepGrooveBallBearingElement:
        """Special nested class for casting LoadedDeepGrooveBallBearingElement to subclasses."""

        def __init__(
            self: "LoadedDeepGrooveBallBearingElement._Cast_LoadedDeepGrooveBallBearingElement",
            parent: "LoadedDeepGrooveBallBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_element(
            self: "LoadedDeepGrooveBallBearingElement._Cast_LoadedDeepGrooveBallBearingElement",
        ) -> "_2007.LoadedBallBearingElement":
            return self._parent._cast(_2007.LoadedBallBearingElement)

        @property
        def loaded_element(
            self: "LoadedDeepGrooveBallBearingElement._Cast_LoadedDeepGrooveBallBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_deep_groove_ball_bearing_element(
            self: "LoadedDeepGrooveBallBearingElement._Cast_LoadedDeepGrooveBallBearingElement",
        ) -> "LoadedDeepGrooveBallBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedDeepGrooveBallBearingElement._Cast_LoadedDeepGrooveBallBearingElement",
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
        self: Self, instance_to_wrap: "LoadedDeepGrooveBallBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedDeepGrooveBallBearingElement._Cast_LoadedDeepGrooveBallBearingElement":
        return self._Cast_LoadedDeepGrooveBallBearingElement(self)
