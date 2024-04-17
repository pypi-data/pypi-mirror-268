"""GearFilletNodeStressResultsColumn"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_FILLET_NODE_STRESS_RESULTS_COLUMN = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearFilletNodeStressResultsColumn"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _840, _832


__docformat__ = "restructuredtext en"
__all__ = ("GearFilletNodeStressResultsColumn",)


Self = TypeVar("Self", bound="GearFilletNodeStressResultsColumn")


class GearFilletNodeStressResultsColumn(_0.APIBase):
    """GearFilletNodeStressResultsColumn

    This is a mastapy class.
    """

    TYPE = _GEAR_FILLET_NODE_STRESS_RESULTS_COLUMN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearFilletNodeStressResultsColumn")

    class _Cast_GearFilletNodeStressResultsColumn:
        """Special nested class for casting GearFilletNodeStressResultsColumn to subclasses."""

        def __init__(
            self: "GearFilletNodeStressResultsColumn._Cast_GearFilletNodeStressResultsColumn",
            parent: "GearFilletNodeStressResultsColumn",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_fillet_node_stress_results_column(
            self: "GearFilletNodeStressResultsColumn._Cast_GearFilletNodeStressResultsColumn",
        ) -> "_832.CylindricalGearFilletNodeStressResultsColumn":
            from mastapy.gears.ltca import _832

            return self._parent._cast(_832.CylindricalGearFilletNodeStressResultsColumn)

        @property
        def gear_fillet_node_stress_results_column(
            self: "GearFilletNodeStressResultsColumn._Cast_GearFilletNodeStressResultsColumn",
        ) -> "GearFilletNodeStressResultsColumn":
            return self._parent

        def __getattr__(
            self: "GearFilletNodeStressResultsColumn._Cast_GearFilletNodeStressResultsColumn",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "GearFilletNodeStressResultsColumn.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fillet_column_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilletColumnIndex

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
    ) -> "GearFilletNodeStressResultsColumn._Cast_GearFilletNodeStressResultsColumn":
        return self._Cast_GearFilletNodeStressResultsColumn(self)
