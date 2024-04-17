"""ConceptCouplingHalfLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6861
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingHalfLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfLoadCase",)


Self = TypeVar("Self", bound="ConceptCouplingHalfLoadCase")


class ConceptCouplingHalfLoadCase(_6861.CouplingHalfLoadCase):
    """ConceptCouplingHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingHalfLoadCase")

    class _Cast_ConceptCouplingHalfLoadCase:
        """Special nested class for casting ConceptCouplingHalfLoadCase to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
            parent: "ConceptCouplingHalfLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
        ) -> "_6861.CouplingHalfLoadCase":
            return self._parent._cast(_6861.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_half_load_case(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
        ) -> "ConceptCouplingHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingHalfLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfLoadCase._Cast_ConceptCouplingHalfLoadCase":
        return self._Cast_ConceptCouplingHalfLoadCase(self)
