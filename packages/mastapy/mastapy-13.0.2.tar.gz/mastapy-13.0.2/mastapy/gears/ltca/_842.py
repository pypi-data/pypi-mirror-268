"""GearFilletNodeStressResultsRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_FILLET_NODE_STRESS_RESULTS_ROW = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearFilletNodeStressResultsRow"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _840, _833


__docformat__ = "restructuredtext en"
__all__ = ("GearFilletNodeStressResultsRow",)


Self = TypeVar("Self", bound="GearFilletNodeStressResultsRow")


class GearFilletNodeStressResultsRow(_0.APIBase):
    """GearFilletNodeStressResultsRow

    This is a mastapy class.
    """

    TYPE = _GEAR_FILLET_NODE_STRESS_RESULTS_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearFilletNodeStressResultsRow")

    class _Cast_GearFilletNodeStressResultsRow:
        """Special nested class for casting GearFilletNodeStressResultsRow to subclasses."""

        def __init__(
            self: "GearFilletNodeStressResultsRow._Cast_GearFilletNodeStressResultsRow",
            parent: "GearFilletNodeStressResultsRow",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_fillet_node_stress_results_row(
            self: "GearFilletNodeStressResultsRow._Cast_GearFilletNodeStressResultsRow",
        ) -> "_833.CylindricalGearFilletNodeStressResultsRow":
            from mastapy.gears.ltca import _833

            return self._parent._cast(_833.CylindricalGearFilletNodeStressResultsRow)

        @property
        def gear_fillet_node_stress_results_row(
            self: "GearFilletNodeStressResultsRow._Cast_GearFilletNodeStressResultsRow",
        ) -> "GearFilletNodeStressResultsRow":
            return self._parent

        def __getattr__(
            self: "GearFilletNodeStressResultsRow._Cast_GearFilletNodeStressResultsRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearFilletNodeStressResultsRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fillet_row_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilletRowIndex

        if temp is None:
            return 0

        return temp

    @property
    def node_results(self: Self) -> "List[_840.GearFilletNodeStressResults]":
        """List[mastapy.gears.ltca.GearFilletNodeStressResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearFilletNodeStressResultsRow._Cast_GearFilletNodeStressResultsRow":
        return self._Cast_GearFilletNodeStressResultsRow(self)
