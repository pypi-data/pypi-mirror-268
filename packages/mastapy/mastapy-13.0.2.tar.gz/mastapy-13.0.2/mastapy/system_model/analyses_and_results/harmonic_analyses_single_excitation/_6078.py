"""HarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "HarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="HarmonicAnalysisOfSingleExcitation")


class HarmonicAnalysisOfSingleExcitation(_7558.StaticLoadAnalysisCase):
    """HarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicAnalysisOfSingleExcitation")

    class _Cast_HarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting HarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "HarmonicAnalysisOfSingleExcitation._Cast_HarmonicAnalysisOfSingleExcitation",
            parent: "HarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "HarmonicAnalysisOfSingleExcitation._Cast_HarmonicAnalysisOfSingleExcitation",
        ) -> "_7558.StaticLoadAnalysisCase":
            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "HarmonicAnalysisOfSingleExcitation._Cast_HarmonicAnalysisOfSingleExcitation",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "HarmonicAnalysisOfSingleExcitation._Cast_HarmonicAnalysisOfSingleExcitation",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def harmonic_analysis_of_single_excitation(
            self: "HarmonicAnalysisOfSingleExcitation._Cast_HarmonicAnalysisOfSingleExcitation",
        ) -> "HarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisOfSingleExcitation._Cast_HarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "HarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_detail(self: Self) -> "_5687.AbstractPeriodicExcitationDetail":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractPeriodicExcitationDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisOfSingleExcitation._Cast_HarmonicAnalysisOfSingleExcitation":
        return self._Cast_HarmonicAnalysisOfSingleExcitation(self)
