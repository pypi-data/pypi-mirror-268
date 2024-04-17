"""GearMeshHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6082,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "GearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2320
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6021,
        _6028,
        _6033,
        _6046,
        _6049,
        _6064,
        _6070,
        _6080,
        _6084,
        _6087,
        _6090,
        _6118,
        _6124,
        _6127,
        _6142,
        _6145,
        _6051,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearMeshHarmonicAnalysisOfSingleExcitation")


class GearMeshHarmonicAnalysisOfSingleExcitation(
    _6082.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """GearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6082.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            return self._parent._cast(
                _6082.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6021.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(
                _6021.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6028.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6028,
            )

            return self._parent._cast(
                _6028.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.BevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(
                _6033.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.ConceptGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(
                _6046.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6049.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(
                _6049.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6064.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(
                _6064.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6070.FaceGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(
                _6070.FaceGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6080.HypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6084.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6090.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(
                _6090.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6118.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6124.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6127.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6142.WormGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6142,
            )

            return self._parent._cast(
                _6142.WormGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6145.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6145,
            )

            return self._parent._cast(
                _6145.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "GearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "GearMeshHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
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
    ) -> "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearMeshHarmonicAnalysisOfSingleExcitation(self)
