"""SMTRibStressResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SMT_RIB_STRESS_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "SMTRibStressResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("SMTRibStressResults",)


Self = TypeVar("Self", bound="SMTRibStressResults")


class SMTRibStressResults(_0.APIBase):
    """SMTRibStressResults

    This is a mastapy class.
    """

    TYPE = _SMT_RIB_STRESS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SMTRibStressResults")

    class _Cast_SMTRibStressResults:
        """Special nested class for casting SMTRibStressResults to subclasses."""

        def __init__(
            self: "SMTRibStressResults._Cast_SMTRibStressResults",
            parent: "SMTRibStressResults",
        ):
            self._parent = parent

        @property
        def smt_rib_stress_results(
            self: "SMTRibStressResults._Cast_SMTRibStressResults",
        ) -> "SMTRibStressResults":
            return self._parent

        def __getattr__(
            self: "SMTRibStressResults._Cast_SMTRibStressResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SMTRibStressResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_rib_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRibLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "SMTRibStressResults._Cast_SMTRibStressResults":
        return self._Cast_SMTRibStressResults(self)
