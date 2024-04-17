"""StraightBevelPlanetGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4280
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "StraightBevelPlanetGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4156
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4191,
        _4179,
        _4207,
        _4233,
        _4252,
        _4200,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundPowerFlow")


class StraightBevelPlanetGearCompoundPowerFlow(
    _4280.StraightBevelDiffGearCompoundPowerFlow
):
    """StraightBevelPlanetGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundPowerFlow"
    )

    class _Cast_StraightBevelPlanetGearCompoundPowerFlow:
        """Special nested class for casting StraightBevelPlanetGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
            parent: "StraightBevelPlanetGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_4280.StraightBevelDiffGearCompoundPowerFlow":
            return self._parent._cast(_4280.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_4191.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_4179.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_4207.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4207,
            )

            return self._parent._cast(_4207.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_4233.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(_4233.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_4252.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_4200.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "StraightBevelPlanetGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4156.StraightBevelPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelPlanetGearPowerFlow]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4156.StraightBevelPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelPlanetGearPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow":
        return self._Cast_StraightBevelPlanetGearCompoundPowerFlow(self)
