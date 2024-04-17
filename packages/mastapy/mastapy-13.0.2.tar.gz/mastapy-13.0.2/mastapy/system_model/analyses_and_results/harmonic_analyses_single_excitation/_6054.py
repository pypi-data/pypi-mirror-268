"""CouplingHalfHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6095,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CouplingHalfHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2592
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6038,
        _6043,
        _6058,
        _6099,
        _6106,
        _6111,
        _6121,
        _6131,
        _6133,
        _6134,
        _6137,
        _6138,
        _6041,
        _6097,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CouplingHalfHarmonicAnalysisOfSingleExcitation")


class CouplingHalfHarmonicAnalysisOfSingleExcitation(
    _6095.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """CouplingHalfHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingHalfHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
            parent: "CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6095.MountableComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6095.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6041.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(_6041.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6038.ClutchHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6043.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6058.CVTPulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(_6058.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6099.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(
                _6099.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6106.PulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(_6106.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6111.RollingRingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6121.SpringDamperHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6131.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6133.SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(
                _6133.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6137.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6137,
            )

            return self._parent._cast(
                _6137.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6138.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6138,
            )

            return self._parent._cast(
                _6138.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "CouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CouplingHalfHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2592.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation(self)
