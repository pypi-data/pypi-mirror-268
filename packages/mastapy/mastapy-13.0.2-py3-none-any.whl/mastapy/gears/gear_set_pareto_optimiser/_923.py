"""MicroGeometryGearSetDesignSpaceSearch"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_set_pareto_optimiser import _919
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_MICRO_GEOMETRY_GEAR_SET_DESIGN_SPACE_SEARCH = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser", "MicroGeometryGearSetDesignSpaceSearch"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import _909


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryGearSetDesignSpaceSearch",)


Self = TypeVar("Self", bound="MicroGeometryGearSetDesignSpaceSearch")


class MicroGeometryGearSetDesignSpaceSearch(_919.MicroGeometryDesignSpaceSearch):
    """MicroGeometryGearSetDesignSpaceSearch

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_GEAR_SET_DESIGN_SPACE_SEARCH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MicroGeometryGearSetDesignSpaceSearch"
    )

    class _Cast_MicroGeometryGearSetDesignSpaceSearch:
        """Special nested class for casting MicroGeometryGearSetDesignSpaceSearch to subclasses."""

        def __init__(
            self: "MicroGeometryGearSetDesignSpaceSearch._Cast_MicroGeometryGearSetDesignSpaceSearch",
            parent: "MicroGeometryGearSetDesignSpaceSearch",
        ):
            self._parent = parent

        @property
        def micro_geometry_design_space_search(
            self: "MicroGeometryGearSetDesignSpaceSearch._Cast_MicroGeometryGearSetDesignSpaceSearch",
        ) -> "_919.MicroGeometryDesignSpaceSearch":
            return self._parent._cast(_919.MicroGeometryDesignSpaceSearch)

        @property
        def design_space_search_base(
            self: "MicroGeometryGearSetDesignSpaceSearch._Cast_MicroGeometryGearSetDesignSpaceSearch",
        ) -> "_909.DesignSpaceSearchBase":
            pass

            from mastapy.gears.gear_set_pareto_optimiser import _909

            return self._parent._cast(_909.DesignSpaceSearchBase)

        @property
        def micro_geometry_gear_set_design_space_search(
            self: "MicroGeometryGearSetDesignSpaceSearch._Cast_MicroGeometryGearSetDesignSpaceSearch",
        ) -> "MicroGeometryGearSetDesignSpaceSearch":
            return self._parent

        def __getattr__(
            self: "MicroGeometryGearSetDesignSpaceSearch._Cast_MicroGeometryGearSetDesignSpaceSearch",
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
        self: Self, instance_to_wrap: "MicroGeometryGearSetDesignSpaceSearch.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_space_search_strategy(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignSpaceSearchStrategy.SelectedItemName

        if temp is None:
            return ""

        return temp

    @design_space_search_strategy.setter
    @enforce_parameter_types
    def design_space_search_strategy(self: Self, value: "str"):
        self.wrapped.DesignSpaceSearchStrategy.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def design_space_search_strategy_duty_cycle(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignSpaceSearchStrategyDutyCycle.SelectedItemName

        if temp is None:
            return ""

        return temp

    @design_space_search_strategy_duty_cycle.setter
    @enforce_parameter_types
    def design_space_search_strategy_duty_cycle(self: Self, value: "str"):
        self.wrapped.DesignSpaceSearchStrategyDutyCycle.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def cast_to(
        self: Self,
    ) -> "MicroGeometryGearSetDesignSpaceSearch._Cast_MicroGeometryGearSetDesignSpaceSearch":
        return self._Cast_MicroGeometryGearSetDesignSpaceSearch(self)
