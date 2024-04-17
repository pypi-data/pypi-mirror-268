"""PartLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.system_model.analyses_and_results.static_loads import _6906, _6813
from mastapy.system_model.analyses_and_results import _2665
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6814,
        _6815,
        _6816,
        _6817,
        _6822,
        _6824,
        _6827,
        _6828,
        _6830,
        _6831,
        _6833,
        _6834,
        _6835,
        _6836,
        _6838,
        _6839,
        _6840,
        _6842,
        _6843,
        _6846,
        _6848,
        _6849,
        _6850,
        _6852,
        _6853,
        _6857,
        _6859,
        _6861,
        _6862,
        _6864,
        _6865,
        _6866,
        _6868,
        _6870,
        _6874,
        _6875,
        _6878,
        _6892,
        _6893,
        _6895,
        _6896,
        _6897,
        _6899,
        _6904,
        _6905,
        _6914,
        _6916,
        _6921,
        _6923,
        _6924,
        _6926,
        _6927,
        _6929,
        _6930,
        _6931,
        _6933,
        _6935,
        _6939,
        _6940,
        _6942,
        _6944,
        _6947,
        _6948,
        _6949,
        _6952,
        _6954,
        _6956,
        _6957,
        _6958,
        _6959,
        _6961,
        _6962,
        _6964,
        _6966,
        _6967,
        _6968,
        _6970,
        _6971,
        _6973,
        _6974,
        _6975,
        _6976,
        _6977,
        _6978,
        _6979,
        _6982,
        _6983,
        _6984,
        _6989,
        _6990,
        _6991,
        _6993,
        _6994,
        _6996,
    )
    from mastapy.electric_machines.harmonic_load_data import _1387
    from mastapy.system_model.analyses_and_results import _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartLoadCase",)


Self = TypeVar("Self", bound="PartLoadCase")


class PartLoadCase(_2665.PartAnalysis):
    """PartLoadCase

    This is a mastapy class.
    """

    TYPE = _PART_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartLoadCase")

    class _Cast_PartLoadCase:
        """Special nested class for casting PartLoadCase to subclasses."""

        def __init__(self: "PartLoadCase._Cast_PartLoadCase", parent: "PartLoadCase"):
            self._parent = parent

        @property
        def part_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_2665.PartAnalysis":
            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def abstract_shaft_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6816.AbstractShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6816

            return self._parent._cast(_6816.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6817.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6822.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.AGMAGleasonConicalGearLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6824.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6827.AssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.AssemblyLoadCase)

        @property
        def bearing_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6828.BearingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BearingLoadCase)

        @property
        def belt_drive_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6830.BeltDriveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6831.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6833.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6834.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6835.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6836.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.BevelGearLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6838.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6839.BoltedJointLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.BoltedJointLoadCase)

        @property
        def bolt_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6840.BoltLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.BoltLoadCase)

        @property
        def clutch_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6842.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.ClutchHalfLoadCase)

        @property
        def clutch_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6843.ClutchLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.ClutchLoadCase)

        @property
        def component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6848.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConceptCouplingHalfLoadCase)

        @property
        def concept_coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6849.ConceptCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConceptCouplingLoadCase)

        @property
        def concept_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6850.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.ConceptGearLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6852.ConceptGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.ConceptGearSetLoadCase)

        @property
        def conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6853.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.ConicalGearLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6857.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.ConicalGearSetLoadCase)

        @property
        def connector_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6859.ConnectorLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ConnectorLoadCase)

        @property
        def coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6861.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.CouplingHalfLoadCase)

        @property
        def coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6862.CouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6862

            return self._parent._cast(_6862.CouplingLoadCase)

        @property
        def cvt_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6864.CVTLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.CVTLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6865.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6865

            return self._parent._cast(_6865.CVTPulleyLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6866.CycloidalAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.CycloidalAssemblyLoadCase)

        @property
        def cycloidal_disc_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6868.CycloidalDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6870.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.CylindricalGearLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6874.CylindricalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6874

            return self._parent._cast(_6874.CylindricalGearSetLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6875.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6878.DatumLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6878

            return self._parent._cast(_6878.DatumLoadCase)

        @property
        def external_cad_model_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6892.ExternalCADModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6893.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.FaceGearLoadCase)

        @property
        def face_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6895.FaceGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.FaceGearSetLoadCase)

        @property
        def fe_part_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6896.FEPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6896

            return self._parent._cast(_6896.FEPartLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6897.FlexiblePinAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6897

            return self._parent._cast(_6897.FlexiblePinAssemblyLoadCase)

        @property
        def gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6899.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6899

            return self._parent._cast(_6899.GearLoadCase)

        @property
        def gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6904.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6904

            return self._parent._cast(_6904.GearSetLoadCase)

        @property
        def guide_dxf_model_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6905.GuideDxfModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6905

            return self._parent._cast(_6905.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6914.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.HypoidGearLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6916.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(_6916.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6921.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(_6921.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6923.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(
                _6923.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6924.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6926.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(
                _6926.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6927.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(
                _6927.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(
                _6929.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6930.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6930

            return self._parent._cast(_6930.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6931.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6935.OilSealLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6935

            return self._parent._cast(_6935.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6939.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.PartToPartShearCouplingHalfLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6940.PartToPartShearCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(_6940.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6942.PlanetaryGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.PlanetaryGearSetLoadCase)

        @property
        def planet_carrier_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6944.PlanetCarrierLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(_6944.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6947.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6948.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6949.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6952.RingPinsLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.RingPinsLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6954.RollingRingAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.RollingRingAssemblyLoadCase)

        @property
        def rolling_ring_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6956.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.RollingRingLoadCase)

        @property
        def root_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6957.RootAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.RootAssemblyLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6958.ShaftHubConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6959.ShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.ShaftLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6962.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.SpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6964.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6966.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.SpringDamperHalfLoadCase)

        @property
        def spring_damper_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6967.SpringDamperLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6968.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6970.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6971.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.StraightBevelGearLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6973.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.StraightBevelGearSetLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6974.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6975.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6976.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.SynchroniserHalfLoadCase)

        @property
        def synchroniser_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6977.SynchroniserLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6977

            return self._parent._cast(_6977.SynchroniserLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6978.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6978

            return self._parent._cast(_6978.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6979.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6982.TorqueConverterLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.TorqueConverterLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6983.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6984.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6989.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6990.VirtualComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6990

            return self._parent._cast(_6990.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6991.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6991

            return self._parent._cast(_6991.WormGearLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6993.WormGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6993

            return self._parent._cast(_6993.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6994.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.ZerolBevelGearLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6996.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.ZerolBevelGearSetLoadCase)

        @property
        def part_load_case(self: "PartLoadCase._Cast_PartLoadCase") -> "PartLoadCase":
            return self._parent

        def __getattr__(self: "PartLoadCase._Cast_PartLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_data_is_up_to_date(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationDataIsUpToDate

        if temp is None:
            return False

        return temp

    @property
    def harmonic_excitation_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.HarmonicExcitationType]"""
        temp = self.wrapped.HarmonicExcitationType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @harmonic_excitation_type.setter
    @enforce_parameter_types
    def harmonic_excitation_type(self: Self, value: "_6906.HarmonicExcitationType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.HarmonicExcitationType = value

    @property
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = (
            self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp
        )

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: Self, value: "_6813.StaticLoadCase"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp = (
            value
        )

    @property
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp
        )

        if temp is None:
            return False

        return temp

    @use_this_load_case_for_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: Self, value: "bool"
    ):
        self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp = (
            bool(value) if value is not None else False
        )

    @property
    def component_design(self: Self) -> "_2475.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_load_case(self: Self) -> "_6813.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: Self) -> "_6814.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def clear_user_specified_excitation_data_for_this_load_case(self: Self):
        """Method does not return."""
        self.wrapped.ClearUserSpecifiedExcitationDataForThisLoadCase()

    def get_harmonic_load_data_for_import(self: Self) -> "_1387.HarmonicLoadDataBase":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartLoadCase._Cast_PartLoadCase":
        return self._Cast_PartLoadCase(self)
