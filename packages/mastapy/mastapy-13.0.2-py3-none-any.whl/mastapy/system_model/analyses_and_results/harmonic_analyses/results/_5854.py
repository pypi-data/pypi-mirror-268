"""ExcitationSourceSelectionBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Optional

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCITATION_SOURCE_SELECTION_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results",
    "ExcitationSourceSelectionBase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.results import (
        _5853,
        _5855,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ExcitationSourceSelectionBase",)


Self = TypeVar("Self", bound="ExcitationSourceSelectionBase")


class ExcitationSourceSelectionBase(_0.APIBase):
    """ExcitationSourceSelectionBase

    This is a mastapy class.
    """

    TYPE = _EXCITATION_SOURCE_SELECTION_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExcitationSourceSelectionBase")

    class _Cast_ExcitationSourceSelectionBase:
        """Special nested class for casting ExcitationSourceSelectionBase to subclasses."""

        def __init__(
            self: "ExcitationSourceSelectionBase._Cast_ExcitationSourceSelectionBase",
            parent: "ExcitationSourceSelectionBase",
        ):
            self._parent = parent

        @property
        def excitation_source_selection(
            self: "ExcitationSourceSelectionBase._Cast_ExcitationSourceSelectionBase",
        ) -> "_5853.ExcitationSourceSelection":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.results import (
                _5853,
            )

            return self._parent._cast(_5853.ExcitationSourceSelection)

        @property
        def excitation_source_selection_group(
            self: "ExcitationSourceSelectionBase._Cast_ExcitationSourceSelectionBase",
        ) -> "_5855.ExcitationSourceSelectionGroup":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.results import (
                _5855,
            )

            return self._parent._cast(_5855.ExcitationSourceSelectionGroup)

        @property
        def excitation_source_selection_base(
            self: "ExcitationSourceSelectionBase._Cast_ExcitationSourceSelectionBase",
        ) -> "ExcitationSourceSelectionBase":
            return self._parent

        def __getattr__(
            self: "ExcitationSourceSelectionBase._Cast_ExcitationSourceSelectionBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExcitationSourceSelectionBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def included(self: Self) -> "Optional[bool]":
        """Optional[bool]"""
        temp = self.wrapped.Included

        if temp is None:
            return None

        return temp

    @included.setter
    @enforce_parameter_types
    def included(self: Self, value: "Optional[bool]"):
        self.wrapped.Included = value

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ExcitationSourceSelectionBase._Cast_ExcitationSourceSelectionBase":
        return self._Cast_ExcitationSourceSelectionBase(self)
