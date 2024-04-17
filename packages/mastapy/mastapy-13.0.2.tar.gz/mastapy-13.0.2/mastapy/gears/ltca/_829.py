"""ConicalGearRootFilletStressResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _848
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_ROOT_FILLET_STRESS_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "ConicalGearRootFilletStressResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearRootFilletStressResults",)


Self = TypeVar("Self", bound="ConicalGearRootFilletStressResults")


class ConicalGearRootFilletStressResults(_848.GearRootFilletStressResults):
    """ConicalGearRootFilletStressResults

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_ROOT_FILLET_STRESS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearRootFilletStressResults")

    class _Cast_ConicalGearRootFilletStressResults:
        """Special nested class for casting ConicalGearRootFilletStressResults to subclasses."""

        def __init__(
            self: "ConicalGearRootFilletStressResults._Cast_ConicalGearRootFilletStressResults",
            parent: "ConicalGearRootFilletStressResults",
        ):
            self._parent = parent

        @property
        def gear_root_fillet_stress_results(
            self: "ConicalGearRootFilletStressResults._Cast_ConicalGearRootFilletStressResults",
        ) -> "_848.GearRootFilletStressResults":
            return self._parent._cast(_848.GearRootFilletStressResults)

        @property
        def conical_gear_root_fillet_stress_results(
            self: "ConicalGearRootFilletStressResults._Cast_ConicalGearRootFilletStressResults",
        ) -> "ConicalGearRootFilletStressResults":
            return self._parent

        def __getattr__(
            self: "ConicalGearRootFilletStressResults._Cast_ConicalGearRootFilletStressResults",
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
        self: Self, instance_to_wrap: "ConicalGearRootFilletStressResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearRootFilletStressResults._Cast_ConicalGearRootFilletStressResults":
        return self._Cast_ConicalGearRootFilletStressResults(self)
