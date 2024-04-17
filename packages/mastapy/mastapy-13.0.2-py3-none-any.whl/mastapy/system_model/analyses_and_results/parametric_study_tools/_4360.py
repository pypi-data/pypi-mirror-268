"""DutyCycleResultsForRootAssembly"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_RESULTS_FOR_ROOT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "DutyCycleResultsForRootAssembly",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2911,
    )


__docformat__ = "restructuredtext en"
__all__ = ("DutyCycleResultsForRootAssembly",)


Self = TypeVar("Self", bound="DutyCycleResultsForRootAssembly")


class DutyCycleResultsForRootAssembly(_0.APIBase):
    """DutyCycleResultsForRootAssembly

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_RESULTS_FOR_ROOT_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCycleResultsForRootAssembly")

    class _Cast_DutyCycleResultsForRootAssembly:
        """Special nested class for casting DutyCycleResultsForRootAssembly to subclasses."""

        def __init__(
            self: "DutyCycleResultsForRootAssembly._Cast_DutyCycleResultsForRootAssembly",
            parent: "DutyCycleResultsForRootAssembly",
        ):
            self._parent = parent

        @property
        def duty_cycle_results_for_root_assembly(
            self: "DutyCycleResultsForRootAssembly._Cast_DutyCycleResultsForRootAssembly",
        ) -> "DutyCycleResultsForRootAssembly":
            return self._parent

        def __getattr__(
            self: "DutyCycleResultsForRootAssembly._Cast_DutyCycleResultsForRootAssembly",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCycleResultsForRootAssembly.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_efficiency_results(self: Self) -> "_2911.DutyCycleEfficiencyResults":
        """mastapy.system_model.analyses_and_results.system_deflections.compound.DutyCycleEfficiencyResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycleEfficiencyResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "DutyCycleResultsForRootAssembly._Cast_DutyCycleResultsForRootAssembly":
        return self._Cast_DutyCycleResultsForRootAssembly(self)
