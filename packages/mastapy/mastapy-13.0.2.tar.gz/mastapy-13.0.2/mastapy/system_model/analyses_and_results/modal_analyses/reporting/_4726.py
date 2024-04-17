"""ComponentPerModeResult"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_PER_MODE_RESULT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "ComponentPerModeResult",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4733


__docformat__ = "restructuredtext en"
__all__ = ("ComponentPerModeResult",)


Self = TypeVar("Self", bound="ComponentPerModeResult")


class ComponentPerModeResult(_0.APIBase):
    """ComponentPerModeResult

    This is a mastapy class.
    """

    TYPE = _COMPONENT_PER_MODE_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentPerModeResult")

    class _Cast_ComponentPerModeResult:
        """Special nested class for casting ComponentPerModeResult to subclasses."""

        def __init__(
            self: "ComponentPerModeResult._Cast_ComponentPerModeResult",
            parent: "ComponentPerModeResult",
        ):
            self._parent = parent

        @property
        def shaft_per_mode_result(
            self: "ComponentPerModeResult._Cast_ComponentPerModeResult",
        ) -> "_4733.ShaftPerModeResult":
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4733,
            )

            return self._parent._cast(_4733.ShaftPerModeResult)

        @property
        def component_per_mode_result(
            self: "ComponentPerModeResult._Cast_ComponentPerModeResult",
        ) -> "ComponentPerModeResult":
            return self._parent

        def __getattr__(
            self: "ComponentPerModeResult._Cast_ComponentPerModeResult", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentPerModeResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mode_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModeFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def mode_id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModeID

        if temp is None:
            return 0

        return temp

    @property
    def percentage_kinetic_energy(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PercentageKineticEnergy

        if temp is None:
            return 0.0

        return temp

    @percentage_kinetic_energy.setter
    @enforce_parameter_types
    def percentage_kinetic_energy(self: Self, value: "float"):
        self.wrapped.PercentageKineticEnergy = (
            float(value) if value is not None else 0.0
        )

    @property
    def percentage_strain_energy(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PercentageStrainEnergy

        if temp is None:
            return 0.0

        return temp

    @percentage_strain_energy.setter
    @enforce_parameter_types
    def percentage_strain_energy(self: Self, value: "float"):
        self.wrapped.PercentageStrainEnergy = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ComponentPerModeResult._Cast_ComponentPerModeResult":
        return self._Cast_ComponentPerModeResult(self)
