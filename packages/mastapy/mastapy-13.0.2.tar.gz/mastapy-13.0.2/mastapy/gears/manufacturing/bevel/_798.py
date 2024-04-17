"""EaseOffBasedTCA"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.bevel import _775
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EASE_OFF_BASED_TCA = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "EaseOffBasedTCA"
)


__docformat__ = "restructuredtext en"
__all__ = ("EaseOffBasedTCA",)


Self = TypeVar("Self", bound="EaseOffBasedTCA")


class EaseOffBasedTCA(_775.AbstractTCA):
    """EaseOffBasedTCA

    This is a mastapy class.
    """

    TYPE = _EASE_OFF_BASED_TCA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EaseOffBasedTCA")

    class _Cast_EaseOffBasedTCA:
        """Special nested class for casting EaseOffBasedTCA to subclasses."""

        def __init__(
            self: "EaseOffBasedTCA._Cast_EaseOffBasedTCA", parent: "EaseOffBasedTCA"
        ):
            self._parent = parent

        @property
        def abstract_tca(
            self: "EaseOffBasedTCA._Cast_EaseOffBasedTCA",
        ) -> "_775.AbstractTCA":
            return self._parent._cast(_775.AbstractTCA)

        @property
        def ease_off_based_tca(
            self: "EaseOffBasedTCA._Cast_EaseOffBasedTCA",
        ) -> "EaseOffBasedTCA":
            return self._parent

        def __getattr__(self: "EaseOffBasedTCA._Cast_EaseOffBasedTCA", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EaseOffBasedTCA.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_ease_off_optimisation_wheel_u(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CurrentEaseOffOptimisationWheelU

        if temp is None:
            return 0.0

        return temp

    @current_ease_off_optimisation_wheel_u.setter
    @enforce_parameter_types
    def current_ease_off_optimisation_wheel_u(self: Self, value: "float"):
        self.wrapped.CurrentEaseOffOptimisationWheelU = (
            float(value) if value is not None else 0.0
        )

    @property
    def current_ease_off_optimisation_wheel_v(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CurrentEaseOffOptimisationWheelV

        if temp is None:
            return 0.0

        return temp

    @current_ease_off_optimisation_wheel_v.setter
    @enforce_parameter_types
    def current_ease_off_optimisation_wheel_v(self: Self, value: "float"):
        self.wrapped.CurrentEaseOffOptimisationWheelV = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "EaseOffBasedTCA._Cast_EaseOffBasedTCA":
        return self._Cast_EaseOffBasedTCA(self)
