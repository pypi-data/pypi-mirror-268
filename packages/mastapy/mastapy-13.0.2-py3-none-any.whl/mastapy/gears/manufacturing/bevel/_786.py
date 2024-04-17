"""ConicalMeshFlankNURBSMicroGeometryConfig"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.bevel import _785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FLANK_NURBS_MICRO_GEOMETRY_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshFlankNURBSMicroGeometryConfig"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshFlankNURBSMicroGeometryConfig",)


Self = TypeVar("Self", bound="ConicalMeshFlankNURBSMicroGeometryConfig")


class ConicalMeshFlankNURBSMicroGeometryConfig(
    _785.ConicalMeshFlankMicroGeometryConfig
):
    """ConicalMeshFlankNURBSMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FLANK_NURBS_MICRO_GEOMETRY_CONFIG
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalMeshFlankNURBSMicroGeometryConfig"
    )

    class _Cast_ConicalMeshFlankNURBSMicroGeometryConfig:
        """Special nested class for casting ConicalMeshFlankNURBSMicroGeometryConfig to subclasses."""

        def __init__(
            self: "ConicalMeshFlankNURBSMicroGeometryConfig._Cast_ConicalMeshFlankNURBSMicroGeometryConfig",
            parent: "ConicalMeshFlankNURBSMicroGeometryConfig",
        ):
            self._parent = parent

        @property
        def conical_mesh_flank_micro_geometry_config(
            self: "ConicalMeshFlankNURBSMicroGeometryConfig._Cast_ConicalMeshFlankNURBSMicroGeometryConfig",
        ) -> "_785.ConicalMeshFlankMicroGeometryConfig":
            return self._parent._cast(_785.ConicalMeshFlankMicroGeometryConfig)

        @property
        def conical_mesh_flank_nurbs_micro_geometry_config(
            self: "ConicalMeshFlankNURBSMicroGeometryConfig._Cast_ConicalMeshFlankNURBSMicroGeometryConfig",
        ) -> "ConicalMeshFlankNURBSMicroGeometryConfig":
            return self._parent

        def __getattr__(
            self: "ConicalMeshFlankNURBSMicroGeometryConfig._Cast_ConicalMeshFlankNURBSMicroGeometryConfig",
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
        self: Self, instance_to_wrap: "ConicalMeshFlankNURBSMicroGeometryConfig.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshFlankNURBSMicroGeometryConfig._Cast_ConicalMeshFlankNURBSMicroGeometryConfig":
        return self._Cast_ConicalMeshFlankNURBSMicroGeometryConfig(self)
