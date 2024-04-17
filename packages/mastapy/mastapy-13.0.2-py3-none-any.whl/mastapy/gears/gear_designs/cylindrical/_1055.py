"""HardenedMaterialProperties"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARDENED_MATERIAL_PROPERTIES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "HardenedMaterialProperties"
)


__docformat__ = "restructuredtext en"
__all__ = ("HardenedMaterialProperties",)


Self = TypeVar("Self", bound="HardenedMaterialProperties")


class HardenedMaterialProperties(
    _1593.IndependentReportablePropertiesBase["HardenedMaterialProperties"]
):
    """HardenedMaterialProperties

    This is a mastapy class.
    """

    TYPE = _HARDENED_MATERIAL_PROPERTIES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HardenedMaterialProperties")

    class _Cast_HardenedMaterialProperties:
        """Special nested class for casting HardenedMaterialProperties to subclasses."""

        def __init__(
            self: "HardenedMaterialProperties._Cast_HardenedMaterialProperties",
            parent: "HardenedMaterialProperties",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "HardenedMaterialProperties._Cast_HardenedMaterialProperties",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def hardened_material_properties(
            self: "HardenedMaterialProperties._Cast_HardenedMaterialProperties",
        ) -> "HardenedMaterialProperties":
            return self._parent

        def __getattr__(
            self: "HardenedMaterialProperties._Cast_HardenedMaterialProperties",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HardenedMaterialProperties.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def critical_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CriticalStress

        if temp is None:
            return 0.0

        return temp

    @critical_stress.setter
    @enforce_parameter_types
    def critical_stress(self: Self, value: "float"):
        self.wrapped.CriticalStress = float(value) if value is not None else 0.0

    @property
    def fatigue_sensitivity_to_normal_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FatigueSensitivityToNormalStress

        if temp is None:
            return 0.0

        return temp

    @fatigue_sensitivity_to_normal_stress.setter
    @enforce_parameter_types
    def fatigue_sensitivity_to_normal_stress(self: Self, value: "float"):
        self.wrapped.FatigueSensitivityToNormalStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "HardenedMaterialProperties._Cast_HardenedMaterialProperties":
        return self._Cast_HardenedMaterialProperties(self)
