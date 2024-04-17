"""CylindricalGearRootFilletStressResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _848
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ROOT_FILLET_STRESS_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "CylindricalGearRootFilletStressResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearRootFilletStressResults",)


Self = TypeVar("Self", bound="CylindricalGearRootFilletStressResults")


class CylindricalGearRootFilletStressResults(_848.GearRootFilletStressResults):
    """CylindricalGearRootFilletStressResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ROOT_FILLET_STRESS_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearRootFilletStressResults"
    )

    class _Cast_CylindricalGearRootFilletStressResults:
        """Special nested class for casting CylindricalGearRootFilletStressResults to subclasses."""

        def __init__(
            self: "CylindricalGearRootFilletStressResults._Cast_CylindricalGearRootFilletStressResults",
            parent: "CylindricalGearRootFilletStressResults",
        ):
            self._parent = parent

        @property
        def gear_root_fillet_stress_results(
            self: "CylindricalGearRootFilletStressResults._Cast_CylindricalGearRootFilletStressResults",
        ) -> "_848.GearRootFilletStressResults":
            return self._parent._cast(_848.GearRootFilletStressResults)

        @property
        def cylindrical_gear_root_fillet_stress_results(
            self: "CylindricalGearRootFilletStressResults._Cast_CylindricalGearRootFilletStressResults",
        ) -> "CylindricalGearRootFilletStressResults":
            return self._parent

        def __getattr__(
            self: "CylindricalGearRootFilletStressResults._Cast_CylindricalGearRootFilletStressResults",
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
        self: Self, instance_to_wrap: "CylindricalGearRootFilletStressResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearRootFilletStressResults._Cast_CylindricalGearRootFilletStressResults":
        return self._Cast_CylindricalGearRootFilletStressResults(self)
