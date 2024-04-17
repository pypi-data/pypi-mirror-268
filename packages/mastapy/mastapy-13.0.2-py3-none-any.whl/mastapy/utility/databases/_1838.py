"""SQLDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.databases import _1831
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SQL_DATABASE = python_net_import("SMT.MastaAPI.Utility.Databases", "SQLDatabase")

if TYPE_CHECKING:
    from mastapy.utility.databases import _1833, _1835
    from mastapy.shafts import _25, _39
    from mastapy.nodal_analysis import _49
    from mastapy.materials import _249, _252, _271, _273, _275
    from mastapy.gears import _346
    from mastapy.gears.rating.cylindrical import _456, _472
    from mastapy.gears.materials import (
        _587,
        _589,
        _591,
        _592,
        _593,
        _595,
        _596,
        _598,
        _602,
        _603,
        _610,
    )
    from mastapy.gears.manufacturing.cylindrical import _613, _618, _629
    from mastapy.gears.manufacturing.cylindrical.cutters import _708, _714, _719, _720
    from mastapy.gears.manufacturing.bevel import _803
    from mastapy.gears.gear_set_pareto_optimiser import (
        _922,
        _924,
        _925,
        _927,
        _928,
        _929,
        _930,
        _931,
        _932,
        _933,
        _934,
        _935,
        _937,
        _938,
        _939,
        _940,
    )
    from mastapy.gears.gear_designs import _944, _946, _949
    from mastapy.gears.gear_designs.cylindrical import _1019, _1025
    from mastapy.electric_machines import _1291, _1309, _1322
    from mastapy.cycloidal import _1464, _1471
    from mastapy.bolts import _1474, _1476, _1478, _1483
    from mastapy.math_utility.optimisation import _1547, _1559
    from mastapy.bearings import _1887, _1900
    from mastapy.bearings.bearing_results.rolling import _1982
    from mastapy.system_model.optimization import _2235, _2243
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2571


__docformat__ = "restructuredtext en"
__all__ = ("SQLDatabase",)


Self = TypeVar("Self", bound="SQLDatabase")
TKey = TypeVar("TKey", bound="_1833.DatabaseKey")
TValue = TypeVar("TValue", bound="_0.APIBase")


class SQLDatabase(_1831.Database[TKey, TValue]):
    """SQLDatabase

    This is a mastapy class.

    Generic Types:
        TKey
        TValue
    """

    TYPE = _SQL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SQLDatabase")

    class _Cast_SQLDatabase:
        """Special nested class for casting SQLDatabase to subclasses."""

        def __init__(self: "SQLDatabase._Cast_SQLDatabase", parent: "SQLDatabase"):
            self._parent = parent

        @property
        def database(self: "SQLDatabase._Cast_SQLDatabase") -> "_1831.Database":
            return self._parent._cast(_1831.Database)

        @property
        def shaft_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_25.ShaftMaterialDatabase":
            from mastapy.shafts import _25

            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def shaft_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_39.ShaftSettingsDatabase":
            from mastapy.shafts import _39

            return self._parent._cast(_39.ShaftSettingsDatabase)

        @property
        def analysis_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_49.AnalysisSettingsDatabase":
            from mastapy.nodal_analysis import _49

            return self._parent._cast(_49.AnalysisSettingsDatabase)

        @property
        def bearing_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_249.BearingMaterialDatabase":
            from mastapy.materials import _249

            return self._parent._cast(_249.BearingMaterialDatabase)

        @property
        def component_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_252.ComponentMaterialDatabase":
            from mastapy.materials import _252

            return self._parent._cast(_252.ComponentMaterialDatabase)

        @property
        def lubrication_detail_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_271.LubricationDetailDatabase":
            from mastapy.materials import _271

            return self._parent._cast(_271.LubricationDetailDatabase)

        @property
        def material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_273.MaterialDatabase":
            from mastapy.materials import _273

            return self._parent._cast(_273.MaterialDatabase)

        @property
        def materials_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_275.MaterialsSettingsDatabase":
            from mastapy.materials import _275

            return self._parent._cast(_275.MaterialsSettingsDatabase)

        @property
        def pocketing_power_loss_coefficients_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_346.PocketingPowerLossCoefficientsDatabase":
            from mastapy.gears import _346

            return self._parent._cast(_346.PocketingPowerLossCoefficientsDatabase)

        @property
        def cylindrical_gear_design_and_rating_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_456.CylindricalGearDesignAndRatingSettingsDatabase":
            from mastapy.gears.rating.cylindrical import _456

            return self._parent._cast(
                _456.CylindricalGearDesignAndRatingSettingsDatabase
            )

        @property
        def cylindrical_plastic_gear_rating_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_472.CylindricalPlasticGearRatingSettingsDatabase":
            from mastapy.gears.rating.cylindrical import _472

            return self._parent._cast(_472.CylindricalPlasticGearRatingSettingsDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_587.BevelGearAbstractMaterialDatabase":
            from mastapy.gears.materials import _587

            return self._parent._cast(_587.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_589.BevelGearISOMaterialDatabase":
            from mastapy.gears.materials import _589

            return self._parent._cast(_589.BevelGearISOMaterialDatabase)

        @property
        def bevel_gear_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_591.BevelGearMaterialDatabase":
            from mastapy.gears.materials import _591

            return self._parent._cast(_591.BevelGearMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_592.CylindricalGearAGMAMaterialDatabase":
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_593.CylindricalGearISOMaterialDatabase":
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_595.CylindricalGearMaterialDatabase":
            from mastapy.gears.materials import _595

            return self._parent._cast(_595.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_596.CylindricalGearPlasticMaterialDatabase":
            from mastapy.gears.materials import _596

            return self._parent._cast(_596.CylindricalGearPlasticMaterialDatabase)

        @property
        def gear_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_598.GearMaterialDatabase":
            from mastapy.gears.materials import _598

            return self._parent._cast(_598.GearMaterialDatabase)

        @property
        def isotr1417912001_coefficient_of_friction_constants_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_602.ISOTR1417912001CoefficientOfFrictionConstantsDatabase":
            from mastapy.gears.materials import _602

            return self._parent._cast(
                _602.ISOTR1417912001CoefficientOfFrictionConstantsDatabase
            )

        @property
        def klingelnberg_conical_gear_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_603.KlingelnbergConicalGearMaterialDatabase":
            from mastapy.gears.materials import _603

            return self._parent._cast(_603.KlingelnbergConicalGearMaterialDatabase)

        @property
        def raw_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_610.RawMaterialDatabase":
            from mastapy.gears.materials import _610

            return self._parent._cast(_610.RawMaterialDatabase)

        @property
        def cylindrical_cutter_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_613.CylindricalCutterDatabase":
            from mastapy.gears.manufacturing.cylindrical import _613

            return self._parent._cast(_613.CylindricalCutterDatabase)

        @property
        def cylindrical_hob_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_618.CylindricalHobDatabase":
            from mastapy.gears.manufacturing.cylindrical import _618

            return self._parent._cast(_618.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_629.CylindricalShaperDatabase":
            from mastapy.gears.manufacturing.cylindrical import _629

            return self._parent._cast(_629.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_708.CylindricalFormedWheelGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _708

            return self._parent._cast(_708.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_714.CylindricalGearPlungeShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _714

            return self._parent._cast(_714.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_719.CylindricalGearShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _719

            return self._parent._cast(_719.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_720.CylindricalWormGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _720

            return self._parent._cast(_720.CylindricalWormGrinderDatabase)

        @property
        def manufacturing_machine_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_803.ManufacturingMachineDatabase":
            from mastapy.gears.manufacturing.bevel import _803

            return self._parent._cast(_803.ManufacturingMachineDatabase)

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_922.MicroGeometryDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _922

            return self._parent._cast(
                _922.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_924.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _924

            return self._parent._cast(
                _924.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_925.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_927.ParetoConicalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(
                _927.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_928.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_929.ParetoCylindricalGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_930.ParetoCylindricalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(
                _930.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_931.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_932.ParetoFaceGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _932

            return self._parent._cast(
                _932.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_933.ParetoFaceRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _933

            return self._parent._cast(_933.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_934.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_935.ParetoHypoidGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_937.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _937

            return self._parent._cast(
                _937.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_938.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _938

            return self._parent._cast(
                _938.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_939.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _939

            return self._parent._cast(
                _939.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_940.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _940

            return self._parent._cast(
                _940.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def bevel_hypoid_gear_design_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_944.BevelHypoidGearDesignSettingsDatabase":
            from mastapy.gears.gear_designs import _944

            return self._parent._cast(_944.BevelHypoidGearDesignSettingsDatabase)

        @property
        def bevel_hypoid_gear_rating_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_946.BevelHypoidGearRatingSettingsDatabase":
            from mastapy.gears.gear_designs import _946

            return self._parent._cast(_946.BevelHypoidGearRatingSettingsDatabase)

        @property
        def design_constraint_collection_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_949.DesignConstraintCollectionDatabase":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.DesignConstraintCollectionDatabase)

        @property
        def cylindrical_gear_design_constraints_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1019.CylindricalGearDesignConstraintsDatabase":
            from mastapy.gears.gear_designs.cylindrical import _1019

            return self._parent._cast(_1019.CylindricalGearDesignConstraintsDatabase)

        @property
        def cylindrical_gear_micro_geometry_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1025.CylindricalGearMicroGeometrySettingsDatabase":
            from mastapy.gears.gear_designs.cylindrical import _1025

            return self._parent._cast(
                _1025.CylindricalGearMicroGeometrySettingsDatabase
            )

        @property
        def magnet_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1291.MagnetMaterialDatabase":
            from mastapy.electric_machines import _1291

            return self._parent._cast(_1291.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1309.StatorRotorMaterialDatabase":
            from mastapy.electric_machines import _1309

            return self._parent._cast(_1309.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1322.WindingMaterialDatabase":
            from mastapy.electric_machines import _1322

            return self._parent._cast(_1322.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1464.CycloidalDiscMaterialDatabase":
            from mastapy.cycloidal import _1464

            return self._parent._cast(_1464.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1471.RingPinsMaterialDatabase":
            from mastapy.cycloidal import _1471

            return self._parent._cast(_1471.RingPinsMaterialDatabase)

        @property
        def bolted_joint_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1474.BoltedJointMaterialDatabase":
            from mastapy.bolts import _1474

            return self._parent._cast(_1474.BoltedJointMaterialDatabase)

        @property
        def bolt_geometry_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1476.BoltGeometryDatabase":
            from mastapy.bolts import _1476

            return self._parent._cast(_1476.BoltGeometryDatabase)

        @property
        def bolt_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1478.BoltMaterialDatabase":
            from mastapy.bolts import _1478

            return self._parent._cast(_1478.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1483.ClampedSectionMaterialDatabase":
            from mastapy.bolts import _1483

            return self._parent._cast(_1483.ClampedSectionMaterialDatabase)

        @property
        def design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1547.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1547

            return self._parent._cast(_1547.DesignSpaceSearchStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1559.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1559

            return self._parent._cast(_1559.ParetoOptimisationStrategyDatabase)

        @property
        def named_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1835.NamedDatabase":
            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def bearing_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1887.BearingSettingsDatabase":
            from mastapy.bearings import _1887

            return self._parent._cast(_1887.BearingSettingsDatabase)

        @property
        def rolling_bearing_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1900.RollingBearingDatabase":
            from mastapy.bearings import _1900

            return self._parent._cast(_1900.RollingBearingDatabase)

        @property
        def iso14179_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1982.ISO14179SettingsDatabase":
            from mastapy.bearings.bearing_results.rolling import _1982

            return self._parent._cast(_1982.ISO14179SettingsDatabase)

        @property
        def conical_gear_optimization_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_2235.ConicalGearOptimizationStrategyDatabase":
            from mastapy.system_model.optimization import _2235

            return self._parent._cast(_2235.ConicalGearOptimizationStrategyDatabase)

        @property
        def optimization_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_2243.OptimizationStrategyDatabase":
            from mastapy.system_model.optimization import _2243

            return self._parent._cast(_2243.OptimizationStrategyDatabase)

        @property
        def supercharger_rotor_set_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_2571.SuperchargerRotorSetDatabase":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2571,
            )

            return self._parent._cast(_2571.SuperchargerRotorSetDatabase)

        @property
        def sql_database(self: "SQLDatabase._Cast_SQLDatabase") -> "SQLDatabase":
            return self._parent

        def __getattr__(self: "SQLDatabase._Cast_SQLDatabase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SQLDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allow_network_database(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowNetworkDatabase

        if temp is None:
            return False

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def uses_database(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UsesDatabase

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def delete(self: Self, key: "TKey"):
        """Method does not return.

        Args:
            key (TKey)
        """
        self.wrapped.Delete(key)

    def reload(self: Self):
        """Method does not return."""
        self.wrapped.Reload()

    @enforce_parameter_types
    def save(self: Self, item: "TValue"):
        """Method does not return.

        Args:
            item (TValue)
        """
        self.wrapped.Save(item)

    @property
    def cast_to(self: Self) -> "SQLDatabase._Cast_SQLDatabase":
        return self._Cast_SQLDatabase(self)
