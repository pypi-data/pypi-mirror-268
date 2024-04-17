"""BallISOTS162812008Results"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2113
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BALL_ISOTS162812008_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults",
    "BallISOTS162812008Results",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2112


__docformat__ = "restructuredtext en"
__all__ = ("BallISOTS162812008Results",)


Self = TypeVar("Self", bound="BallISOTS162812008Results")


class BallISOTS162812008Results(_2113.ISOTS162812008Results):
    """BallISOTS162812008Results

    This is a mastapy class.
    """

    TYPE = _BALL_ISOTS162812008_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BallISOTS162812008Results")

    class _Cast_BallISOTS162812008Results:
        """Special nested class for casting BallISOTS162812008Results to subclasses."""

        def __init__(
            self: "BallISOTS162812008Results._Cast_BallISOTS162812008Results",
            parent: "BallISOTS162812008Results",
        ):
            self._parent = parent

        @property
        def isots162812008_results(
            self: "BallISOTS162812008Results._Cast_BallISOTS162812008Results",
        ) -> "_2113.ISOTS162812008Results":
            return self._parent._cast(_2113.ISOTS162812008Results)

        @property
        def iso_results(
            self: "BallISOTS162812008Results._Cast_BallISOTS162812008Results",
        ) -> "_2112.ISOResults":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2112,
            )

            return self._parent._cast(_2112.ISOResults)

        @property
        def ball_isots162812008_results(
            self: "BallISOTS162812008Results._Cast_BallISOTS162812008Results",
        ) -> "BallISOTS162812008Results":
            return self._parent

        def __getattr__(
            self: "BallISOTS162812008Results._Cast_BallISOTS162812008Results", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BallISOTS162812008Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_stiffness_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStiffnessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stiffness_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStiffnessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "BallISOTS162812008Results._Cast_BallISOTS162812008Results":
        return self._Cast_BallISOTS162812008Results(self)
