"""UnbalancedMassAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7142,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.static_loads import _6989
    from mastapy.system_model.analyses_and_results.system_deflections import _2842
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7097,
        _7044,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="UnbalancedMassAdvancedTimeSteppingAnalysisForModulation")


class UnbalancedMassAdvancedTimeSteppingAnalysisForModulation(
    _7142.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
):
    """UnbalancedMassAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting UnbalancedMassAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
            parent: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7142.VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7142.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6989.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2842.UnbalancedMassSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation(self)
