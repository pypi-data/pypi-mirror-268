"""PlanetCarrierAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7097,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.system_model.analyses_and_results.system_deflections import _2798
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7044,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="PlanetCarrierAdvancedTimeSteppingAnalysisForModulation")


class PlanetCarrierAdvancedTimeSteppingAnalysisForModulation(
    _7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation
):
    """PlanetCarrierAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PlanetCarrierAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
            parent: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2476.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6944.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2798.PlanetCarrierSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PlanetCarrierSystemDeflection

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
    ) -> "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PlanetCarrierAdvancedTimeSteppingAnalysisForModulation(self)
