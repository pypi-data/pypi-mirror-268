"""AGMAGleasonConicalGearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AGMAGleasonConicalGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.power_flows import _4046
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2710,
        _2715,
        _2772,
        _2816,
        _2822,
        _2825,
        _2848,
        _2768,
        _2814,
        _2693,
        _2793,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetSystemDeflection")


class AGMAGleasonConicalGearSetSystemDeflection(_2733.ConicalGearSetSystemDeflection):
    """AGMAGleasonConicalGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearSetSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
            parent: "AGMAGleasonConicalGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2733.ConicalGearSetSystemDeflection":
            return self._parent._cast(_2733.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2768.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(_2768.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2814.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2693.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2693,
            )

            return self._parent._cast(_2693.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2710.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2715.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.BevelGearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2772.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(_2772.HypoidGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2816.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.SpiralBevelGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2822.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2825.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.StraightBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "_2848.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2848,
            )

            return self._parent._cast(_2848.ZerolBevelGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "AGMAGleasonConicalGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetSystemDeflection.TYPE"
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
    def power_flow_results(self: Self) -> "_4046.AGMAGleasonConicalGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSetSystemDeflection(self)
