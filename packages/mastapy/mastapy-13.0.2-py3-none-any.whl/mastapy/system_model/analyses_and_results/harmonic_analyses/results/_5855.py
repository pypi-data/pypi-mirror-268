"""ExcitationSourceSelectionGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCITATION_SOURCE_SELECTION_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results",
    "ExcitationSourceSelectionGroup",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1536


__docformat__ = "restructuredtext en"
__all__ = ("ExcitationSourceSelectionGroup",)


Self = TypeVar("Self", bound="ExcitationSourceSelectionGroup")


class ExcitationSourceSelectionGroup(_5854.ExcitationSourceSelectionBase):
    """ExcitationSourceSelectionGroup

    This is a mastapy class.
    """

    TYPE = _EXCITATION_SOURCE_SELECTION_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExcitationSourceSelectionGroup")

    class _Cast_ExcitationSourceSelectionGroup:
        """Special nested class for casting ExcitationSourceSelectionGroup to subclasses."""

        def __init__(
            self: "ExcitationSourceSelectionGroup._Cast_ExcitationSourceSelectionGroup",
            parent: "ExcitationSourceSelectionGroup",
        ):
            self._parent = parent

        @property
        def excitation_source_selection_base(
            self: "ExcitationSourceSelectionGroup._Cast_ExcitationSourceSelectionGroup",
        ) -> "_5854.ExcitationSourceSelectionBase":
            return self._parent._cast(_5854.ExcitationSourceSelectionBase)

        @property
        def excitation_source_selection_group(
            self: "ExcitationSourceSelectionGroup._Cast_ExcitationSourceSelectionGroup",
        ) -> "ExcitationSourceSelectionGroup":
            return self._parent

        def __getattr__(
            self: "ExcitationSourceSelectionGroup._Cast_ExcitationSourceSelectionGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExcitationSourceSelectionGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def sub_items(self: Self) -> "List[_5854.ExcitationSourceSelectionBase]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.results.ExcitationSourceSelectionBase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubItems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def selection_as_xml_string(self: Self) -> "str":
        """str"""
        temp = self.wrapped.SelectionAsXmlString

        if temp is None:
            return ""

        return temp

    @selection_as_xml_string.setter
    @enforce_parameter_types
    def selection_as_xml_string(self: Self, value: "str"):
        self.wrapped.SelectionAsXmlString = str(value) if value is not None else ""

    @enforce_parameter_types
    def include_only_harmonics_with_order(self: Self, order: "_1536.RoundedOrder"):
        """Method does not return.

        Args:
            order (mastapy.math_utility.RoundedOrder)
        """
        self.wrapped.IncludeOnlyHarmonicsWithOrder(order.wrapped if order else None)

    @property
    def cast_to(
        self: Self,
    ) -> "ExcitationSourceSelectionGroup._Cast_ExcitationSourceSelectionGroup":
        return self._Cast_ExcitationSourceSelectionGroup(self)
