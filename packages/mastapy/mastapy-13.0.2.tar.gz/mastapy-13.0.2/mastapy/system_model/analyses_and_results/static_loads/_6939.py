"""PartToPartShearCouplingHalfLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6861
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingHalfLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfLoadCase",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfLoadCase")


class PartToPartShearCouplingHalfLoadCase(_6861.CouplingHalfLoadCase):
    """PartToPartShearCouplingHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartToPartShearCouplingHalfLoadCase")

    class _Cast_PartToPartShearCouplingHalfLoadCase:
        """Special nested class for casting PartToPartShearCouplingHalfLoadCase to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
            parent: "PartToPartShearCouplingHalfLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ) -> "_6861.CouplingHalfLoadCase":
            return self._parent._cast(_6861.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
        ) -> "PartToPartShearCouplingHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingHalfLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

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
    ) -> (
        "PartToPartShearCouplingHalfLoadCase._Cast_PartToPartShearCouplingHalfLoadCase"
    ):
        return self._Cast_PartToPartShearCouplingHalfLoadCase(self)
