"""CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults",
        "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    )
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
)


class CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(
    _2627.CompoundAnalysis
):
    """CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = (
        _COMPOUND_HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
            parent: "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(
            self
        )
