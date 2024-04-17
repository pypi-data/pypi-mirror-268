"""GenericStressConcentrationFactor"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.shafts import _21
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GENERIC_STRESS_CONCENTRATION_FACTOR = python_net_import(
    "SMT.MastaAPI.Shafts", "GenericStressConcentrationFactor"
)


__docformat__ = "restructuredtext en"
__all__ = ("GenericStressConcentrationFactor",)


Self = TypeVar("Self", bound="GenericStressConcentrationFactor")


class GenericStressConcentrationFactor(_21.ShaftFeature):
    """GenericStressConcentrationFactor

    This is a mastapy class.
    """

    TYPE = _GENERIC_STRESS_CONCENTRATION_FACTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GenericStressConcentrationFactor")

    class _Cast_GenericStressConcentrationFactor:
        """Special nested class for casting GenericStressConcentrationFactor to subclasses."""

        def __init__(
            self: "GenericStressConcentrationFactor._Cast_GenericStressConcentrationFactor",
            parent: "GenericStressConcentrationFactor",
        ):
            self._parent = parent

        @property
        def shaft_feature(
            self: "GenericStressConcentrationFactor._Cast_GenericStressConcentrationFactor",
        ) -> "_21.ShaftFeature":
            return self._parent._cast(_21.ShaftFeature)

        @property
        def generic_stress_concentration_factor(
            self: "GenericStressConcentrationFactor._Cast_GenericStressConcentrationFactor",
        ) -> "GenericStressConcentrationFactor":
            return self._parent

        def __getattr__(
            self: "GenericStressConcentrationFactor._Cast_GenericStressConcentrationFactor",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GenericStressConcentrationFactor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BendingFactor

        if temp is None:
            return 0.0

        return temp

    @bending_factor.setter
    @enforce_parameter_types
    def bending_factor(self: Self, value: "float"):
        self.wrapped.BendingFactor = float(value) if value is not None else 0.0

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def tension_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TensionFactor

        if temp is None:
            return 0.0

        return temp

    @tension_factor.setter
    @enforce_parameter_types
    def tension_factor(self: Self, value: "float"):
        self.wrapped.TensionFactor = float(value) if value is not None else 0.0

    @property
    def torsion_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorsionFactor

        if temp is None:
            return 0.0

        return temp

    @torsion_factor.setter
    @enforce_parameter_types
    def torsion_factor(self: Self, value: "float"):
        self.wrapped.TorsionFactor = float(value) if value is not None else 0.0

    def add_new_generic_scf(self: Self):
        """Method does not return."""
        self.wrapped.AddNewGenericSCF()

    @property
    def cast_to(
        self: Self,
    ) -> "GenericStressConcentrationFactor._Cast_GenericStressConcentrationFactor":
        return self._Cast_GenericStressConcentrationFactor(self)
