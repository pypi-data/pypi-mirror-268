"""ComponentStaticLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
    _5685,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups",
    "ComponentStaticLoadCaseGroup",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.static_loads import _6846
    from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
        _5683,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentStaticLoadCaseGroup",)


Self = TypeVar("Self", bound="ComponentStaticLoadCaseGroup")
TReal = TypeVar("TReal", bound="_2451.Component")
TComponentStaticLoad = TypeVar("TComponentStaticLoad", bound="_6846.ComponentLoadCase")


class ComponentStaticLoadCaseGroup(
    _5685.PartStaticLoadCaseGroup, Generic[TReal, TComponentStaticLoad]
):
    """ComponentStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TReal
        TComponentStaticLoad
    """

    TYPE = _COMPONENT_STATIC_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentStaticLoadCaseGroup")

    class _Cast_ComponentStaticLoadCaseGroup:
        """Special nested class for casting ComponentStaticLoadCaseGroup to subclasses."""

        def __init__(
            self: "ComponentStaticLoadCaseGroup._Cast_ComponentStaticLoadCaseGroup",
            parent: "ComponentStaticLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def part_static_load_case_group(
            self: "ComponentStaticLoadCaseGroup._Cast_ComponentStaticLoadCaseGroup",
        ) -> "_5685.PartStaticLoadCaseGroup":
            return self._parent._cast(_5685.PartStaticLoadCaseGroup)

        @property
        def design_entity_static_load_case_group(
            self: "ComponentStaticLoadCaseGroup._Cast_ComponentStaticLoadCaseGroup",
        ) -> "_5683.DesignEntityStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5683,
            )

            return self._parent._cast(_5683.DesignEntityStaticLoadCaseGroup)

        @property
        def component_static_load_case_group(
            self: "ComponentStaticLoadCaseGroup._Cast_ComponentStaticLoadCaseGroup",
        ) -> "ComponentStaticLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "ComponentStaticLoadCaseGroup._Cast_ComponentStaticLoadCaseGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentStaticLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self: Self) -> "TReal":
        """TReal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component(self: Self) -> "TReal":
        """TReal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Component

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def part_load_cases(self: Self) -> "List[TComponentStaticLoad]":
        """List[TComponentStaticLoad]

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

    @property
    def component_load_cases(self: Self) -> "List[TComponentStaticLoad]":
        """List[TComponentStaticLoad]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentStaticLoadCaseGroup._Cast_ComponentStaticLoadCaseGroup":
        return self._Cast_ComponentStaticLoadCaseGroup(self)
