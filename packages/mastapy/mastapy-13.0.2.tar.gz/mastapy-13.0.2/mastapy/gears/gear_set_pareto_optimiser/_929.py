"""ParetoCylindricalGearSetOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _930
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CYLINDRICAL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoCylindricalGearSetOptimisationStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1559, _1547
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("ParetoCylindricalGearSetOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoCylindricalGearSetOptimisationStrategyDatabase")


class ParetoCylindricalGearSetOptimisationStrategyDatabase(
    _930.ParetoCylindricalRatingOptimisationStrategyDatabase
):
    """ParetoCylindricalGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CYLINDRICAL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase"
    )

    class _Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoCylindricalGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
            parent: "ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_930.ParetoCylindricalRatingOptimisationStrategyDatabase":
            return self._parent._cast(
                _930.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1559.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1559

            return self._parent._cast(_1559.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1547.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1547

            return self._parent._cast(_1547.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1835.NamedDatabase":
            pass

            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "ParetoCylindricalGearSetOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoCylindricalGearSetOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase":
        return self._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase(self)
