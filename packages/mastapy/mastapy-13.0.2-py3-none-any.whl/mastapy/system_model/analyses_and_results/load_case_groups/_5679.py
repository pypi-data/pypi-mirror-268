"""TimeSeriesLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups import _5667
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_SERIES_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "TimeSeriesLoadCaseGroup",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6814, _6826
    from mastapy.system_model.analyses_and_results import _2683, _2627


__docformat__ = "restructuredtext en"
__all__ = ("TimeSeriesLoadCaseGroup",)


Self = TypeVar("Self", bound="TimeSeriesLoadCaseGroup")


class TimeSeriesLoadCaseGroup(_5667.AbstractLoadCaseGroup):
    """TimeSeriesLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _TIME_SERIES_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TimeSeriesLoadCaseGroup")

    class _Cast_TimeSeriesLoadCaseGroup:
        """Special nested class for casting TimeSeriesLoadCaseGroup to subclasses."""

        def __init__(
            self: "TimeSeriesLoadCaseGroup._Cast_TimeSeriesLoadCaseGroup",
            parent: "TimeSeriesLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def abstract_load_case_group(
            self: "TimeSeriesLoadCaseGroup._Cast_TimeSeriesLoadCaseGroup",
        ) -> "_5667.AbstractLoadCaseGroup":
            return self._parent._cast(_5667.AbstractLoadCaseGroup)

        @property
        def time_series_load_case_group(
            self: "TimeSeriesLoadCaseGroup._Cast_TimeSeriesLoadCaseGroup",
        ) -> "TimeSeriesLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "TimeSeriesLoadCaseGroup._Cast_TimeSeriesLoadCaseGroup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TimeSeriesLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_cases(self: Self) -> "List[_6814.TimeSeriesLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "_2683.CompoundMultibodyDynamicsAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundMultibodyDynamicsAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def analysis_of(
        self: Self, analysis_type: "_6826.AnalysisType"
    ) -> "_2627.CompoundAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundAnalysis

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)
        """
        analysis_type = conversion.mp_to_pn_enum(
            analysis_type,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType",
        )
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "TimeSeriesLoadCaseGroup._Cast_TimeSeriesLoadCaseGroup":
        return self._Cast_TimeSeriesLoadCaseGroup(self)
