"""ComponentLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6937
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ComponentLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6816,
        _6817,
        _6822,
        _6828,
        _6831,
        _6834,
        _6835,
        _6836,
        _6840,
        _6842,
        _6848,
        _6850,
        _6853,
        _6859,
        _6861,
        _6865,
        _6868,
        _6870,
        _6875,
        _6878,
        _6892,
        _6893,
        _6896,
        _6899,
        _6905,
        _6914,
        _6921,
        _6924,
        _6927,
        _6930,
        _6931,
        _6933,
        _6935,
        _6939,
        _6944,
        _6947,
        _6948,
        _6949,
        _6952,
        _6956,
        _6958,
        _6959,
        _6962,
        _6966,
        _6968,
        _6971,
        _6974,
        _6975,
        _6976,
        _6978,
        _6979,
        _6983,
        _6984,
        _6989,
        _6990,
        _6991,
        _6994,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentLoadCase",)


Self = TypeVar("Self", bound="ComponentLoadCase")


class ComponentLoadCase(_6937.PartLoadCase):
    """ComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentLoadCase")

    class _Cast_ComponentLoadCase:
        """Special nested class for casting ComponentLoadCase to subclasses."""

        def __init__(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
            parent: "ComponentLoadCase",
        ):
            self._parent = parent

        @property
        def part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6937.PartLoadCase":
            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6816.AbstractShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6816

            return self._parent._cast(_6816.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6817.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6822.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.AGMAGleasonConicalGearLoadCase)

        @property
        def bearing_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6828.BearingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BearingLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6831.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6834.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6835.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6836.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.BevelGearLoadCase)

        @property
        def bolt_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6840.BoltLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.BoltLoadCase)

        @property
        def clutch_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6842.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6848.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConceptCouplingHalfLoadCase)

        @property
        def concept_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6850.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6853.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.ConicalGearLoadCase)

        @property
        def connector_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6859.ConnectorLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ConnectorLoadCase)

        @property
        def coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6861.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.CouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6865.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6865

            return self._parent._cast(_6865.CVTPulleyLoadCase)

        @property
        def cycloidal_disc_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6868.CycloidalDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6870.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6875.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6878.DatumLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6878

            return self._parent._cast(_6878.DatumLoadCase)

        @property
        def external_cad_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6892.ExternalCADModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6893.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.FaceGearLoadCase)

        @property
        def fe_part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6896.FEPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6896

            return self._parent._cast(_6896.FEPartLoadCase)

        @property
        def gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6899.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6899

            return self._parent._cast(_6899.GearLoadCase)

        @property
        def guide_dxf_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6905.GuideDxfModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6905

            return self._parent._cast(_6905.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6914.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6921.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(_6921.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6924.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6927.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(
                _6927.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6930.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6930

            return self._parent._cast(_6930.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6931.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6935.OilSealLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6935

            return self._parent._cast(_6935.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6939.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.PartToPartShearCouplingHalfLoadCase)

        @property
        def planet_carrier_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6944.PlanetCarrierLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(_6944.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6947.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6948.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6949.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6952.RingPinsLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.RingPinsLoadCase)

        @property
        def rolling_ring_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6956.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.RollingRingLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6958.ShaftHubConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6959.ShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.ShaftLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6962.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.SpiralBevelGearLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6966.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.SpringDamperHalfLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6968.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6971.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6974.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6975.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6976.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6978.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6978

            return self._parent._cast(_6978.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6979.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6983.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6984.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6989.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6990.VirtualComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6990

            return self._parent._cast(_6990.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6991.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6991

            return self._parent._cast(_6991.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6994.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.ZerolBevelGearLoadCase)

        @property
        def component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "ComponentLoadCase":
            return self._parent

        def __getattr__(self: "ComponentLoadCase._Cast_ComponentLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalModalDampingRatio = value

    @property
    def is_connected_to_ground(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsConnectedToGround

        if temp is None:
            return False

        return temp

    @property
    def is_torsionally_free(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsTorsionallyFree

        if temp is None:
            return False

        return temp

    @property
    def magnitude_of_rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MagnitudeOfRotation

        if temp is None:
            return 0.0

        return temp

    @magnitude_of_rotation.setter
    @enforce_parameter_types
    def magnitude_of_rotation(self: Self, value: "float"):
        self.wrapped.MagnitudeOfRotation = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingBeta = value

    @property
    def rotation_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAngle

        if temp is None:
            return 0.0

        return temp

    @rotation_angle.setter
    @enforce_parameter_types
    def rotation_angle(self: Self, value: "float"):
        self.wrapped.RotationAngle = float(value) if value is not None else 0.0

    @property
    def component_design(self: Self) -> "_2451.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ComponentLoadCase._Cast_ComponentLoadCase":
        return self._Cast_ComponentLoadCase(self)
