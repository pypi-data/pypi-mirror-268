"""AbstractAssemblyCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4254
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AbstractAssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4040
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4181,
        _4182,
        _4185,
        _4188,
        _4193,
        _4195,
        _4196,
        _4201,
        _4206,
        _4209,
        _4212,
        _4216,
        _4218,
        _4224,
        _4230,
        _4232,
        _4235,
        _4239,
        _4243,
        _4246,
        _4249,
        _4255,
        _4259,
        _4266,
        _4269,
        _4273,
        _4276,
        _4277,
        _4282,
        _4285,
        _4288,
        _4292,
        _4300,
        _4303,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundPowerFlow")


class AbstractAssemblyCompoundPowerFlow(_4254.PartCompoundPowerFlow):
    """AbstractAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyCompoundPowerFlow")

    class _Cast_AbstractAssemblyCompoundPowerFlow:
        """Special nested class for casting AbstractAssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
            parent: "AbstractAssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def part_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4181.AGMAGleasonConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4182.AssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.AssemblyCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4185.BeltDriveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4188.BevelDifferentialGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4193.BevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.BevelGearSetCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4195.BoltedJointCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4196.ClutchCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.ClutchCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4201.ConceptCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4206.ConceptGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4209.ConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4209,
            )

            return self._parent._cast(_4209.ConicalGearSetCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4212.CouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CouplingCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4216.CVTCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.CVTCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4218.CycloidalAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4224.CylindricalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.CylindricalGearSetCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4230.FaceGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(_4230.FaceGearSetCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4232.FlexiblePinAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(_4232.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4235.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(_4235.GearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4239.HypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4243.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(
                _4243.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4246.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(
                _4246.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4249.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(
                _4249.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4255.PartToPartShearCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4259.PlanetaryGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(_4259.PlanetaryGearSetCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4266.RollingRingAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.RollingRingAssemblyCompoundPowerFlow)

        @property
        def root_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4269.RootAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.RootAssemblyCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4273.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4276.SpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4277.SpringDamperCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.SpringDamperCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4282.StraightBevelDiffGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4285.StraightBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.StraightBevelGearSetCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4288.SynchroniserCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.SynchroniserCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4292.TorqueConverterCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.TorqueConverterCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4300.WormGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4300,
            )

            return self._parent._cast(_4300.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "_4303.ZerolBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4303,
            )

            return self._parent._cast(_4303.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "AbstractAssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4040.AbstractAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractAssemblyPowerFlow]

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
    ) -> "List[_4040.AbstractAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractAssemblyPowerFlow]

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
    ) -> "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow":
        return self._Cast_AbstractAssemblyCompoundPowerFlow(self)
