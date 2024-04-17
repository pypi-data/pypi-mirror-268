"""CylindricalGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.load_case import _876
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Cylindrical", "CylindricalGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearLoadCase",)


Self = TypeVar("Self", bound="CylindricalGearLoadCase")


class CylindricalGearLoadCase(_876.GearLoadCaseBase):
    """CylindricalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearLoadCase")

    class _Cast_CylindricalGearLoadCase:
        """Special nested class for casting CylindricalGearLoadCase to subclasses."""

        def __init__(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
            parent: "CylindricalGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_load_case_base(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_876.GearLoadCaseBase":
            return self._parent._cast(_876.GearLoadCaseBase)

        @property
        def gear_design_analysis(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_gear_load_case(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase",
        ) -> "CylindricalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reversed_bending_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ReversedBendingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @reversed_bending_factor.setter
    @enforce_parameter_types
    def reversed_bending_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ReversedBendingFactor = value

    @property
    def cast_to(self: Self) -> "CylindricalGearLoadCase._Cast_CylindricalGearLoadCase":
        return self._Cast_CylindricalGearLoadCase(self)
