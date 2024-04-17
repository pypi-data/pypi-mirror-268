"""GearMeshModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5190
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "GearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2320
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5129,
        _5136,
        _5141,
        _5154,
        _5157,
        _5172,
        _5178,
        _5187,
        _5191,
        _5194,
        _5197,
        _5225,
        _5231,
        _5234,
        _5249,
        _5252,
        _5160,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="GearMeshModalAnalysisAtASpeed")


class GearMeshModalAnalysisAtASpeed(
    _5190.InterMountableComponentConnectionModalAnalysisAtASpeed
):
    """GearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshModalAnalysisAtASpeed")

    class _Cast_GearMeshModalAnalysisAtASpeed:
        """Special nested class for casting GearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
            parent: "GearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5190.InterMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent._cast(
                _5190.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5160.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5129.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5129,
            )

            return self._parent._cast(
                _5129.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5136.BevelDifferentialGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5136,
            )

            return self._parent._cast(
                _5136.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5141.BevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5154.ConceptGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(_5154.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5157.ConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5172.CylindricalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5178.FaceGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(_5178.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5187.HypoidGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5187,
            )

            return self._parent._cast(_5187.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5191.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(
                _5191.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5194.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(
                _5194.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5197.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(
                _5197.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5225.SpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(_5225.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5231.StraightBevelDiffGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5231,
            )

            return self._parent._cast(
                _5231.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5234.StraightBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5249.WormGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5249,
            )

            return self._parent._cast(_5249.WormGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "_5252.ZerolBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5252,
            )

            return self._parent._cast(_5252.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "GearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2320.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed":
        return self._Cast_GearMeshModalAnalysisAtASpeed(self)
