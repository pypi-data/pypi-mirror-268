"""GeometryModellerDimension"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_DIMENSION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "GeometryModellerDimension"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.geometry_modeller_link import _161


__docformat__ = "restructuredtext en"
__all__ = ("GeometryModellerDimension",)


Self = TypeVar("Self", bound="GeometryModellerDimension")


class GeometryModellerDimension(_0.APIBase):
    """GeometryModellerDimension

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_DIMENSION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeometryModellerDimension")

    class _Cast_GeometryModellerDimension:
        """Special nested class for casting GeometryModellerDimension to subclasses."""

        def __init__(
            self: "GeometryModellerDimension._Cast_GeometryModellerDimension",
            parent: "GeometryModellerDimension",
        ):
            self._parent = parent

        @property
        def geometry_modeller_dimension(
            self: "GeometryModellerDimension._Cast_GeometryModellerDimension",
        ) -> "GeometryModellerDimension":
            return self._parent

        def __getattr__(
            self: "GeometryModellerDimension._Cast_GeometryModellerDimension", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GeometryModellerDimension.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def type_(self: Self) -> "_161.GeometryModellerDimensionType":
        """mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimensionType"""
        temp = self.wrapped.Type

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink.GeometryModellerDimensionType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis.geometry_modeller_link._161",
            "GeometryModellerDimensionType",
        )(value)

    @type_.setter
    @enforce_parameter_types
    def type_(self: Self, value: "_161.GeometryModellerDimensionType"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink.GeometryModellerDimensionType",
        )
        self.wrapped.Type = value

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
    ) -> "GeometryModellerDimension._Cast_GeometryModellerDimension":
        return self._Cast_GeometryModellerDimension(self)
