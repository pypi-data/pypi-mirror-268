"""ConicalMeshFlankMicroGeometryConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FLANK_MICRO_GEOMETRY_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshFlankMicroGeometryConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical.micro_geometry import _1179
    from mastapy.gears.manufacturing.bevel import _784, _786


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshFlankMicroGeometryConfig",)


Self = TypeVar("Self", bound="ConicalMeshFlankMicroGeometryConfig")


class ConicalMeshFlankMicroGeometryConfig(_0.APIBase):
    """ConicalMeshFlankMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FLANK_MICRO_GEOMETRY_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshFlankMicroGeometryConfig")

    class _Cast_ConicalMeshFlankMicroGeometryConfig:
        """Special nested class for casting ConicalMeshFlankMicroGeometryConfig to subclasses."""

        def __init__(
            self: "ConicalMeshFlankMicroGeometryConfig._Cast_ConicalMeshFlankMicroGeometryConfig",
            parent: "ConicalMeshFlankMicroGeometryConfig",
        ):
            self._parent = parent

        @property
        def conical_mesh_flank_manufacturing_config(
            self: "ConicalMeshFlankMicroGeometryConfig._Cast_ConicalMeshFlankMicroGeometryConfig",
        ) -> "_784.ConicalMeshFlankManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _784

            return self._parent._cast(_784.ConicalMeshFlankManufacturingConfig)

        @property
        def conical_mesh_flank_nurbs_micro_geometry_config(
            self: "ConicalMeshFlankMicroGeometryConfig._Cast_ConicalMeshFlankMicroGeometryConfig",
        ) -> "_786.ConicalMeshFlankNURBSMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _786

            return self._parent._cast(_786.ConicalMeshFlankNURBSMicroGeometryConfig)

        @property
        def conical_mesh_flank_micro_geometry_config(
            self: "ConicalMeshFlankMicroGeometryConfig._Cast_ConicalMeshFlankMicroGeometryConfig",
        ) -> "ConicalMeshFlankMicroGeometryConfig":
            return self._parent

        def __getattr__(
            self: "ConicalMeshFlankMicroGeometryConfig._Cast_ConicalMeshFlankMicroGeometryConfig",
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
        self: Self, instance_to_wrap: "ConicalMeshFlankMicroGeometryConfig.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def delta_h_as_percent_of_face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaHAsPercentOfFaceWidth

        if temp is None:
            return 0.0

        return temp

    @delta_h_as_percent_of_face_width.setter
    @enforce_parameter_types
    def delta_h_as_percent_of_face_width(self: Self, value: "float"):
        self.wrapped.DeltaHAsPercentOfFaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def delta_v_as_percent_of_wheel_tip_to_fillet_flank_boundary(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaVAsPercentOfWheelTipToFilletFlankBoundary

        if temp is None:
            return 0.0

        return temp

    @delta_v_as_percent_of_wheel_tip_to_fillet_flank_boundary.setter
    @enforce_parameter_types
    def delta_v_as_percent_of_wheel_tip_to_fillet_flank_boundary(
        self: Self, value: "float"
    ):
        self.wrapped.DeltaVAsPercentOfWheelTipToFilletFlankBoundary = (
            float(value) if value is not None else 0.0
        )

    @property
    def perform_vh_check(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PerformVHCheck

        if temp is None:
            return False

        return temp

    @perform_vh_check.setter
    @enforce_parameter_types
    def perform_vh_check(self: Self, value: "bool"):
        self.wrapped.PerformVHCheck = bool(value) if value is not None else False

    @property
    def specified_ease_off_surface(self: Self) -> "_1179.ConicalGearFlankMicroGeometry":
        """mastapy.gears.gear_designs.conical.micro_geometry.ConicalGearFlankMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecifiedEaseOffSurface

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConicalMeshFlankMicroGeometryConfig._Cast_ConicalMeshFlankMicroGeometryConfig"
    ):
        return self._Cast_ConicalMeshFlankMicroGeometryConfig(self)
