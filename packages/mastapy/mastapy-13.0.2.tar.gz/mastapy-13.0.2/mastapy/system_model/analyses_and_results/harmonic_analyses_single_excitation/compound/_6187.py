"""CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6156,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6056,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6212,
        _6182,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation"
)


class CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6156.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6156.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6156.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6212.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6212,
            )

            return self._parent._cast(
                _6212.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6056.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6056.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
