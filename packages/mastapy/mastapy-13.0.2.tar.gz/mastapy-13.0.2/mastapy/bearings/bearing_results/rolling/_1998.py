"""LoadedAsymmetricSphericalRollerBearingStripLoadResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _1988
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_STRIP_LOAD_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAsymmetricSphericalRollerBearingStripLoadResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2038


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAsymmetricSphericalRollerBearingStripLoadResults",)


Self = TypeVar("Self", bound="LoadedAsymmetricSphericalRollerBearingStripLoadResults")


class LoadedAsymmetricSphericalRollerBearingStripLoadResults(
    _1988.LoadedAbstractSphericalRollerBearingStripLoadResults
):
    """LoadedAsymmetricSphericalRollerBearingStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_STRIP_LOAD_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults",
    )

    class _Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults:
        """Special nested class for casting LoadedAsymmetricSphericalRollerBearingStripLoadResults to subclasses."""

        def __init__(
            self: "LoadedAsymmetricSphericalRollerBearingStripLoadResults._Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults",
            parent: "LoadedAsymmetricSphericalRollerBearingStripLoadResults",
        ):
            self._parent = parent

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(
            self: "LoadedAsymmetricSphericalRollerBearingStripLoadResults._Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults",
        ) -> "_1988.LoadedAbstractSphericalRollerBearingStripLoadResults":
            return self._parent._cast(
                _1988.LoadedAbstractSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_roller_strip_load_results(
            self: "LoadedAsymmetricSphericalRollerBearingStripLoadResults._Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults",
        ) -> "_2038.LoadedRollerStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2038

            return self._parent._cast(_2038.LoadedRollerStripLoadResults)

        @property
        def loaded_asymmetric_spherical_roller_bearing_strip_load_results(
            self: "LoadedAsymmetricSphericalRollerBearingStripLoadResults._Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults",
        ) -> "LoadedAsymmetricSphericalRollerBearingStripLoadResults":
            return self._parent

        def __getattr__(
            self: "LoadedAsymmetricSphericalRollerBearingStripLoadResults._Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults",
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
        instance_to_wrap: "LoadedAsymmetricSphericalRollerBearingStripLoadResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAsymmetricSphericalRollerBearingStripLoadResults._Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults":
        return self._Cast_LoadedAsymmetricSphericalRollerBearingStripLoadResults(self)
