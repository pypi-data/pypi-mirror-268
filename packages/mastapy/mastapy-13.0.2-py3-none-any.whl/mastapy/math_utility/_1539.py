"""StressPoint"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRESS_POINT = python_net_import("SMT.MastaAPI.MathUtility", "StressPoint")

if TYPE_CHECKING:
    from mastapy.shafts import _27


__docformat__ = "restructuredtext en"
__all__ = ("StressPoint",)


Self = TypeVar("Self", bound="StressPoint")


class StressPoint(_0.APIBase):
    """StressPoint

    This is a mastapy class.
    """

    TYPE = _STRESS_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StressPoint")

    class _Cast_StressPoint:
        """Special nested class for casting StressPoint to subclasses."""

        def __init__(self: "StressPoint._Cast_StressPoint", parent: "StressPoint"):
            self._parent = parent

        @property
        def shaft_point_stress(
            self: "StressPoint._Cast_StressPoint",
        ) -> "_27.ShaftPointStress":
            from mastapy.shafts import _27

            return self._parent._cast(_27.ShaftPointStress)

        @property
        def stress_point(self: "StressPoint._Cast_StressPoint") -> "StressPoint":
            return self._parent

        def __getattr__(self: "StressPoint._Cast_StressPoint", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StressPoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialStress

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorsionalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def x_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def y_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "StressPoint._Cast_StressPoint":
        return self._Cast_StressPoint(self)
