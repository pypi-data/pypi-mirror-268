"""ConicalMeshedGearLoadDistributionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESHED_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalMeshedGearLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.cylindrical import _1219, _1218
    from mastapy.gears.ltca.conical import _870


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshedGearLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="ConicalMeshedGearLoadDistributionAnalysis")


class ConicalMeshedGearLoadDistributionAnalysis(_0.APIBase):
    """ConicalMeshedGearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESHED_GEAR_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalMeshedGearLoadDistributionAnalysis"
    )

    class _Cast_ConicalMeshedGearLoadDistributionAnalysis:
        """Special nested class for casting ConicalMeshedGearLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "ConicalMeshedGearLoadDistributionAnalysis._Cast_ConicalMeshedGearLoadDistributionAnalysis",
            parent: "ConicalMeshedGearLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def conical_meshed_gear_load_distribution_analysis(
            self: "ConicalMeshedGearLoadDistributionAnalysis._Cast_ConicalMeshedGearLoadDistributionAnalysis",
        ) -> "ConicalMeshedGearLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalMeshedGearLoadDistributionAnalysis._Cast_ConicalMeshedGearLoadDistributionAnalysis",
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
        self: Self, instance_to_wrap: "ConicalMeshedGearLoadDistributionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def estimated_gear_stiffness_from_fe_model(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedGearStiffnessFromFEModel

        if temp is None:
            return 0.0

        return temp

    @property
    def max_tensile_principal_root_stress_compression_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxTensilePrincipalRootStressCompressionSide

        if temp is None:
            return 0.0

        return temp

    @property
    def max_tensile_principal_root_stress_tension_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxTensilePrincipalRootStressTensionSide

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_compression_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumVonMisesRootStressCompressionSide

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_tension_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumVonMisesRootStressTensionSide

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_charts(self: Self) -> "_1219.GearLTCAContactCharts":
        """mastapy.gears.cylindrical.GearLTCAContactCharts

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactCharts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_charts_as_text_file(
        self: Self,
    ) -> "_1218.GearLTCAContactChartDataAsTextFile":
        """mastapy.gears.cylindrical.GearLTCAContactChartDataAsTextFile

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartsAsTextFile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_load_distribution_analysis(
        self: Self,
    ) -> "_870.ConicalGearLoadDistributionAnalysis":
        """mastapy.gears.ltca.conical.ConicalGearLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearLoadDistributionAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshedGearLoadDistributionAnalysis._Cast_ConicalMeshedGearLoadDistributionAnalysis":
        return self._Cast_ConicalMeshedGearLoadDistributionAnalysis(self)
