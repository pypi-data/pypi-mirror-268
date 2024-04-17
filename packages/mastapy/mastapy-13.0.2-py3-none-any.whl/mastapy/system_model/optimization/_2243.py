"""OptimizationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "OptimizationStrategyDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("OptimizationStrategyDatabase",)


Self = TypeVar("Self", bound="OptimizationStrategyDatabase")


class OptimizationStrategyDatabase(
    _1835.NamedDatabase["_2236.CylindricalGearOptimisationStrategy"]
):
    """OptimizationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_STRATEGY_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OptimizationStrategyDatabase")

    class _Cast_OptimizationStrategyDatabase:
        """Special nested class for casting OptimizationStrategyDatabase to subclasses."""

        def __init__(
            self: "OptimizationStrategyDatabase._Cast_OptimizationStrategyDatabase",
            parent: "OptimizationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "OptimizationStrategyDatabase._Cast_OptimizationStrategyDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "OptimizationStrategyDatabase._Cast_OptimizationStrategyDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "OptimizationStrategyDatabase._Cast_OptimizationStrategyDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def optimization_strategy_database(
            self: "OptimizationStrategyDatabase._Cast_OptimizationStrategyDatabase",
        ) -> "OptimizationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "OptimizationStrategyDatabase._Cast_OptimizationStrategyDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OptimizationStrategyDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "OptimizationStrategyDatabase._Cast_OptimizationStrategyDatabase":
        return self._Cast_OptimizationStrategyDatabase(self)
