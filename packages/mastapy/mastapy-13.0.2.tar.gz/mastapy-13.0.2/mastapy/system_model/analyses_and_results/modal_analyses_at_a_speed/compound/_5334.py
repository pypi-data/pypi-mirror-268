"""PartCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7554
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "PartCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5205,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5255,
        _5256,
        _5257,
        _5259,
        _5261,
        _5262,
        _5263,
        _5265,
        _5266,
        _5268,
        _5269,
        _5270,
        _5271,
        _5273,
        _5274,
        _5275,
        _5276,
        _5278,
        _5280,
        _5281,
        _5283,
        _5284,
        _5286,
        _5287,
        _5289,
        _5291,
        _5292,
        _5294,
        _5296,
        _5297,
        _5298,
        _5300,
        _5302,
        _5304,
        _5305,
        _5306,
        _5307,
        _5308,
        _5310,
        _5311,
        _5312,
        _5313,
        _5315,
        _5316,
        _5317,
        _5319,
        _5321,
        _5323,
        _5324,
        _5326,
        _5327,
        _5329,
        _5330,
        _5331,
        _5332,
        _5333,
        _5335,
        _5337,
        _5339,
        _5340,
        _5341,
        _5342,
        _5343,
        _5344,
        _5346,
        _5347,
        _5349,
        _5350,
        _5351,
        _5353,
        _5354,
        _5356,
        _5357,
        _5359,
        _5360,
        _5362,
        _5363,
        _5365,
        _5366,
        _5367,
        _5368,
        _5369,
        _5370,
        _5371,
        _5372,
        _5374,
        _5375,
        _5376,
        _5377,
        _5378,
        _5380,
        _5381,
        _5383,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PartCompoundModalAnalysisAtASpeed")


class PartCompoundModalAnalysisAtASpeed(_7554.PartCompoundAnalysis):
    """PartCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundModalAnalysisAtASpeed")

    class _Cast_PartCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PartCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
            parent: "PartCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5255.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(
                _5255.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5256.AbstractShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(_5256.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5257.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5257,
            )

            return self._parent._cast(
                _5257.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5259.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(
                _5259.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5261.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(
                _5261.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5262.AssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5262,
            )

            return self._parent._cast(_5262.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def bearing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5263.BearingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(_5263.BearingCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5265.BeltDriveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5265,
            )

            return self._parent._cast(_5265.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5266.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(
                _5266.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5268.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5269.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(
                _5269.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5270.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(
                _5270.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5271.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(_5271.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5273.BevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5273,
            )

            return self._parent._cast(_5273.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5274.BoltCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(_5274.BoltCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5275.BoltedJointCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(_5275.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5276.ClutchCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5276,
            )

            return self._parent._cast(_5276.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5278.ClutchHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5281.ConceptCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(
                _5281.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5283.ConceptCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5283,
            )

            return self._parent._cast(
                _5283.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5284.ConceptGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5286.ConceptGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5287.ConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(_5287.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5289.ConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5289,
            )

            return self._parent._cast(_5289.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5291.ConnectorCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5291,
            )

            return self._parent._cast(_5291.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5292.CouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(_5292.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5294.CouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(_5294.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5296.CVTCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(_5296.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5297.CVTPulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5297,
            )

            return self._parent._cast(_5297.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5298.CycloidalAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(
                _5298.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5300.CycloidalDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(_5300.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5302.CylindricalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(
                _5302.CylindricalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5304.CylindricalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(
                _5304.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5305.CylindricalPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(
                _5305.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def datum_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5306.DatumCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(_5306.DatumCompoundModalAnalysisAtASpeed)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5307.ExternalCADModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(
                _5307.ExternalCADModelCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5308.FaceGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5308,
            )

            return self._parent._cast(_5308.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5310.FaceGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5310,
            )

            return self._parent._cast(_5310.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5311.FEPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(_5311.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5312.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5313.GearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(_5313.GearCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5315.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(_5315.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5316.GuideDxfModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5316,
            )

            return self._parent._cast(_5316.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5317.HypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(_5317.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5319.HypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5319,
            )

            return self._parent._cast(_5319.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5321.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(
                _5321.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5323.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5324.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(
                _5324.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5326.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(
                _5326.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5327.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5329.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(
                _5329.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5330.MassDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5331.MeasurementComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(
                _5331.MeasurementComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5333.OilSealCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5333,
            )

            return self._parent._cast(_5333.OilSealCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5335.PartToPartShearCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(
                _5335.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5337.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(
                _5337.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5339.PlanetaryGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5339,
            )

            return self._parent._cast(
                _5339.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5340.PlanetCarrierCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5340,
            )

            return self._parent._cast(_5340.PlanetCarrierCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5341.PointLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(_5341.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5342.PowerLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(_5342.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5343.PulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5343,
            )

            return self._parent._cast(_5343.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5344.RingPinsCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(_5344.RingPinsCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5346.RollingRingAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5346,
            )

            return self._parent._cast(
                _5346.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5347.RollingRingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5349.RootAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5350.ShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(_5350.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5351.ShaftHubConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5351,
            )

            return self._parent._cast(
                _5351.ShaftHubConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5354.SpiralBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5356.SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(
                _5356.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5357.SpringDamperCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(_5357.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5359.SpringDamperHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5360.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(
                _5360.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5362.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(
                _5362.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5363.StraightBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5363,
            )

            return self._parent._cast(
                _5363.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5365.StraightBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(
                _5365.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5366.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5367.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5367,
            )

            return self._parent._cast(
                _5367.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5368.SynchroniserCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(_5368.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5369.SynchroniserHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(
                _5369.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5370.SynchroniserPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5370,
            )

            return self._parent._cast(
                _5370.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5371.SynchroniserSleeveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5372.TorqueConverterCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5372,
            )

            return self._parent._cast(
                _5372.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5374.TorqueConverterPumpCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5375.TorqueConverterTurbineCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(
                _5375.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5376.UnbalancedMassCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5376,
            )

            return self._parent._cast(_5376.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5377.VirtualComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5377,
            )

            return self._parent._cast(
                _5377.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5378.WormGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5378,
            )

            return self._parent._cast(_5378.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5380.WormGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5380,
            )

            return self._parent._cast(_5380.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5381.ZerolBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5381,
            )

            return self._parent._cast(_5381.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "_5383.ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5383,
            )

            return self._parent._cast(
                _5383.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "PartCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PartCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_5205.PartModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PartModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5205.PartModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PartModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed":
        return self._Cast_PartCompoundModalAnalysisAtASpeed(self)
