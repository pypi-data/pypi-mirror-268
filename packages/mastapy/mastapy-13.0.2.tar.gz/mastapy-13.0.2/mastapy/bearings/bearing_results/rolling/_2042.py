"""LoadedSelfAligningBallBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2007
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SELF_ALIGNING_BALL_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSelfAligningBallBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSelfAligningBallBearingElement",)


Self = TypeVar("Self", bound="LoadedSelfAligningBallBearingElement")


class LoadedSelfAligningBallBearingElement(_2007.LoadedBallBearingElement):
    """LoadedSelfAligningBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_SELF_ALIGNING_BALL_BEARING_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedSelfAligningBallBearingElement")

    class _Cast_LoadedSelfAligningBallBearingElement:
        """Special nested class for casting LoadedSelfAligningBallBearingElement to subclasses."""

        def __init__(
            self: "LoadedSelfAligningBallBearingElement._Cast_LoadedSelfAligningBallBearingElement",
            parent: "LoadedSelfAligningBallBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_element(
            self: "LoadedSelfAligningBallBearingElement._Cast_LoadedSelfAligningBallBearingElement",
        ) -> "_2007.LoadedBallBearingElement":
            return self._parent._cast(_2007.LoadedBallBearingElement)

        @property
        def loaded_element(
            self: "LoadedSelfAligningBallBearingElement._Cast_LoadedSelfAligningBallBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_self_aligning_ball_bearing_element(
            self: "LoadedSelfAligningBallBearingElement._Cast_LoadedSelfAligningBallBearingElement",
        ) -> "LoadedSelfAligningBallBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedSelfAligningBallBearingElement._Cast_LoadedSelfAligningBallBearingElement",
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
        self: Self, instance_to_wrap: "LoadedSelfAligningBallBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedSelfAligningBallBearingElement._Cast_LoadedSelfAligningBallBearingElement":
        return self._Cast_LoadedSelfAligningBallBearingElement(self)
