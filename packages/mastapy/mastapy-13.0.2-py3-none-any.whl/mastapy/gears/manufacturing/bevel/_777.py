"""ConicalFlankDeviationsData"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_FLANK_DEVIATIONS_DATA = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalFlankDeviationsData"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalFlankDeviationsData",)


Self = TypeVar("Self", bound="ConicalFlankDeviationsData")


class ConicalFlankDeviationsData(_0.APIBase):
    """ConicalFlankDeviationsData

    This is a mastapy class.
    """

    TYPE = _CONICAL_FLANK_DEVIATIONS_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalFlankDeviationsData")

    class _Cast_ConicalFlankDeviationsData:
        """Special nested class for casting ConicalFlankDeviationsData to subclasses."""

        def __init__(
            self: "ConicalFlankDeviationsData._Cast_ConicalFlankDeviationsData",
            parent: "ConicalFlankDeviationsData",
        ):
            self._parent = parent

        @property
        def conical_flank_deviations_data(
            self: "ConicalFlankDeviationsData._Cast_ConicalFlankDeviationsData",
        ) -> "ConicalFlankDeviationsData":
            return self._parent

        def __getattr__(
            self: "ConicalFlankDeviationsData._Cast_ConicalFlankDeviationsData",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalFlankDeviationsData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_crowning_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageCrowningDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def average_pressure_angle_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragePressureAngleDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def average_profile_curvature_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageProfileCurvatureDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def average_spiral_angle_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageSpiralAngleDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def bias_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BiasDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalFlankDeviationsData._Cast_ConicalFlankDeviationsData":
        return self._Cast_ConicalFlankDeviationsData(self)
