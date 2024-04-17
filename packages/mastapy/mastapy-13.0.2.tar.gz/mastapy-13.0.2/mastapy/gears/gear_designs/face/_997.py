"""FaceGearMicroGeometry"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Face", "FaceGearMicroGeometry"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _993
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107
    from mastapy.gears.analysis import _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMicroGeometry",)


Self = TypeVar("Self", bound="FaceGearMicroGeometry")


class FaceGearMicroGeometry(_1227.GearImplementationDetail):
    """FaceGearMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMicroGeometry")

    class _Cast_FaceGearMicroGeometry:
        """Special nested class for casting FaceGearMicroGeometry to subclasses."""

        def __init__(
            self: "FaceGearMicroGeometry._Cast_FaceGearMicroGeometry",
            parent: "FaceGearMicroGeometry",
        ):
            self._parent = parent

        @property
        def gear_implementation_detail(
            self: "FaceGearMicroGeometry._Cast_FaceGearMicroGeometry",
        ) -> "_1227.GearImplementationDetail":
            return self._parent._cast(_1227.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "FaceGearMicroGeometry._Cast_FaceGearMicroGeometry",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "FaceGearMicroGeometry._Cast_FaceGearMicroGeometry",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def face_gear_micro_geometry(
            self: "FaceGearMicroGeometry._Cast_FaceGearMicroGeometry",
        ) -> "FaceGearMicroGeometry":
            return self._parent

        def __getattr__(
            self: "FaceGearMicroGeometry._Cast_FaceGearMicroGeometry", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMicroGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_gear(self: Self) -> "_993.FaceGearDesign":
        """mastapy.gears.gear_designs.face.FaceGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry(self: Self) -> "_1107.CylindricalGearMicroGeometryBase":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMicroGeometryBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGearMicroGeometry._Cast_FaceGearMicroGeometry":
        return self._Cast_FaceGearMicroGeometry(self)
