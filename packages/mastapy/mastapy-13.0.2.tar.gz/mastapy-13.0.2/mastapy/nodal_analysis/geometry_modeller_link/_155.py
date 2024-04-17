"""BaseGeometryModellerDimension"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASE_GEOMETRY_MODELLER_DIMENSION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "BaseGeometryModellerDimension"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.geometry_modeller_link import _156, _157, _162, _164


__docformat__ = "restructuredtext en"
__all__ = ("BaseGeometryModellerDimension",)


Self = TypeVar("Self", bound="BaseGeometryModellerDimension")


class BaseGeometryModellerDimension(_0.APIBase):
    """BaseGeometryModellerDimension

    This is a mastapy class.
    """

    TYPE = _BASE_GEOMETRY_MODELLER_DIMENSION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BaseGeometryModellerDimension")

    class _Cast_BaseGeometryModellerDimension:
        """Special nested class for casting BaseGeometryModellerDimension to subclasses."""

        def __init__(
            self: "BaseGeometryModellerDimension._Cast_BaseGeometryModellerDimension",
            parent: "BaseGeometryModellerDimension",
        ):
            self._parent = parent

        @property
        def geometry_modeller_angle_dimension(
            self: "BaseGeometryModellerDimension._Cast_BaseGeometryModellerDimension",
        ) -> "_156.GeometryModellerAngleDimension":
            from mastapy.nodal_analysis.geometry_modeller_link import _156

            return self._parent._cast(_156.GeometryModellerAngleDimension)

        @property
        def geometry_modeller_count_dimension(
            self: "BaseGeometryModellerDimension._Cast_BaseGeometryModellerDimension",
        ) -> "_157.GeometryModellerCountDimension":
            from mastapy.nodal_analysis.geometry_modeller_link import _157

            return self._parent._cast(_157.GeometryModellerCountDimension)

        @property
        def geometry_modeller_length_dimension(
            self: "BaseGeometryModellerDimension._Cast_BaseGeometryModellerDimension",
        ) -> "_162.GeometryModellerLengthDimension":
            from mastapy.nodal_analysis.geometry_modeller_link import _162

            return self._parent._cast(_162.GeometryModellerLengthDimension)

        @property
        def geometry_modeller_unitless_dimension(
            self: "BaseGeometryModellerDimension._Cast_BaseGeometryModellerDimension",
        ) -> "_164.GeometryModellerUnitlessDimension":
            from mastapy.nodal_analysis.geometry_modeller_link import _164

            return self._parent._cast(_164.GeometryModellerUnitlessDimension)

        @property
        def base_geometry_modeller_dimension(
            self: "BaseGeometryModellerDimension._Cast_BaseGeometryModellerDimension",
        ) -> "BaseGeometryModellerDimension":
            return self._parent

        def __getattr__(
            self: "BaseGeometryModellerDimension._Cast_BaseGeometryModellerDimension",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BaseGeometryModellerDimension.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "BaseGeometryModellerDimension._Cast_BaseGeometryModellerDimension":
        return self._Cast_BaseGeometryModellerDimension(self)
