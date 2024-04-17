"""LoadedRollerStripLoadResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_STRIP_LOAD_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollerStripLoadResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _1988,
        _1998,
        _2033,
        _2049,
        _2066,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerStripLoadResults",)


Self = TypeVar("Self", bound="LoadedRollerStripLoadResults")


class LoadedRollerStripLoadResults(_0.APIBase):
    """LoadedRollerStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_STRIP_LOAD_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollerStripLoadResults")

    class _Cast_LoadedRollerStripLoadResults:
        """Special nested class for casting LoadedRollerStripLoadResults to subclasses."""

        def __init__(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
            parent: "LoadedRollerStripLoadResults",
        ):
            self._parent = parent

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_1988.LoadedAbstractSphericalRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _1988

            return self._parent._cast(
                _1988.LoadedAbstractSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_1998.LoadedAsymmetricSphericalRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _1998

            return self._parent._cast(
                _1998.LoadedAsymmetricSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_non_barrel_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_2033.LoadedNonBarrelRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(
                _2033.LoadedNonBarrelRollerBearingStripLoadResults
            )

        @property
        def loaded_spherical_roller_radial_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_2049.LoadedSphericalRollerRadialBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2049

            return self._parent._cast(
                _2049.LoadedSphericalRollerRadialBearingStripLoadResults
            )

        @property
        def loaded_toroidal_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_2066.LoadedToroidalRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2066

            return self._parent._cast(_2066.LoadedToroidalRollerBearingStripLoadResults)

        @property
        def loaded_roller_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "LoadedRollerStripLoadResults":
            return self._parent

        def __getattr__(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollerStripLoadResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults":
        return self._Cast_LoadedRollerStripLoadResults(self)
