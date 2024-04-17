"""VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6224,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6140,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6222,
        _6223,
        _6233,
        _6234,
        _6268,
        _6172,
        _6226,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation"
)


class VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation(
    _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6224.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6226.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6222.MassDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6223.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6233.PointLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6234.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6234,
            )

            return self._parent._cast(
                _6234.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6268.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6268,
            )

            return self._parent._cast(
                _6268.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6140.VirtualComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.VirtualComponentHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6140.VirtualComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.VirtualComponentHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
