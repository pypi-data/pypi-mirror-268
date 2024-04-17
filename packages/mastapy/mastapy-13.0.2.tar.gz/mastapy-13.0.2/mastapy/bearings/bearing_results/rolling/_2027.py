"""LoadedNeedleRollerBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_results.rolling import _2015
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NEEDLE_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedNeedleRollerBearingElement"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2034, _2035, _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNeedleRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedNeedleRollerBearingElement")


class LoadedNeedleRollerBearingElement(_2015.LoadedCylindricalRollerBearingElement):
    """LoadedNeedleRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_NEEDLE_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNeedleRollerBearingElement")

    class _Cast_LoadedNeedleRollerBearingElement:
        """Special nested class for casting LoadedNeedleRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedNeedleRollerBearingElement._Cast_LoadedNeedleRollerBearingElement",
            parent: "LoadedNeedleRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_cylindrical_roller_bearing_element(
            self: "LoadedNeedleRollerBearingElement._Cast_LoadedNeedleRollerBearingElement",
        ) -> "_2015.LoadedCylindricalRollerBearingElement":
            return self._parent._cast(_2015.LoadedCylindricalRollerBearingElement)

        @property
        def loaded_non_barrel_roller_element(
            self: "LoadedNeedleRollerBearingElement._Cast_LoadedNeedleRollerBearingElement",
        ) -> "_2034.LoadedNonBarrelRollerElement":
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedNonBarrelRollerElement)

        @property
        def loaded_roller_bearing_element(
            self: "LoadedNeedleRollerBearingElement._Cast_LoadedNeedleRollerBearingElement",
        ) -> "_2035.LoadedRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedNeedleRollerBearingElement._Cast_LoadedNeedleRollerBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_needle_roller_bearing_element(
            self: "LoadedNeedleRollerBearingElement._Cast_LoadedNeedleRollerBearingElement",
        ) -> "LoadedNeedleRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedNeedleRollerBearingElement._Cast_LoadedNeedleRollerBearingElement",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedNeedleRollerBearingElement.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def sliding_power_loss_from_hysteresis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidingPowerLossFromHysteresis

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_from_hysteresis.setter
    @enforce_parameter_types
    def sliding_power_loss_from_hysteresis(self: Self, value: "float"):
        self.wrapped.SlidingPowerLossFromHysteresis = (
            float(value) if value is not None else 0.0
        )

    @property
    def sliding_power_loss_from_macro_sliding_due_to_roller_skew(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidingPowerLossFromMacroSlidingDueToRollerSkew

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_from_macro_sliding_due_to_roller_skew.setter
    @enforce_parameter_types
    def sliding_power_loss_from_macro_sliding_due_to_roller_skew(
        self: Self, value: "float"
    ):
        self.wrapped.SlidingPowerLossFromMacroSlidingDueToRollerSkew = (
            float(value) if value is not None else 0.0
        )

    @property
    def sliding_power_loss_roller_cage_axial_component(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidingPowerLossRollerCageAxialComponent

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_roller_cage_axial_component.setter
    @enforce_parameter_types
    def sliding_power_loss_roller_cage_axial_component(self: Self, value: "float"):
        self.wrapped.SlidingPowerLossRollerCageAxialComponent = (
            float(value) if value is not None else 0.0
        )

    @property
    def sliding_power_loss_roller_cage_moment_component(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidingPowerLossRollerCageMomentComponent

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_roller_cage_moment_component.setter
    @enforce_parameter_types
    def sliding_power_loss_roller_cage_moment_component(self: Self, value: "float"):
        self.wrapped.SlidingPowerLossRollerCageMomentComponent = (
            float(value) if value is not None else 0.0
        )

    @property
    def sliding_power_loss_roller_cage_radial_component(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidingPowerLossRollerCageRadialComponent

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_roller_cage_radial_component.setter
    @enforce_parameter_types
    def sliding_power_loss_roller_cage_radial_component(self: Self, value: "float"):
        self.wrapped.SlidingPowerLossRollerCageRadialComponent = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNeedleRollerBearingElement._Cast_LoadedNeedleRollerBearingElement":
        return self._Cast_LoadedNeedleRollerBearingElement(self)
