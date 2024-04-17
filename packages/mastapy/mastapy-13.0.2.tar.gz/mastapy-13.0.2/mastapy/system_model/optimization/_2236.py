"""CylindricalGearOptimisationStrategy"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.optimization import _2241
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_OPTIMISATION_STRATEGY = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "CylindricalGearOptimisationStrategy"
)

if TYPE_CHECKING:
    from mastapy.system_model.optimization import _2242
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearOptimisationStrategy",)


Self = TypeVar("Self", bound="CylindricalGearOptimisationStrategy")


class CylindricalGearOptimisationStrategy(
    _2241.OptimizationStrategy["_2237.CylindricalGearOptimizationStep"]
):
    """CylindricalGearOptimisationStrategy

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_OPTIMISATION_STRATEGY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearOptimisationStrategy")

    class _Cast_CylindricalGearOptimisationStrategy:
        """Special nested class for casting CylindricalGearOptimisationStrategy to subclasses."""

        def __init__(
            self: "CylindricalGearOptimisationStrategy._Cast_CylindricalGearOptimisationStrategy",
            parent: "CylindricalGearOptimisationStrategy",
        ):
            self._parent = parent

        @property
        def optimization_strategy(
            self: "CylindricalGearOptimisationStrategy._Cast_CylindricalGearOptimisationStrategy",
        ) -> "_2241.OptimizationStrategy":
            return self._parent._cast(_2241.OptimizationStrategy)

        @property
        def optimization_strategy_base(
            self: "CylindricalGearOptimisationStrategy._Cast_CylindricalGearOptimisationStrategy",
        ) -> "_2242.OptimizationStrategyBase":
            from mastapy.system_model.optimization import _2242

            return self._parent._cast(_2242.OptimizationStrategyBase)

        @property
        def named_database_item(
            self: "CylindricalGearOptimisationStrategy._Cast_CylindricalGearOptimisationStrategy",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def cylindrical_gear_optimisation_strategy(
            self: "CylindricalGearOptimisationStrategy._Cast_CylindricalGearOptimisationStrategy",
        ) -> "CylindricalGearOptimisationStrategy":
            return self._parent

        def __getattr__(
            self: "CylindricalGearOptimisationStrategy._Cast_CylindricalGearOptimisationStrategy",
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
        self: Self, instance_to_wrap: "CylindricalGearOptimisationStrategy.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearOptimisationStrategy._Cast_CylindricalGearOptimisationStrategy"
    ):
        return self._Cast_CylindricalGearOptimisationStrategy(self)
