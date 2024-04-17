"""PartStaticLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
    _5683,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups",
    "PartStaticLoadCaseGroup",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.static_loads import _6937
    from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
        _5680,
        _5681,
        _5684,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartStaticLoadCaseGroup",)


Self = TypeVar("Self", bound="PartStaticLoadCaseGroup")


class PartStaticLoadCaseGroup(_5683.DesignEntityStaticLoadCaseGroup):
    """PartStaticLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _PART_STATIC_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartStaticLoadCaseGroup")

    class _Cast_PartStaticLoadCaseGroup:
        """Special nested class for casting PartStaticLoadCaseGroup to subclasses."""

        def __init__(
            self: "PartStaticLoadCaseGroup._Cast_PartStaticLoadCaseGroup",
            parent: "PartStaticLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def design_entity_static_load_case_group(
            self: "PartStaticLoadCaseGroup._Cast_PartStaticLoadCaseGroup",
        ) -> "_5683.DesignEntityStaticLoadCaseGroup":
            return self._parent._cast(_5683.DesignEntityStaticLoadCaseGroup)

        @property
        def abstract_assembly_static_load_case_group(
            self: "PartStaticLoadCaseGroup._Cast_PartStaticLoadCaseGroup",
        ) -> "_5680.AbstractAssemblyStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5680,
            )

            return self._parent._cast(_5680.AbstractAssemblyStaticLoadCaseGroup)

        @property
        def component_static_load_case_group(
            self: "PartStaticLoadCaseGroup._Cast_PartStaticLoadCaseGroup",
        ) -> "_5681.ComponentStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5681,
            )

            return self._parent._cast(_5681.ComponentStaticLoadCaseGroup)

        @property
        def gear_set_static_load_case_group(
            self: "PartStaticLoadCaseGroup._Cast_PartStaticLoadCaseGroup",
        ) -> "_5684.GearSetStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5684,
            )

            return self._parent._cast(_5684.GearSetStaticLoadCaseGroup)

        @property
        def part_static_load_case_group(
            self: "PartStaticLoadCaseGroup._Cast_PartStaticLoadCaseGroup",
        ) -> "PartStaticLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "PartStaticLoadCaseGroup._Cast_PartStaticLoadCaseGroup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartStaticLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self: Self) -> "_2475.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def part_load_cases(self: Self) -> "List[_6937.PartLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.PartLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def clear_user_specified_excitation_data_for_all_load_cases(self: Self):
        """Method does not return."""
        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()

    @property
    def cast_to(self: Self) -> "PartStaticLoadCaseGroup._Cast_PartStaticLoadCaseGroup":
        return self._Cast_PartStaticLoadCaseGroup(self)
