"""SpiralBevelGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SpiralBevelGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.stability_analyses import _3873
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _4004,
        _4005,
        _3911,
        _3939,
        _3965,
        _4003,
        _3905,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearSetCompoundStabilityAnalysis")


class SpiralBevelGearSetCompoundStabilityAnalysis(
    _3923.BevelGearSetCompoundStabilityAnalysis
):
    """SpiralBevelGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSetCompoundStabilityAnalysis"
    )

    class _Cast_SpiralBevelGearSetCompoundStabilityAnalysis:
        """Special nested class for casting SpiralBevelGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
            parent: "SpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_3923.BevelGearSetCompoundStabilityAnalysis":
            return self._parent._cast(_3923.BevelGearSetCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_3911.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(
                _3911.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_3939.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_3965.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(_3965.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_4003.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_3905.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "SpiralBevelGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearSetCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2551.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3873.SpiralBevelGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpiralBevelGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gears_compound_stability_analysis(
        self: Self,
    ) -> "List[_4004.SpiralBevelGearCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.SpiralBevelGearCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_stability_analysis(
        self: Self,
    ) -> "List[_4005.SpiralBevelGearMeshCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.SpiralBevelGearMeshCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3873.SpiralBevelGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpiralBevelGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetCompoundStabilityAnalysis._Cast_SpiralBevelGearSetCompoundStabilityAnalysis":
        return self._Cast_SpiralBevelGearSetCompoundStabilityAnalysis(self)
