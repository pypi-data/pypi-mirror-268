"""ParetoOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility.optimisation import _1547
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationStrategyDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import (
        _927,
        _928,
        _929,
        _930,
        _931,
        _932,
        _933,
        _934,
        _935,
        _937,
        _938,
        _939,
        _940,
    )
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoOptimisationStrategyDatabase")


class ParetoOptimisationStrategyDatabase(_1547.DesignSpaceSearchStrategyDatabase):
    """ParetoOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimisationStrategyDatabase")

    class _Cast_ParetoOptimisationStrategyDatabase:
        """Special nested class for casting ParetoOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
            parent: "ParetoOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def design_space_search_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_1547.DesignSpaceSearchStrategyDatabase":
            return self._parent._cast(_1547.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_1835.NamedDatabase":
            pass

            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_927.ParetoConicalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(
                _927.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_928.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_929.ParetoCylindricalGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_930.ParetoCylindricalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(
                _930.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_931.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_932.ParetoFaceGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _932

            return self._parent._cast(
                _932.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_933.ParetoFaceRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _933

            return self._parent._cast(_933.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_934.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_935.ParetoHypoidGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_937.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _937

            return self._parent._cast(
                _937.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_938.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _938

            return self._parent._cast(
                _938.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_939.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _939

            return self._parent._cast(
                _939.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "_940.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _940

            return self._parent._cast(
                _940.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
        ) -> "ParetoOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase",
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
        self: Self, instance_to_wrap: "ParetoOptimisationStrategyDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase":
        return self._Cast_ParetoOptimisationStrategyDatabase(self)
