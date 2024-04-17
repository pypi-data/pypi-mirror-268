"""HarmonicAnalysisShaftExportOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5771
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_SHAFT_EXPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HarmonicAnalysisShaftExportOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisShaftExportOptions",)


Self = TypeVar("Self", bound="HarmonicAnalysisShaftExportOptions")


class HarmonicAnalysisShaftExportOptions(
    _5771.HarmonicAnalysisExportOptions[
        "_2664.IHaveShaftHarmonicResults", "_2489.Shaft"
    ]
):
    """HarmonicAnalysisShaftExportOptions

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_SHAFT_EXPORT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicAnalysisShaftExportOptions")

    class _Cast_HarmonicAnalysisShaftExportOptions:
        """Special nested class for casting HarmonicAnalysisShaftExportOptions to subclasses."""

        def __init__(
            self: "HarmonicAnalysisShaftExportOptions._Cast_HarmonicAnalysisShaftExportOptions",
            parent: "HarmonicAnalysisShaftExportOptions",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_export_options(
            self: "HarmonicAnalysisShaftExportOptions._Cast_HarmonicAnalysisShaftExportOptions",
        ) -> "_5771.HarmonicAnalysisExportOptions":
            return self._parent._cast(_5771.HarmonicAnalysisExportOptions)

        @property
        def harmonic_analysis_shaft_export_options(
            self: "HarmonicAnalysisShaftExportOptions._Cast_HarmonicAnalysisShaftExportOptions",
        ) -> "HarmonicAnalysisShaftExportOptions":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisShaftExportOptions._Cast_HarmonicAnalysisShaftExportOptions",
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
        self: Self, instance_to_wrap: "HarmonicAnalysisShaftExportOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisShaftExportOptions._Cast_HarmonicAnalysisShaftExportOptions":
        return self._Cast_HarmonicAnalysisShaftExportOptions(self)
