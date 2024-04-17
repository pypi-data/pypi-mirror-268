"""LoadedAsymmetricSphericalRollerBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2035
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAsymmetricSphericalRollerBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAsymmetricSphericalRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedAsymmetricSphericalRollerBearingElement")


class LoadedAsymmetricSphericalRollerBearingElement(_2035.LoadedRollerBearingElement):
    """LoadedAsymmetricSphericalRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAsymmetricSphericalRollerBearingElement"
    )

    class _Cast_LoadedAsymmetricSphericalRollerBearingElement:
        """Special nested class for casting LoadedAsymmetricSphericalRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedAsymmetricSphericalRollerBearingElement._Cast_LoadedAsymmetricSphericalRollerBearingElement",
            parent: "LoadedAsymmetricSphericalRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(
            self: "LoadedAsymmetricSphericalRollerBearingElement._Cast_LoadedAsymmetricSphericalRollerBearingElement",
        ) -> "_2035.LoadedRollerBearingElement":
            return self._parent._cast(_2035.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedAsymmetricSphericalRollerBearingElement._Cast_LoadedAsymmetricSphericalRollerBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_asymmetric_spherical_roller_bearing_element(
            self: "LoadedAsymmetricSphericalRollerBearingElement._Cast_LoadedAsymmetricSphericalRollerBearingElement",
        ) -> "LoadedAsymmetricSphericalRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedAsymmetricSphericalRollerBearingElement._Cast_LoadedAsymmetricSphericalRollerBearingElement",
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
        instance_to_wrap: "LoadedAsymmetricSphericalRollerBearingElement.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAsymmetricSphericalRollerBearingElement._Cast_LoadedAsymmetricSphericalRollerBearingElement":
        return self._Cast_LoadedAsymmetricSphericalRollerBearingElement(self)
