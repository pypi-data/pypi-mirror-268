"""BearingLoads"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_LOADS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "BearingLoads"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingLoads",)


Self = TypeVar("Self", bound="BearingLoads")


class BearingLoads(_2103.SKFCalculationResult):
    """BearingLoads

    This is a mastapy class.
    """

    TYPE = _BEARING_LOADS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingLoads")

    class _Cast_BearingLoads:
        """Special nested class for casting BearingLoads to subclasses."""

        def __init__(self: "BearingLoads._Cast_BearingLoads", parent: "BearingLoads"):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "BearingLoads._Cast_BearingLoads",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def bearing_loads(self: "BearingLoads._Cast_BearingLoads") -> "BearingLoads":
            return self._parent

        def __getattr__(self: "BearingLoads._Cast_BearingLoads", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingLoads.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equivalent_dynamic_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentDynamicLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def load_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "BearingLoads._Cast_BearingLoads":
        return self._Cast_BearingLoads(self)
