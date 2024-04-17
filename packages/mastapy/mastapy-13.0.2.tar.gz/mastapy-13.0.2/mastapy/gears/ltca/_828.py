"""ConicalGearFilletStressResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _840
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_FILLET_STRESS_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "ConicalGearFilletStressResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearFilletStressResults",)


Self = TypeVar("Self", bound="ConicalGearFilletStressResults")


class ConicalGearFilletStressResults(_840.GearFilletNodeStressResults):
    """ConicalGearFilletStressResults

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_FILLET_STRESS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearFilletStressResults")

    class _Cast_ConicalGearFilletStressResults:
        """Special nested class for casting ConicalGearFilletStressResults to subclasses."""

        def __init__(
            self: "ConicalGearFilletStressResults._Cast_ConicalGearFilletStressResults",
            parent: "ConicalGearFilletStressResults",
        ):
            self._parent = parent

        @property
        def gear_fillet_node_stress_results(
            self: "ConicalGearFilletStressResults._Cast_ConicalGearFilletStressResults",
        ) -> "_840.GearFilletNodeStressResults":
            return self._parent._cast(_840.GearFilletNodeStressResults)

        @property
        def conical_gear_fillet_stress_results(
            self: "ConicalGearFilletStressResults._Cast_ConicalGearFilletStressResults",
        ) -> "ConicalGearFilletStressResults":
            return self._parent

        def __getattr__(
            self: "ConicalGearFilletStressResults._Cast_ConicalGearFilletStressResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearFilletStressResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearFilletStressResults._Cast_ConicalGearFilletStressResults":
        return self._Cast_ConicalGearFilletStressResults(self)
