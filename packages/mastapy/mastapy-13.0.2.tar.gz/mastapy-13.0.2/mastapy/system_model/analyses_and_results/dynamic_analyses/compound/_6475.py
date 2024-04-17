"""GearMeshCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6481
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "GearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6421,
        _6428,
        _6433,
        _6446,
        _6449,
        _6464,
        _6470,
        _6479,
        _6483,
        _6486,
        _6489,
        _6516,
        _6522,
        _6525,
        _6540,
        _6543,
        _6451,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundDynamicAnalysis")


class GearMeshCompoundDynamicAnalysis(
    _6481.InterMountableComponentConnectionCompoundDynamicAnalysis
):
    """GearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundDynamicAnalysis")

    class _Cast_GearMeshCompoundDynamicAnalysis:
        """Special nested class for casting GearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
            parent: "GearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6481.InterMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent._cast(
                _6481.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6451.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6421.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(
                _6421.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6428.BevelDifferentialGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(
                _6428.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6433.BevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def concept_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6446.ConceptGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6449.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(_6449.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6464.CylindricalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6470.FaceGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(_6470.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6479.HypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(_6479.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6483.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(
                _6483.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6486.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(
                _6486.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6489.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(
                _6489.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6516.SpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6516,
            )

            return self._parent._cast(_6516.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6522.StraightBevelDiffGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6522,
            )

            return self._parent._cast(
                _6522.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6525.StraightBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(
                _6525.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def worm_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6540.WormGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6540,
            )

            return self._parent._cast(_6540.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "_6543.ZerolBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6543,
            )

            return self._parent._cast(_6543.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
        ) -> "GearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_6346.GearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearMeshDynamicAnalysis]

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
    ) -> "List[_6346.GearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearMeshDynamicAnalysis]

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
    ) -> "GearMeshCompoundDynamicAnalysis._Cast_GearMeshCompoundDynamicAnalysis":
        return self._Cast_GearMeshCompoundDynamicAnalysis(self)
