"""WormGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.load_case import _876
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Worm", "WormGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("WormGearLoadCase",)


Self = TypeVar("Self", bound="WormGearLoadCase")


class WormGearLoadCase(_876.GearLoadCaseBase):
    """WormGearLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearLoadCase")

    class _Cast_WormGearLoadCase:
        """Special nested class for casting WormGearLoadCase to subclasses."""

        def __init__(
            self: "WormGearLoadCase._Cast_WormGearLoadCase", parent: "WormGearLoadCase"
        ):
            self._parent = parent

        @property
        def gear_load_case_base(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_876.GearLoadCaseBase":
            return self._parent._cast(_876.GearLoadCaseBase)

        @property
        def gear_design_analysis(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def worm_gear_load_case(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "WormGearLoadCase":
            return self._parent

        def __getattr__(self: "WormGearLoadCase._Cast_WormGearLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "WormGearLoadCase._Cast_WormGearLoadCase":
        return self._Cast_WormGearLoadCase(self)
