"""GeometryModellerAngleDimension"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.geometry_modeller_link import _155
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_ANGLE_DIMENSION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "GeometryModellerAngleDimension"
)


__docformat__ = "restructuredtext en"
__all__ = ("GeometryModellerAngleDimension",)


Self = TypeVar("Self", bound="GeometryModellerAngleDimension")


class GeometryModellerAngleDimension(_155.BaseGeometryModellerDimension):
    """GeometryModellerAngleDimension

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_ANGLE_DIMENSION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeometryModellerAngleDimension")

    class _Cast_GeometryModellerAngleDimension:
        """Special nested class for casting GeometryModellerAngleDimension to subclasses."""

        def __init__(
            self: "GeometryModellerAngleDimension._Cast_GeometryModellerAngleDimension",
            parent: "GeometryModellerAngleDimension",
        ):
            self._parent = parent

        @property
        def base_geometry_modeller_dimension(
            self: "GeometryModellerAngleDimension._Cast_GeometryModellerAngleDimension",
        ) -> "_155.BaseGeometryModellerDimension":
            return self._parent._cast(_155.BaseGeometryModellerDimension)

        @property
        def geometry_modeller_angle_dimension(
            self: "GeometryModellerAngleDimension._Cast_GeometryModellerAngleDimension",
        ) -> "GeometryModellerAngleDimension":
            return self._parent

        def __getattr__(
            self: "GeometryModellerAngleDimension._Cast_GeometryModellerAngleDimension",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GeometryModellerAngleDimension.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    @enforce_parameter_types
    def angle(self: Self, value: "float"):
        self.wrapped.Angle = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "GeometryModellerAngleDimension._Cast_GeometryModellerAngleDimension":
        return self._Cast_GeometryModellerAngleDimension(self)
