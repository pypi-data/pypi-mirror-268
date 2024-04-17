"""IHaveFEPartHarmonicAnalysisResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.python_net import python_net_import

_I_HAVE_FE_PART_HARMONIC_ANALYSIS_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "IHaveFEPartHarmonicAnalysisResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("IHaveFEPartHarmonicAnalysisResults",)


Self = TypeVar("Self", bound="IHaveFEPartHarmonicAnalysisResults")


class IHaveFEPartHarmonicAnalysisResults:
    """This class is a public interface.
    The class body has intentionally been left empty.
    """
