"""SpecificationForTheEffectOfOilKinematicViscosity"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIFICATION_FOR_THE_EFFECT_OF_OIL_KINEMATIC_VISCOSITY = python_net_import(
    "SMT.MastaAPI.Gears", "SpecificationForTheEffectOfOilKinematicViscosity"
)


__docformat__ = "restructuredtext en"
__all__ = ("SpecificationForTheEffectOfOilKinematicViscosity",)


Self = TypeVar("Self", bound="SpecificationForTheEffectOfOilKinematicViscosity")


class SpecificationForTheEffectOfOilKinematicViscosity(
    _1593.IndependentReportablePropertiesBase[
        "SpecificationForTheEffectOfOilKinematicViscosity"
    ]
):
    """SpecificationForTheEffectOfOilKinematicViscosity

    This is a mastapy class.
    """

    TYPE = _SPECIFICATION_FOR_THE_EFFECT_OF_OIL_KINEMATIC_VISCOSITY
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecificationForTheEffectOfOilKinematicViscosity"
    )

    class _Cast_SpecificationForTheEffectOfOilKinematicViscosity:
        """Special nested class for casting SpecificationForTheEffectOfOilKinematicViscosity to subclasses."""

        def __init__(
            self: "SpecificationForTheEffectOfOilKinematicViscosity._Cast_SpecificationForTheEffectOfOilKinematicViscosity",
            parent: "SpecificationForTheEffectOfOilKinematicViscosity",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "SpecificationForTheEffectOfOilKinematicViscosity._Cast_SpecificationForTheEffectOfOilKinematicViscosity",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def specification_for_the_effect_of_oil_kinematic_viscosity(
            self: "SpecificationForTheEffectOfOilKinematicViscosity._Cast_SpecificationForTheEffectOfOilKinematicViscosity",
        ) -> "SpecificationForTheEffectOfOilKinematicViscosity":
            return self._parent

        def __getattr__(
            self: "SpecificationForTheEffectOfOilKinematicViscosity._Cast_SpecificationForTheEffectOfOilKinematicViscosity",
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
        instance_to_wrap: "SpecificationForTheEffectOfOilKinematicViscosity.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def condition(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Condition

        if temp is None:
            return ""

        return temp

    @property
    def intercept_of_linear_equation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InterceptOfLinearEquation

        if temp is None:
            return 0.0

        return temp

    @intercept_of_linear_equation.setter
    @enforce_parameter_types
    def intercept_of_linear_equation(self: Self, value: "float"):
        self.wrapped.InterceptOfLinearEquation = (
            float(value) if value is not None else 0.0
        )

    @property
    def slope_of_linear_equation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlopeOfLinearEquation

        if temp is None:
            return 0.0

        return temp

    @slope_of_linear_equation.setter
    @enforce_parameter_types
    def slope_of_linear_equation(self: Self, value: "float"):
        self.wrapped.SlopeOfLinearEquation = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "SpecificationForTheEffectOfOilKinematicViscosity._Cast_SpecificationForTheEffectOfOilKinematicViscosity":
        return self._Cast_SpecificationForTheEffectOfOilKinematicViscosity(self)
