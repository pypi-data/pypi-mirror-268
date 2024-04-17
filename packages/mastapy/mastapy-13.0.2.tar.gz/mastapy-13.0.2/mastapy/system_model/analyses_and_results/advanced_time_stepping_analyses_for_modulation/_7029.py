"""BeltDriveAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7118,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.static_loads import _6830
    from mastapy.system_model.analyses_and_results.system_deflections import _2708
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7059,
        _7014,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="BeltDriveAdvancedTimeSteppingAnalysisForModulation")


class BeltDriveAdvancedTimeSteppingAnalysisForModulation(
    _7118.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
):
    """BeltDriveAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BeltDriveAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
            parent: "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7118.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7118.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7014,
            )

            return self._parent._cast(
                _7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7059.CVTAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7059,
            )

            return self._parent._cast(
                _7059.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BeltDriveAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BeltDriveAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6830.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2708.BeltDriveSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection

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
    ) -> "BeltDriveAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BeltDriveAdvancedTimeSteppingAnalysisForModulation(self)
