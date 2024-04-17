"""LoadedTiltingThrustPad"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_results.fluid_film import _2125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TILTING_THRUST_PAD = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm", "LoadedTiltingThrustPad"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedTiltingThrustPad",)


Self = TypeVar("Self", bound="LoadedTiltingThrustPad")


class LoadedTiltingThrustPad(_2125.LoadedFluidFilmBearingPad):
    """LoadedTiltingThrustPad

    This is a mastapy class.
    """

    TYPE = _LOADED_TILTING_THRUST_PAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedTiltingThrustPad")

    class _Cast_LoadedTiltingThrustPad:
        """Special nested class for casting LoadedTiltingThrustPad to subclasses."""

        def __init__(
            self: "LoadedTiltingThrustPad._Cast_LoadedTiltingThrustPad",
            parent: "LoadedTiltingThrustPad",
        ):
            self._parent = parent

        @property
        def loaded_fluid_film_bearing_pad(
            self: "LoadedTiltingThrustPad._Cast_LoadedTiltingThrustPad",
        ) -> "_2125.LoadedFluidFilmBearingPad":
            return self._parent._cast(_2125.LoadedFluidFilmBearingPad)

        @property
        def loaded_tilting_thrust_pad(
            self: "LoadedTiltingThrustPad._Cast_LoadedTiltingThrustPad",
        ) -> "LoadedTiltingThrustPad":
            return self._parent

        def __getattr__(
            self: "LoadedTiltingThrustPad._Cast_LoadedTiltingThrustPad", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedTiltingThrustPad.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_film_kinematic_viscosity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveFilmKinematicViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_film_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EffectiveFilmTemperature

        if temp is None:
            return 0.0

        return temp

    @effective_film_temperature.setter
    @enforce_parameter_types
    def effective_film_temperature(self: Self, value: "float"):
        self.wrapped.EffectiveFilmTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def film_thickness_minimum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilmThicknessMinimum

        if temp is None:
            return 0.0

        return temp

    @property
    def film_thickness_at_pivot(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilmThicknessAtPivot

        if temp is None:
            return 0.0

        return temp

    @property
    def force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Force

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_flow_at_leading_edge(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFlowAtLeadingEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_flow_at_trailing_edge(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantFlowAtTrailingEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_side_flow(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantSideFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_temperature_at_leading_edge(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantTemperatureAtLeadingEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_temperature_at_trailing_edge(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantTemperatureAtTrailingEdge

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def reynolds_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReynoldsNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Tilt

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "LoadedTiltingThrustPad._Cast_LoadedTiltingThrustPad":
        return self._Cast_LoadedTiltingThrustPad(self)
