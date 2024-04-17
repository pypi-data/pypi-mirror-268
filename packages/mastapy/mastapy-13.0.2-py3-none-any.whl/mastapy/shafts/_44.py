"""StressMeasurementShaftAxialBendingTorsionalComponentValues"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRESS_MEASUREMENT_SHAFT_AXIAL_BENDING_TORSIONAL_COMPONENT_VALUES = python_net_import(
    "SMT.MastaAPI.Shafts", "StressMeasurementShaftAxialBendingTorsionalComponentValues"
)


__docformat__ = "restructuredtext en"
__all__ = ("StressMeasurementShaftAxialBendingTorsionalComponentValues",)


Self = TypeVar(
    "Self", bound="StressMeasurementShaftAxialBendingTorsionalComponentValues"
)


class StressMeasurementShaftAxialBendingTorsionalComponentValues(_0.APIBase):
    """StressMeasurementShaftAxialBendingTorsionalComponentValues

    This is a mastapy class.
    """

    TYPE = _STRESS_MEASUREMENT_SHAFT_AXIAL_BENDING_TORSIONAL_COMPONENT_VALUES
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StressMeasurementShaftAxialBendingTorsionalComponentValues",
    )

    class _Cast_StressMeasurementShaftAxialBendingTorsionalComponentValues:
        """Special nested class for casting StressMeasurementShaftAxialBendingTorsionalComponentValues to subclasses."""

        def __init__(
            self: "StressMeasurementShaftAxialBendingTorsionalComponentValues._Cast_StressMeasurementShaftAxialBendingTorsionalComponentValues",
            parent: "StressMeasurementShaftAxialBendingTorsionalComponentValues",
        ):
            self._parent = parent

        @property
        def stress_measurement_shaft_axial_bending_torsional_component_values(
            self: "StressMeasurementShaftAxialBendingTorsionalComponentValues._Cast_StressMeasurementShaftAxialBendingTorsionalComponentValues",
        ) -> "StressMeasurementShaftAxialBendingTorsionalComponentValues":
            return self._parent

        def __getattr__(
            self: "StressMeasurementShaftAxialBendingTorsionalComponentValues._Cast_StressMeasurementShaftAxialBendingTorsionalComponentValues",
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
        instance_to_wrap: "StressMeasurementShaftAxialBendingTorsionalComponentValues.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Axial

        if temp is None:
            return 0.0

        return temp

    @property
    def bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torsional

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "StressMeasurementShaftAxialBendingTorsionalComponentValues._Cast_StressMeasurementShaftAxialBendingTorsionalComponentValues":
        return self._Cast_StressMeasurementShaftAxialBendingTorsionalComponentValues(
            self
        )
