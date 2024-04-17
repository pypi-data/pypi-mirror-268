"""HarmonicSelection"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results",
    "HarmonicSelection",
)


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicSelection",)


Self = TypeVar("Self", bound="HarmonicSelection")


class HarmonicSelection(_0.APIBase):
    """HarmonicSelection

    This is a mastapy class.
    """

    TYPE = _HARMONIC_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicSelection")

    class _Cast_HarmonicSelection:
        """Special nested class for casting HarmonicSelection to subclasses."""

        def __init__(
            self: "HarmonicSelection._Cast_HarmonicSelection",
            parent: "HarmonicSelection",
        ):
            self._parent = parent

        @property
        def harmonic_selection(
            self: "HarmonicSelection._Cast_HarmonicSelection",
        ) -> "HarmonicSelection":
            return self._parent

        def __getattr__(self: "HarmonicSelection._Cast_HarmonicSelection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Harmonic

        if temp is None:
            return 0

        return temp

    @property
    def included(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Included

        if temp is None:
            return False

        return temp

    @included.setter
    @enforce_parameter_types
    def included(self: Self, value: "bool"):
        self.wrapped.Included = bool(value) if value is not None else False

    @property
    def is_included_in_excitations(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsIncludedInExcitations

        if temp is None:
            return False

        return temp

    @is_included_in_excitations.setter
    @enforce_parameter_types
    def is_included_in_excitations(self: Self, value: "bool"):
        self.wrapped.IsIncludedInExcitations = (
            bool(value) if value is not None else False
        )

    @property
    def order(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Order

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "HarmonicSelection._Cast_HarmonicSelection":
        return self._Cast_HarmonicSelection(self)
