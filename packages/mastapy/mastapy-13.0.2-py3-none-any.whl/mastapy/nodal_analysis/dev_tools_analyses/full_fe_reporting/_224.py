"""ShearModulusOrthotropicComponents"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHEAR_MODULUS_ORTHOTROPIC_COMPONENTS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ShearModulusOrthotropicComponents",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShearModulusOrthotropicComponents",)


Self = TypeVar("Self", bound="ShearModulusOrthotropicComponents")


class ShearModulusOrthotropicComponents(_0.APIBase):
    """ShearModulusOrthotropicComponents

    This is a mastapy class.
    """

    TYPE = _SHEAR_MODULUS_ORTHOTROPIC_COMPONENTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShearModulusOrthotropicComponents")

    class _Cast_ShearModulusOrthotropicComponents:
        """Special nested class for casting ShearModulusOrthotropicComponents to subclasses."""

        def __init__(
            self: "ShearModulusOrthotropicComponents._Cast_ShearModulusOrthotropicComponents",
            parent: "ShearModulusOrthotropicComponents",
        ):
            self._parent = parent

        @property
        def shear_modulus_orthotropic_components(
            self: "ShearModulusOrthotropicComponents._Cast_ShearModulusOrthotropicComponents",
        ) -> "ShearModulusOrthotropicComponents":
            return self._parent

        def __getattr__(
            self: "ShearModulusOrthotropicComponents._Cast_ShearModulusOrthotropicComponents",
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
        self: Self, instance_to_wrap: "ShearModulusOrthotropicComponents.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gxy(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GXY

        if temp is None:
            return 0.0

        return temp

    @gxy.setter
    @enforce_parameter_types
    def gxy(self: Self, value: "float"):
        self.wrapped.GXY = float(value) if value is not None else 0.0

    @property
    def gxz(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GXZ

        if temp is None:
            return 0.0

        return temp

    @gxz.setter
    @enforce_parameter_types
    def gxz(self: Self, value: "float"):
        self.wrapped.GXZ = float(value) if value is not None else 0.0

    @property
    def gyz(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GYZ

        if temp is None:
            return 0.0

        return temp

    @gyz.setter
    @enforce_parameter_types
    def gyz(self: Self, value: "float"):
        self.wrapped.GYZ = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "ShearModulusOrthotropicComponents._Cast_ShearModulusOrthotropicComponents":
        return self._Cast_ShearModulusOrthotropicComponents(self)
