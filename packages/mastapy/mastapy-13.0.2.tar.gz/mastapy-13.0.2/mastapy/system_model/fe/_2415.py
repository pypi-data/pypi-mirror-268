"""RaceBearingFEWithSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.fe import _2367
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACE_BEARING_FE_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "RaceBearingFEWithSelection"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1507
    from mastapy.system_model.fe import _2413


__docformat__ = "restructuredtext en"
__all__ = ("RaceBearingFEWithSelection",)


Self = TypeVar("Self", bound="RaceBearingFEWithSelection")


class RaceBearingFEWithSelection(_2367.BaseFEWithSelection):
    """RaceBearingFEWithSelection

    This is a mastapy class.
    """

    TYPE = _RACE_BEARING_FE_WITH_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RaceBearingFEWithSelection")

    class _Cast_RaceBearingFEWithSelection:
        """Special nested class for casting RaceBearingFEWithSelection to subclasses."""

        def __init__(
            self: "RaceBearingFEWithSelection._Cast_RaceBearingFEWithSelection",
            parent: "RaceBearingFEWithSelection",
        ):
            self._parent = parent

        @property
        def base_fe_with_selection(
            self: "RaceBearingFEWithSelection._Cast_RaceBearingFEWithSelection",
        ) -> "_2367.BaseFEWithSelection":
            return self._parent._cast(_2367.BaseFEWithSelection)

        @property
        def race_bearing_fe_with_selection(
            self: "RaceBearingFEWithSelection._Cast_RaceBearingFEWithSelection",
        ) -> "RaceBearingFEWithSelection":
            return self._parent

        def __getattr__(
            self: "RaceBearingFEWithSelection._Cast_RaceBearingFEWithSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RaceBearingFEWithSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def manual_alignment(self: Self) -> "_1507.CoordinateSystemEditor":
        """mastapy.math_utility.CoordinateSystemEditor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManualAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def race_bearing(self: Self) -> "_2413.RaceBearingFE":
        """mastapy.system_model.fe.RaceBearingFE

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RaceBearingFEWithSelection._Cast_RaceBearingFEWithSelection":
        return self._Cast_RaceBearingFEWithSelection(self)
