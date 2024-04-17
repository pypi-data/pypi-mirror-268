"""SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7135,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2614
    from mastapy.system_model.analyses_and_results.static_loads import _6979
    from mastapy.system_model.analyses_and_results.system_deflections import _2831
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7058,
        _7097,
        _7044,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation"
)


class SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation(
    _7135.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
):
    """SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
            parent: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7135.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7135.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7058.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2614.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6979.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2831.SynchroniserSleeveSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection

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
    ) -> "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation(
            self
        )
