"""LoadedThreePointContactBallBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2026
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_THREE_POINT_CONTACT_BALL_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedThreePointContactBallBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2007, _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedThreePointContactBallBearingElement",)


Self = TypeVar("Self", bound="LoadedThreePointContactBallBearingElement")


class LoadedThreePointContactBallBearingElement(
    _2026.LoadedMultiPointContactBallBearingElement
):
    """LoadedThreePointContactBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_THREE_POINT_CONTACT_BALL_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedThreePointContactBallBearingElement"
    )

    class _Cast_LoadedThreePointContactBallBearingElement:
        """Special nested class for casting LoadedThreePointContactBallBearingElement to subclasses."""

        def __init__(
            self: "LoadedThreePointContactBallBearingElement._Cast_LoadedThreePointContactBallBearingElement",
            parent: "LoadedThreePointContactBallBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_multi_point_contact_ball_bearing_element(
            self: "LoadedThreePointContactBallBearingElement._Cast_LoadedThreePointContactBallBearingElement",
        ) -> "_2026.LoadedMultiPointContactBallBearingElement":
            return self._parent._cast(_2026.LoadedMultiPointContactBallBearingElement)

        @property
        def loaded_ball_bearing_element(
            self: "LoadedThreePointContactBallBearingElement._Cast_LoadedThreePointContactBallBearingElement",
        ) -> "_2007.LoadedBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(_2007.LoadedBallBearingElement)

        @property
        def loaded_element(
            self: "LoadedThreePointContactBallBearingElement._Cast_LoadedThreePointContactBallBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_three_point_contact_ball_bearing_element(
            self: "LoadedThreePointContactBallBearingElement._Cast_LoadedThreePointContactBallBearingElement",
        ) -> "LoadedThreePointContactBallBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedThreePointContactBallBearingElement._Cast_LoadedThreePointContactBallBearingElement",
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
        self: Self, instance_to_wrap: "LoadedThreePointContactBallBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedThreePointContactBallBearingElement._Cast_LoadedThreePointContactBallBearingElement":
        return self._Cast_LoadedThreePointContactBallBearingElement(self)
