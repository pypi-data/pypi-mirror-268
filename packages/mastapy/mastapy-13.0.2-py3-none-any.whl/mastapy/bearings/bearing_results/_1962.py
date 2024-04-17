"""LoadedLinearBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results import _1956
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_LINEAR_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedLinearBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedLinearBearingResults",)


Self = TypeVar("Self", bound="LoadedLinearBearingResults")


class LoadedLinearBearingResults(_1956.LoadedBearingResults):
    """LoadedLinearBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_LINEAR_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedLinearBearingResults")

    class _Cast_LoadedLinearBearingResults:
        """Special nested class for casting LoadedLinearBearingResults to subclasses."""

        def __init__(
            self: "LoadedLinearBearingResults._Cast_LoadedLinearBearingResults",
            parent: "LoadedLinearBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_bearing_results(
            self: "LoadedLinearBearingResults._Cast_LoadedLinearBearingResults",
        ) -> "_1956.LoadedBearingResults":
            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedLinearBearingResults._Cast_LoadedLinearBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_linear_bearing_results(
            self: "LoadedLinearBearingResults._Cast_LoadedLinearBearingResults",
        ) -> "LoadedLinearBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedLinearBearingResults._Cast_LoadedLinearBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedLinearBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedLinearBearingResults._Cast_LoadedLinearBearingResults":
        return self._Cast_LoadedLinearBearingResults(self)
