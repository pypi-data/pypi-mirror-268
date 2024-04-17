"""DesignSpaceSearchStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "DesignSpaceSearchStrategyDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import (
        _922,
        _924,
        _925,
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
    from mastapy.math_utility.optimisation import _1559
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("DesignSpaceSearchStrategyDatabase",)


Self = TypeVar("Self", bound="DesignSpaceSearchStrategyDatabase")


class DesignSpaceSearchStrategyDatabase(
    _1835.NamedDatabase["_1556.ParetoOptimisationStrategy"]
):
    """DesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _DESIGN_SPACE_SEARCH_STRATEGY_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignSpaceSearchStrategyDatabase")

    class _Cast_DesignSpaceSearchStrategyDatabase:
        """Special nested class for casting DesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
            parent: "DesignSpaceSearchStrategyDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_922.MicroGeometryDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _922

            return self._parent._cast(
                _922.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_924.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _924

            return self._parent._cast(
                _924.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_925.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_927.ParetoConicalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(
                _927.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_928.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_929.ParetoCylindricalGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_930.ParetoCylindricalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(
                _930.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_931.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_932.ParetoFaceGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _932

            return self._parent._cast(
                _932.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_933.ParetoFaceRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _933

            return self._parent._cast(_933.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_934.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_935.ParetoHypoidGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_937.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _937

            return self._parent._cast(
                _937.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_938.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _938

            return self._parent._cast(
                _938.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_939.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _939

            return self._parent._cast(
                _939.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_940.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _940

            return self._parent._cast(
                _940.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "_1559.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1559

            return self._parent._cast(_1559.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
        ) -> "DesignSpaceSearchStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase",
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
        self: Self, instance_to_wrap: "DesignSpaceSearchStrategyDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase":
        return self._Cast_DesignSpaceSearchStrategyDatabase(self)
