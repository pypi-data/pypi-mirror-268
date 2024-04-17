"""SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6033,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2330
    from mastapy.system_model.analyses_and_results.static_loads import _6963
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6021,
        _6049,
        _6075,
        _6082,
        _6051,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation")


class SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation(
    _6033.BevelGearMeshHarmonicAnalysisOfSingleExcitation
):
    """SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.BevelGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6033.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6021.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(
                _6021.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6049.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(
                _6049.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6075.GearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(_6075.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6082.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2330.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6963.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation(self)
