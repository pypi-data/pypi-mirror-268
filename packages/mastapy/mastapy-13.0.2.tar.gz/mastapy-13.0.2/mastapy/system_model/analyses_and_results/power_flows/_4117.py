"""KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4111
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _410
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4116,
        _4115,
        _4074,
        _4103,
        _4143,
        _4040,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow")


class KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow(
    _4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            return self._parent._cast(
                _4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_4074.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_4103.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_4143.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_410.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_410.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(
        self: Self,
    ) -> "List[_4116.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_power_flow(
        self: Self,
    ) -> "List[_4116.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(
        self: Self,
    ) -> "List[_4115.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_power_flow(
        self: Self,
    ) -> "List[_4115.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow(self)
