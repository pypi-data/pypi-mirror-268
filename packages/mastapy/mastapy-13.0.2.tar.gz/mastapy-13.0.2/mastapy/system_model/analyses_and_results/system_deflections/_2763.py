"""FaceGearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2768
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "FaceGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6895
    from mastapy.gears.rating.face import _453
    from mastapy.system_model.analyses_and_results.power_flows import _4096
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2764,
        _2762,
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
__all__ = ("FaceGearSetSystemDeflection",)


Self = TypeVar("Self", bound="FaceGearSetSystemDeflection")


class FaceGearSetSystemDeflection(_2768.GearSetSystemDeflection):
    """FaceGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetSystemDeflection")

    class _Cast_FaceGearSetSystemDeflection:
        """Special nested class for casting FaceGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
            parent: "FaceGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_system_deflection(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_2768.GearSetSystemDeflection":
            return self._parent._cast(_2768.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_2814.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_2693.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2693,
            )

            return self._parent._cast(_2693.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_set_system_deflection(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
        ) -> "FaceGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetSystemDeflection.TYPE"):
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
    def rating(self: Self) -> "_453.FaceGearSetRating":
        """mastapy.gears.rating.face.FaceGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_453.FaceGearSetRating":
        """mastapy.gears.rating.face.FaceGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4096.FaceGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.FaceGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears_system_deflection(
        self: Self,
    ) -> "List[_2764.FaceGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_system_deflection(
        self: Self,
    ) -> "List[_2762.FaceGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FaceGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetSystemDeflection._Cast_FaceGearSetSystemDeflection":
        return self._Cast_FaceGearSetSystemDeflection(self)
