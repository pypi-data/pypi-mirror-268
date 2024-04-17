"""BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7247,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7029,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7190,
        _7149,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7190.CVTCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7190,
            )

            return self._parent._cast(
                _7190.CVTCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2583.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7029.BeltDriveAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BeltDriveAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7029.BeltDriveAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BeltDriveAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
