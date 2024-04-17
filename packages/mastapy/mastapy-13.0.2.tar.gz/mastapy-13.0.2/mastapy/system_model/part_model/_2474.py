"""OuterBearingRaceMountingOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model import _2448
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_BEARING_RACE_MOUNTING_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "OuterBearingRaceMountingOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("OuterBearingRaceMountingOptions",)


Self = TypeVar("Self", bound="OuterBearingRaceMountingOptions")


class OuterBearingRaceMountingOptions(_2448.BearingRaceMountingOptions):
    """OuterBearingRaceMountingOptions

    This is a mastapy class.
    """

    TYPE = _OUTER_BEARING_RACE_MOUNTING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OuterBearingRaceMountingOptions")

    class _Cast_OuterBearingRaceMountingOptions:
        """Special nested class for casting OuterBearingRaceMountingOptions to subclasses."""

        def __init__(
            self: "OuterBearingRaceMountingOptions._Cast_OuterBearingRaceMountingOptions",
            parent: "OuterBearingRaceMountingOptions",
        ):
            self._parent = parent

        @property
        def bearing_race_mounting_options(
            self: "OuterBearingRaceMountingOptions._Cast_OuterBearingRaceMountingOptions",
        ) -> "_2448.BearingRaceMountingOptions":
            return self._parent._cast(_2448.BearingRaceMountingOptions)

        @property
        def outer_bearing_race_mounting_options(
            self: "OuterBearingRaceMountingOptions._Cast_OuterBearingRaceMountingOptions",
        ) -> "OuterBearingRaceMountingOptions":
            return self._parent

        def __getattr__(
            self: "OuterBearingRaceMountingOptions._Cast_OuterBearingRaceMountingOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OuterBearingRaceMountingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "OuterBearingRaceMountingOptions._Cast_OuterBearingRaceMountingOptions":
        return self._Cast_OuterBearingRaceMountingOptions(self)
