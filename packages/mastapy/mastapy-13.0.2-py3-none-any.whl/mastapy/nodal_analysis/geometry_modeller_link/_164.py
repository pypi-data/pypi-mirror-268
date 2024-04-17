"""GeometryModellerUnitlessDimension"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.geometry_modeller_link import _155
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_UNITLESS_DIMENSION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink",
    "GeometryModellerUnitlessDimension",
)


__docformat__ = "restructuredtext en"
__all__ = ("GeometryModellerUnitlessDimension",)


Self = TypeVar("Self", bound="GeometryModellerUnitlessDimension")


class GeometryModellerUnitlessDimension(_155.BaseGeometryModellerDimension):
    """GeometryModellerUnitlessDimension

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_UNITLESS_DIMENSION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeometryModellerUnitlessDimension")

    class _Cast_GeometryModellerUnitlessDimension:
        """Special nested class for casting GeometryModellerUnitlessDimension to subclasses."""

        def __init__(
            self: "GeometryModellerUnitlessDimension._Cast_GeometryModellerUnitlessDimension",
            parent: "GeometryModellerUnitlessDimension",
        ):
            self._parent = parent

        @property
        def base_geometry_modeller_dimension(
            self: "GeometryModellerUnitlessDimension._Cast_GeometryModellerUnitlessDimension",
        ) -> "_155.BaseGeometryModellerDimension":
            return self._parent._cast(_155.BaseGeometryModellerDimension)

        @property
        def geometry_modeller_unitless_dimension(
            self: "GeometryModellerUnitlessDimension._Cast_GeometryModellerUnitlessDimension",
        ) -> "GeometryModellerUnitlessDimension":
            return self._parent

        def __getattr__(
            self: "GeometryModellerUnitlessDimension._Cast_GeometryModellerUnitlessDimension",
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
        self: Self, instance_to_wrap: "GeometryModellerUnitlessDimension.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @value.setter
    @enforce_parameter_types
    def value(self: Self, value: "float"):
        self.wrapped.Value = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "GeometryModellerUnitlessDimension._Cast_GeometryModellerUnitlessDimension":
        return self._Cast_GeometryModellerUnitlessDimension(self)
