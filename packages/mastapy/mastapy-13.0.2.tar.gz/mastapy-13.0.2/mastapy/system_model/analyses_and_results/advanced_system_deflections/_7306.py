"""ComponentAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ComponentAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7279,
        _7280,
        _7285,
        _7289,
        _7292,
        _7295,
        _7296,
        _7297,
        _7300,
        _7304,
        _7309,
        _7310,
        _7313,
        _7317,
        _7321,
        _7324,
        _7326,
        _7329,
        _7333,
        _7334,
        _7335,
        _7336,
        _7339,
        _7341,
        _7344,
        _7345,
        _7349,
        _7352,
        _7355,
        _7359,
        _7360,
        _7361,
        _7362,
        _7366,
        _7369,
        _7370,
        _7371,
        _7372,
        _7373,
        _7375,
        _7379,
        _7380,
        _7383,
        _7388,
        _7389,
        _7392,
        _7395,
        _7396,
        _7398,
        _7399,
        _7400,
        _7403,
        _7404,
        _7406,
        _7407,
        _7408,
        _7411,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ComponentAdvancedSystemDeflection")


class ComponentAdvancedSystemDeflection(_7363.PartAdvancedSystemDeflection):
    """ComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentAdvancedSystemDeflection")

    class _Cast_ComponentAdvancedSystemDeflection:
        """Special nested class for casting ComponentAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
            parent: "ComponentAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7279.AbstractShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(_7279.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7280.AbstractShaftOrHousingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7280,
            )

            return self._parent._cast(
                _7280.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7285.AGMAGleasonConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(
                _7285.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def bearing_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7289.BearingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7289,
            )

            return self._parent._cast(_7289.BearingAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7292.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(
                _7292.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7295.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(
                _7295.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7296.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(
                _7296.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7297.BevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.BevelGearAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7300.BoltAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.BoltAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7304.ClutchHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ClutchHalfAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7309.ConceptCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7310.ConceptGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(_7310.ConceptGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7313.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.ConicalGearAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7317.ConnectorAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7321.CouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7321,
            )

            return self._parent._cast(_7321.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7324.CVTPulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7326.CycloidalDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7329.CylindricalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7333.CylindricalPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(
                _7333.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def datum_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7334.DatumAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7335.ExternalCADModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7336.FaceGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(_7336.FaceGearAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7339.FEPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.FEPartAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7341.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7341,
            )

            return self._parent._cast(_7341.GearAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7344.GuideDxfModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(_7344.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7345.HypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(_7345.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7349.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(
                _7349.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7352.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(
                _7352.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7355.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(
                _7355.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7359.MassDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7360.MeasurementComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(
                _7360.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def mountable_component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7361.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7362.OilSealAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.OilSealAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7366.PartToPartShearCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planet_carrier_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7369.PlanetCarrierAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(_7369.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7370.PointLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(_7370.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7371.PowerLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7372.PulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7373.RingPinsAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7375.RollingRingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(_7375.RollingRingAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7379.ShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7380.ShaftHubConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(_7380.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7383.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(_7383.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7388.SpringDamperHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7389.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(
                _7389.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7392.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7395.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(
                _7395.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7396.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(
                _7396.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7398.SynchroniserHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7399.SynchroniserPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(_7399.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7400.SynchroniserSleeveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7403.TorqueConverterPumpAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(_7403.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7404.TorqueConverterTurbineAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(
                _7404.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7406.UnbalancedMassAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7406,
            )

            return self._parent._cast(_7406.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7407.VirtualComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7407,
            )

            return self._parent._cast(_7407.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7408.WormGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7408,
            )

            return self._parent._cast(_7408.WormGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7411.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7411,
            )

            return self._parent._cast(_7411.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "ComponentAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ComponentAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection":
        return self._Cast_ComponentAdvancedSystemDeflection(self)
