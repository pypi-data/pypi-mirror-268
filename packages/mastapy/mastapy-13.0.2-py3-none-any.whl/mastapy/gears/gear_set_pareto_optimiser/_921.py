"""MicroGeometryDesignSpaceSearchChartInformation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.gear_set_pareto_optimiser import _907
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CHART_INFORMATION = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "MicroGeometryDesignSpaceSearchChartInformation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import _919


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryDesignSpaceSearchChartInformation",)


Self = TypeVar("Self", bound="MicroGeometryDesignSpaceSearchChartInformation")


class MicroGeometryDesignSpaceSearchChartInformation(
    _907.ChartInfoBase[
        "_863.CylindricalGearSetLoadDistributionAnalysis",
        "_920.MicroGeometryDesignSpaceSearchCandidate",
    ]
):
    """MicroGeometryDesignSpaceSearchChartInformation

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CHART_INFORMATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MicroGeometryDesignSpaceSearchChartInformation"
    )

    class _Cast_MicroGeometryDesignSpaceSearchChartInformation:
        """Special nested class for casting MicroGeometryDesignSpaceSearchChartInformation to subclasses."""

        def __init__(
            self: "MicroGeometryDesignSpaceSearchChartInformation._Cast_MicroGeometryDesignSpaceSearchChartInformation",
            parent: "MicroGeometryDesignSpaceSearchChartInformation",
        ):
            self._parent = parent

        @property
        def chart_info_base(
            self: "MicroGeometryDesignSpaceSearchChartInformation._Cast_MicroGeometryDesignSpaceSearchChartInformation",
        ) -> "_907.ChartInfoBase":
            return self._parent._cast(_907.ChartInfoBase)

        @property
        def micro_geometry_design_space_search_chart_information(
            self: "MicroGeometryDesignSpaceSearchChartInformation._Cast_MicroGeometryDesignSpaceSearchChartInformation",
        ) -> "MicroGeometryDesignSpaceSearchChartInformation":
            return self._parent

        def __getattr__(
            self: "MicroGeometryDesignSpaceSearchChartInformation._Cast_MicroGeometryDesignSpaceSearchChartInformation",
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
        instance_to_wrap: "MicroGeometryDesignSpaceSearchChartInformation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def optimiser(self: Self) -> "_919.MicroGeometryDesignSpaceSearch":
        """mastapy.gears.gear_set_pareto_optimiser.MicroGeometryDesignSpaceSearch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Optimiser

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MicroGeometryDesignSpaceSearchChartInformation._Cast_MicroGeometryDesignSpaceSearchChartInformation":
        return self._Cast_MicroGeometryDesignSpaceSearchChartInformation(self)
