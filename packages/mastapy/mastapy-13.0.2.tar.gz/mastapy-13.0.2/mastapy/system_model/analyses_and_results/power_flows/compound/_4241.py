"""KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4207
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4110
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4244,
        _4247,
        _4233,
        _4252,
        _4200,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearCompoundPowerFlow")


class KlingelnbergCycloPalloidConicalGearCompoundPowerFlow(
    _4207.ConicalGearCompoundPowerFlow
):
    """KlingelnbergCycloPalloidConicalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4207.ConicalGearCompoundPowerFlow":
            return self._parent._cast(_4207.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4233.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(_4233.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4252.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4200.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4244.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(
                _4244.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4247.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(
                _4247.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4110.KlingelnbergCycloPalloidConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4110.KlingelnbergCycloPalloidConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow(self)
