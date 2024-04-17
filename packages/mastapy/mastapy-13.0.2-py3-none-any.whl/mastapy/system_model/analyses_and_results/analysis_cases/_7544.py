"""AbstractAnalysisOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "AbstractAnalysisOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6812
    from mastapy.system_model.analyses_and_results.system_deflections import _2835
    from mastapy.system_model.analyses_and_results.modal_analyses import _4642
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5470
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5760,
        _5819,
        _5826,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAnalysisOptions",)


Self = TypeVar("Self", bound="AbstractAnalysisOptions")
T = TypeVar("T", bound="_6812.LoadCase")


class AbstractAnalysisOptions(_0.APIBase, Generic[T]):
    """AbstractAnalysisOptions

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ABSTRACT_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAnalysisOptions")

    class _Cast_AbstractAnalysisOptions:
        """Special nested class for casting AbstractAnalysisOptions to subclasses."""

        def __init__(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
            parent: "AbstractAnalysisOptions",
        ):
            self._parent = parent

        @property
        def system_deflection_options(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_2835.SystemDeflectionOptions":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.SystemDeflectionOptions)

        @property
        def frequency_response_analysis_options(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_4642.FrequencyResponseAnalysisOptions":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(_4642.FrequencyResponseAnalysisOptions)

        @property
        def mbd_run_up_analysis_options(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_5470.MBDRunUpAnalysisOptions":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(_5470.MBDRunUpAnalysisOptions)

        @property
        def frequency_options_for_harmonic_analysis_results(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_5760.FrequencyOptionsForHarmonicAnalysisResults":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5760,
            )

            return self._parent._cast(_5760.FrequencyOptionsForHarmonicAnalysisResults)

        @property
        def speed_options_for_harmonic_analysis_results(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_5819.SpeedOptionsForHarmonicAnalysisResults":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.SpeedOptionsForHarmonicAnalysisResults)

        @property
        def stiffness_options_for_harmonic_analysis(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_5826.StiffnessOptionsForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.StiffnessOptionsForHarmonicAnalysis)

        @property
        def abstract_analysis_options(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "AbstractAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions":
        return self._Cast_AbstractAnalysisOptions(self)
