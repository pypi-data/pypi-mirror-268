"""CylindricalGearFilletNodeStressResultsColumn"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _841
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS_COLUMN = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "CylindricalGearFilletNodeStressResultsColumn"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFilletNodeStressResultsColumn",)


Self = TypeVar("Self", bound="CylindricalGearFilletNodeStressResultsColumn")


class CylindricalGearFilletNodeStressResultsColumn(
    _841.GearFilletNodeStressResultsColumn
):
    """CylindricalGearFilletNodeStressResultsColumn

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS_COLUMN
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearFilletNodeStressResultsColumn"
    )

    class _Cast_CylindricalGearFilletNodeStressResultsColumn:
        """Special nested class for casting CylindricalGearFilletNodeStressResultsColumn to subclasses."""

        def __init__(
            self: "CylindricalGearFilletNodeStressResultsColumn._Cast_CylindricalGearFilletNodeStressResultsColumn",
            parent: "CylindricalGearFilletNodeStressResultsColumn",
        ):
            self._parent = parent

        @property
        def gear_fillet_node_stress_results_column(
            self: "CylindricalGearFilletNodeStressResultsColumn._Cast_CylindricalGearFilletNodeStressResultsColumn",
        ) -> "_841.GearFilletNodeStressResultsColumn":
            return self._parent._cast(_841.GearFilletNodeStressResultsColumn)

        @property
        def cylindrical_gear_fillet_node_stress_results_column(
            self: "CylindricalGearFilletNodeStressResultsColumn._Cast_CylindricalGearFilletNodeStressResultsColumn",
        ) -> "CylindricalGearFilletNodeStressResultsColumn":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFilletNodeStressResultsColumn._Cast_CylindricalGearFilletNodeStressResultsColumn",
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
        self: Self,
        instance_to_wrap: "CylindricalGearFilletNodeStressResultsColumn.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width_position(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidthPosition

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearFilletNodeStressResultsColumn._Cast_CylindricalGearFilletNodeStressResultsColumn":
        return self._Cast_CylindricalGearFilletNodeStressResultsColumn(self)
