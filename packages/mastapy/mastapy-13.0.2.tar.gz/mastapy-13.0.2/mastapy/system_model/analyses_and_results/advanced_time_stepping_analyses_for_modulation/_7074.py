"""FaceGearSetAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7079,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6895
    from mastapy.system_model.analyses_and_results.system_deflections import _2763
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7072,
        _7073,
        _7118,
        _7014,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="FaceGearSetAdvancedTimeSteppingAnalysisForModulation")


class FaceGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7079.GearSetAdvancedTimeSteppingAnalysisForModulation
):
    """FaceGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting FaceGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7079.GearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7079.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7118.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7014,
            )

            return self._parent._cast(
                _7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "FaceGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "FaceGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
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
    def system_deflection_results(self: Self) -> "_2763.FaceGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7072.FaceGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.FaceGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7073.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation(self)
