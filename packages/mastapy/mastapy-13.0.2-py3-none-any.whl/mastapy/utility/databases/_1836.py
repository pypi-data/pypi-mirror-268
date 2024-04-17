"""NamedDatabaseItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_DATABASE_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Databases", "NamedDatabaseItem"
)

if TYPE_CHECKING:
    from mastapy.utility import _1589
    from mastapy.utility.databases import _1837
    from mastapy.shafts import _24, _40, _43
    from mastapy.nodal_analysis import _50
    from mastapy.materials import _248, _270, _272, _276
    from mastapy.gears import _345
    from mastapy.gears.rating.cylindrical import _457, _473
    from mastapy.gears.materials import (
        _586,
        _588,
        _590,
        _594,
        _597,
        _600,
        _601,
        _604,
        _606,
        _609,
    )
    from mastapy.gears.manufacturing.cylindrical.cutters import (
        _709,
        _710,
        _711,
        _712,
        _713,
        _715,
        _716,
        _717,
        _718,
        _721,
    )
    from mastapy.gears.manufacturing.bevel import _802
    from mastapy.gears.gear_designs import _945, _947, _950
    from mastapy.gears.gear_designs.cylindrical import _1018, _1026
    from mastapy.electric_machines import _1290, _1308, _1321
    from mastapy.detailed_rigid_connectors.splines import _1423
    from mastapy.cycloidal import _1463, _1470
    from mastapy.bolts import _1473, _1475, _1477
    from mastapy.math_utility.optimisation import _1556
    from mastapy.bearings import _1888
    from mastapy.bearings.bearing_results.rolling import _1981
    from mastapy.system_model.optimization import _2233, _2236, _2241, _2242
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2570


__docformat__ = "restructuredtext en"
__all__ = ("NamedDatabaseItem",)


Self = TypeVar("Self", bound="NamedDatabaseItem")


class NamedDatabaseItem(_0.APIBase):
    """NamedDatabaseItem

    This is a mastapy class.
    """

    TYPE = _NAMED_DATABASE_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedDatabaseItem")

    class _Cast_NamedDatabaseItem:
        """Special nested class for casting NamedDatabaseItem to subclasses."""

        def __init__(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
            parent: "NamedDatabaseItem",
        ):
            self._parent = parent

        @property
        def shaft_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_24.ShaftMaterial":
            from mastapy.shafts import _24

            return self._parent._cast(_24.ShaftMaterial)

        @property
        def shaft_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_40.ShaftSettingsItem":
            from mastapy.shafts import _40

            return self._parent._cast(_40.ShaftSettingsItem)

        @property
        def simple_shaft_definition(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_43.SimpleShaftDefinition":
            from mastapy.shafts import _43

            return self._parent._cast(_43.SimpleShaftDefinition)

        @property
        def analysis_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_50.AnalysisSettingsItem":
            from mastapy.nodal_analysis import _50

            return self._parent._cast(_50.AnalysisSettingsItem)

        @property
        def bearing_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_248.BearingMaterial":
            from mastapy.materials import _248

            return self._parent._cast(_248.BearingMaterial)

        @property
        def lubrication_detail(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_270.LubricationDetail":
            from mastapy.materials import _270

            return self._parent._cast(_270.LubricationDetail)

        @property
        def material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_272.Material":
            from mastapy.materials import _272

            return self._parent._cast(_272.Material)

        @property
        def materials_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_276.MaterialsSettingsItem":
            from mastapy.materials import _276

            return self._parent._cast(_276.MaterialsSettingsItem)

        @property
        def pocketing_power_loss_coefficients(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_345.PocketingPowerLossCoefficients":
            from mastapy.gears import _345

            return self._parent._cast(_345.PocketingPowerLossCoefficients)

        @property
        def cylindrical_gear_design_and_rating_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_457.CylindricalGearDesignAndRatingSettingsItem":
            from mastapy.gears.rating.cylindrical import _457

            return self._parent._cast(_457.CylindricalGearDesignAndRatingSettingsItem)

        @property
        def cylindrical_plastic_gear_rating_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_473.CylindricalPlasticGearRatingSettingsItem":
            from mastapy.gears.rating.cylindrical import _473

            return self._parent._cast(_473.CylindricalPlasticGearRatingSettingsItem)

        @property
        def agma_cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_586.AGMACylindricalGearMaterial":
            from mastapy.gears.materials import _586

            return self._parent._cast(_586.AGMACylindricalGearMaterial)

        @property
        def bevel_gear_iso_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_588.BevelGearISOMaterial":
            from mastapy.gears.materials import _588

            return self._parent._cast(_588.BevelGearISOMaterial)

        @property
        def bevel_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_590.BevelGearMaterial":
            from mastapy.gears.materials import _590

            return self._parent._cast(_590.BevelGearMaterial)

        @property
        def cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_594.CylindricalGearMaterial":
            from mastapy.gears.materials import _594

            return self._parent._cast(_594.CylindricalGearMaterial)

        @property
        def gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_597.GearMaterial":
            from mastapy.gears.materials import _597

            return self._parent._cast(_597.GearMaterial)

        @property
        def iso_cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_600.ISOCylindricalGearMaterial":
            from mastapy.gears.materials import _600

            return self._parent._cast(_600.ISOCylindricalGearMaterial)

        @property
        def isotr1417912001_coefficient_of_friction_constants(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_601.ISOTR1417912001CoefficientOfFrictionConstants":
            from mastapy.gears.materials import _601

            return self._parent._cast(
                _601.ISOTR1417912001CoefficientOfFrictionConstants
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_604.KlingelnbergCycloPalloidConicalGearMaterial":
            from mastapy.gears.materials import _604

            return self._parent._cast(_604.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_606.PlasticCylindricalGearMaterial":
            from mastapy.gears.materials import _606

            return self._parent._cast(_606.PlasticCylindricalGearMaterial)

        @property
        def raw_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_609.RawMaterial":
            from mastapy.gears.materials import _609

            return self._parent._cast(_609.RawMaterial)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_709.CylindricalGearAbstractCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _709

            return self._parent._cast(_709.CylindricalGearAbstractCutterDesign)

        @property
        def cylindrical_gear_form_grinding_wheel(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_710.CylindricalGearFormGrindingWheel":
            from mastapy.gears.manufacturing.cylindrical.cutters import _710

            return self._parent._cast(_710.CylindricalGearFormGrindingWheel)

        @property
        def cylindrical_gear_grinding_worm(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_711.CylindricalGearGrindingWorm":
            from mastapy.gears.manufacturing.cylindrical.cutters import _711

            return self._parent._cast(_711.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_712.CylindricalGearHobDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _712

            return self._parent._cast(_712.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_plunge_shaver(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_713.CylindricalGearPlungeShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _713

            return self._parent._cast(_713.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_rack_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_715.CylindricalGearRackDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _715

            return self._parent._cast(_715.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_real_cutter_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_716.CylindricalGearRealCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _716

            return self._parent._cast(_716.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_shaper(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_717.CylindricalGearShaper":
            from mastapy.gears.manufacturing.cylindrical.cutters import _717

            return self._parent._cast(_717.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_718.CylindricalGearShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _718

            return self._parent._cast(_718.CylindricalGearShaver)

        @property
        def involute_cutter_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_721.InvoluteCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _721

            return self._parent._cast(_721.InvoluteCutterDesign)

        @property
        def manufacturing_machine(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_802.ManufacturingMachine":
            from mastapy.gears.manufacturing.bevel import _802

            return self._parent._cast(_802.ManufacturingMachine)

        @property
        def bevel_hypoid_gear_design_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_945.BevelHypoidGearDesignSettingsItem":
            from mastapy.gears.gear_designs import _945

            return self._parent._cast(_945.BevelHypoidGearDesignSettingsItem)

        @property
        def bevel_hypoid_gear_rating_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_947.BevelHypoidGearRatingSettingsItem":
            from mastapy.gears.gear_designs import _947

            return self._parent._cast(_947.BevelHypoidGearRatingSettingsItem)

        @property
        def design_constraints_collection(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_950.DesignConstraintsCollection":
            from mastapy.gears.gear_designs import _950

            return self._parent._cast(_950.DesignConstraintsCollection)

        @property
        def cylindrical_gear_design_constraints(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1018.CylindricalGearDesignConstraints":
            from mastapy.gears.gear_designs.cylindrical import _1018

            return self._parent._cast(_1018.CylindricalGearDesignConstraints)

        @property
        def cylindrical_gear_micro_geometry_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1026.CylindricalGearMicroGeometrySettingsItem":
            from mastapy.gears.gear_designs.cylindrical import _1026

            return self._parent._cast(_1026.CylindricalGearMicroGeometrySettingsItem)

        @property
        def magnet_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1290.MagnetMaterial":
            from mastapy.electric_machines import _1290

            return self._parent._cast(_1290.MagnetMaterial)

        @property
        def stator_rotor_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1308.StatorRotorMaterial":
            from mastapy.electric_machines import _1308

            return self._parent._cast(_1308.StatorRotorMaterial)

        @property
        def winding_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1321.WindingMaterial":
            from mastapy.electric_machines import _1321

            return self._parent._cast(_1321.WindingMaterial)

        @property
        def spline_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1423.SplineMaterial":
            from mastapy.detailed_rigid_connectors.splines import _1423

            return self._parent._cast(_1423.SplineMaterial)

        @property
        def cycloidal_disc_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1463.CycloidalDiscMaterial":
            from mastapy.cycloidal import _1463

            return self._parent._cast(_1463.CycloidalDiscMaterial)

        @property
        def ring_pins_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1470.RingPinsMaterial":
            from mastapy.cycloidal import _1470

            return self._parent._cast(_1470.RingPinsMaterial)

        @property
        def bolted_joint_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1473.BoltedJointMaterial":
            from mastapy.bolts import _1473

            return self._parent._cast(_1473.BoltedJointMaterial)

        @property
        def bolt_geometry(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1475.BoltGeometry":
            from mastapy.bolts import _1475

            return self._parent._cast(_1475.BoltGeometry)

        @property
        def bolt_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1477.BoltMaterial":
            from mastapy.bolts import _1477

            return self._parent._cast(_1477.BoltMaterial)

        @property
        def pareto_optimisation_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1556.ParetoOptimisationStrategy":
            from mastapy.math_utility.optimisation import _1556

            return self._parent._cast(_1556.ParetoOptimisationStrategy)

        @property
        def bearing_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1888.BearingSettingsItem":
            from mastapy.bearings import _1888

            return self._parent._cast(_1888.BearingSettingsItem)

        @property
        def iso14179_settings(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1981.ISO14179Settings":
            from mastapy.bearings.bearing_results.rolling import _1981

            return self._parent._cast(_1981.ISO14179Settings)

        @property
        def conical_gear_optimisation_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2233.ConicalGearOptimisationStrategy":
            from mastapy.system_model.optimization import _2233

            return self._parent._cast(_2233.ConicalGearOptimisationStrategy)

        @property
        def cylindrical_gear_optimisation_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2236.CylindricalGearOptimisationStrategy":
            from mastapy.system_model.optimization import _2236

            return self._parent._cast(_2236.CylindricalGearOptimisationStrategy)

        @property
        def optimization_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2241.OptimizationStrategy":
            from mastapy.system_model.optimization import _2241

            return self._parent._cast(_2241.OptimizationStrategy)

        @property
        def optimization_strategy_base(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2242.OptimizationStrategyBase":
            from mastapy.system_model.optimization import _2242

            return self._parent._cast(_2242.OptimizationStrategyBase)

        @property
        def supercharger_rotor_set(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2570.SuperchargerRotorSet":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2570,
            )

            return self._parent._cast(_2570.SuperchargerRotorSet)

        @property
        def named_database_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "NamedDatabaseItem":
            return self._parent

        def __getattr__(self: "NamedDatabaseItem._Cast_NamedDatabaseItem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedDatabaseItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

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
    def no_history(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NoHistory

        if temp is None:
            return ""

        return temp

    @property
    def history(self: Self) -> "_1589.FileHistory":
        """mastapy.utility.FileHistory

        Note:
            This property is readonly.
        """
        temp = self.wrapped.History

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def database_key(self: Self) -> "_1837.NamedKey":
        """mastapy.utility.databases.NamedKey"""
        temp = self.wrapped.DatabaseKey

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @database_key.setter
    @enforce_parameter_types
    def database_key(self: Self, value: "_1837.NamedKey"):
        self.wrapped.DatabaseKey = value.wrapped

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "NamedDatabaseItem._Cast_NamedDatabaseItem":
        return self._Cast_NamedDatabaseItem(self)
