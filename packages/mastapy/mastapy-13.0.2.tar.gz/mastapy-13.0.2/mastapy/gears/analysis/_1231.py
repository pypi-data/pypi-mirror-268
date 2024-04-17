"""GearMeshImplementationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshImplementationDetail"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _625
    from mastapy.gears.manufacturing.bevel import _788, _789, _790
    from mastapy.gears.gear_designs.face import _996
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104
    from mastapy.gears.fe_model import _1204
    from mastapy.gears.fe_model.cylindrical import _1208
    from mastapy.gears.fe_model.conical import _1211
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshImplementationDetail",)


Self = TypeVar("Self", bound="GearMeshImplementationDetail")


class GearMeshImplementationDetail(_1228.GearMeshDesignAnalysis):
    """GearMeshImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshImplementationDetail")

    class _Cast_GearMeshImplementationDetail:
        """Special nested class for casting GearMeshImplementationDetail to subclasses."""

        def __init__(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
            parent: "GearMeshImplementationDetail",
        ):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1228.GearMeshDesignAnalysis":
            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_625.CylindricalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _625

            return self._parent._cast(_625.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_config(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_788.ConicalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _788

            return self._parent._cast(_788.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_789.ConicalMeshMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_790.ConicalMeshMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _790

            return self._parent._cast(_790.ConicalMeshMicroGeometryConfigBase)

        @property
        def face_gear_mesh_micro_geometry(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_996.FaceGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.face import _996

            return self._parent._cast(_996.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1104.CylindricalGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104

            return self._parent._cast(_1104.CylindricalGearMeshMicroGeometry)

        @property
        def gear_mesh_fe_model(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1204.GearMeshFEModel":
            from mastapy.gears.fe_model import _1204

            return self._parent._cast(_1204.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1208.CylindricalGearMeshFEModel":
            from mastapy.gears.fe_model.cylindrical import _1208

            return self._parent._cast(_1208.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1211.ConicalMeshFEModel":
            from mastapy.gears.fe_model.conical import _1211

            return self._parent._cast(_1211.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_detail(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "GearMeshImplementationDetail":
            return self._parent

        def __getattr__(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshImplementationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail":
        return self._Cast_GearMeshImplementationDetail(self)
