"""IHaveShaftHarmonicResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.python_net import python_net_import

_I_HAVE_SHAFT_HARMONIC_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "IHaveShaftHarmonicResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("IHaveShaftHarmonicResults",)


Self = TypeVar("Self", bound="IHaveShaftHarmonicResults")


class IHaveShaftHarmonicResults:
    """This class is a public interface.
    The class body has intentionally been left empty.
    """
