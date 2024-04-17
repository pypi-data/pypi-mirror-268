"""ShaftLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ShaftLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6817,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftLoadCase",)


Self = TypeVar("Self", bound="ShaftLoadCase")


class ShaftLoadCase(_6816.AbstractShaftLoadCase):
    """ShaftLoadCase

    This is a mastapy class.
    """

    TYPE = _SHAFT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftLoadCase")

    class _Cast_ShaftLoadCase:
        """Special nested class for casting ShaftLoadCase to subclasses."""

        def __init__(
            self: "ShaftLoadCase._Cast_ShaftLoadCase", parent: "ShaftLoadCase"
        ):
            self._parent = parent

        @property
        def abstract_shaft_load_case(
            self: "ShaftLoadCase._Cast_ShaftLoadCase",
        ) -> "_6816.AbstractShaftLoadCase":
            return self._parent._cast(_6816.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "ShaftLoadCase._Cast_ShaftLoadCase",
        ) -> "_6817.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.AbstractShaftOrHousingLoadCase)

        @property
        def component_load_case(
            self: "ShaftLoadCase._Cast_ShaftLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "ShaftLoadCase._Cast_ShaftLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "ShaftLoadCase._Cast_ShaftLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftLoadCase._Cast_ShaftLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftLoadCase._Cast_ShaftLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_load_case(
            self: "ShaftLoadCase._Cast_ShaftLoadCase",
        ) -> "ShaftLoadCase":
            return self._parent

        def __getattr__(self: "ShaftLoadCase._Cast_ShaftLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_scaling_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiameterScalingFactor

        if temp is None:
            return 0.0

        return temp

    @diameter_scaling_factor.setter
    @enforce_parameter_types
    def diameter_scaling_factor(self: Self, value: "float"):
        self.wrapped.DiameterScalingFactor = float(value) if value is not None else 0.0

    @property
    def component_design(self: Self) -> "_2489.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ShaftLoadCase._Cast_ShaftLoadCase":
        return self._Cast_ShaftLoadCase(self)
