"""AGMAGleasonConicalGearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AGMAGleasonConicalGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7294,
        _7299,
        _7347,
        _7385,
        _7391,
        _7394,
        _7413,
        _7343,
        _7382,
        _7278,
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetAdvancedSystemDeflection")


class AGMAGleasonConicalGearSetAdvancedSystemDeflection(
    _7315.ConicalGearSetAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7315.ConicalGearSetAdvancedSystemDeflection":
            return self._parent._cast(_7315.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7343.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(_7343.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7382.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(_7382.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7278.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(_7278.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7294.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(
                _7294.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7299.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(_7299.BevelGearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7347.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(_7347.HypoidGearSetAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7385.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(_7385.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7391.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(
                _7391.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7394.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(
                _7394.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "_7413.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7413,
            )

            return self._parent._cast(_7413.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection",
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
        self: Self,
        instance_to_wrap: "AGMAGleasonConicalGearSetAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2521.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSetAdvancedSystemDeflection(self)
