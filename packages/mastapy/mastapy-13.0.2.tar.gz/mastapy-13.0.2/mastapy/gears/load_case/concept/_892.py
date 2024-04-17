"""ConceptGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.load_case import _877
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Concept", "ConceptGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetLoadCase",)


Self = TypeVar("Self", bound="ConceptGearSetLoadCase")


class ConceptGearSetLoadCase(_877.GearSetLoadCaseBase):
    """ConceptGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetLoadCase")

    class _Cast_ConceptGearSetLoadCase:
        """Special nested class for casting ConceptGearSetLoadCase to subclasses."""

        def __init__(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
            parent: "ConceptGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case_base(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_877.GearSetLoadCaseBase":
            return self._parent._cast(_877.GearSetLoadCaseBase)

        @property
        def gear_set_design_analysis(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def concept_gear_set_load_case(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "ConceptGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase":
        return self._Cast_ConceptGearSetLoadCase(self)
