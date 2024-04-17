"""GearSetStaticLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
    _5685,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups",
    "GearSetStaticLoadCaseGroup",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
        _5681,
        _5682,
        _5683,
    )
    from mastapy.system_model.part_model.gears import _2539, _2537
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6899,
        _6901,
        _6904,
    )
    from mastapy.system_model.connections_and_sockets.gears import _2320


__docformat__ = "restructuredtext en"
__all__ = ("GearSetStaticLoadCaseGroup",)


Self = TypeVar("Self", bound="GearSetStaticLoadCaseGroup")
TGearSet = TypeVar("TGearSet", bound="_2539.GearSet")
TGear = TypeVar("TGear", bound="_2537.Gear")
TGearStaticLoad = TypeVar("TGearStaticLoad", bound="_6899.GearLoadCase")
TGearMesh = TypeVar("TGearMesh", bound="_2320.GearMesh")
TGearMeshStaticLoad = TypeVar("TGearMeshStaticLoad", bound="_6901.GearMeshLoadCase")
TGearSetStaticLoad = TypeVar("TGearSetStaticLoad", bound="_6904.GearSetLoadCase")


class GearSetStaticLoadCaseGroup(
    _5685.PartStaticLoadCaseGroup,
    Generic[
        TGearSet,
        TGear,
        TGearStaticLoad,
        TGearMesh,
        TGearMeshStaticLoad,
        TGearSetStaticLoad,
    ],
):
    """GearSetStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TGearSet
        TGear
        TGearStaticLoad
        TGearMesh
        TGearMeshStaticLoad
        TGearSetStaticLoad
    """

    TYPE = _GEAR_SET_STATIC_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetStaticLoadCaseGroup")

    class _Cast_GearSetStaticLoadCaseGroup:
        """Special nested class for casting GearSetStaticLoadCaseGroup to subclasses."""

        def __init__(
            self: "GearSetStaticLoadCaseGroup._Cast_GearSetStaticLoadCaseGroup",
            parent: "GearSetStaticLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def part_static_load_case_group(
            self: "GearSetStaticLoadCaseGroup._Cast_GearSetStaticLoadCaseGroup",
        ) -> "_5685.PartStaticLoadCaseGroup":
            return self._parent._cast(_5685.PartStaticLoadCaseGroup)

        @property
        def design_entity_static_load_case_group(
            self: "GearSetStaticLoadCaseGroup._Cast_GearSetStaticLoadCaseGroup",
        ) -> "_5683.DesignEntityStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
                _5683,
            )

            return self._parent._cast(_5683.DesignEntityStaticLoadCaseGroup)

        @property
        def gear_set_static_load_case_group(
            self: "GearSetStaticLoadCaseGroup._Cast_GearSetStaticLoadCaseGroup",
        ) -> "GearSetStaticLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "GearSetStaticLoadCaseGroup._Cast_GearSetStaticLoadCaseGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetStaticLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self: Self) -> "TGearSet":
        """TGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set(self: Self) -> "TGearSet":
        """TGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def part_load_cases(self: Self) -> "List[TGearSetStaticLoad]":
        """List[TGearSetStaticLoad]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set_load_cases(self: Self) -> "List[TGearSetStaticLoad]":
        """List[TGearSetStaticLoad]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gears_load_cases(
        self: Self,
    ) -> "List[_5681.ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_load_cases(
        self: Self,
    ) -> "List[_5682.ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetStaticLoadCaseGroup._Cast_GearSetStaticLoadCaseGroup":
        return self._Cast_GearSetStaticLoadCaseGroup(self)
