"""RollerISOTS162812008Results"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2113
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_ISOTS162812008_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults",
    "RollerISOTS162812008Results",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2112


__docformat__ = "restructuredtext en"
__all__ = ("RollerISOTS162812008Results",)


Self = TypeVar("Self", bound="RollerISOTS162812008Results")


class RollerISOTS162812008Results(_2113.ISOTS162812008Results):
    """RollerISOTS162812008Results

    This is a mastapy class.
    """

    TYPE = _ROLLER_ISOTS162812008_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerISOTS162812008Results")

    class _Cast_RollerISOTS162812008Results:
        """Special nested class for casting RollerISOTS162812008Results to subclasses."""

        def __init__(
            self: "RollerISOTS162812008Results._Cast_RollerISOTS162812008Results",
            parent: "RollerISOTS162812008Results",
        ):
            self._parent = parent

        @property
        def isots162812008_results(
            self: "RollerISOTS162812008Results._Cast_RollerISOTS162812008Results",
        ) -> "_2113.ISOTS162812008Results":
            return self._parent._cast(_2113.ISOTS162812008Results)

        @property
        def iso_results(
            self: "RollerISOTS162812008Results._Cast_RollerISOTS162812008Results",
        ) -> "_2112.ISOResults":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2112,
            )

            return self._parent._cast(_2112.ISOResults)

        @property
        def roller_isots162812008_results(
            self: "RollerISOTS162812008Results._Cast_RollerISOTS162812008Results",
        ) -> "RollerISOTS162812008Results":
            return self._parent

        def __getattr__(
            self: "RollerISOTS162812008Results._Cast_RollerISOTS162812008Results",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerISOTS162812008Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_dynamic_load_rating_of_a_bearing_lamina_of_the_inner_ring(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicDynamicLoadRatingOfABearingLaminaOfTheInnerRing

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_dynamic_load_rating_of_a_bearing_lamina_of_the_outer_ring(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicDynamicLoadRatingOfABearingLaminaOfTheOuterRing

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_load_assuming_line_contacts(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentLoadAssumingLineContacts

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "RollerISOTS162812008Results._Cast_RollerISOTS162812008Results":
        return self._Cast_RollerISOTS162812008Results(self)
