"""ThermalExpansionOrthotropicComponents"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THERMAL_EXPANSION_ORTHOTROPIC_COMPONENTS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ThermalExpansionOrthotropicComponents",
)


__docformat__ = "restructuredtext en"
__all__ = ("ThermalExpansionOrthotropicComponents",)


Self = TypeVar("Self", bound="ThermalExpansionOrthotropicComponents")


class ThermalExpansionOrthotropicComponents(_0.APIBase):
    """ThermalExpansionOrthotropicComponents

    This is a mastapy class.
    """

    TYPE = _THERMAL_EXPANSION_ORTHOTROPIC_COMPONENTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ThermalExpansionOrthotropicComponents"
    )

    class _Cast_ThermalExpansionOrthotropicComponents:
        """Special nested class for casting ThermalExpansionOrthotropicComponents to subclasses."""

        def __init__(
            self: "ThermalExpansionOrthotropicComponents._Cast_ThermalExpansionOrthotropicComponents",
            parent: "ThermalExpansionOrthotropicComponents",
        ):
            self._parent = parent

        @property
        def thermal_expansion_orthotropic_components(
            self: "ThermalExpansionOrthotropicComponents._Cast_ThermalExpansionOrthotropicComponents",
        ) -> "ThermalExpansionOrthotropicComponents":
            return self._parent

        def __getattr__(
            self: "ThermalExpansionOrthotropicComponents._Cast_ThermalExpansionOrthotropicComponents",
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
        self: Self, instance_to_wrap: "ThermalExpansionOrthotropicComponents.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    ) -> "ThermalExpansionOrthotropicComponents._Cast_ThermalExpansionOrthotropicComponents":
        return self._Cast_ThermalExpansionOrthotropicComponents(self)
