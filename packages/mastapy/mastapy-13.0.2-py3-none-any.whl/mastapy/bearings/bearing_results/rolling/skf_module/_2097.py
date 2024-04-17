"""LifeModel"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LIFE_MODEL = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "LifeModel"
)


__docformat__ = "restructuredtext en"
__all__ = ("LifeModel",)


Self = TypeVar("Self", bound="LifeModel")


class LifeModel(_2103.SKFCalculationResult):
    """LifeModel

    This is a mastapy class.
    """

    TYPE = _LIFE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LifeModel")

    class _Cast_LifeModel:
        """Special nested class for casting LifeModel to subclasses."""

        def __init__(self: "LifeModel._Cast_LifeModel", parent: "LifeModel"):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "LifeModel._Cast_LifeModel",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def life_model(self: "LifeModel._Cast_LifeModel") -> "LifeModel":
            return self._parent

        def __getattr__(self: "LifeModel._Cast_LifeModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LifeModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Basic

        if temp is None:
            return 0.0

        return temp

    @property
    def skf(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKF

        if temp is None:
            return 0.0

        return temp

    @property
    def skfgblm(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFGBLM

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "LifeModel._Cast_LifeModel":
        return self._Cast_LifeModel(self)
