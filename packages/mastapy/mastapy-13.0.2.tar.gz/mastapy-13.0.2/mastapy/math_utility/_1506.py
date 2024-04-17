"""CoordinateSystem3D"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy._math.matrix_4x4 import Matrix4x4
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COORDINATE_SYSTEM_3D = python_net_import(
    "SMT.MastaAPI.MathUtility", "CoordinateSystem3D"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1511


__docformat__ = "restructuredtext en"
__all__ = ("CoordinateSystem3D",)


Self = TypeVar("Self", bound="CoordinateSystem3D")


class CoordinateSystem3D(_0.APIBase):
    """CoordinateSystem3D

    This is a mastapy class.
    """

    TYPE = _COORDINATE_SYSTEM_3D
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoordinateSystem3D")

    class _Cast_CoordinateSystem3D:
        """Special nested class for casting CoordinateSystem3D to subclasses."""

        def __init__(
            self: "CoordinateSystem3D._Cast_CoordinateSystem3D",
            parent: "CoordinateSystem3D",
        ):
            self._parent = parent

        @property
        def coordinate_system_3d(
            self: "CoordinateSystem3D._Cast_CoordinateSystem3D",
        ) -> "CoordinateSystem3D":
            return self._parent

        def __getattr__(self: "CoordinateSystem3D._Cast_CoordinateSystem3D", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoordinateSystem3D.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def origin(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Origin

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def x_axis(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def y_axis(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def z_axis(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def axis(self: Self, degree_of_freedom: "_1511.DegreeOfFreedom") -> "Vector3D":
        """Vector3D

        Args:
            degree_of_freedom (mastapy.math_utility.DegreeOfFreedom)
        """
        degree_of_freedom = conversion.mp_to_pn_enum(
            degree_of_freedom, "SMT.MastaAPI.MathUtility.DegreeOfFreedom"
        )
        return conversion.pn_to_mp_vector3d(self.wrapped.Axis(degree_of_freedom))

    @enforce_parameter_types
    def rotated_about_axis(
        self: Self, axis: "Vector3D", angle: "float"
    ) -> "CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Args:
            axis (Vector3D)
            angle (float)
        """
        axis = conversion.mp_to_pn_vector3d(axis)
        angle = float(angle)
        method_result = self.wrapped.RotatedAboutAxis(axis, angle if angle else 0.0)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def transform_from_world_to_this(self: Self) -> "Matrix4x4":
        """Matrix4x4"""
        return conversion.pn_to_mp_matrix4x4(self.wrapped.TransformFromWorldToThis())

    def transform_to_world_from_this(self: Self) -> "Matrix4x4":
        """Matrix4x4"""
        return conversion.pn_to_mp_matrix4x4(self.wrapped.TransformToWorldFromThis())

    @enforce_parameter_types
    def transformed_by(self: Self, transform: "Matrix4x4") -> "CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Args:
            transform (Matrix4x4)
        """
        transform = conversion.mp_to_pn_matrix4x4(transform)
        method_result = self.wrapped.TransformedBy(transform)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def without_translation(self: Self) -> "CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D"""
        method_result = self.wrapped.WithoutTranslation()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "CoordinateSystem3D._Cast_CoordinateSystem3D":
        return self._Cast_CoordinateSystem3D(self)
