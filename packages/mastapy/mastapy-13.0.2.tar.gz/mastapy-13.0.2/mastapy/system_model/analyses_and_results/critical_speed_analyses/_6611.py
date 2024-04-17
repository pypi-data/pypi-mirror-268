"""FlexiblePinAssemblyCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6652
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "FlexiblePinAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.static_loads import _6897
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6551,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCriticalSpeedAnalysis")


class FlexiblePinAssemblyCriticalSpeedAnalysis(
    _6652.SpecialisedAssemblyCriticalSpeedAnalysis
):
    """FlexiblePinAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyCriticalSpeedAnalysis"
    )

    class _Cast_FlexiblePinAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting FlexiblePinAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
            parent: "FlexiblePinAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
        ) -> "_6652.SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6652.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
        ) -> "_6551.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
        ) -> "FlexiblePinAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "FlexiblePinAssemblyCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2461.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6897.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis":
        return self._Cast_FlexiblePinAssemblyCriticalSpeedAnalysis(self)
