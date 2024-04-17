"""LoadedTiltingPadThrustBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_results.fluid_film import _2128
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TILTING_PAD_THRUST_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm",
    "LoadedTiltingPadThrustBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import _2126
    from mastapy.bearings.bearing_results import _1961, _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedTiltingPadThrustBearingResults",)


Self = TypeVar("Self", bound="LoadedTiltingPadThrustBearingResults")


class LoadedTiltingPadThrustBearingResults(_2128.LoadedPadFluidFilmBearingResults):
    """LoadedTiltingPadThrustBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_TILTING_PAD_THRUST_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedTiltingPadThrustBearingResults")

    class _Cast_LoadedTiltingPadThrustBearingResults:
        """Special nested class for casting LoadedTiltingPadThrustBearingResults to subclasses."""

        def __init__(
            self: "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults",
            parent: "LoadedTiltingPadThrustBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults",
        ) -> "_2128.LoadedPadFluidFilmBearingResults":
            return self._parent._cast(_2128.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults",
        ) -> "_2126.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2126

            return self._parent._cast(_2126.LoadedFluidFilmBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults",
        ) -> "_1961.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1961

            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults",
        ) -> "LoadedTiltingPadThrustBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults",
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
        self: Self, instance_to_wrap: "LoadedTiltingPadThrustBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_pad_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragePadLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_internal_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @axial_internal_clearance.setter
    @enforce_parameter_types
    def axial_internal_clearance(self: Self, value: "float"):
        self.wrapped.AxialInternalClearance = float(value) if value is not None else 0.0

    @property
    def maximum_bearing_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumBearingTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pad_film_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPadFilmTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pad_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPadLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pad_specific_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPadSpecificLoad

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
    def maximum_reynolds_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumReynoldsNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_reynolds_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanReynoldsNumber

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
    def minimum_flow_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFlowRate

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_exit_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilExitTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedTiltingPadThrustBearingResults._Cast_LoadedTiltingPadThrustBearingResults":
        return self._Cast_LoadedTiltingPadThrustBearingResults(self)
