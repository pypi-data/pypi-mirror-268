"""ShaftModalComplexShapeAtSpeeds"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.rotor_dynamics import _4037
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_COMPLEX_SHAPE_AT_SPEEDS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics",
    "ShaftModalComplexShapeAtSpeeds",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.rotor_dynamics import _4035


__docformat__ = "restructuredtext en"
__all__ = ("ShaftModalComplexShapeAtSpeeds",)


Self = TypeVar("Self", bound="ShaftModalComplexShapeAtSpeeds")


class ShaftModalComplexShapeAtSpeeds(_4037.ShaftModalComplexShape):
    """ShaftModalComplexShapeAtSpeeds

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_COMPLEX_SHAPE_AT_SPEEDS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftModalComplexShapeAtSpeeds")

    class _Cast_ShaftModalComplexShapeAtSpeeds:
        """Special nested class for casting ShaftModalComplexShapeAtSpeeds to subclasses."""

        def __init__(
            self: "ShaftModalComplexShapeAtSpeeds._Cast_ShaftModalComplexShapeAtSpeeds",
            parent: "ShaftModalComplexShapeAtSpeeds",
        ):
            self._parent = parent

        @property
        def shaft_modal_complex_shape(
            self: "ShaftModalComplexShapeAtSpeeds._Cast_ShaftModalComplexShapeAtSpeeds",
        ) -> "_4037.ShaftModalComplexShape":
            return self._parent._cast(_4037.ShaftModalComplexShape)

        @property
        def shaft_complex_shape(
            self: "ShaftModalComplexShapeAtSpeeds._Cast_ShaftModalComplexShapeAtSpeeds",
        ) -> "_4035.ShaftComplexShape":
            pass

            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4035

            return self._parent._cast(_4035.ShaftComplexShape)

        @property
        def shaft_modal_complex_shape_at_speeds(
            self: "ShaftModalComplexShapeAtSpeeds._Cast_ShaftModalComplexShapeAtSpeeds",
        ) -> "ShaftModalComplexShapeAtSpeeds":
            return self._parent

        def __getattr__(
            self: "ShaftModalComplexShapeAtSpeeds._Cast_ShaftModalComplexShapeAtSpeeds",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftModalComplexShapeAtSpeeds.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftModalComplexShapeAtSpeeds._Cast_ShaftModalComplexShapeAtSpeeds":
        return self._Cast_ShaftModalComplexShapeAtSpeeds(self)
