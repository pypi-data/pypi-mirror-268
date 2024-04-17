"""LoadedRollerBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2040
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollerBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _1996,
        _2001,
        _2004,
        _2012,
        _2016,
        _2028,
        _2031,
        _2047,
        _2050,
        _2055,
        _2064,
    )
    from mastapy.bearings.bearing_results import _1961, _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedRollerBearingResults")


class LoadedRollerBearingResults(_2040.LoadedRollingBearingResults):
    """LoadedRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollerBearingResults")

    class _Cast_LoadedRollerBearingResults:
        """Special nested class for casting LoadedRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
            parent: "LoadedRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2040.LoadedRollingBearingResults":
            return self._parent._cast(_2040.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1961.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1961

            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_1996.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1996

            return self._parent._cast(
                _1996.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2001.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2001

            return self._parent._cast(
                _2001.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2004.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(_2004.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2012.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(_2012.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2016.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2016

            return self._parent._cast(_2016.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2028.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2031.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2031

            return self._parent._cast(_2031.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2047.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2047

            return self._parent._cast(_2047.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2050.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2050

            return self._parent._cast(_2050.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2055.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2055

            return self._parent._cast(_2055.LoadedTaperRollerBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "_2064.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2064

            return self._parent._cast(_2064.LoadedToroidalRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
        ) -> "LoadedRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollerBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_angular_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def element_centrifugal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementCentrifugalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def element_surface_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementSurfaceVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactWidthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactWidthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollerBearingResults._Cast_LoadedRollerBearingResults":
        return self._Cast_LoadedRollerBearingResults(self)
