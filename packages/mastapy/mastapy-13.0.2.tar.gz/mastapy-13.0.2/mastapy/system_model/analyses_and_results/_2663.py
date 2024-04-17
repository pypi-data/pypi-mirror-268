"""IHaveRootHarmonicAnalysisResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.python_net import python_net_import

_I_HAVE_ROOT_HARMONIC_ANALYSIS_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "IHaveRootHarmonicAnalysisResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("IHaveRootHarmonicAnalysisResults",)


Self = TypeVar("Self", bound="IHaveRootHarmonicAnalysisResults")


class IHaveRootHarmonicAnalysisResults:
    """This class is a public interface.
    The class body has intentionally been left empty.
    """
