"""ParetoStraightBevelGearSetOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _927
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_STRAIGHT_BEVEL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoStraightBevelGearSetOptimisationStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1559, _1547
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("ParetoStraightBevelGearSetOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoStraightBevelGearSetOptimisationStrategyDatabase")


class ParetoStraightBevelGearSetOptimisationStrategyDatabase(
    _927.ParetoConicalRatingOptimisationStrategyDatabase
):
    """ParetoStraightBevelGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_STRAIGHT_BEVEL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
    )

    class _Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoStraightBevelGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
            parent: "ParetoStraightBevelGearSetOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
        ) -> "_927.ParetoConicalRatingOptimisationStrategyDatabase":
            return self._parent._cast(
                _927.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1559.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1559

            return self._parent._cast(_1559.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1547.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1547

            return self._parent._cast(_1547.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1835.NamedDatabase":
            pass

            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
        ) -> "ParetoStraightBevelGearSetOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase",
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
        self: Self,
        instance_to_wrap: "ParetoStraightBevelGearSetOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase":
        return self._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase(self)
