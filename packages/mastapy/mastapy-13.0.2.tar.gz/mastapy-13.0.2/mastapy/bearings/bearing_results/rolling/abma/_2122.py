"""ANSIABMA112014Results"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling.abma import _2124
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANSIABMA112014_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.ABMA", "ANSIABMA112014Results"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2112


__docformat__ = "restructuredtext en"
__all__ = ("ANSIABMA112014Results",)


Self = TypeVar("Self", bound="ANSIABMA112014Results")


class ANSIABMA112014Results(_2124.ANSIABMAResults):
    """ANSIABMA112014Results

    This is a mastapy class.
    """

    TYPE = _ANSIABMA112014_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ANSIABMA112014Results")

    class _Cast_ANSIABMA112014Results:
        """Special nested class for casting ANSIABMA112014Results to subclasses."""

        def __init__(
            self: "ANSIABMA112014Results._Cast_ANSIABMA112014Results",
            parent: "ANSIABMA112014Results",
        ):
            self._parent = parent

        @property
        def ansiabma_results(
            self: "ANSIABMA112014Results._Cast_ANSIABMA112014Results",
        ) -> "_2124.ANSIABMAResults":
            return self._parent._cast(_2124.ANSIABMAResults)

        @property
        def iso_results(
            self: "ANSIABMA112014Results._Cast_ANSIABMA112014Results",
        ) -> "_2112.ISOResults":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2112,
            )

            return self._parent._cast(_2112.ISOResults)

        @property
        def ansiabma112014_results(
            self: "ANSIABMA112014Results._Cast_ANSIABMA112014Results",
        ) -> "ANSIABMA112014Results":
            return self._parent

        def __getattr__(
            self: "ANSIABMA112014Results._Cast_ANSIABMA112014Results", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ANSIABMA112014Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ANSIABMA112014Results._Cast_ANSIABMA112014Results":
        return self._Cast_ANSIABMA112014Results(self)
