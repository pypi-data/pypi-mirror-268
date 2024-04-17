"""AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7182,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7023,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7161,
        _7166,
        _7212,
        _7249,
        _7255,
        _7258,
        _7276,
        _7208,
        _7214,
        _7184,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7182.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7182.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7182.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7208.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7214.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7214,
            )

            return self._parent._cast(
                _7214.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7184.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7161.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7161,
            )

            return self._parent._cast(
                _7161.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7166.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7212.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7212,
            )

            return self._parent._cast(
                _7212.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7249.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7249,
            )

            return self._parent._cast(
                _7249.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7255.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7255,
            )

            return self._parent._cast(
                _7255.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7258.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7258,
            )

            return self._parent._cast(
                _7258.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7276.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7276,
            )

            return self._parent._cast(
                _7276.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7023.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7023.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
