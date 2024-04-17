"""ZerolBevelGearMeshCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4753
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ZerolBevelGearMeshCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2338
    from mastapy.system_model.analyses_and_results.modal_analyses import _4721
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4741,
        _4769,
        _4795,
        _4801,
        _4771,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundModalAnalysis")


class ZerolBevelGearMeshCompoundModalAnalysis(_4753.BevelGearMeshCompoundModalAnalysis):
    """ZerolBevelGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMeshCompoundModalAnalysis"
    )

    class _Cast_ZerolBevelGearMeshCompoundModalAnalysis:
        """Special nested class for casting ZerolBevelGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
            parent: "ZerolBevelGearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "_4753.BevelGearMeshCompoundModalAnalysis":
            return self._parent._cast(_4753.BevelGearMeshCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "_4741.AGMAGleasonConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(
                _4741.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "_4769.ConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.ConicalGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "_4795.GearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(_4795.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "_4801.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(
                _4801.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "_4771.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
        ) -> "ZerolBevelGearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2338.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2338.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4721.ZerolBevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4721.ZerolBevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis":
        return self._Cast_ZerolBevelGearMeshCompoundModalAnalysis(self)
