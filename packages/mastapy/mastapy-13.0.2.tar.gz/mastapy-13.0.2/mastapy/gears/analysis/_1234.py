"""GearSetImplementationAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.analysis import _1235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7567
    from mastapy.gears.manufacturing.cylindrical import _624
    from mastapy.gears.manufacturing.bevel import _793
    from mastapy.gears.ltca import _849
    from mastapy.gears.ltca.cylindrical import _863, _865
    from mastapy.gears.ltca.conical import _871
    from mastapy.gears.analysis import _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("GearSetImplementationAnalysis",)


Self = TypeVar("Self", bound="GearSetImplementationAnalysis")


class GearSetImplementationAnalysis(_1235.GearSetImplementationAnalysisAbstract):
    """GearSetImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetImplementationAnalysis")

    class _Cast_GearSetImplementationAnalysis:
        """Special nested class for casting GearSetImplementationAnalysis to subclasses."""

        def __init__(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
            parent: "GearSetImplementationAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_1235.GearSetImplementationAnalysisAbstract":
            return self._parent._cast(_1235.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_624.CylindricalManufacturedGearSetLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _624

            return self._parent._cast(_624.CylindricalManufacturedGearSetLoadCase)

        @property
        def conical_set_manufacturing_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_793.ConicalSetManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _793

            return self._parent._cast(_793.ConicalSetManufacturingAnalysis)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_849.GearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca import _849

            return self._parent._cast(_849.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _863

            return self._parent._cast(_863.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_865.FaceGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _865

            return self._parent._cast(_865.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_871.ConicalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _871

            return self._parent._cast(_871.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_implementation_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "GearSetImplementationAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetImplementationAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def valid_results_ready(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ValidResultsReady

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def perform_analysis(self: Self, run_all_planetary_meshes: "bool" = True):
        """Method does not return.

        Args:
            run_all_planetary_meshes (bool, optional)
        """
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformAnalysis(
            run_all_planetary_meshes if run_all_planetary_meshes else False
        )

    @enforce_parameter_types
    def perform_analysis_with_progress(
        self: Self, run_all_planetary_meshes: "bool", progress: "_7567.TaskProgress"
    ):
        """Method does not return.

        Args:
            run_all_planetary_meshes (bool)
            progress (mastapy.TaskProgress)
        """
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformAnalysisWithProgress(
            run_all_planetary_meshes if run_all_planetary_meshes else False,
            progress.wrapped if progress else None,
        )

    @enforce_parameter_types
    def results_ready_for(
        self: Self, run_all_planetary_meshes: "bool" = True
    ) -> "bool":
        """bool

        Args:
            run_all_planetary_meshes (bool, optional)
        """
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        method_result = self.wrapped.ResultsReadyFor(
            run_all_planetary_meshes if run_all_planetary_meshes else False
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis":
        return self._Cast_GearSetImplementationAnalysis(self)
