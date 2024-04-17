"""LoadedNonBarrelRollerBearingStripLoadResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2038
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_STRIP_LOAD_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedNonBarrelRollerBearingStripLoadResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerBearingStripLoadResults",)


Self = TypeVar("Self", bound="LoadedNonBarrelRollerBearingStripLoadResults")


class LoadedNonBarrelRollerBearingStripLoadResults(_2038.LoadedRollerStripLoadResults):
    """LoadedNonBarrelRollerBearingStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_STRIP_LOAD_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedNonBarrelRollerBearingStripLoadResults"
    )

    class _Cast_LoadedNonBarrelRollerBearingStripLoadResults:
        """Special nested class for casting LoadedNonBarrelRollerBearingStripLoadResults to subclasses."""

        def __init__(
            self: "LoadedNonBarrelRollerBearingStripLoadResults._Cast_LoadedNonBarrelRollerBearingStripLoadResults",
            parent: "LoadedNonBarrelRollerBearingStripLoadResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_strip_load_results(
            self: "LoadedNonBarrelRollerBearingStripLoadResults._Cast_LoadedNonBarrelRollerBearingStripLoadResults",
        ) -> "_2038.LoadedRollerStripLoadResults":
            return self._parent._cast(_2038.LoadedRollerStripLoadResults)

        @property
        def loaded_non_barrel_roller_bearing_strip_load_results(
            self: "LoadedNonBarrelRollerBearingStripLoadResults._Cast_LoadedNonBarrelRollerBearingStripLoadResults",
        ) -> "LoadedNonBarrelRollerBearingStripLoadResults":
            return self._parent

        def __getattr__(
            self: "LoadedNonBarrelRollerBearingStripLoadResults._Cast_LoadedNonBarrelRollerBearingStripLoadResults",
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
        instance_to_wrap: "LoadedNonBarrelRollerBearingStripLoadResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonBarrelRollerBearingStripLoadResults._Cast_LoadedNonBarrelRollerBearingStripLoadResults":
        return self._Cast_LoadedNonBarrelRollerBearingStripLoadResults(self)
