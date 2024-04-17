"""CADFace"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._math.vector_2d import Vector2D
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_FACE = python_net_import("SMT.MastaAPI.Geometry.TwoD", "CADFace")


__docformat__ = "restructuredtext en"
__all__ = ("CADFace",)


Self = TypeVar("Self", bound="CADFace")


class CADFace(_0.APIBase):
    """CADFace

    This is a mastapy class.
    """

    TYPE = _CAD_FACE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADFace")

    class _Cast_CADFace:
        """Special nested class for casting CADFace to subclasses."""

        def __init__(self: "CADFace._Cast_CADFace", parent: "CADFace"):
            self._parent = parent

        @property
        def cad_face(self: "CADFace._Cast_CADFace") -> "CADFace":
            return self._parent

        def __getattr__(self: "CADFace._Cast_CADFace", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADFace.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def add_arc(
        self: Self,
        circle_origin: "Vector2D",
        radius: "float",
        start_angle: "float",
        sweep_angle: "float",
    ):
        """Method does not return.

        Args:
            circle_origin (Vector2D)
            radius (float)
            start_angle (float)
            sweep_angle (float)
        """
        circle_origin = conversion.mp_to_pn_vector2d(circle_origin)
        radius = float(radius)
        start_angle = float(start_angle)
        sweep_angle = float(sweep_angle)
        self.wrapped.AddArc(
            circle_origin,
            radius if radius else 0.0,
            start_angle if start_angle else 0.0,
            sweep_angle if sweep_angle else 0.0,
        )

    @enforce_parameter_types
    def add_line(self: Self, point_1: "Vector2D", point_2: "Vector2D"):
        """Method does not return.

        Args:
            point_1 (Vector2D)
            point_2 (Vector2D)
        """
        point_1 = conversion.mp_to_pn_vector2d(point_1)
        point_2 = conversion.mp_to_pn_vector2d(point_2)
        self.wrapped.AddLine(point_1, point_2)

    @enforce_parameter_types
    def add_poly_line(self: Self, points: "List[Vector2D]"):
        """Method does not return.

        Args:
            points (List[Vector2D])
        """
        points = conversion.mp_to_pn_objects_in_list(points)
        self.wrapped.AddPolyLine(points)

    @property
    def cast_to(self: Self) -> "CADFace._Cast_CADFace":
        return self._Cast_CADFace(self)
