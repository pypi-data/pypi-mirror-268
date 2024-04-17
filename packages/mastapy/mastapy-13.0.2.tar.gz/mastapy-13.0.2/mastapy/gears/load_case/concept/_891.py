"""ConceptGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.load_case import _876
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Concept", "ConceptGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearLoadCase",)


Self = TypeVar("Self", bound="ConceptGearLoadCase")


class ConceptGearLoadCase(_876.GearLoadCaseBase):
    """ConceptGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearLoadCase")

    class _Cast_ConceptGearLoadCase:
        """Special nested class for casting ConceptGearLoadCase to subclasses."""

        def __init__(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
            parent: "ConceptGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_load_case_base(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_876.GearLoadCaseBase":
            return self._parent._cast(_876.GearLoadCaseBase)

        @property
        def gear_design_analysis(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def concept_gear_load_case(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "ConceptGearLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConceptGearLoadCase._Cast_ConceptGearLoadCase":
        return self._Cast_ConceptGearLoadCase(self)
