"""ShaftPointStress"""

from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility import _1539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_POINT_STRESS = python_net_import("SMT.MastaAPI.Shafts", "ShaftPointStress")


__docformat__ = "restructuredtext en"
__all__ = ("ShaftPointStress",)


Self = TypeVar("Self", bound="ShaftPointStress")


class ShaftPointStress(_1539.StressPoint):
    """ShaftPointStress

    This is a mastapy class.
    """

    TYPE = _SHAFT_POINT_STRESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftPointStress")

    class _Cast_ShaftPointStress:
        """Special nested class for casting ShaftPointStress to subclasses."""

        def __init__(
            self: "ShaftPointStress._Cast_ShaftPointStress", parent: "ShaftPointStress"
        ):
            self._parent = parent

        @property
        def stress_point(
            self: "ShaftPointStress._Cast_ShaftPointStress",
        ) -> "_1539.StressPoint":
            return self._parent._cast(_1539.StressPoint)

        @property
        def shaft_point_stress(
            self: "ShaftPointStress._Cast_ShaftPointStress",
        ) -> "ShaftPointStress":
            return self._parent

        def __getattr__(self: "ShaftPointStress._Cast_ShaftPointStress", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftPointStress.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_max_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleOfMaxBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_principal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPrincipalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_principal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumPrincipalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def von_mises_stress_max(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VonMisesStressMax

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ShaftPointStress._Cast_ShaftPointStress":
        return self._Cast_ShaftPointStress(self)
