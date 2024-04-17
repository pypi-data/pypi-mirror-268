"""CylindricalPlanetGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6870
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalPlanetGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6899,
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearLoadCase",)


Self = TypeVar("Self", bound="CylindricalPlanetGearLoadCase")


class CylindricalPlanetGearLoadCase(_6870.CylindricalGearLoadCase):
    """CylindricalPlanetGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGearLoadCase")

    class _Cast_CylindricalPlanetGearLoadCase:
        """Special nested class for casting CylindricalPlanetGearLoadCase to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
            parent: "CylindricalPlanetGearLoadCase",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "_6870.CylindricalGearLoadCase":
            return self._parent._cast(_6870.CylindricalGearLoadCase)

        @property
        def gear_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "_6899.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6899

            return self._parent._cast(_6899.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "CylindricalPlanetGearLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalPlanetGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase":
        return self._Cast_CylindricalPlanetGearLoadCase(self)
