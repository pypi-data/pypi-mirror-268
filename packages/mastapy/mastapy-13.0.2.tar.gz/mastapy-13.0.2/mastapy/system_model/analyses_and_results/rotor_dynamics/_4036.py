"""ShaftForcedComplexShape"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.rotor_dynamics import _4035
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_FORCED_COMPLEX_SHAPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics",
    "ShaftForcedComplexShape",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftForcedComplexShape",)


Self = TypeVar("Self", bound="ShaftForcedComplexShape")


class ShaftForcedComplexShape(
    _4035.ShaftComplexShape["_1677.LengthVeryShort", "_1622.AngleSmall"]
):
    """ShaftForcedComplexShape

    This is a mastapy class.
    """

    TYPE = _SHAFT_FORCED_COMPLEX_SHAPE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftForcedComplexShape")

    class _Cast_ShaftForcedComplexShape:
        """Special nested class for casting ShaftForcedComplexShape to subclasses."""

        def __init__(
            self: "ShaftForcedComplexShape._Cast_ShaftForcedComplexShape",
            parent: "ShaftForcedComplexShape",
        ):
            self._parent = parent

        @property
        def shaft_complex_shape(
            self: "ShaftForcedComplexShape._Cast_ShaftForcedComplexShape",
        ) -> "_4035.ShaftComplexShape":
            return self._parent._cast(_4035.ShaftComplexShape)

        @property
        def shaft_forced_complex_shape(
            self: "ShaftForcedComplexShape._Cast_ShaftForcedComplexShape",
        ) -> "ShaftForcedComplexShape":
            return self._parent

        def __getattr__(
            self: "ShaftForcedComplexShape._Cast_ShaftForcedComplexShape", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftForcedComplexShape.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftForcedComplexShape._Cast_ShaftForcedComplexShape":
        return self._Cast_ShaftForcedComplexShape(self)
