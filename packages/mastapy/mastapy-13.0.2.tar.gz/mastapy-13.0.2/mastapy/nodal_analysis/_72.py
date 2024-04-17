"""LinearDampingConnectionProperties"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis import _46
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_DAMPING_CONNECTION_PROPERTIES = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "LinearDampingConnectionProperties"
)


__docformat__ = "restructuredtext en"
__all__ = ("LinearDampingConnectionProperties",)


Self = TypeVar("Self", bound="LinearDampingConnectionProperties")


class LinearDampingConnectionProperties(_46.AbstractLinearConnectionProperties):
    """LinearDampingConnectionProperties

    This is a mastapy class.
    """

    TYPE = _LINEAR_DAMPING_CONNECTION_PROPERTIES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearDampingConnectionProperties")

    class _Cast_LinearDampingConnectionProperties:
        """Special nested class for casting LinearDampingConnectionProperties to subclasses."""

        def __init__(
            self: "LinearDampingConnectionProperties._Cast_LinearDampingConnectionProperties",
            parent: "LinearDampingConnectionProperties",
        ):
            self._parent = parent

        @property
        def abstract_linear_connection_properties(
            self: "LinearDampingConnectionProperties._Cast_LinearDampingConnectionProperties",
        ) -> "_46.AbstractLinearConnectionProperties":
            return self._parent._cast(_46.AbstractLinearConnectionProperties)

        @property
        def linear_damping_connection_properties(
            self: "LinearDampingConnectionProperties._Cast_LinearDampingConnectionProperties",
        ) -> "LinearDampingConnectionProperties":
            return self._parent

        def __getattr__(
            self: "LinearDampingConnectionProperties._Cast_LinearDampingConnectionProperties",
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
        self: Self, instance_to_wrap: "LinearDampingConnectionProperties.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_damping(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialDamping

        if temp is None:
            return 0.0

        return temp

    @axial_damping.setter
    @enforce_parameter_types
    def axial_damping(self: Self, value: "float"):
        self.wrapped.AxialDamping = float(value) if value is not None else 0.0

    @property
    def radial_damping(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialDamping

        if temp is None:
            return 0.0

        return temp

    @radial_damping.setter
    @enforce_parameter_types
    def radial_damping(self: Self, value: "float"):
        self.wrapped.RadialDamping = float(value) if value is not None else 0.0

    @property
    def tilt_damping(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltDamping

        if temp is None:
            return 0.0

        return temp

    @tilt_damping.setter
    @enforce_parameter_types
    def tilt_damping(self: Self, value: "float"):
        self.wrapped.TiltDamping = float(value) if value is not None else 0.0

    @property
    def torsional_damping(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorsionalDamping

        if temp is None:
            return 0.0

        return temp

    @torsional_damping.setter
    @enforce_parameter_types
    def torsional_damping(self: Self, value: "float"):
        self.wrapped.TorsionalDamping = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "LinearDampingConnectionProperties._Cast_LinearDampingConnectionProperties":
        return self._Cast_LinearDampingConnectionProperties(self)
