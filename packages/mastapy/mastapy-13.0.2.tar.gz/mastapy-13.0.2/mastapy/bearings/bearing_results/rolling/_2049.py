"""LoadedSphericalRollerRadialBearingStripLoadResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _1988
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_STRIP_LOAD_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalRollerRadialBearingStripLoadResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2066, _2038


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalRollerRadialBearingStripLoadResults",)


Self = TypeVar("Self", bound="LoadedSphericalRollerRadialBearingStripLoadResults")


class LoadedSphericalRollerRadialBearingStripLoadResults(
    _1988.LoadedAbstractSphericalRollerBearingStripLoadResults
):
    """LoadedSphericalRollerRadialBearingStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_STRIP_LOAD_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedSphericalRollerRadialBearingStripLoadResults"
    )

    class _Cast_LoadedSphericalRollerRadialBearingStripLoadResults:
        """Special nested class for casting LoadedSphericalRollerRadialBearingStripLoadResults to subclasses."""

        def __init__(
            self: "LoadedSphericalRollerRadialBearingStripLoadResults._Cast_LoadedSphericalRollerRadialBearingStripLoadResults",
            parent: "LoadedSphericalRollerRadialBearingStripLoadResults",
        ):
            self._parent = parent

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(
            self: "LoadedSphericalRollerRadialBearingStripLoadResults._Cast_LoadedSphericalRollerRadialBearingStripLoadResults",
        ) -> "_1988.LoadedAbstractSphericalRollerBearingStripLoadResults":
            return self._parent._cast(
                _1988.LoadedAbstractSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_roller_strip_load_results(
            self: "LoadedSphericalRollerRadialBearingStripLoadResults._Cast_LoadedSphericalRollerRadialBearingStripLoadResults",
        ) -> "_2038.LoadedRollerStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2038

            return self._parent._cast(_2038.LoadedRollerStripLoadResults)

        @property
        def loaded_toroidal_roller_bearing_strip_load_results(
            self: "LoadedSphericalRollerRadialBearingStripLoadResults._Cast_LoadedSphericalRollerRadialBearingStripLoadResults",
        ) -> "_2066.LoadedToroidalRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2066

            return self._parent._cast(_2066.LoadedToroidalRollerBearingStripLoadResults)

        @property
        def loaded_spherical_roller_radial_bearing_strip_load_results(
            self: "LoadedSphericalRollerRadialBearingStripLoadResults._Cast_LoadedSphericalRollerRadialBearingStripLoadResults",
        ) -> "LoadedSphericalRollerRadialBearingStripLoadResults":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalRollerRadialBearingStripLoadResults._Cast_LoadedSphericalRollerRadialBearingStripLoadResults",
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
        instance_to_wrap: "LoadedSphericalRollerRadialBearingStripLoadResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedSphericalRollerRadialBearingStripLoadResults._Cast_LoadedSphericalRollerRadialBearingStripLoadResults":
        return self._Cast_LoadedSphericalRollerRadialBearingStripLoadResults(self)
