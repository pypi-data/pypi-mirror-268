"""CylindricalGearFilletNodeStressResultsRow"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS_ROW = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "CylindricalGearFilletNodeStressResultsRow"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFilletNodeStressResultsRow",)


Self = TypeVar("Self", bound="CylindricalGearFilletNodeStressResultsRow")


class CylindricalGearFilletNodeStressResultsRow(_842.GearFilletNodeStressResultsRow):
    """CylindricalGearFilletNodeStressResultsRow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS_ROW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearFilletNodeStressResultsRow"
    )

    class _Cast_CylindricalGearFilletNodeStressResultsRow:
        """Special nested class for casting CylindricalGearFilletNodeStressResultsRow to subclasses."""

        def __init__(
            self: "CylindricalGearFilletNodeStressResultsRow._Cast_CylindricalGearFilletNodeStressResultsRow",
            parent: "CylindricalGearFilletNodeStressResultsRow",
        ):
            self._parent = parent

        @property
        def gear_fillet_node_stress_results_row(
            self: "CylindricalGearFilletNodeStressResultsRow._Cast_CylindricalGearFilletNodeStressResultsRow",
        ) -> "_842.GearFilletNodeStressResultsRow":
            return self._parent._cast(_842.GearFilletNodeStressResultsRow)

        @property
        def cylindrical_gear_fillet_node_stress_results_row(
            self: "CylindricalGearFilletNodeStressResultsRow._Cast_CylindricalGearFilletNodeStressResultsRow",
        ) -> "CylindricalGearFilletNodeStressResultsRow":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFilletNodeStressResultsRow._Cast_CylindricalGearFilletNodeStressResultsRow",
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
        self: Self, instance_to_wrap: "CylindricalGearFilletNodeStressResultsRow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_along_fillet(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistanceAlongFillet

        if temp is None:
            return 0.0

        return temp

    @property
    def radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearFilletNodeStressResultsRow._Cast_CylindricalGearFilletNodeStressResultsRow":
        return self._Cast_CylindricalGearFilletNodeStressResultsRow(self)
