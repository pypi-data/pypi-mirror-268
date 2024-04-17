"""ShaftPointStressCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_POINT_STRESS_CYCLE = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftPointStressCycle"
)

if TYPE_CHECKING:
    from mastapy.shafts import _44, _27


__docformat__ = "restructuredtext en"
__all__ = ("ShaftPointStressCycle",)


Self = TypeVar("Self", bound="ShaftPointStressCycle")


class ShaftPointStressCycle(_0.APIBase):
    """ShaftPointStressCycle

    This is a mastapy class.
    """

    TYPE = _SHAFT_POINT_STRESS_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftPointStressCycle")

    class _Cast_ShaftPointStressCycle:
        """Special nested class for casting ShaftPointStressCycle to subclasses."""

        def __init__(
            self: "ShaftPointStressCycle._Cast_ShaftPointStressCycle",
            parent: "ShaftPointStressCycle",
        ):
            self._parent = parent

        @property
        def shaft_point_stress_cycle(
            self: "ShaftPointStressCycle._Cast_ShaftPointStressCycle",
        ) -> "ShaftPointStressCycle":
            return self._parent

        def __getattr__(
            self: "ShaftPointStressCycle._Cast_ShaftPointStressCycle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftPointStressCycle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def din743201212_comparative_mean_stress(
        self: Self,
    ) -> "_44.StressMeasurementShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.StressMeasurementShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN743201212ComparativeMeanStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stress_amplitude(self: Self) -> "_27.ShaftPointStress":
        """mastapy.shafts.ShaftPointStress

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressAmplitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stress_mean(self: Self) -> "_27.ShaftPointStress":
        """mastapy.shafts.ShaftPointStress

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressMean

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stress_total(self: Self) -> "_27.ShaftPointStress":
        """mastapy.shafts.ShaftPointStress

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ShaftPointStressCycle._Cast_ShaftPointStressCycle":
        return self._Cast_ShaftPointStressCycle(self)
