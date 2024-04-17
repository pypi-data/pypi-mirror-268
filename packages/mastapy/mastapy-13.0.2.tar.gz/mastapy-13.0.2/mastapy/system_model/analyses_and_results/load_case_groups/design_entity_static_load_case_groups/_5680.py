"""AbstractAssemblyStaticLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
    _5685,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups",
    "AbstractAssemblyStaticLoadCaseGroup",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.static_loads import _6815
    from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
        _5683,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyStaticLoadCaseGroup",)


Self = TypeVar("Self", bound="AbstractAssemblyStaticLoadCaseGroup")
TAssembly = TypeVar("TAssembly", bound="_2441.AbstractAssembly")
TAssemblyStaticLoad = TypeVar(
    "TAssemblyStaticLoad", bound="_6815.AbstractAssemblyLoadCase"
)


class AbstractAssemblyStaticLoadCaseGroup(
    _5685.PartStaticLoadCaseGroup, Generic[TAssembly, TAssemblyStaticLoad]
):
    """AbstractAssemblyStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TAssembly
        TAssemblyStaticLoad
    """

    TYPE = _ABSTRACT_ASSEMBLY_STATIC_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyStaticLoadCaseGroup")

    class _Cast_AbstractAssemblyStaticLoadCaseGroup:
        """Special nested class for casting AbstractAssemblyStaticLoadCaseGroup to subclasses."""

        def __init__(
            self: "AbstractAssemblyStaticLoadCaseGroup._Cast_AbstractAssemblyStaticLoadCaseGroup",
            parent: "AbstractAssemblyStaticLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def part_static_load_case_group(
            self: "AbstractAssemblyStaticLoadCaseGroup._Cast_AbstractAssemblyStaticLoadCaseGroup",
        ) -> "_5685.PartStaticLoadCaseGroup":
            return self._parent._cast(_5685.PartStaticLoadCaseGroup)

        @property
        def design_entity_static_load_case_group(
            self: "AbstractAssemblyStaticLoadCaseGroup._Cast_AbstractAssemblyStaticLoadCaseGroup",
        ) -> "_5683.DesignEntityStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5683,
            )

            return self._parent._cast(_5683.DesignEntityStaticLoadCaseGroup)

        @property
        def abstract_assembly_static_load_case_group(
            self: "AbstractAssemblyStaticLoadCaseGroup._Cast_AbstractAssemblyStaticLoadCaseGroup",
        ) -> "AbstractAssemblyStaticLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyStaticLoadCaseGroup._Cast_AbstractAssemblyStaticLoadCaseGroup",
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
        self: Self, instance_to_wrap: "AbstractAssemblyStaticLoadCaseGroup.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self: Self) -> "TAssembly":
        """TAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly(self: Self) -> "TAssembly":
        """TAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Assembly

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def part_load_cases(self: Self) -> "List[TAssemblyStaticLoad]":
        """List[TAssemblyStaticLoad]

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
    def assembly_load_cases(self: Self) -> "List[TAssemblyStaticLoad]":
        """List[TAssemblyStaticLoad]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "AbstractAssemblyStaticLoadCaseGroup._Cast_AbstractAssemblyStaticLoadCaseGroup"
    ):
        return self._Cast_AbstractAssemblyStaticLoadCaseGroup(self)
