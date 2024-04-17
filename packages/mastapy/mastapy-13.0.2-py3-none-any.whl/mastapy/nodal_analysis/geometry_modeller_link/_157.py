"""GeometryModellerCountDimension"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.geometry_modeller_link import _155
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_COUNT_DIMENSION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "GeometryModellerCountDimension"
)


__docformat__ = "restructuredtext en"
__all__ = ("GeometryModellerCountDimension",)


Self = TypeVar("Self", bound="GeometryModellerCountDimension")


class GeometryModellerCountDimension(_155.BaseGeometryModellerDimension):
    """GeometryModellerCountDimension

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_COUNT_DIMENSION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeometryModellerCountDimension")

    class _Cast_GeometryModellerCountDimension:
        """Special nested class for casting GeometryModellerCountDimension to subclasses."""

        def __init__(
            self: "GeometryModellerCountDimension._Cast_GeometryModellerCountDimension",
            parent: "GeometryModellerCountDimension",
        ):
            self._parent = parent

        @property
        def base_geometry_modeller_dimension(
            self: "GeometryModellerCountDimension._Cast_GeometryModellerCountDimension",
        ) -> "_155.BaseGeometryModellerDimension":
            return self._parent._cast(_155.BaseGeometryModellerDimension)

        @property
        def geometry_modeller_count_dimension(
            self: "GeometryModellerCountDimension._Cast_GeometryModellerCountDimension",
        ) -> "GeometryModellerCountDimension":
            return self._parent

        def __getattr__(
            self: "GeometryModellerCountDimension._Cast_GeometryModellerCountDimension",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GeometryModellerCountDimension.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def count(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Count

        if temp is None:
            return 0

        return temp

    @count.setter
    @enforce_parameter_types
    def count(self: Self, value: "int"):
        self.wrapped.Count = int(value) if value is not None else 0

    @property
    def cast_to(
        self: Self,
    ) -> "GeometryModellerCountDimension._Cast_GeometryModellerCountDimension":
        return self._Cast_GeometryModellerCountDimension(self)
