"""FaceGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Face", "FaceGearMeshDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _999, _993
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshDesign",)


Self = TypeVar("Self", bound="FaceGearMeshDesign")


class FaceGearMeshDesign(_953.GearMeshDesign):
    """FaceGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshDesign")

    class _Cast_FaceGearMeshDesign:
        """Special nested class for casting FaceGearMeshDesign to subclasses."""

        def __init__(
            self: "FaceGearMeshDesign._Cast_FaceGearMeshDesign",
            parent: "FaceGearMeshDesign",
        ):
            self._parent = parent

        @property
        def gear_mesh_design(
            self: "FaceGearMeshDesign._Cast_FaceGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "FaceGearMeshDesign._Cast_FaceGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def face_gear_mesh_design(
            self: "FaceGearMeshDesign._Cast_FaceGearMeshDesign",
        ) -> "FaceGearMeshDesign":
            return self._parent

        def __getattr__(self: "FaceGearMeshDesign._Cast_FaceGearMeshDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMeshDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @property
    def working_normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def face_gear_set(self: Self) -> "_999.FaceGearSetDesign":
        """mastapy.gears.gear_designs.face.FaceGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears(self: Self) -> "List[_993.FaceGearDesign]":
        """List[mastapy.gears.gear_designs.face.FaceGearDesign]

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
    def cast_to(self: Self) -> "FaceGearMeshDesign._Cast_FaceGearMeshDesign":
        return self._Cast_FaceGearMeshDesign(self)
