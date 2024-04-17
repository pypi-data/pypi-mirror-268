"""FindleyCriticalPlaneAnalysis"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FINDLEY_CRITICAL_PLANE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.GearTwoDFEAnalysis", "FindleyCriticalPlaneAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("FindleyCriticalPlaneAnalysis",)


Self = TypeVar("Self", bound="FindleyCriticalPlaneAnalysis")


class FindleyCriticalPlaneAnalysis(_0.APIBase):
    """FindleyCriticalPlaneAnalysis

    This is a mastapy class.
    """

    TYPE = _FINDLEY_CRITICAL_PLANE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FindleyCriticalPlaneAnalysis")

    class _Cast_FindleyCriticalPlaneAnalysis:
        """Special nested class for casting FindleyCriticalPlaneAnalysis to subclasses."""

        def __init__(
            self: "FindleyCriticalPlaneAnalysis._Cast_FindleyCriticalPlaneAnalysis",
            parent: "FindleyCriticalPlaneAnalysis",
        ):
            self._parent = parent

        @property
        def findley_critical_plane_analysis(
            self: "FindleyCriticalPlaneAnalysis._Cast_FindleyCriticalPlaneAnalysis",
        ) -> "FindleyCriticalPlaneAnalysis":
            return self._parent

        def __getattr__(
            self: "FindleyCriticalPlaneAnalysis._Cast_FindleyCriticalPlaneAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FindleyCriticalPlaneAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crack_initiation_risk_factor(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrackInitiationRiskFactor

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def max_normal_stress(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxNormalStress

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def max_shear_amplitude(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxShearAmplitude

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def maximum_findley_critical_plane_angle(self: Self) -> "List[Vector2D]":
        """List[Vector2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumFindleyCriticalPlaneAngle

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector2D)

        if value is None:
            return None

        return value

    @property
    def maximum_findley_critical_plane_stress(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumFindleyCriticalPlaneStress

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FindleyCriticalPlaneAnalysis._Cast_FindleyCriticalPlaneAnalysis":
        return self._Cast_FindleyCriticalPlaneAnalysis(self)
