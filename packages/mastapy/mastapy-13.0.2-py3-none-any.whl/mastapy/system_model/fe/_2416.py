"""ReplacedShaftSelectionHelper"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REPLACED_SHAFT_SELECTION_HELPER = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "ReplacedShaftSelectionHelper"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2489


__docformat__ = "restructuredtext en"
__all__ = ("ReplacedShaftSelectionHelper",)


Self = TypeVar("Self", bound="ReplacedShaftSelectionHelper")


class ReplacedShaftSelectionHelper(_0.APIBase):
    """ReplacedShaftSelectionHelper

    This is a mastapy class.
    """

    TYPE = _REPLACED_SHAFT_SELECTION_HELPER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ReplacedShaftSelectionHelper")

    class _Cast_ReplacedShaftSelectionHelper:
        """Special nested class for casting ReplacedShaftSelectionHelper to subclasses."""

        def __init__(
            self: "ReplacedShaftSelectionHelper._Cast_ReplacedShaftSelectionHelper",
            parent: "ReplacedShaftSelectionHelper",
        ):
            self._parent = parent

        @property
        def replaced_shaft_selection_helper(
            self: "ReplacedShaftSelectionHelper._Cast_ReplacedShaftSelectionHelper",
        ) -> "ReplacedShaftSelectionHelper":
            return self._parent

        def __getattr__(
            self: "ReplacedShaftSelectionHelper._Cast_ReplacedShaftSelectionHelper",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ReplacedShaftSelectionHelper.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_replaced_by_fe(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsReplacedByFE

        if temp is None:
            return False

        return temp

    @is_replaced_by_fe.setter
    @enforce_parameter_types
    def is_replaced_by_fe(self: Self, value: "bool"):
        self.wrapped.IsReplacedByFE = bool(value) if value is not None else False

    @property
    def shaft(self: Self) -> "_2489.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ReplacedShaftSelectionHelper._Cast_ReplacedShaftSelectionHelper":
        return self._Cast_ReplacedShaftSelectionHelper(self)
