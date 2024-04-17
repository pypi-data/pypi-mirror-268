"""BearingLoadCaseResultsForPST"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings import _1882
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_LOAD_CASE_RESULTS_FOR_PST = python_net_import(
    "SMT.MastaAPI.Bearings", "BearingLoadCaseResultsForPST"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingLoadCaseResultsForPST",)


Self = TypeVar("Self", bound="BearingLoadCaseResultsForPST")


class BearingLoadCaseResultsForPST(_1882.BearingLoadCaseResultsLightweight):
    """BearingLoadCaseResultsForPST

    This is a mastapy class.
    """

    TYPE = _BEARING_LOAD_CASE_RESULTS_FOR_PST
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingLoadCaseResultsForPST")

    class _Cast_BearingLoadCaseResultsForPST:
        """Special nested class for casting BearingLoadCaseResultsForPST to subclasses."""

        def __init__(
            self: "BearingLoadCaseResultsForPST._Cast_BearingLoadCaseResultsForPST",
            parent: "BearingLoadCaseResultsForPST",
        ):
            self._parent = parent

        @property
        def bearing_load_case_results_lightweight(
            self: "BearingLoadCaseResultsForPST._Cast_BearingLoadCaseResultsForPST",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def bearing_load_case_results_for_pst(
            self: "BearingLoadCaseResultsForPST._Cast_BearingLoadCaseResultsForPST",
        ) -> "BearingLoadCaseResultsForPST":
            return self._parent

        def __getattr__(
            self: "BearingLoadCaseResultsForPST._Cast_BearingLoadCaseResultsForPST",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingLoadCaseResultsForPST.TYPE"):
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
    ) -> "BearingLoadCaseResultsForPST._Cast_BearingLoadCaseResultsForPST":
        return self._Cast_BearingLoadCaseResultsForPST(self)
