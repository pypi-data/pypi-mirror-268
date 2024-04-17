"""LinearStiffnessProperties"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis import _46
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_STIFFNESS_PROPERTIES = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "LinearStiffnessProperties"
)


__docformat__ = "restructuredtext en"
__all__ = ("LinearStiffnessProperties",)


Self = TypeVar("Self", bound="LinearStiffnessProperties")


class LinearStiffnessProperties(_46.AbstractLinearConnectionProperties):
    """LinearStiffnessProperties

    This is a mastapy class.
    """

    TYPE = _LINEAR_STIFFNESS_PROPERTIES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearStiffnessProperties")

    class _Cast_LinearStiffnessProperties:
        """Special nested class for casting LinearStiffnessProperties to subclasses."""

        def __init__(
            self: "LinearStiffnessProperties._Cast_LinearStiffnessProperties",
            parent: "LinearStiffnessProperties",
        ):
            self._parent = parent

        @property
        def abstract_linear_connection_properties(
            self: "LinearStiffnessProperties._Cast_LinearStiffnessProperties",
        ) -> "_46.AbstractLinearConnectionProperties":
            return self._parent._cast(_46.AbstractLinearConnectionProperties)

        @property
        def linear_stiffness_properties(
            self: "LinearStiffnessProperties._Cast_LinearStiffnessProperties",
        ) -> "LinearStiffnessProperties":
            return self._parent

        def __getattr__(
            self: "LinearStiffnessProperties._Cast_LinearStiffnessProperties", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LinearStiffnessProperties.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness.setter
    @enforce_parameter_types
    def axial_stiffness(self: Self, value: "float"):
        self.wrapped.AxialStiffness = float(value) if value is not None else 0.0

    @property
    def radial_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialStiffness

        if temp is None:
            return 0.0

        return temp

    @radial_stiffness.setter
    @enforce_parameter_types
    def radial_stiffness(self: Self, value: "float"):
        self.wrapped.RadialStiffness = float(value) if value is not None else 0.0

    @property
    def tilt_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @tilt_stiffness.setter
    @enforce_parameter_types
    def tilt_stiffness(self: Self, value: "float"):
        self.wrapped.TiltStiffness = float(value) if value is not None else 0.0

    @property
    def torsional_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return temp

    @torsional_stiffness.setter
    @enforce_parameter_types
    def torsional_stiffness(self: Self, value: "float"):
        self.wrapped.TorsionalStiffness = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "LinearStiffnessProperties._Cast_LinearStiffnessProperties":
        return self._Cast_LinearStiffnessProperties(self)
