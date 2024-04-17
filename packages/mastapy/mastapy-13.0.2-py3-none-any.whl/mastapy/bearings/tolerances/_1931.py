"""ToleranceCombination"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOLERANCE_COMBINATION = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "ToleranceCombination"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1912


__docformat__ = "restructuredtext en"
__all__ = ("ToleranceCombination",)


Self = TypeVar("Self", bound="ToleranceCombination")


class ToleranceCombination(_0.APIBase):
    """ToleranceCombination

    This is a mastapy class.
    """

    TYPE = _TOLERANCE_COMBINATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToleranceCombination")

    class _Cast_ToleranceCombination:
        """Special nested class for casting ToleranceCombination to subclasses."""

        def __init__(
            self: "ToleranceCombination._Cast_ToleranceCombination",
            parent: "ToleranceCombination",
        ):
            self._parent = parent

        @property
        def tolerance_combination(
            self: "ToleranceCombination._Cast_ToleranceCombination",
        ) -> "ToleranceCombination":
            return self._parent

        def __getattr__(
            self: "ToleranceCombination._Cast_ToleranceCombination", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ToleranceCombination.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fit(self: Self) -> "_1912.FitType":
        """mastapy.bearings.tolerances.FitType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Fit

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.Tolerances.FitType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.tolerances._1912", "FitType"
        )(value)

    @property
    def lower_value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowerValue

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def upper_value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UpperValue

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ToleranceCombination._Cast_ToleranceCombination":
        return self._Cast_ToleranceCombination(self)
