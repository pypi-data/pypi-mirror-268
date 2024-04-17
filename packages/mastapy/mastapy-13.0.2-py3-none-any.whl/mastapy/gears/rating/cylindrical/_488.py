"""ScuffingResultsRowGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCUFFING_RESULTS_ROW_GEAR = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "ScuffingResultsRowGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029


__docformat__ = "restructuredtext en"
__all__ = ("ScuffingResultsRowGear",)


Self = TypeVar("Self", bound="ScuffingResultsRowGear")


class ScuffingResultsRowGear(_0.APIBase):
    """ScuffingResultsRowGear

    This is a mastapy class.
    """

    TYPE = _SCUFFING_RESULTS_ROW_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ScuffingResultsRowGear")

    class _Cast_ScuffingResultsRowGear:
        """Special nested class for casting ScuffingResultsRowGear to subclasses."""

        def __init__(
            self: "ScuffingResultsRowGear._Cast_ScuffingResultsRowGear",
            parent: "ScuffingResultsRowGear",
        ):
            self._parent = parent

        @property
        def scuffing_results_row_gear(
            self: "ScuffingResultsRowGear._Cast_ScuffingResultsRowGear",
        ) -> "ScuffingResultsRowGear":
            return self._parent

        def __getattr__(
            self: "ScuffingResultsRowGear._Cast_ScuffingResultsRowGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ScuffingResultsRowGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def profile_measurement(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileMeasurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ScuffingResultsRowGear._Cast_ScuffingResultsRowGear":
        return self._Cast_ScuffingResultsRowGear(self)
