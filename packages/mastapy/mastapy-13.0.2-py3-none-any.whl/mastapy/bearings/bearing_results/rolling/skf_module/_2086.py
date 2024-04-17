"""BearingRatingLife"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_RATING_LIFE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "BearingRatingLife"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import _2097


__docformat__ = "restructuredtext en"
__all__ = ("BearingRatingLife",)


Self = TypeVar("Self", bound="BearingRatingLife")


class BearingRatingLife(_2103.SKFCalculationResult):
    """BearingRatingLife

    This is a mastapy class.
    """

    TYPE = _BEARING_RATING_LIFE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingRatingLife")

    class _Cast_BearingRatingLife:
        """Special nested class for casting BearingRatingLife to subclasses."""

        def __init__(
            self: "BearingRatingLife._Cast_BearingRatingLife",
            parent: "BearingRatingLife",
        ):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "BearingRatingLife._Cast_BearingRatingLife",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def bearing_rating_life(
            self: "BearingRatingLife._Cast_BearingRatingLife",
        ) -> "BearingRatingLife":
            return self._parent

        def __getattr__(self: "BearingRatingLife._Cast_BearingRatingLife", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingRatingLife.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contamination_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContaminationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def skf_life_modification_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFLifeModificationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def life_model(self: Self) -> "_2097.LifeModel":
        """mastapy.bearings.bearing_results.rolling.skf_module.LifeModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BearingRatingLife._Cast_BearingRatingLife":
        return self._Cast_BearingRatingLife(self)
