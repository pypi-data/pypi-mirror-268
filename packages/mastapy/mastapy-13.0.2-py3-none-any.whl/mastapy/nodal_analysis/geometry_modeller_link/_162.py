"""GeometryModellerLengthDimension"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.geometry_modeller_link import _155
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_LENGTH_DIMENSION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "GeometryModellerLengthDimension"
)


__docformat__ = "restructuredtext en"
__all__ = ("GeometryModellerLengthDimension",)


Self = TypeVar("Self", bound="GeometryModellerLengthDimension")


class GeometryModellerLengthDimension(_155.BaseGeometryModellerDimension):
    """GeometryModellerLengthDimension

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_LENGTH_DIMENSION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeometryModellerLengthDimension")

    class _Cast_GeometryModellerLengthDimension:
        """Special nested class for casting GeometryModellerLengthDimension to subclasses."""

        def __init__(
            self: "GeometryModellerLengthDimension._Cast_GeometryModellerLengthDimension",
            parent: "GeometryModellerLengthDimension",
        ):
            self._parent = parent

        @property
        def base_geometry_modeller_dimension(
            self: "GeometryModellerLengthDimension._Cast_GeometryModellerLengthDimension",
        ) -> "_155.BaseGeometryModellerDimension":
            return self._parent._cast(_155.BaseGeometryModellerDimension)

        @property
        def geometry_modeller_length_dimension(
            self: "GeometryModellerLengthDimension._Cast_GeometryModellerLengthDimension",
        ) -> "GeometryModellerLengthDimension":
            return self._parent

        def __getattr__(
            self: "GeometryModellerLengthDimension._Cast_GeometryModellerLengthDimension",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GeometryModellerLengthDimension.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "GeometryModellerLengthDimension._Cast_GeometryModellerLengthDimension":
        return self._Cast_GeometryModellerLengthDimension(self)
