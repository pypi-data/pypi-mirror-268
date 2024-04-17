"""PartAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PartAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7282,
        _7278,
        _7279,
        _7280,
        _7285,
        _7287,
        _7288,
        _7289,
        _7291,
        _7292,
        _7294,
        _7295,
        _7296,
        _7297,
        _7299,
        _7300,
        _7301,
        _7302,
        _7304,
        _7306,
        _7307,
        _7309,
        _7310,
        _7312,
        _7313,
        _7315,
        _7317,
        _7319,
        _7321,
        _7322,
        _7324,
        _7325,
        _7326,
        _7329,
        _7331,
        _7333,
        _7334,
        _7335,
        _7336,
        _7338,
        _7339,
        _7340,
        _7341,
        _7343,
        _7344,
        _7345,
        _7347,
        _7349,
        _7351,
        _7352,
        _7354,
        _7355,
        _7357,
        _7359,
        _7360,
        _7361,
        _7362,
        _7364,
        _7366,
        _7368,
        _7369,
        _7370,
        _7371,
        _7372,
        _7373,
        _7375,
        _7376,
        _7378,
        _7379,
        _7380,
        _7382,
        _7383,
        _7385,
        _7386,
        _7388,
        _7389,
        _7391,
        _7392,
        _7394,
        _7395,
        _7396,
        _7397,
        _7398,
        _7399,
        _7400,
        _7401,
        _7403,
        _7404,
        _7406,
        _7407,
        _7408,
        _7410,
        _7411,
        _7413,
    )
    from mastapy.system_model.part_model import _2475
    from mastapy.math_utility.convergence import _1582
    from mastapy.system_model.drawing import _2251
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PartAdvancedSystemDeflection")


class PartAdvancedSystemDeflection(_7556.PartStaticLoadAnalysisCase):
    """PartAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartAdvancedSystemDeflection")

    class _Cast_PartAdvancedSystemDeflection:
        """Special nested class for casting PartAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
            parent: "PartAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7278.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(_7278.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7279.AbstractShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(_7279.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7280.AbstractShaftOrHousingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7280,
            )

            return self._parent._cast(
                _7280.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7285.AGMAGleasonConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(
                _7285.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7287.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(
                _7287.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7288.AssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7288,
            )

            return self._parent._cast(_7288.AssemblyAdvancedSystemDeflection)

        @property
        def bearing_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7289.BearingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7289,
            )

            return self._parent._cast(_7289.BearingAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7291.BeltDriveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7291,
            )

            return self._parent._cast(_7291.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7292.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(
                _7292.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7294.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(
                _7294.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7295.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(
                _7295.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7296.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(
                _7296.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7297.BevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.BevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7299.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(_7299.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7300.BoltAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.BoltAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7301.BoltedJointAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7301,
            )

            return self._parent._cast(_7301.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7302.ClutchAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.ClutchAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7304.ClutchHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ClutchHalfAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7306.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.ComponentAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7307.ConceptCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7309.ConceptCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7310.ConceptGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(_7310.ConceptGearAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7312.ConceptGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7313.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.ConicalGearAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7315.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.ConicalGearSetAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7317.ConnectorAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7319.CouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.CouplingAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7321.CouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7321,
            )

            return self._parent._cast(_7321.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7322.CVTAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(_7322.CVTAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7324.CVTPulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7325.CycloidalAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(_7325.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7326.CycloidalDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7329.CylindricalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7331.CylindricalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7333.CylindricalPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(
                _7333.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def datum_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7334.DatumAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7335.ExternalCADModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7336.FaceGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(_7336.FaceGearAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7338.FaceGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(_7338.FaceGearSetAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7339.FEPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.FEPartAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7340.FlexiblePinAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(_7340.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7341.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7341,
            )

            return self._parent._cast(_7341.GearAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7343.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(_7343.GearSetAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7344.GuideDxfModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(_7344.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7345.HypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(_7345.HypoidGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7347.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(_7347.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7349.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(
                _7349.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7351.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(
                _7351.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7352.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(
                _7352.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7354.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(
                _7354.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7355.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(
                _7355.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7357.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(
                _7357.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7359.MassDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7360.MeasurementComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(
                _7360.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def mountable_component_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7361.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7362.OilSealAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.OilSealAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7364.PartToPartShearCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(
                _7364.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7366.PartToPartShearCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7368.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(_7368.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def planet_carrier_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7369.PlanetCarrierAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(_7369.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7370.PointLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(_7370.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7371.PowerLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7372.PulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7373.RingPinsAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7375.RollingRingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(_7375.RollingRingAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7376.RollingRingAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def root_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7378.RootAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(_7378.RootAssemblyAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7379.ShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7380.ShaftHubConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(_7380.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7382.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(_7382.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7383.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(_7383.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7385.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(_7385.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7386.SpringDamperAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.SpringDamperAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7388.SpringDamperHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7389.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(
                _7389.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7391.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(
                _7391.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7392.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7394.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(
                _7394.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7395.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(
                _7395.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7396.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(
                _7396.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7397.SynchroniserAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.SynchroniserAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7398.SynchroniserHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7399.SynchroniserPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(_7399.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7400.SynchroniserSleeveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7401.TorqueConverterAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.TorqueConverterAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7403.TorqueConverterPumpAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(_7403.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7404.TorqueConverterTurbineAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(
                _7404.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7406.UnbalancedMassAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7406,
            )

            return self._parent._cast(_7406.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7407.VirtualComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7407,
            )

            return self._parent._cast(_7407.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7408.WormGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7408,
            )

            return self._parent._cast(_7408.WormGearAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7410.WormGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7410,
            )

            return self._parent._cast(_7410.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7411.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7411,
            )

            return self._parent._cast(_7411.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7413.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7413,
            )

            return self._parent._cast(_7413.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "PartAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_system_deflection(self: Self) -> "_7282.AdvancedSystemDeflection":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.AdvancedSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def data_logger(self: Self) -> "_1582.DataLogger":
        """mastapy.math_utility.convergence.DataLogger

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2251.AdvancedSystemDeflectionViewable":
        """mastapy.system_model.drawing.AdvancedSystemDeflectionViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection":
        return self._Cast_PartAdvancedSystemDeflection(self)
