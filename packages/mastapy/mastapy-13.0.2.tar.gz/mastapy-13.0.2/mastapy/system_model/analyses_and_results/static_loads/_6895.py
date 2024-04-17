"""FaceGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6904
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6893,
        _6894,
        _6961,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetLoadCase",)


Self = TypeVar("Self", bound="FaceGearSetLoadCase")


class FaceGearSetLoadCase(_6904.GearSetLoadCase):
    """FaceGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetLoadCase")

    class _Cast_FaceGearSetLoadCase:
        """Special nested class for casting FaceGearSetLoadCase to subclasses."""

        def __init__(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
            parent: "FaceGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_6904.GearSetLoadCase":
            return self._parent._cast(_6904.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_set_load_case(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase",
        ) -> "FaceGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetLoadCase.TYPE"):
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
    def gears(self: Self) -> "List[_6893.FaceGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_load_case(self: Self) -> "List[_6893.FaceGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_load_case(self: Self) -> "List[_6894.FaceGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FaceGearSetLoadCase._Cast_FaceGearSetLoadCase":
        return self._Cast_FaceGearSetLoadCase(self)
