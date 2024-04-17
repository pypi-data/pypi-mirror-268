"""ElasticModulusOrthotropicComponents"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELASTIC_MODULUS_ORTHOTROPIC_COMPONENTS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElasticModulusOrthotropicComponents",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElasticModulusOrthotropicComponents",)


Self = TypeVar("Self", bound="ElasticModulusOrthotropicComponents")


class ElasticModulusOrthotropicComponents(_0.APIBase):
    """ElasticModulusOrthotropicComponents

    This is a mastapy class.
    """

    TYPE = _ELASTIC_MODULUS_ORTHOTROPIC_COMPONENTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElasticModulusOrthotropicComponents")

    class _Cast_ElasticModulusOrthotropicComponents:
        """Special nested class for casting ElasticModulusOrthotropicComponents to subclasses."""

        def __init__(
            self: "ElasticModulusOrthotropicComponents._Cast_ElasticModulusOrthotropicComponents",
            parent: "ElasticModulusOrthotropicComponents",
        ):
            self._parent = parent

        @property
        def elastic_modulus_orthotropic_components(
            self: "ElasticModulusOrthotropicComponents._Cast_ElasticModulusOrthotropicComponents",
        ) -> "ElasticModulusOrthotropicComponents":
            return self._parent

        def __getattr__(
            self: "ElasticModulusOrthotropicComponents._Cast_ElasticModulusOrthotropicComponents",
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
        self: Self, instance_to_wrap: "ElasticModulusOrthotropicComponents.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EX

        if temp is None:
            return 0.0

        return temp

    @ex.setter
    @enforce_parameter_types
    def ex(self: Self, value: "float"):
        self.wrapped.EX = float(value) if value is not None else 0.0

    @property
    def ey(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EY

        if temp is None:
            return 0.0

        return temp

    @ey.setter
    @enforce_parameter_types
    def ey(self: Self, value: "float"):
        self.wrapped.EY = float(value) if value is not None else 0.0

    @property
    def ez(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EZ

        if temp is None:
            return 0.0

        return temp

    @ez.setter
    @enforce_parameter_types
    def ez(self: Self, value: "float"):
        self.wrapped.EZ = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ElasticModulusOrthotropicComponents._Cast_ElasticModulusOrthotropicComponents"
    ):
        return self._Cast_ElasticModulusOrthotropicComponents(self)
