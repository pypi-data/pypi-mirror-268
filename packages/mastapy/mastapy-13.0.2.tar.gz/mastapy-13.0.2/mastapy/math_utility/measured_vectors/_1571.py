"""VectorWithLinearAndAngularComponents"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VECTOR_WITH_LINEAR_AND_ANGULAR_COMPONENTS = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredVectors", "VectorWithLinearAndAngularComponents"
)


__docformat__ = "restructuredtext en"
__all__ = ("VectorWithLinearAndAngularComponents",)


Self = TypeVar("Self", bound="VectorWithLinearAndAngularComponents")


class VectorWithLinearAndAngularComponents(_0.APIBase):
    """VectorWithLinearAndAngularComponents

    This is a mastapy class.
    """

    TYPE = _VECTOR_WITH_LINEAR_AND_ANGULAR_COMPONENTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VectorWithLinearAndAngularComponents")

    class _Cast_VectorWithLinearAndAngularComponents:
        """Special nested class for casting VectorWithLinearAndAngularComponents to subclasses."""

        def __init__(
            self: "VectorWithLinearAndAngularComponents._Cast_VectorWithLinearAndAngularComponents",
            parent: "VectorWithLinearAndAngularComponents",
        ):
            self._parent = parent

        @property
        def vector_with_linear_and_angular_components(
            self: "VectorWithLinearAndAngularComponents._Cast_VectorWithLinearAndAngularComponents",
        ) -> "VectorWithLinearAndAngularComponents":
            return self._parent

        def __getattr__(
            self: "VectorWithLinearAndAngularComponents._Cast_VectorWithLinearAndAngularComponents",
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
        self: Self, instance_to_wrap: "VectorWithLinearAndAngularComponents.TYPE"
    ):
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
    def angular(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Angular

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def linear(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Linear

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def theta_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThetaX

        if temp is None:
            return 0.0

        return temp

    @theta_x.setter
    @enforce_parameter_types
    def theta_x(self: Self, value: "float"):
        self.wrapped.ThetaX = float(value) if value is not None else 0.0

    @property
    def theta_y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThetaY

        if temp is None:
            return 0.0

        return temp

    @theta_y.setter
    @enforce_parameter_types
    def theta_y(self: Self, value: "float"):
        self.wrapped.ThetaY = float(value) if value is not None else 0.0

    @property
    def theta_z(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThetaZ

        if temp is None:
            return 0.0

        return temp

    @theta_z.setter
    @enforce_parameter_types
    def theta_z(self: Self, value: "float"):
        self.wrapped.ThetaZ = float(value) if value is not None else 0.0

    @property
    def x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.X

        if temp is None:
            return 0.0

        return temp

    @x.setter
    @enforce_parameter_types
    def x(self: Self, value: "float"):
        self.wrapped.X = float(value) if value is not None else 0.0

    @property
    def y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Y

        if temp is None:
            return 0.0

        return temp

    @y.setter
    @enforce_parameter_types
    def y(self: Self, value: "float"):
        self.wrapped.Y = float(value) if value is not None else 0.0

    @property
    def z(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Z

        if temp is None:
            return 0.0

        return temp

    @z.setter
    @enforce_parameter_types
    def z(self: Self, value: "float"):
        self.wrapped.Z = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "VectorWithLinearAndAngularComponents._Cast_VectorWithLinearAndAngularComponents":
        return self._Cast_VectorWithLinearAndAngularComponents(self)
