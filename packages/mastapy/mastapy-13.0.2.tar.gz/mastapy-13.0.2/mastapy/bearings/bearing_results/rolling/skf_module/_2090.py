"""Friction"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FRICTION = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "Friction"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import _2092, _2091


__docformat__ = "restructuredtext en"
__all__ = ("Friction",)


Self = TypeVar("Self", bound="Friction")


class Friction(_2103.SKFCalculationResult):
    """Friction

    This is a mastapy class.
    """

    TYPE = _FRICTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Friction")

    class _Cast_Friction:
        """Special nested class for casting Friction to subclasses."""

        def __init__(self: "Friction._Cast_Friction", parent: "Friction"):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "Friction._Cast_Friction",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def friction(self: "Friction._Cast_Friction") -> "Friction":
            return self._parent

        def __getattr__(self: "Friction._Cast_Friction", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Friction.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def friction_sources(self: Self) -> "_2092.FrictionSources":
        """mastapy.bearings.bearing_results.rolling.skf_module.FrictionSources

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionSources

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def frictional_moment(self: Self) -> "_2091.FrictionalMoment":
        """mastapy.bearings.bearing_results.rolling.skf_module.FrictionalMoment

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalMoment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Friction._Cast_Friction":
        return self._Cast_Friction(self)
