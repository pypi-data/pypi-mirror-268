"""CylindricalGearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CylindricalGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.gears.rating.cylindrical import _466
    from mastapy.system_model.analyses_and_results.power_flows import _4090
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4222,
        _4223,
        _4259,
        _4273,
        _4175,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="CylindricalGearSetCompoundPowerFlow")


class CylindricalGearSetCompoundPowerFlow(_4235.GearSetCompoundPowerFlow):
    """CylindricalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetCompoundPowerFlow")

    class _Cast_CylindricalGearSetCompoundPowerFlow:
        """Special nested class for casting CylindricalGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
            parent: "CylindricalGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_compound_power_flow(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
        ) -> "_4235.GearSetCompoundPowerFlow":
            return self._parent._cast(_4235.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
        ) -> "_4273.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
        ) -> "_4175.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
        ) -> "_4259.PlanetaryGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(_4259.PlanetaryGearSetCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
        ) -> "CylindricalGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "CylindricalGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2533.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_duty_cycle_rating(
        self: Self,
    ) -> "_466.CylindricalGearSetDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_duty_cycle_rating(
        self: Self,
    ) -> "_466.CylindricalGearSetDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4090.CylindricalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalGearSetPowerFlow]

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
    def cylindrical_gears_compound_power_flow(
        self: Self,
    ) -> "List[_4222.CylindricalGearCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CylindricalGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_compound_power_flow(
        self: Self,
    ) -> "List[_4223.CylindricalGearMeshCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CylindricalGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ratings_for_all_designs(
        self: Self,
    ) -> "List[_466.CylindricalGearSetDutyCycleRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingsForAllDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4090.CylindricalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalGearSetPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearSetCompoundPowerFlow._Cast_CylindricalGearSetCompoundPowerFlow"
    ):
        return self._Cast_CylindricalGearSetCompoundPowerFlow(self)
