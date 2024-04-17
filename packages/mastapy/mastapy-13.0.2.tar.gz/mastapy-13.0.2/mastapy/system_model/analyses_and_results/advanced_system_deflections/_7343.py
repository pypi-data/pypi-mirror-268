"""GearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7382
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "GearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7358,
        _7287,
        _7294,
        _7299,
        _7312,
        _7315,
        _7331,
        _7338,
        _7347,
        _7351,
        _7354,
        _7357,
        _7368,
        _7385,
        _7391,
        _7394,
        _7410,
        _7413,
        _7278,
        _7363,
    )
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.gears.rating import _366
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="GearSetAdvancedSystemDeflection")


class GearSetAdvancedSystemDeflection(
    _7382.SpecialisedAssemblyAdvancedSystemDeflection
):
    """GearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetAdvancedSystemDeflection")

    class _Cast_GearSetAdvancedSystemDeflection:
        """Special nested class for casting GearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
            parent: "GearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7382.SpecialisedAssemblyAdvancedSystemDeflection":
            return self._parent._cast(_7382.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7278.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(_7278.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7287.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(
                _7287.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7294.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(
                _7294.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7299.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(_7299.BevelGearSetAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7312.ConceptGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7315.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.ConicalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7331.CylindricalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7338.FaceGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(_7338.FaceGearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7347.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(_7347.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7351.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(
                _7351.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7354.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(
                _7354.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7357.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(
                _7357.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7368.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(_7368.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7385.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(_7385.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7391.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(
                _7391.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7394.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(
                _7394.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7410.WormGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7410,
            )

            return self._parent._cast(_7410.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7413.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7413,
            )

            return self._parent._cast(_7413.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "GearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def use_ltca_in_advanced_system_deflection(
        self: Self,
    ) -> "_7358.UseLtcaInAsdOption":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.UseLtcaInAsdOption"""
        temp = self.wrapped.UseLTCAInAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.UseLtcaInAsdOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.advanced_system_deflections._7358",
            "UseLtcaInAsdOption",
        )(value)

    @use_ltca_in_advanced_system_deflection.setter
    @enforce_parameter_types
    def use_ltca_in_advanced_system_deflection(
        self: Self, value: "_7358.UseLtcaInAsdOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.UseLtcaInAsdOption",
        )
        self.wrapped.UseLTCAInAdvancedSystemDeflection = value

    @property
    def assembly_design(self: Self) -> "_2539.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_366.GearSetRating":
        """mastapy.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection":
        return self._Cast_GearSetAdvancedSystemDeflection(self)
