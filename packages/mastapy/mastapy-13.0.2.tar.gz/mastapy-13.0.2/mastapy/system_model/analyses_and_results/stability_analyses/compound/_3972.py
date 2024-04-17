"""KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3938
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3839
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3975,
        _3978,
        _3964,
        _3970,
        _3940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis(
    _3938.ConicalGearMeshCompoundStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3938.ConicalGearMeshCompoundStabilityAnalysis":
            return self._parent._cast(_3938.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3964.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(_3964.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3970.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3940.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "_3975.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3975,
            )

            return self._parent._cast(
                _3975.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> (
            "_3978.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(
                _3978.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3839.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis]

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
    ) -> "List[_3839.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis(
                self
            )
        )
