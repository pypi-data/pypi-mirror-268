"""KlingelnbergCycloPalloidHypoidGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6853,
        _6899,
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearLoadCase")


class KlingelnbergCycloPalloidHypoidGearLoadCase(
    _6921.KlingelnbergCycloPalloidConicalGearLoadCase
):
    """KlingelnbergCycloPalloidHypoidGearLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
            parent: "KlingelnbergCycloPalloidHypoidGearLoadCase",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "_6921.KlingelnbergCycloPalloidConicalGearLoadCase":
            return self._parent._cast(_6921.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "_6853.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "_6899.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6899

            return self._parent._cast(_6899.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
        ) -> "KlingelnbergCycloPalloidHypoidGearLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

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
    ) -> "KlingelnbergCycloPalloidHypoidGearLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearLoadCase(self)
