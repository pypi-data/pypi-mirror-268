"""Viscosities"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VISCOSITIES = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "Viscosities"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import _2099


__docformat__ = "restructuredtext en"
__all__ = ("Viscosities",)


Self = TypeVar("Self", bound="Viscosities")


class Viscosities(_2103.SKFCalculationResult):
    """Viscosities

    This is a mastapy class.
    """

    TYPE = _VISCOSITIES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Viscosities")

    class _Cast_Viscosities:
        """Special nested class for casting Viscosities to subclasses."""

        def __init__(self: "Viscosities._Cast_Viscosities", parent: "Viscosities"):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "Viscosities._Cast_Viscosities",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def viscosities(self: "Viscosities._Cast_Viscosities") -> "Viscosities":
            return self._parent

        def __getattr__(self: "Viscosities._Cast_Viscosities", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Viscosities.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def viscosity_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ViscosityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_viscosity(self: Self) -> "_2099.OperatingViscosity":
        """mastapy.bearings.bearing_results.rolling.skf_module.OperatingViscosity

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingViscosity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Viscosities._Cast_Viscosities":
        return self._Cast_Viscosities(self)
