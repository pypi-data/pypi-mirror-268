"""BallBearingRaceContactGeometry"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal import conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BALL_BEARING_RACE_CONTACT_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "BallBearingRaceContactGeometry"
)


__docformat__ = "restructuredtext en"
__all__ = ("BallBearingRaceContactGeometry",)


Self = TypeVar("Self", bound="BallBearingRaceContactGeometry")


class BallBearingRaceContactGeometry(_0.APIBase):
    """BallBearingRaceContactGeometry

    This is a mastapy class.
    """

    TYPE = _BALL_BEARING_RACE_CONTACT_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BallBearingRaceContactGeometry")

    class _Cast_BallBearingRaceContactGeometry:
        """Special nested class for casting BallBearingRaceContactGeometry to subclasses."""

        def __init__(
            self: "BallBearingRaceContactGeometry._Cast_BallBearingRaceContactGeometry",
            parent: "BallBearingRaceContactGeometry",
        ):
            self._parent = parent

        @property
        def ball_bearing_race_contact_geometry(
            self: "BallBearingRaceContactGeometry._Cast_BallBearingRaceContactGeometry",
        ) -> "BallBearingRaceContactGeometry":
            return self._parent

        def __getattr__(
            self: "BallBearingRaceContactGeometry._Cast_BallBearingRaceContactGeometry",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BallBearingRaceContactGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ball_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BallDiameter

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
    def race_groove_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceGrooveRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def ball_centre(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BallCentre

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def race_centre(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceCentre

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BallBearingRaceContactGeometry._Cast_BallBearingRaceContactGeometry":
        return self._Cast_BallBearingRaceContactGeometry(self)
