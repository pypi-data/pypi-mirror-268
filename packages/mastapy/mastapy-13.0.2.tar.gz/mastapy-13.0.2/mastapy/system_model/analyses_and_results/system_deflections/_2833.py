"""SystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections", "SystemDeflection"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2835,
        _2785,
        _2840,
    )
    from mastapy.system_model.fe import _2414
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7284,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7558, _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("SystemDeflection",)


Self = TypeVar("Self", bound="SystemDeflection")


class SystemDeflection(_7552.FEAnalysis):
    """SystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemDeflection")

    class _Cast_SystemDeflection:
        """Special nested class for casting SystemDeflection to subclasses."""

        def __init__(
            self: "SystemDeflection._Cast_SystemDeflection", parent: "SystemDeflection"
        ):
            self._parent = parent

        @property
        def fe_analysis(
            self: "SystemDeflection._Cast_SystemDeflection",
        ) -> "_7552.FEAnalysis":
            return self._parent._cast(_7552.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "SystemDeflection._Cast_SystemDeflection",
        ) -> "_7558.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7558

            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "SystemDeflection._Cast_SystemDeflection",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(self: "SystemDeflection._Cast_SystemDeflection") -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def torsional_system_deflection(
            self: "SystemDeflection._Cast_SystemDeflection",
        ) -> "_2840.TorsionalSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.TorsionalSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "SystemDeflection._Cast_SystemDeflection",
        ) -> "_7284.AdvancedSystemDeflectionSubAnalysis":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(_7284.AdvancedSystemDeflectionSubAnalysis)

        @property
        def system_deflection(
            self: "SystemDeflection._Cast_SystemDeflection",
        ) -> "SystemDeflection":
            return self._parent

        def __getattr__(self: "SystemDeflection._Cast_SystemDeflection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CurrentTime

        if temp is None:
            return 0.0

        return temp

    @current_time.setter
    @enforce_parameter_types
    def current_time(self: Self, value: "float"):
        self.wrapped.CurrentTime = float(value) if value is not None else 0.0

    @property
    def include_twist_in_misalignments(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeTwistInMisalignments

        if temp is None:
            return False

        return temp

    @include_twist_in_misalignments.setter
    @enforce_parameter_types
    def include_twist_in_misalignments(self: Self, value: "bool"):
        self.wrapped.IncludeTwistInMisalignments = (
            bool(value) if value is not None else False
        )

    @property
    def iterations(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Iterations

        if temp is None:
            return 0

        return temp

    @property
    def largest_power_across_a_connection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LargestPowerAcrossAConnection

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_circulating_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumCirculatingPower

        if temp is None:
            return 0.0

        return temp

    @property
    def power_convergence_error(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerConvergenceError

        if temp is None:
            return 0.0

        return temp

    @property
    def power_error(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerError

        if temp is None:
            return 0.0

        return temp

    @property
    def power_lost(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLost

        if temp is None:
            return 0.0

        return temp

    @property
    def total_input_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalInputPower

        if temp is None:
            return 0.0

        return temp

    @property
    def total_load_dependent_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalLoadDependentPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def total_speed_dependent_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalSpeedDependentPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def analysis_options(self: Self) -> "_2835.SystemDeflectionOptions":
        """mastapy.system_model.analyses_and_results.system_deflections.SystemDeflectionOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def overall_efficiency_results(
        self: Self,
    ) -> "_2785.LoadCaseOverallEfficiencyResult":
        """mastapy.system_model.analyses_and_results.system_deflections.LoadCaseOverallEfficiencyResult

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverallEfficiencyResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_race_f_es(self: Self) -> "List[_2414.RaceBearingFESystemDeflection]":
        """List[mastapy.system_model.fe.RaceBearingFESystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingRaceFEs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "SystemDeflection._Cast_SystemDeflection":
        return self._Cast_SystemDeflection(self)
