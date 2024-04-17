"""ConicalGearOptimizationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_OPTIMIZATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "ConicalGearOptimizationStrategyDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearOptimizationStrategyDatabase",)


Self = TypeVar("Self", bound="ConicalGearOptimizationStrategyDatabase")


class ConicalGearOptimizationStrategyDatabase(
    _1835.NamedDatabase["_2233.ConicalGearOptimisationStrategy"]
):
    """ConicalGearOptimizationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_OPTIMIZATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearOptimizationStrategyDatabase"
    )

    class _Cast_ConicalGearOptimizationStrategyDatabase:
        """Special nested class for casting ConicalGearOptimizationStrategyDatabase to subclasses."""

        def __init__(
            self: "ConicalGearOptimizationStrategyDatabase._Cast_ConicalGearOptimizationStrategyDatabase",
            parent: "ConicalGearOptimizationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "ConicalGearOptimizationStrategyDatabase._Cast_ConicalGearOptimizationStrategyDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "ConicalGearOptimizationStrategyDatabase._Cast_ConicalGearOptimizationStrategyDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "ConicalGearOptimizationStrategyDatabase._Cast_ConicalGearOptimizationStrategyDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def conical_gear_optimization_strategy_database(
            self: "ConicalGearOptimizationStrategyDatabase._Cast_ConicalGearOptimizationStrategyDatabase",
        ) -> "ConicalGearOptimizationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ConicalGearOptimizationStrategyDatabase._Cast_ConicalGearOptimizationStrategyDatabase",
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
        self: Self, instance_to_wrap: "ConicalGearOptimizationStrategyDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearOptimizationStrategyDatabase._Cast_ConicalGearOptimizationStrategyDatabase":
        return self._Cast_ConicalGearOptimizationStrategyDatabase(self)
