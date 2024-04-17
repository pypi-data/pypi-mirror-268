"""GeometricConstants"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRIC_CONSTANTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "GeometricConstants"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2163, _2164


__docformat__ = "restructuredtext en"
__all__ = ("GeometricConstants",)


Self = TypeVar("Self", bound="GeometricConstants")


class GeometricConstants(_0.APIBase):
    """GeometricConstants

    This is a mastapy class.
    """

    TYPE = _GEOMETRIC_CONSTANTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeometricConstants")

    class _Cast_GeometricConstants:
        """Special nested class for casting GeometricConstants to subclasses."""

        def __init__(
            self: "GeometricConstants._Cast_GeometricConstants",
            parent: "GeometricConstants",
        ):
            self._parent = parent

        @property
        def geometric_constants(
            self: "GeometricConstants._Cast_GeometricConstants",
        ) -> "GeometricConstants":
            return self._parent

        def __getattr__(self: "GeometricConstants._Cast_GeometricConstants", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GeometricConstants.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometric_constants_for_rolling_frictional_moments(
        self: Self,
    ) -> "_2163.GeometricConstantsForRollingFrictionalMoments":
        """mastapy.bearings.bearing_designs.rolling.GeometricConstantsForRollingFrictionalMoments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometricConstantsForRollingFrictionalMoments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def geometric_constants_for_sliding_frictional_moments(
        self: Self,
    ) -> "_2164.GeometricConstantsForSlidingFrictionalMoments":
        """mastapy.bearings.bearing_designs.rolling.GeometricConstantsForSlidingFrictionalMoments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometricConstantsForSlidingFrictionalMoments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GeometricConstants._Cast_GeometricConstants":
        return self._Cast_GeometricConstants(self)
