"""StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.materials import _239
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRESS_CYCLES_DATA_FOR_THE_BENDING_SN_CURVE_OF_A_PLASTIC_MATERIAL = python_net_import(
    "SMT.MastaAPI.Materials", "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial"
)


__docformat__ = "restructuredtext en"
__all__ = ("StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",)


Self = TypeVar("Self", bound="StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial")


class StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial(
    _239.AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial
):
    """StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial

    This is a mastapy class.
    """

    TYPE = _STRESS_CYCLES_DATA_FOR_THE_BENDING_SN_CURVE_OF_A_PLASTIC_MATERIAL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
    )

    class _Cast_StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial:
        """Special nested class for casting StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial to subclasses."""

        def __init__(
            self: "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
            parent: "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
        ):
            self._parent = parent

        @property
        def abstract_stress_cycles_data_for_an_sn_curve_of_a_plastic_material(
            self: "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
        ) -> "_239.AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial":
            return self._parent._cast(
                _239.AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial
            )

        @property
        def stress_cycles_data_for_the_bending_sn_curve_of_a_plastic_material(
            self: "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
        ) -> "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial":
            return self._parent

        def __getattr__(
            self: "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
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
        self: Self,
        instance_to_wrap: "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_fatigue_strength_under_pulsating_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BendingFatigueStrengthUnderPulsatingStress

        if temp is None:
            return 0.0

        return temp

    @bending_fatigue_strength_under_pulsating_stress.setter
    @enforce_parameter_types
    def bending_fatigue_strength_under_pulsating_stress(self: Self, value: "float"):
        self.wrapped.BendingFatigueStrengthUnderPulsatingStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial":
        return self._Cast_StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial(self)
