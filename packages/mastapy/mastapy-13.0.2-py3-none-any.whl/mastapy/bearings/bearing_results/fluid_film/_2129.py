"""LoadedPlainJournalBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.bearings.bearing_results.fluid_film import _2126
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_PLAIN_JOURNAL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm", "LoadedPlainJournalBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import _2130, _2127, _2131
    from mastapy.bearings.bearing_results import _1961, _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedPlainJournalBearingResults",)


Self = TypeVar("Self", bound="LoadedPlainJournalBearingResults")


class LoadedPlainJournalBearingResults(_2126.LoadedFluidFilmBearingResults):
    """LoadedPlainJournalBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_PLAIN_JOURNAL_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedPlainJournalBearingResults")

    class _Cast_LoadedPlainJournalBearingResults:
        """Special nested class for casting LoadedPlainJournalBearingResults to subclasses."""

        def __init__(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
            parent: "LoadedPlainJournalBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
        ) -> "_2126.LoadedFluidFilmBearingResults":
            return self._parent._cast(_2126.LoadedFluidFilmBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
        ) -> "_1961.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1961

            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
        ) -> "_2127.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2127

            return self._parent._cast(_2127.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
        ) -> "_2131.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2131

            return self._parent._cast(_2131.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
        ) -> "LoadedPlainJournalBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedPlainJournalBearingResults.TYPE"):
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
    def attitude_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AttitudeAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def attitude_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AttitudeForce

        if temp is None:
            return 0.0

        return temp

    @property
    def diametrical_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiametricalClearance

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
    def kinematic_viscosity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KinematicViscosity

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
    def minimum_central_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumCentralFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonDimensionalLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonDimensionalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OperatingTemperature

        if temp is None:
            return 0.0

        return temp

    @operating_temperature.setter
    @enforce_parameter_types
    def operating_temperature(self: Self, value: "float"):
        self.wrapped.OperatingTemperature = float(value) if value is not None else 0.0

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
    def radial_load_per_unit_of_projected_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialLoadPerUnitOfProjectedArea

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_relative_rotation_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftRelativeRotationSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def journal_bearing_rows(self: Self) -> "List[_2130.LoadedPlainJournalBearingRow]":
        """List[mastapy.bearings.bearing_results.fluid_film.LoadedPlainJournalBearingRow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.JournalBearingRows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults":
        return self._Cast_LoadedPlainJournalBearingResults(self)
