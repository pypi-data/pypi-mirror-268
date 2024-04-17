"""GriddedSurfaceAccessor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from clr import GetClrType

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_DOUBLE = python_net_import("System", "Double")
_GRIDDED_SURFACE_ACCESSOR = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredData", "GriddedSurfaceAccessor"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1522


__docformat__ = "restructuredtext en"
__all__ = ("GriddedSurfaceAccessor",)


Self = TypeVar("Self", bound="GriddedSurfaceAccessor")


class GriddedSurfaceAccessor(_0.APIBase):
    """GriddedSurfaceAccessor

    This is a mastapy class.
    """

    TYPE = _GRIDDED_SURFACE_ACCESSOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GriddedSurfaceAccessor")

    class _Cast_GriddedSurfaceAccessor:
        """Special nested class for casting GriddedSurfaceAccessor to subclasses."""

        def __init__(
            self: "GriddedSurfaceAccessor._Cast_GriddedSurfaceAccessor",
            parent: "GriddedSurfaceAccessor",
        ):
            self._parent = parent

        @property
        def gridded_surface_accessor(
            self: "GriddedSurfaceAccessor._Cast_GriddedSurfaceAccessor",
        ) -> "GriddedSurfaceAccessor":
            return self._parent

        def __getattr__(
            self: "GriddedSurfaceAccessor._Cast_GriddedSurfaceAccessor", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GriddedSurfaceAccessor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def create_new_from_gridded_data(
        self: Self, x_values: "List[float]", y_values: "List[float]"
    ) -> "GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor

        Args:
            x_values (List[float])
            y_values (List[float])
        """
        x_values = conversion.mp_to_pn_array_float(x_values)
        y_values = conversion.mp_to_pn_array_float(y_values)
        method_result = self.wrapped.CreateNewFromGriddedData.Overloads[
            _ARRAY[_DOUBLE], _ARRAY[_DOUBLE]
        ](x_values, y_values)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_new_from_gridded_data_3d(
        self: Self,
        x_values: "List[float]",
        y_values: "List[float]",
        z_values: "List[List[float]]",
    ) -> "GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor

        Args:
            x_values (List[float])
            y_values (List[float])
            z_values (List[List[float]])
        """
        x_values = conversion.mp_to_pn_array_float(x_values)
        y_values = conversion.mp_to_pn_array_float(y_values)
        z_values = conversion.mp_to_pn_list_float_2d(z_values)
        method_result = self.wrapped.CreateNewFromGriddedData.Overloads[
            _ARRAY[_DOUBLE], _ARRAY[_DOUBLE], GetClrType(_DOUBLE).MakeArrayType(2)
        ](x_values, y_values, z_values)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_new_from_gridded_surface(
        self: Self, grid: "_1522.GriddedSurface"
    ) -> "GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor

        Args:
            grid (mastapy.math_utility.GriddedSurface)
        """
        method_result = self.wrapped.CreateNewFromGriddedSurface(
            grid.wrapped if grid else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def get_gridded_surface(self: Self) -> "_1522.GriddedSurface":
        """mastapy.math_utility.GriddedSurface"""
        method_result = self.wrapped.GetGriddedSurface()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "GriddedSurfaceAccessor._Cast_GriddedSurfaceAccessor":
        return self._Cast_GriddedSurfaceAccessor(self)
