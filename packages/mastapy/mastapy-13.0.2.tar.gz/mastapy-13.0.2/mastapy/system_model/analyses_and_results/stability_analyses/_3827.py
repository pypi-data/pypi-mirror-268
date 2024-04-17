"""FaceGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "FaceGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6895
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3828,
        _3826,
        _3871,
        _3771,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetStabilityAnalysis")


class FaceGearSetStabilityAnalysis(_3832.GearSetStabilityAnalysis):
    """FaceGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetStabilityAnalysis")

    class _Cast_FaceGearSetStabilityAnalysis:
        """Special nested class for casting FaceGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
            parent: "FaceGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_3832.GearSetStabilityAnalysis":
            return self._parent._cast(_3832.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_3871.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_3771.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "FaceGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2536.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6895.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears_stability_analysis(
        self: Self,
    ) -> "List[_3828.FaceGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FaceGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3826.FaceGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FaceGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis":
        return self._Cast_FaceGearSetStabilityAnalysis(self)
