"""CylindricalGearScuffingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SCUFFING_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearScuffingResults"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _487


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearScuffingResults",)


Self = TypeVar("Self", bound="CylindricalGearScuffingResults")


class CylindricalGearScuffingResults(_0.APIBase):
    """CylindricalGearScuffingResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SCUFFING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearScuffingResults")

    class _Cast_CylindricalGearScuffingResults:
        """Special nested class for casting CylindricalGearScuffingResults to subclasses."""

        def __init__(
            self: "CylindricalGearScuffingResults._Cast_CylindricalGearScuffingResults",
            parent: "CylindricalGearScuffingResults",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_scuffing_results(
            self: "CylindricalGearScuffingResults._Cast_CylindricalGearScuffingResults",
        ) -> "CylindricalGearScuffingResults":
            return self._parent

        def __getattr__(
            self: "CylindricalGearScuffingResults._Cast_CylindricalGearScuffingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearScuffingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def scuffing_results_row(self: Self) -> "List[_487.ScuffingResultsRow]":
        """List[mastapy.gears.rating.cylindrical.ScuffingResultsRow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingResultsRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearScuffingResults._Cast_CylindricalGearScuffingResults":
        return self._Cast_CylindricalGearScuffingResults(self)
