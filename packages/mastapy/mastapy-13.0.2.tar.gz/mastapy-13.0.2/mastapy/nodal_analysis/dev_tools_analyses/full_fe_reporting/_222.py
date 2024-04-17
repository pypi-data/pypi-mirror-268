"""PoissonRatioOrthotropicComponents"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POISSON_RATIO_ORTHOTROPIC_COMPONENTS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "PoissonRatioOrthotropicComponents",
)


__docformat__ = "restructuredtext en"
__all__ = ("PoissonRatioOrthotropicComponents",)


Self = TypeVar("Self", bound="PoissonRatioOrthotropicComponents")


class PoissonRatioOrthotropicComponents(_0.APIBase):
    """PoissonRatioOrthotropicComponents

    This is a mastapy class.
    """

    TYPE = _POISSON_RATIO_ORTHOTROPIC_COMPONENTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PoissonRatioOrthotropicComponents")

    class _Cast_PoissonRatioOrthotropicComponents:
        """Special nested class for casting PoissonRatioOrthotropicComponents to subclasses."""

        def __init__(
            self: "PoissonRatioOrthotropicComponents._Cast_PoissonRatioOrthotropicComponents",
            parent: "PoissonRatioOrthotropicComponents",
        ):
            self._parent = parent

        @property
        def poisson_ratio_orthotropic_components(
            self: "PoissonRatioOrthotropicComponents._Cast_PoissonRatioOrthotropicComponents",
        ) -> "PoissonRatioOrthotropicComponents":
            return self._parent

        def __getattr__(
            self: "PoissonRatioOrthotropicComponents._Cast_PoissonRatioOrthotropicComponents",
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
        self: Self, instance_to_wrap: "PoissonRatioOrthotropicComponents.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def nu_xy(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NuXY

        if temp is None:
            return 0.0

        return temp

    @nu_xy.setter
    @enforce_parameter_types
    def nu_xy(self: Self, value: "float"):
        self.wrapped.NuXY = float(value) if value is not None else 0.0

    @property
    def nu_xz(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NuXZ

        if temp is None:
            return 0.0

        return temp

    @nu_xz.setter
    @enforce_parameter_types
    def nu_xz(self: Self, value: "float"):
        self.wrapped.NuXZ = float(value) if value is not None else 0.0

    @property
    def nu_yz(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NuYZ

        if temp is None:
            return 0.0

        return temp

    @nu_yz.setter
    @enforce_parameter_types
    def nu_yz(self: Self, value: "float"):
        self.wrapped.NuYZ = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "PoissonRatioOrthotropicComponents._Cast_PoissonRatioOrthotropicComponents":
        return self._Cast_PoissonRatioOrthotropicComponents(self)
