"""SpringDamperLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6862
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpringDamperLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6961,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperLoadCase",)


Self = TypeVar("Self", bound="SpringDamperLoadCase")


class SpringDamperLoadCase(_6862.CouplingLoadCase):
    """SpringDamperLoadCase

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperLoadCase")

    class _Cast_SpringDamperLoadCase:
        """Special nested class for casting SpringDamperLoadCase to subclasses."""

        def __init__(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
            parent: "SpringDamperLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_6862.CouplingLoadCase":
            return self._parent._cast(_6862.CouplingLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "SpringDamperLoadCase":
            return self._parent

        def __getattr__(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2608.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SpringDamperLoadCase._Cast_SpringDamperLoadCase":
        return self._Cast_SpringDamperLoadCase(self)
