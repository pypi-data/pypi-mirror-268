"""BallISO2812007Results"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2110
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BALL_ISO2812007_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults",
    "BallISO2812007Results",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2112


__docformat__ = "restructuredtext en"
__all__ = ("BallISO2812007Results",)


Self = TypeVar("Self", bound="BallISO2812007Results")


class BallISO2812007Results(_2110.ISO2812007Results):
    """BallISO2812007Results

    This is a mastapy class.
    """

    TYPE = _BALL_ISO2812007_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BallISO2812007Results")

    class _Cast_BallISO2812007Results:
        """Special nested class for casting BallISO2812007Results to subclasses."""

        def __init__(
            self: "BallISO2812007Results._Cast_BallISO2812007Results",
            parent: "BallISO2812007Results",
        ):
            self._parent = parent

        @property
        def iso2812007_results(
            self: "BallISO2812007Results._Cast_BallISO2812007Results",
        ) -> "_2110.ISO2812007Results":
            return self._parent._cast(_2110.ISO2812007Results)

        @property
        def iso_results(
            self: "BallISO2812007Results._Cast_BallISO2812007Results",
        ) -> "_2112.ISOResults":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2112,
            )

            return self._parent._cast(_2112.ISOResults)

        @property
        def ball_iso2812007_results(
            self: "BallISO2812007Results._Cast_BallISO2812007Results",
        ) -> "BallISO2812007Results":
            return self._parent

        def __getattr__(
            self: "BallISO2812007Results._Cast_BallISO2812007Results", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BallISO2812007Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BallISO2812007Results._Cast_BallISO2812007Results":
        return self._Cast_BallISO2812007Results(self)
