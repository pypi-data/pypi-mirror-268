"""FaceGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _999
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.connections_and_sockets.gears import _2318
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSet",)


Self = TypeVar("Self", bound="FaceGearSet")


class FaceGearSet(_2539.GearSet):
    """FaceGearSet

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSet")

    class _Cast_FaceGearSet:
        """Special nested class for casting FaceGearSet to subclasses."""

        def __init__(self: "FaceGearSet._Cast_FaceGearSet", parent: "FaceGearSet"):
            self._parent = parent

        @property
        def gear_set(self: "FaceGearSet._Cast_FaceGearSet") -> "_2539.GearSet":
            return self._parent._cast(_2539.GearSet)

        @property
        def specialised_assembly(
            self: "FaceGearSet._Cast_FaceGearSet",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "FaceGearSet._Cast_FaceGearSet",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "FaceGearSet._Cast_FaceGearSet") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "FaceGearSet._Cast_FaceGearSet",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def face_gear_set(self: "FaceGearSet._Cast_FaceGearSet") -> "FaceGearSet":
            return self._parent

        def __getattr__(self: "FaceGearSet._Cast_FaceGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self: Self) -> "_999.FaceGearSetDesign":
        """mastapy.gears.gear_designs.face.FaceGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gear_set_design(self: Self) -> "_999.FaceGearSetDesign":
        """mastapy.gears.gear_designs.face.FaceGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears(self: Self) -> "List[_2535.FaceGear]":
        """List[mastapy.system_model.part_model.gears.FaceGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes(self: Self) -> "List[_2318.FaceGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.FaceGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FaceGearSet._Cast_FaceGearSet":
        return self._Cast_FaceGearSet(self)
