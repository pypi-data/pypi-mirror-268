"""TransformMatrix3D"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy._math.matrix_4x4 import Matrix4x4
from mastapy._internal.tuple_with_name import TupleWithName
from mastapy.math_utility import _1532
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRANSFORM_MATRIX_3D = python_net_import(
    "SMT.MastaAPI.MathUtility", "TransformMatrix3D"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1521


__docformat__ = "restructuredtext en"
__all__ = ("TransformMatrix3D",)


Self = TypeVar("Self", bound="TransformMatrix3D")


class TransformMatrix3D(_1532.RealMatrix):
    """TransformMatrix3D

    This is a mastapy class.
    """

    TYPE = _TRANSFORM_MATRIX_3D
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TransformMatrix3D")

    class _Cast_TransformMatrix3D:
        """Special nested class for casting TransformMatrix3D to subclasses."""

        def __init__(
            self: "TransformMatrix3D._Cast_TransformMatrix3D",
            parent: "TransformMatrix3D",
        ):
            self._parent = parent

        @property
        def real_matrix(
            self: "TransformMatrix3D._Cast_TransformMatrix3D",
        ) -> "_1532.RealMatrix":
            return self._parent._cast(_1532.RealMatrix)

        @property
        def generic_matrix(
            self: "TransformMatrix3D._Cast_TransformMatrix3D",
        ) -> "_1521.GenericMatrix":
            from mastapy.math_utility import _1521

            return self._parent._cast(_1521.GenericMatrix)

        @property
        def transform_matrix_3d(
            self: "TransformMatrix3D._Cast_TransformMatrix3D",
        ) -> "TransformMatrix3D":
            return self._parent

        def __getattr__(self: "TransformMatrix3D._Cast_TransformMatrix3D", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TransformMatrix3D.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_identity(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsIdentity

        if temp is None:
            return False

        return temp

    @property
    def translation(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Translation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @translation.setter
    @enforce_parameter_types
    def translation(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Translation = value

    @property
    def x_axis(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.XAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @x_axis.setter
    @enforce_parameter_types
    def x_axis(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.XAxis = value

    @property
    def y_axis(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.YAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @y_axis.setter
    @enforce_parameter_types
    def y_axis(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.YAxis = value

    @property
    def z_axis(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.ZAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @z_axis.setter
    @enforce_parameter_types
    def z_axis(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.ZAxis = value

    @enforce_parameter_types
    def has_rotation(self: Self, tolerance: "float" = 0.0) -> "bool":
        """bool

        Args:
            tolerance (float, optional)
        """
        tolerance = float(tolerance)
        method_result = self.wrapped.HasRotation(tolerance if tolerance else 0.0)
        return method_result

    @enforce_parameter_types
    def has_translation(self: Self, tolerance: "float" = 0.0) -> "bool":
        """bool

        Args:
            tolerance (float, optional)
        """
        tolerance = float(tolerance)
        method_result = self.wrapped.HasTranslation(tolerance if tolerance else 0.0)
        return method_result

    def negated(self: Self) -> "Matrix4x4":
        """Matrix4x4"""
        return conversion.pn_to_mp_matrix4x4(self.wrapped.Negated())

    def rigid_inverse(self: Self) -> "Matrix4x4":
        """Matrix4x4"""
        return conversion.pn_to_mp_matrix4x4(self.wrapped.RigidInverse())

    @enforce_parameter_types
    def rotate(self: Self, angular: "Vector3D") -> "Vector3D":
        """Vector3D

        Args:
            angular (Vector3D)
        """
        angular = conversion.mp_to_pn_vector3d(angular)
        return conversion.pn_to_mp_vector3d(self.wrapped.Rotate(angular))

    @enforce_parameter_types
    def transform(self: Self, linear: "Vector3D") -> "Vector3D":
        """Vector3D

        Args:
            linear (Vector3D)
        """
        linear = conversion.mp_to_pn_vector3d(linear)
        return conversion.pn_to_mp_vector3d(self.wrapped.Transform(linear))

    @enforce_parameter_types
    def transform_linear_and_angular_components(
        self: Self, linear: "Vector3D", angular: "Vector3D"
    ) -> "TupleWithName":
        """TupleWithName

        Args:
            linear (Vector3D)
            angular (Vector3D)
        """
        linear = conversion.mp_to_pn_vector3d(linear)
        angular = conversion.mp_to_pn_vector3d(angular)
        return conversion.pn_to_mp_tuple_with_name(
            self.wrapped.TransformLinearAndAngularComponents(linear, angular),
            (conversion.pn_to_mp_vector3d, conversion.pn_to_mp_vector3d),
        )

    def transposed(self: Self) -> "Matrix4x4":
        """Matrix4x4"""
        return conversion.pn_to_mp_matrix4x4(self.wrapped.Transposed())

    @property
    def cast_to(self: Self) -> "TransformMatrix3D._Cast_TransformMatrix3D":
        return self._Cast_TransformMatrix3D(self)
