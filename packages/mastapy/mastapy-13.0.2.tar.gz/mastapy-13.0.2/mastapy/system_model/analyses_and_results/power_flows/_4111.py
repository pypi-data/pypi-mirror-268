"""KlingelnbergCycloPalloidConicalGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4074
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4114,
        _4117,
        _4103,
        _4143,
        _4040,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetPowerFlow")


class KlingelnbergCycloPalloidConicalGearSetPowerFlow(_4074.ConicalGearSetPowerFlow):
    """KlingelnbergCycloPalloidConicalGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4074.ConicalGearSetPowerFlow":
            return self._parent._cast(_4074.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4103.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4143.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4114.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(
                _4114.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4117.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(
                _4117.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow(self)
