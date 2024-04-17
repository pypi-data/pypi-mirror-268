"""FaceGearSetMicroGeometry"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1237
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Face", "FaceGearSetMicroGeometry"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _999, _997, _996
    from mastapy.gears.analysis import _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetMicroGeometry",)


Self = TypeVar("Self", bound="FaceGearSetMicroGeometry")


class FaceGearSetMicroGeometry(_1237.GearSetImplementationDetail):
    """FaceGearSetMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetMicroGeometry")

    class _Cast_FaceGearSetMicroGeometry:
        """Special nested class for casting FaceGearSetMicroGeometry to subclasses."""

        def __init__(
            self: "FaceGearSetMicroGeometry._Cast_FaceGearSetMicroGeometry",
            parent: "FaceGearSetMicroGeometry",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_detail(
            self: "FaceGearSetMicroGeometry._Cast_FaceGearSetMicroGeometry",
        ) -> "_1237.GearSetImplementationDetail":
            return self._parent._cast(_1237.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "FaceGearSetMicroGeometry._Cast_FaceGearSetMicroGeometry",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "FaceGearSetMicroGeometry._Cast_FaceGearSetMicroGeometry",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def face_gear_set_micro_geometry(
            self: "FaceGearSetMicroGeometry._Cast_FaceGearSetMicroGeometry",
        ) -> "FaceGearSetMicroGeometry":
            return self._parent

        def __getattr__(
            self: "FaceGearSetMicroGeometry._Cast_FaceGearSetMicroGeometry", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetMicroGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def face_gear_micro_geometries(self: Self) -> "List[_997.FaceGearMicroGeometry]":
        """List[mastapy.gears.gear_designs.face.FaceGearMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_mesh_micro_geometries(
        self: Self,
    ) -> "List[_996.FaceGearMeshMicroGeometry]":
        """List[mastapy.gears.gear_designs.face.FaceGearMeshMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def duplicate(self: Self) -> "FaceGearSetMicroGeometry":
        """mastapy.gears.gear_designs.face.FaceGearSetMicroGeometry"""
        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetMicroGeometry._Cast_FaceGearSetMicroGeometry":
        return self._Cast_FaceGearSetMicroGeometry(self)
