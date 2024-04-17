"""LoadedTiltingPadJournalBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_results.fluid_film import _2128
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TILTING_PAD_JOURNAL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm",
    "LoadedTiltingPadJournalBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import _2126
    from mastapy.bearings.bearing_results import _1961, _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedTiltingPadJournalBearingResults",)


Self = TypeVar("Self", bound="LoadedTiltingPadJournalBearingResults")


class LoadedTiltingPadJournalBearingResults(_2128.LoadedPadFluidFilmBearingResults):
    """LoadedTiltingPadJournalBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_TILTING_PAD_JOURNAL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedTiltingPadJournalBearingResults"
    )

    class _Cast_LoadedTiltingPadJournalBearingResults:
        """Special nested class for casting LoadedTiltingPadJournalBearingResults to subclasses."""

        def __init__(
            self: "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults",
            parent: "LoadedTiltingPadJournalBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults",
        ) -> "_2128.LoadedPadFluidFilmBearingResults":
            return self._parent._cast(_2128.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults",
        ) -> "_2126.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2126

            return self._parent._cast(_2126.LoadedFluidFilmBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults",
        ) -> "_1961.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1961

            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults",
        ) -> "LoadedTiltingPadJournalBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults",
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
        self: Self, instance_to_wrap: "LoadedTiltingPadJournalBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_position_of_the_minimum_film_thickness_from_the_x_axis(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularPositionOfTheMinimumFilmThicknessFromTheXAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def critical_reynolds_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalReynoldsNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def eccentricity_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EccentricityRatio

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
    def exit_flow(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExitFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def force_in_direction_of_eccentricity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceInDirectionOfEccentricity

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_preload_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicPreloadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def inlet_flow(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InletFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_density(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_dynamic_viscosity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricantDynamicViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pad_eccentricity_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPadEccentricityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pressure_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPressureVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_friction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonDimensionalFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_maximum_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonDimensionalMaximumPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_minimum_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonDimensionalMinimumFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_out_flow(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonDimensionalOutFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_side_flow(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonDimensionalSideFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_shape_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadShapeFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeClearance

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
    def side_flow(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SideFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def sommerfeld_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SommerfeldNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedTiltingPadJournalBearingResults._Cast_LoadedTiltingPadJournalBearingResults":
        return self._Cast_LoadedTiltingPadJournalBearingResults(self)
