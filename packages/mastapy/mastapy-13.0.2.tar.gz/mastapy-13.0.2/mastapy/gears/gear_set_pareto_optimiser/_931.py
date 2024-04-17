"""ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _933
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_FACE_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1559, _1547
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase")


class ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase(
    _933.ParetoFaceRatingOptimisationStrategyDatabase
):
    """ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_FACE_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
    )

    class _Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase:
        """Special nested class for casting ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
            parent: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_933.ParetoFaceRatingOptimisationStrategyDatabase":
            return self._parent._cast(_933.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1559.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1559

            return self._parent._cast(_1559.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1547.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1547

            return self._parent._cast(_1547.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1835.NamedDatabase":
            pass

            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
        return self._Cast_ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase(self)
