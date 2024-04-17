"""MASTASettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASTA_SETTINGS = python_net_import("SMT.MastaAPI.SystemModel", "MASTASettings")

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1982
    from mastapy.bearings import _1886, _1887, _1900, _1906
    from mastapy.bolts import _1476, _1478, _1483
    from mastapy.cycloidal import _1464, _1471
    from mastapy.electric_machines import _1291, _1309, _1322
    from mastapy.gears import _319, _320, _346
    from mastapy.gears.gear_designs import _944, _946, _949, _955
    from mastapy.gears.gear_designs.cylindrical import _1015, _1019, _1020, _1025, _1036
    from mastapy.gears.gear_set_pareto_optimiser import (
        _924,
        _925,
        _928,
        _929,
        _931,
        _932,
        _934,
        _935,
        _937,
        _938,
        _939,
        _940,
    )
    from mastapy.gears.ltca.cylindrical import _858
    from mastapy.gears.manufacturing.bevel import _803
    from mastapy.gears.manufacturing.cylindrical.cutters import _708, _714, _719, _720
    from mastapy.gears.manufacturing.cylindrical import _618, _629
    from mastapy.gears.materials import (
        _589,
        _591,
        _592,
        _593,
        _596,
        _599,
        _602,
        _603,
        _610,
    )
    from mastapy.gears.rating.cylindrical import _455, _456, _471, _472
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6592
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5770
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5468
    from mastapy.system_model.analyses_and_results.modal_analyses import _4664
    from mastapy.system_model.analyses_and_results.power_flows import _4131
    from mastapy.system_model.analyses_and_results.stability_analyses import _3879
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3098,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2834
    from mastapy.system_model.drawing import _2259
    from mastapy.system_model.optimization import _2235, _2243
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2571
    from mastapy.system_model.part_model import _2477
    from mastapy.materials import _249, _252, _271, _274, _275
    from mastapy.nodal_analysis import _48, _49, _68
    from mastapy.nodal_analysis.geometry_modeller_link import _163
    from mastapy.shafts import _25, _38, _39
    from mastapy.utility.cad_export import _1839
    from mastapy.utility.databases import _1834
    from mastapy.utility import _1603, _1604
    from mastapy.utility.scripting import _1746
    from mastapy.utility.units_and_measurements import _1613


__docformat__ = "restructuredtext en"
__all__ = ("MASTASettings",)


Self = TypeVar("Self", bound="MASTASettings")


class MASTASettings(_0.APIBase):
    """MASTASettings

    This is a mastapy class.
    """

    TYPE = _MASTA_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MASTASettings")

    class _Cast_MASTASettings:
        """Special nested class for casting MASTASettings to subclasses."""

        def __init__(
            self: "MASTASettings._Cast_MASTASettings", parent: "MASTASettings"
        ):
            self._parent = parent

        @property
        def masta_settings(
            self: "MASTASettings._Cast_MASTASettings",
        ) -> "MASTASettings":
            return self._parent

        def __getattr__(self: "MASTASettings._Cast_MASTASettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MASTASettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def iso14179_settings_database(self: Self) -> "_1982.ISO14179SettingsDatabase":
        """mastapy.bearings.bearing_results.rolling.ISO14179SettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO14179SettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_settings(self: Self) -> "_1886.BearingSettings":
        """mastapy.bearings.BearingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_settings_database(self: Self) -> "_1887.BearingSettingsDatabase":
        """mastapy.bearings.BearingSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rolling_bearing_database(self: Self) -> "_1900.RollingBearingDatabase":
        """mastapy.bearings.RollingBearingDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingBearingDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def skf_settings(self: Self) -> "_1906.SKFSettings":
        """mastapy.bearings.SKFSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bolt_geometry_database(self: Self) -> "_1476.BoltGeometryDatabase":
        """mastapy.bolts.BoltGeometryDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltGeometryDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bolt_material_database(self: Self) -> "_1478.BoltMaterialDatabase":
        """mastapy.bolts.BoltMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def clamped_section_material_database(
        self: Self,
    ) -> "_1483.ClampedSectionMaterialDatabase":
        """mastapy.bolts.ClampedSectionMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClampedSectionMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cycloidal_disc_material_database(
        self: Self,
    ) -> "_1464.CycloidalDiscMaterialDatabase":
        """mastapy.cycloidal.CycloidalDiscMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalDiscMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_pins_material_database(self: Self) -> "_1471.RingPinsMaterialDatabase":
        """mastapy.cycloidal.RingPinsMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPinsMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def magnet_material_database(self: Self) -> "_1291.MagnetMaterialDatabase":
        """mastapy.electric_machines.MagnetMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagnetMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator_rotor_material_database(
        self: Self,
    ) -> "_1309.StatorRotorMaterialDatabase":
        """mastapy.electric_machines.StatorRotorMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorRotorMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def winding_material_database(self: Self) -> "_1322.WindingMaterialDatabase":
        """mastapy.electric_machines.WindingMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_hypoid_gear_design_settings(
        self: Self,
    ) -> "_319.BevelHypoidGearDesignSettings":
        """mastapy.gears.BevelHypoidGearDesignSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearDesignSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_hypoid_gear_rating_settings(
        self: Self,
    ) -> "_320.BevelHypoidGearRatingSettings":
        """mastapy.gears.BevelHypoidGearRatingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_hypoid_gear_design_settings_database(
        self: Self,
    ) -> "_944.BevelHypoidGearDesignSettingsDatabase":
        """mastapy.gears.gear_designs.BevelHypoidGearDesignSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearDesignSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_hypoid_gear_rating_settings_database(
        self: Self,
    ) -> "_946.BevelHypoidGearRatingSettingsDatabase":
        """mastapy.gears.gear_designs.BevelHypoidGearRatingSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelHypoidGearRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_defaults(self: Self) -> "_1015.CylindricalGearDefaults":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDefaults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDefaults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_constraints_database(
        self: Self,
    ) -> "_1019.CylindricalGearDesignConstraintsDatabase":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesignConstraintsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignConstraintsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_constraint_settings(
        self: Self,
    ) -> "_1020.CylindricalGearDesignConstraintSettings":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesignConstraintSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignConstraintSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_micro_geometry_settings_database(
        self: Self,
    ) -> "_1025.CylindricalGearMicroGeometrySettingsDatabase":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMicroGeometrySettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMicroGeometrySettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set_micro_geometry_settings(
        self: Self,
    ) -> "_1036.CylindricalGearSetMicroGeometrySettings":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetMicroGeometrySettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetMicroGeometrySettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_constraint_collection_database(
        self: Self,
    ) -> "_949.DesignConstraintCollectionDatabase":
        """mastapy.gears.gear_designs.DesignConstraintCollectionDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignConstraintCollectionDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_design_constraints_collection(
        self: Self,
    ) -> "_955.SelectedDesignConstraintsCollection":
        """mastapy.gears.gear_designs.SelectedDesignConstraintsCollection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedDesignConstraintsCollection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry_gear_set_design_space_search_strategy_database(
        self: Self,
    ) -> "_924.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
        self: Self,
    ) -> "_925.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
        self: Self,
    ) -> "_928.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_cylindrical_gear_set_optimisation_strategy_database(
        self: Self,
    ) -> "_929.ParetoCylindricalGearSetOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoCylindricalGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoCylindricalGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
        self: Self,
    ) -> "_931.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_face_gear_set_optimisation_strategy_database(
        self: Self,
    ) -> "_932.ParetoFaceGearSetOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoFaceGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoFaceGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
        self: Self,
    ) -> "_934.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_hypoid_gear_set_optimisation_strategy_database(
        self: Self,
    ) -> "_935.ParetoHypoidGearSetOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoHypoidGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoHypoidGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
        self: Self,
    ) -> "_937.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
        self: Self,
    ) -> "_938.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoSpiralBevelGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoSpiralBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
        self: Self,
    ) -> "_939.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pareto_straight_bevel_gear_set_optimisation_strategy_database(
        self: Self,
    ) -> "_940.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
        """mastapy.gears.gear_set_pareto_optimiser.ParetoStraightBevelGearSetOptimisationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParetoStraightBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_fe_settings(self: Self) -> "_858.CylindricalGearFESettings":
        """mastapy.gears.ltca.cylindrical.CylindricalGearFESettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearFESettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def manufacturing_machine_database(
        self: Self,
    ) -> "_803.ManufacturingMachineDatabase":
        """mastapy.gears.manufacturing.bevel.ManufacturingMachineDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturingMachineDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_formed_wheel_grinder_database(
        self: Self,
    ) -> "_708.CylindricalFormedWheelGrinderDatabase":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalFormedWheelGrinderDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalFormedWheelGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_plunge_shaver_database(
        self: Self,
    ) -> "_714.CylindricalGearPlungeShaverDatabase":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearPlungeShaverDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearPlungeShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_shaver_database(
        self: Self,
    ) -> "_719.CylindricalGearShaverDatabase":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearShaverDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_worm_grinder_database(
        self: Self,
    ) -> "_720.CylindricalWormGrinderDatabase":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalWormGrinderDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalWormGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_hob_database(self: Self) -> "_618.CylindricalHobDatabase":
        """mastapy.gears.manufacturing.cylindrical.CylindricalHobDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalHobDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_shaper_database(self: Self) -> "_629.CylindricalShaperDatabase":
        """mastapy.gears.manufacturing.cylindrical.CylindricalShaperDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalShaperDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_iso_material_database(
        self: Self,
    ) -> "_589.BevelGearISOMaterialDatabase":
        """mastapy.gears.materials.BevelGearISOMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearISOMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_material_database(self: Self) -> "_591.BevelGearMaterialDatabase":
        """mastapy.gears.materials.BevelGearMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_agma_material_database(
        self: Self,
    ) -> "_592.CylindricalGearAGMAMaterialDatabase":
        """mastapy.gears.materials.CylindricalGearAGMAMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearAGMAMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_iso_material_database(
        self: Self,
    ) -> "_593.CylindricalGearISOMaterialDatabase":
        """mastapy.gears.materials.CylindricalGearISOMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearISOMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_plastic_material_database(
        self: Self,
    ) -> "_596.CylindricalGearPlasticMaterialDatabase":
        """mastapy.gears.materials.CylindricalGearPlasticMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearPlasticMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_material_expert_system_factor_settings(
        self: Self,
    ) -> "_599.GearMaterialExpertSystemFactorSettings":
        """mastapy.gears.materials.GearMaterialExpertSystemFactorSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMaterialExpertSystemFactorSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isotr1417912001_coefficient_of_friction_constants_database(
        self: Self,
    ) -> "_602.ISOTR1417912001CoefficientOfFrictionConstantsDatabase":
        """mastapy.gears.materials.ISOTR1417912001CoefficientOfFrictionConstantsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTR1417912001CoefficientOfFrictionConstantsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_conical_gear_material_database(
        self: Self,
    ) -> "_603.KlingelnbergConicalGearMaterialDatabase":
        """mastapy.gears.materials.KlingelnbergConicalGearMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergConicalGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def raw_material_database(self: Self) -> "_610.RawMaterialDatabase":
        """mastapy.gears.materials.RawMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RawMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pocketing_power_loss_coefficients_database(
        self: Self,
    ) -> "_346.PocketingPowerLossCoefficientsDatabase":
        """mastapy.gears.PocketingPowerLossCoefficientsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PocketingPowerLossCoefficientsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_and_rating_settings(
        self: Self,
    ) -> "_455.CylindricalGearDesignAndRatingSettings":
        """mastapy.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignAndRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_design_and_rating_settings_database(
        self: Self,
    ) -> "_456.CylindricalGearDesignAndRatingSettingsDatabase":
        """mastapy.gears.rating.cylindrical.CylindricalGearDesignAndRatingSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDesignAndRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_plastic_gear_rating_settings(
        self: Self,
    ) -> "_471.CylindricalPlasticGearRatingSettings":
        """mastapy.gears.rating.cylindrical.CylindricalPlasticGearRatingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalPlasticGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_plastic_gear_rating_settings_database(
        self: Self,
    ) -> "_472.CylindricalPlasticGearRatingSettingsDatabase":
        """mastapy.gears.rating.cylindrical.CylindricalPlasticGearRatingSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalPlasticGearRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def critical_speed_analysis_draw_style(
        self: Self,
    ) -> "_6592.CriticalSpeedAnalysisDrawStyle":
        """mastapy.system_model.analyses_and_results.critical_speed_analyses.CriticalSpeedAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSpeedAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_draw_style(self: Self) -> "_5770.HarmonicAnalysisDrawStyle":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mbd_analysis_draw_style(self: Self) -> "_5468.MBDAnalysisDrawStyle":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MBDAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MBDAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis_draw_style(self: Self) -> "_4664.ModalAnalysisDrawStyle":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_draw_style(self: Self) -> "_4131.PowerFlowDrawStyle":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlowDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stability_analysis_draw_style(self: Self) -> "_3879.StabilityAnalysisDrawStyle":
        """mastapy.system_model.analyses_and_results.stability_analyses.StabilityAnalysisDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StabilityAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response_draw_style(
        self: Self,
    ) -> "_3098.SteadyStateSynchronousResponseDrawStyle":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SteadyStateSynchronousResponseDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_draw_style(self: Self) -> "_2834.SystemDeflectionDrawStyle":
        """mastapy.system_model.analyses_and_results.system_deflections.SystemDeflectionDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def model_view_options_draw_style(self: Self) -> "_2259.ModelViewOptionsDrawStyle":
        """mastapy.system_model.drawing.ModelViewOptionsDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModelViewOptionsDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_optimization_strategy_database(
        self: Self,
    ) -> "_2235.ConicalGearOptimizationStrategyDatabase":
        """mastapy.system_model.optimization.ConicalGearOptimizationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearOptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def optimization_strategy_database(
        self: Self,
    ) -> "_2243.OptimizationStrategyDatabase":
        """mastapy.system_model.optimization.OptimizationStrategyDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def supercharger_rotor_set_database(
        self: Self,
    ) -> "_2571.SuperchargerRotorSetDatabase":
        """mastapy.system_model.part_model.gears.supercharger_rotor_set.SuperchargerRotorSetDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SuperchargerRotorSetDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planet_carrier_settings(self: Self) -> "_2477.PlanetCarrierSettings":
        """mastapy.system_model.part_model.PlanetCarrierSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetCarrierSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_material_database(self: Self) -> "_249.BearingMaterialDatabase":
        """mastapy.materials.BearingMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_material_database(self: Self) -> "_252.ComponentMaterialDatabase":
        """mastapy.materials.ComponentMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lubrication_detail_database(self: Self) -> "_271.LubricationDetailDatabase":
        """mastapy.materials.LubricationDetailDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricationDetailDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def materials_settings(self: Self) -> "_274.MaterialsSettings":
        """mastapy.materials.MaterialsSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def materials_settings_database(self: Self) -> "_275.MaterialsSettingsDatabase":
        """mastapy.materials.MaterialsSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialsSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def analysis_settings(self: Self) -> "_48.AnalysisSettings":
        """mastapy.nodal_analysis.AnalysisSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def analysis_settings_database(self: Self) -> "_49.AnalysisSettingsDatabase":
        """mastapy.nodal_analysis.AnalysisSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fe_user_settings(self: Self) -> "_68.FEUserSettings":
        """mastapy.nodal_analysis.FEUserSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEUserSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def geometry_modeller_settings(self: Self) -> "_163.GeometryModellerSettings":
        """mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryModellerSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_material_database(self: Self) -> "_25.ShaftMaterialDatabase":
        """mastapy.shafts.ShaftMaterialDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_settings(self: Self) -> "_38.ShaftSettings":
        """mastapy.shafts.ShaftSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_settings_database(self: Self) -> "_39.ShaftSettingsDatabase":
        """mastapy.shafts.ShaftSettingsDatabase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cad_export_settings(self: Self) -> "_1839.CADExportSettings":
        """mastapy.utility.cad_export.CADExportSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CADExportSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def database_settings(self: Self) -> "_1834.DatabaseSettings":
        """mastapy.utility.databases.DatabaseSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DatabaseSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def program_settings(self: Self) -> "_1603.ProgramSettings":
        """mastapy.utility.ProgramSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProgramSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pushbullet_settings(self: Self) -> "_1604.PushbulletSettings":
        """mastapy.utility.PushbulletSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PushbulletSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def scripting_setup(self: Self) -> "_1746.ScriptingSetup":
        """mastapy.utility.scripting.ScriptingSetup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScriptingSetup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def measurement_settings(self: Self) -> "_1613.MeasurementSettings":
        """mastapy.utility.units_and_measurements.MeasurementSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeasurementSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "MASTASettings._Cast_MASTASettings":
        return self._Cast_MASTASettings(self)
