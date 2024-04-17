"""BearingDetailSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Optional, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.configurations import _2626
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Configurations", "BearingDetailSelection"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1967
    from mastapy.system_model.part_model import _2448


__docformat__ = "restructuredtext en"
__all__ = ("BearingDetailSelection",)


Self = TypeVar("Self", bound="BearingDetailSelection")


class BearingDetailSelection(
    _2626.PartDetailSelection["_2446.Bearing", "_2137.BearingDesign"]
):
    """BearingDetailSelection

    This is a mastapy class.
    """

    TYPE = _BEARING_DETAIL_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingDetailSelection")

    class _Cast_BearingDetailSelection:
        """Special nested class for casting BearingDetailSelection to subclasses."""

        def __init__(
            self: "BearingDetailSelection._Cast_BearingDetailSelection",
            parent: "BearingDetailSelection",
        ):
            self._parent = parent

        @property
        def part_detail_selection(
            self: "BearingDetailSelection._Cast_BearingDetailSelection",
        ) -> "_2626.PartDetailSelection":
            return self._parent._cast(_2626.PartDetailSelection)

        @property
        def bearing_detail_selection(
            self: "BearingDetailSelection._Cast_BearingDetailSelection",
        ) -> "BearingDetailSelection":
            return self._parent

        def __getattr__(
            self: "BearingDetailSelection._Cast_BearingDetailSelection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingDetailSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_offset(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.InnerOffset

        if temp is None:
            return None

        return temp

    @inner_offset.setter
    @enforce_parameter_types
    def inner_offset(self: Self, value: "Optional[float]"):
        self.wrapped.InnerOffset = value

    @property
    def orientation(self: Self) -> "_1967.Orientations":
        """mastapy.bearings.bearing_results.Orientations"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results._1967", "Orientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: Self, value: "_1967.Orientations"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )
        self.wrapped.Orientation = value

    @property
    def outer_offset(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.OuterOffset

        if temp is None:
            return None

        return temp

    @outer_offset.setter
    @enforce_parameter_types
    def outer_offset(self: Self, value: "Optional[float]"):
        self.wrapped.OuterOffset = value

    @property
    def mounting(self: Self) -> "List[_2448.BearingRaceMountingOptions]":
        """List[mastapy.system_model.part_model.BearingRaceMountingOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mounting

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "BearingDetailSelection._Cast_BearingDetailSelection":
        return self._Cast_BearingDetailSelection(self)
