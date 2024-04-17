"""LoadedAngularContactThrustBallBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _1989
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAngularContactThrustBallBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2007, _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAngularContactThrustBallBearingElement",)


Self = TypeVar("Self", bound="LoadedAngularContactThrustBallBearingElement")


class LoadedAngularContactThrustBallBearingElement(
    _1989.LoadedAngularContactBallBearingElement
):
    """LoadedAngularContactThrustBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAngularContactThrustBallBearingElement"
    )

    class _Cast_LoadedAngularContactThrustBallBearingElement:
        """Special nested class for casting LoadedAngularContactThrustBallBearingElement to subclasses."""

        def __init__(
            self: "LoadedAngularContactThrustBallBearingElement._Cast_LoadedAngularContactThrustBallBearingElement",
            parent: "LoadedAngularContactThrustBallBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_element(
            self: "LoadedAngularContactThrustBallBearingElement._Cast_LoadedAngularContactThrustBallBearingElement",
        ) -> "_1989.LoadedAngularContactBallBearingElement":
            return self._parent._cast(_1989.LoadedAngularContactBallBearingElement)

        @property
        def loaded_ball_bearing_element(
            self: "LoadedAngularContactThrustBallBearingElement._Cast_LoadedAngularContactThrustBallBearingElement",
        ) -> "_2007.LoadedBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(_2007.LoadedBallBearingElement)

        @property
        def loaded_element(
            self: "LoadedAngularContactThrustBallBearingElement._Cast_LoadedAngularContactThrustBallBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_angular_contact_thrust_ball_bearing_element(
            self: "LoadedAngularContactThrustBallBearingElement._Cast_LoadedAngularContactThrustBallBearingElement",
        ) -> "LoadedAngularContactThrustBallBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedAngularContactThrustBallBearingElement._Cast_LoadedAngularContactThrustBallBearingElement",
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
        self: Self,
        instance_to_wrap: "LoadedAngularContactThrustBallBearingElement.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAngularContactThrustBallBearingElement._Cast_LoadedAngularContactThrustBallBearingElement":
        return self._Cast_LoadedAngularContactThrustBallBearingElement(self)
