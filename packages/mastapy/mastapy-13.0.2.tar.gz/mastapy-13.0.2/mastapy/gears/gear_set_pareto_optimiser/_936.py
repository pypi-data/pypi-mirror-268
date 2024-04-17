"""ParetoOptimiserChartInformation"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _907
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISER_CHART_INFORMATION = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser", "ParetoOptimiserChartInformation"
)


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimiserChartInformation",)


Self = TypeVar("Self", bound="ParetoOptimiserChartInformation")


class ParetoOptimiserChartInformation(
    _907.ChartInfoBase["_358.AbstractGearSetRating", "_914.GearSetOptimiserCandidate"]
):
    """ParetoOptimiserChartInformation

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISER_CHART_INFORMATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimiserChartInformation")

    class _Cast_ParetoOptimiserChartInformation:
        """Special nested class for casting ParetoOptimiserChartInformation to subclasses."""

        def __init__(
            self: "ParetoOptimiserChartInformation._Cast_ParetoOptimiserChartInformation",
            parent: "ParetoOptimiserChartInformation",
        ):
            self._parent = parent

        @property
        def chart_info_base(
            self: "ParetoOptimiserChartInformation._Cast_ParetoOptimiserChartInformation",
        ) -> "_907.ChartInfoBase":
            return self._parent._cast(_907.ChartInfoBase)

        @property
        def pareto_optimiser_chart_information(
            self: "ParetoOptimiserChartInformation._Cast_ParetoOptimiserChartInformation",
        ) -> "ParetoOptimiserChartInformation":
            return self._parent

        def __getattr__(
            self: "ParetoOptimiserChartInformation._Cast_ParetoOptimiserChartInformation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParetoOptimiserChartInformation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoOptimiserChartInformation._Cast_ParetoOptimiserChartInformation":
        return self._Cast_ParetoOptimiserChartInformation(self)
