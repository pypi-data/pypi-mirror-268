"""StressCyclesDataForTheContactSNCurveOfAPlasticMaterial"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.materials import _239
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRESS_CYCLES_DATA_FOR_THE_CONTACT_SN_CURVE_OF_A_PLASTIC_MATERIAL = python_net_import(
    "SMT.MastaAPI.Materials", "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial"
)


__docformat__ = "restructuredtext en"
__all__ = ("StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",)


Self = TypeVar("Self", bound="StressCyclesDataForTheContactSNCurveOfAPlasticMaterial")


class StressCyclesDataForTheContactSNCurveOfAPlasticMaterial(
    _239.AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial
):
    """StressCyclesDataForTheContactSNCurveOfAPlasticMaterial

    This is a mastapy class.
    """

    TYPE = _STRESS_CYCLES_DATA_FOR_THE_CONTACT_SN_CURVE_OF_A_PLASTIC_MATERIAL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
    )

    class _Cast_StressCyclesDataForTheContactSNCurveOfAPlasticMaterial:
        """Special nested class for casting StressCyclesDataForTheContactSNCurveOfAPlasticMaterial to subclasses."""

        def __init__(
            self: "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
            parent: "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
        ):
            self._parent = parent

        @property
        def abstract_stress_cycles_data_for_an_sn_curve_of_a_plastic_material(
            self: "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
        ) -> "_239.AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial":
            return self._parent._cast(
                _239.AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial
            )

        @property
        def stress_cycles_data_for_the_contact_sn_curve_of_a_plastic_material(
            self: "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
        ) -> "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial":
            return self._parent

        def __getattr__(
            self: "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
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
        instance_to_wrap: "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_fatigue_strength_under_pulsating_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactFatigueStrengthUnderPulsatingStress

        if temp is None:
            return 0.0

        return temp

    @contact_fatigue_strength_under_pulsating_stress.setter
    @enforce_parameter_types
    def contact_fatigue_strength_under_pulsating_stress(self: Self, value: "float"):
        self.wrapped.ContactFatigueStrengthUnderPulsatingStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial._Cast_StressCyclesDataForTheContactSNCurveOfAPlasticMaterial":
        return self._Cast_StressCyclesDataForTheContactSNCurveOfAPlasticMaterial(self)
