"""AGMAGleasonConicalGearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4209
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AGMAGleasonConicalGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4046
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4188,
        _4193,
        _4239,
        _4276,
        _4282,
        _4285,
        _4303,
        _4235,
        _4273,
        _4175,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundPowerFlow")


class AGMAGleasonConicalGearSetCompoundPowerFlow(_4209.ConicalGearSetCompoundPowerFlow):
    """AGMAGleasonConicalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundPowerFlow"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
            parent: "AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4209.ConicalGearSetCompoundPowerFlow":
            return self._parent._cast(_4209.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4235.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(_4235.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4273.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4175.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4188.BevelDifferentialGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4193.BevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.BevelGearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4239.HypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.HypoidGearSetCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4276.SpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4282.StraightBevelDiffGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4285.StraightBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.StraightBevelGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "_4303.ZerolBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4303,
            )

            return self._parent._cast(_4303.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "AGMAGleasonConicalGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4046.AGMAGleasonConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4046.AGMAGleasonConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow":
        return self._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow(self)
