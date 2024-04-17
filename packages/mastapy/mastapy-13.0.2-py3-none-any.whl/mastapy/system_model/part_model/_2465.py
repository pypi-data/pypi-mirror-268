"""InnerBearingRaceMountingOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model import _2448
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_BEARING_RACE_MOUNTING_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "InnerBearingRaceMountingOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("InnerBearingRaceMountingOptions",)


Self = TypeVar("Self", bound="InnerBearingRaceMountingOptions")


class InnerBearingRaceMountingOptions(_2448.BearingRaceMountingOptions):
    """InnerBearingRaceMountingOptions

    This is a mastapy class.
    """

    TYPE = _INNER_BEARING_RACE_MOUNTING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InnerBearingRaceMountingOptions")

    class _Cast_InnerBearingRaceMountingOptions:
        """Special nested class for casting InnerBearingRaceMountingOptions to subclasses."""

        def __init__(
            self: "InnerBearingRaceMountingOptions._Cast_InnerBearingRaceMountingOptions",
            parent: "InnerBearingRaceMountingOptions",
        ):
            self._parent = parent

        @property
        def bearing_race_mounting_options(
            self: "InnerBearingRaceMountingOptions._Cast_InnerBearingRaceMountingOptions",
        ) -> "_2448.BearingRaceMountingOptions":
            return self._parent._cast(_2448.BearingRaceMountingOptions)

        @property
        def inner_bearing_race_mounting_options(
            self: "InnerBearingRaceMountingOptions._Cast_InnerBearingRaceMountingOptions",
        ) -> "InnerBearingRaceMountingOptions":
            return self._parent

        def __getattr__(
            self: "InnerBearingRaceMountingOptions._Cast_InnerBearingRaceMountingOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InnerBearingRaceMountingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "InnerBearingRaceMountingOptions._Cast_InnerBearingRaceMountingOptions":
        return self._Cast_InnerBearingRaceMountingOptions(self)
