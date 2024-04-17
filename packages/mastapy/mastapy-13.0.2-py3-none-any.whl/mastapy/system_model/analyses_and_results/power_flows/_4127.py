"""PlanetaryGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4090
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "PlanetaryGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4103,
        _4143,
        _4040,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetPowerFlow",)


Self = TypeVar("Self", bound="PlanetaryGearSetPowerFlow")


class PlanetaryGearSetPowerFlow(_4090.CylindricalGearSetPowerFlow):
    """PlanetaryGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetPowerFlow")

    class _Cast_PlanetaryGearSetPowerFlow:
        """Special nested class for casting PlanetaryGearSetPowerFlow to subclasses."""

        def __init__(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
            parent: "PlanetaryGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4090.CylindricalGearSetPowerFlow":
            return self._parent._cast(_4090.CylindricalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4103.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4143.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "PlanetaryGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2549.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow":
        return self._Cast_PlanetaryGearSetPowerFlow(self)
