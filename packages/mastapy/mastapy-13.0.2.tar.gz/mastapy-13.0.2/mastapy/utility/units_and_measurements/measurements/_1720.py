"""StiffnessPerUnitFaceWidth"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STIFFNESS_PER_UNIT_FACE_WIDTH = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "StiffnessPerUnitFaceWidth",
)


__docformat__ = "restructuredtext en"
__all__ = ("StiffnessPerUnitFaceWidth",)


Self = TypeVar("Self", bound="StiffnessPerUnitFaceWidth")


class StiffnessPerUnitFaceWidth(_1612.MeasurementBase):
    """StiffnessPerUnitFaceWidth

    This is a mastapy class.
    """

    TYPE = _STIFFNESS_PER_UNIT_FACE_WIDTH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StiffnessPerUnitFaceWidth")

    class _Cast_StiffnessPerUnitFaceWidth:
        """Special nested class for casting StiffnessPerUnitFaceWidth to subclasses."""

        def __init__(
            self: "StiffnessPerUnitFaceWidth._Cast_StiffnessPerUnitFaceWidth",
            parent: "StiffnessPerUnitFaceWidth",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "StiffnessPerUnitFaceWidth._Cast_StiffnessPerUnitFaceWidth",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def stiffness_per_unit_face_width(
            self: "StiffnessPerUnitFaceWidth._Cast_StiffnessPerUnitFaceWidth",
        ) -> "StiffnessPerUnitFaceWidth":
            return self._parent

        def __getattr__(
            self: "StiffnessPerUnitFaceWidth._Cast_StiffnessPerUnitFaceWidth", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StiffnessPerUnitFaceWidth.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StiffnessPerUnitFaceWidth._Cast_StiffnessPerUnitFaceWidth":
        return self._Cast_StiffnessPerUnitFaceWidth(self)
