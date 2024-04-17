"""CirclesOnAxis"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._math.vector_3d import Vector3D
from mastapy._internal import conversion
from mastapy._math.vector_2d import Vector2D
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DOUBLE = python_net_import("System", "Double")
_CIRCLES_ON_AXIS = python_net_import("SMT.MastaAPI.MathUtility", "CirclesOnAxis")


__docformat__ = "restructuredtext en"
__all__ = ("CirclesOnAxis",)


Self = TypeVar("Self", bound="CirclesOnAxis")


class CirclesOnAxis(_0.APIBase):
    """CirclesOnAxis

    This is a mastapy class.
    """

    TYPE = _CIRCLES_ON_AXIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CirclesOnAxis")

    class _Cast_CirclesOnAxis:
        """Special nested class for casting CirclesOnAxis to subclasses."""

        def __init__(
            self: "CirclesOnAxis._Cast_CirclesOnAxis", parent: "CirclesOnAxis"
        ):
            self._parent = parent

        @property
        def circles_on_axis(
            self: "CirclesOnAxis._Cast_CirclesOnAxis",
        ) -> "CirclesOnAxis":
            return self._parent

        def __getattr__(self: "CirclesOnAxis._Cast_CirclesOnAxis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CirclesOnAxis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axis(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Axis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @axis.setter
    @enforce_parameter_types
    def axis(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Axis = value

    @property
    def coord_fillet_radii(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoordFilletRadii

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def coords(self: Self) -> "List[Vector2D]":
        """List[Vector2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Coords

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector2D)

        if value is None:
            return None

        return value

    @property
    def mouse_position(self: Self) -> "Vector2D":
        """Vector2D"""
        temp = self.wrapped.MousePosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @mouse_position.setter
    @enforce_parameter_types
    def mouse_position(self: Self, value: "Vector2D"):
        value = conversion.mp_to_pn_vector2d(value)
        self.wrapped.MousePosition = value

    @property
    def origin(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Origin

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @origin.setter
    @enforce_parameter_types
    def origin(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Origin = value

    @enforce_parameter_types
    def add_coords_from_point_in_sketch_plane(
        self: Self, point_in_sketch_plane: "Vector3D"
    ):
        """Method does not return.

        Args:
            point_in_sketch_plane (Vector3D)
        """
        point_in_sketch_plane = conversion.mp_to_pn_vector3d(point_in_sketch_plane)
        self.wrapped.AddCoords.Overloads[Vector3D](point_in_sketch_plane)

    @enforce_parameter_types
    def add_coords_from_point_on_axis(
        self: Self, point_on_axis: "Vector3D", radius: "float"
    ):
        """Method does not return.

        Args:
            point_on_axis (Vector3D)
            radius (float)
        """
        point_on_axis = conversion.mp_to_pn_vector3d(point_on_axis)
        radius = float(radius)
        self.wrapped.AddCoords.Overloads[Vector3D, _DOUBLE](
            point_on_axis, radius if radius else 0.0
        )

    @enforce_parameter_types
    def add_coords(self: Self, offset: "float", radius: "float"):
        """Method does not return.

        Args:
            offset (float)
            radius (float)
        """
        offset = float(offset)
        radius = float(radius)
        self.wrapped.AddCoords.Overloads[_DOUBLE, _DOUBLE](
            offset if offset else 0.0, radius if radius else 0.0
        )

    @enforce_parameter_types
    def add_fillet_point(
        self: Self,
        point_a_in_sketch_plane: "Vector3D",
        point_b_in_sketch_plane: "Vector3D",
        guide_point: "Vector3D",
        radius: "float",
    ):
        """Method does not return.

        Args:
            point_a_in_sketch_plane (Vector3D)
            point_b_in_sketch_plane (Vector3D)
            guide_point (Vector3D)
            radius (float)
        """
        point_a_in_sketch_plane = conversion.mp_to_pn_vector3d(point_a_in_sketch_plane)
        point_b_in_sketch_plane = conversion.mp_to_pn_vector3d(point_b_in_sketch_plane)
        guide_point = conversion.mp_to_pn_vector3d(guide_point)
        radius = float(radius)
        self.wrapped.AddFilletPoint(
            point_a_in_sketch_plane,
            point_b_in_sketch_plane,
            guide_point,
            radius if radius else 0.0,
        )

    @enforce_parameter_types
    def set_mouse_position(self: Self, point_in_sketch_plane: "Vector3D"):
        """Method does not return.

        Args:
            point_in_sketch_plane (Vector3D)
        """
        point_in_sketch_plane = conversion.mp_to_pn_vector3d(point_in_sketch_plane)
        self.wrapped.SetMousePosition(point_in_sketch_plane)

    @property
    def cast_to(self: Self) -> "CirclesOnAxis._Cast_CirclesOnAxis":
        return self._Cast_CirclesOnAxis(self)
