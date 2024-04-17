"""CompoundModalAnalysisForHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundModalAnalysisForHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundModalAnalysisForHarmonicAnalysis",)


Self = TypeVar("Self", bound="CompoundModalAnalysisForHarmonicAnalysis")


class CompoundModalAnalysisForHarmonicAnalysis(_2627.CompoundAnalysis):
    """CompoundModalAnalysisForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CompoundModalAnalysisForHarmonicAnalysis"
    )

    class _Cast_CompoundModalAnalysisForHarmonicAnalysis:
        """Special nested class for casting CompoundModalAnalysisForHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CompoundModalAnalysisForHarmonicAnalysis._Cast_CompoundModalAnalysisForHarmonicAnalysis",
            parent: "CompoundModalAnalysisForHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundModalAnalysisForHarmonicAnalysis._Cast_CompoundModalAnalysisForHarmonicAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundModalAnalysisForHarmonicAnalysis._Cast_CompoundModalAnalysisForHarmonicAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_modal_analysis_for_harmonic_analysis(
            self: "CompoundModalAnalysisForHarmonicAnalysis._Cast_CompoundModalAnalysisForHarmonicAnalysis",
        ) -> "CompoundModalAnalysisForHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundModalAnalysisForHarmonicAnalysis._Cast_CompoundModalAnalysisForHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CompoundModalAnalysisForHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundModalAnalysisForHarmonicAnalysis._Cast_CompoundModalAnalysisForHarmonicAnalysis":
        return self._Cast_CompoundModalAnalysisForHarmonicAnalysis(self)
