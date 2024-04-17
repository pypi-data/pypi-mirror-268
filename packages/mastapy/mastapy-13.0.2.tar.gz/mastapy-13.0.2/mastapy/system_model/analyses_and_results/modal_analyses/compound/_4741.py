"""AGMAGleasonConicalGearMeshCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4584
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4748,
        _4753,
        _4799,
        _4836,
        _4842,
        _4845,
        _4863,
        _4795,
        _4801,
        _4771,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundModalAnalysis")


class AGMAGleasonConicalGearMeshCompoundModalAnalysis(
    _4769.ConicalGearMeshCompoundModalAnalysis
):
    """AGMAGleasonConicalGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
            parent: "AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4769.ConicalGearMeshCompoundModalAnalysis":
            return self._parent._cast(_4769.ConicalGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4795.GearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(_4795.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4801.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(
                _4801.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4771.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4748.BevelDifferentialGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4748,
            )

            return self._parent._cast(
                _4748.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4753.BevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.BevelGearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4799.HypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(_4799.HypoidGearMeshCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4836.SpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4836,
            )

            return self._parent._cast(_4836.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4842.StraightBevelDiffGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(
                _4842.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4845.StraightBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "_4863.ZerolBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4863,
            )

            return self._parent._cast(_4863.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
        ) -> "AGMAGleasonConicalGearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4584.AGMAGleasonConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearMeshModalAnalysis]

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
    ) -> "List[_4584.AGMAGleasonConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearMeshModalAnalysis]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundModalAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysis(self)
