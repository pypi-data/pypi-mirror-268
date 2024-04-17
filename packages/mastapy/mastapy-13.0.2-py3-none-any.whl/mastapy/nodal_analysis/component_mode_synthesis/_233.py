"""HarmonicCMSResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.component_mode_synthesis import _232
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_CMS_RESULTS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "HarmonicCMSResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicCMSResults",)


Self = TypeVar("Self", bound="HarmonicCMSResults")


class HarmonicCMSResults(_232.CMSResults):
    """HarmonicCMSResults

    This is a mastapy class.
    """

    TYPE = _HARMONIC_CMS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicCMSResults")

    class _Cast_HarmonicCMSResults:
        """Special nested class for casting HarmonicCMSResults to subclasses."""

        def __init__(
            self: "HarmonicCMSResults._Cast_HarmonicCMSResults",
            parent: "HarmonicCMSResults",
        ):
            self._parent = parent

        @property
        def cms_results(
            self: "HarmonicCMSResults._Cast_HarmonicCMSResults",
        ) -> "_232.CMSResults":
            return self._parent._cast(_232.CMSResults)

        @property
        def harmonic_cms_results(
            self: "HarmonicCMSResults._Cast_HarmonicCMSResults",
        ) -> "HarmonicCMSResults":
            return self._parent

        def __getattr__(self: "HarmonicCMSResults._Cast_HarmonicCMSResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicCMSResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "HarmonicCMSResults._Cast_HarmonicCMSResults":
        return self._Cast_HarmonicCMSResults(self)
