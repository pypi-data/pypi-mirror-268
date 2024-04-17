"""CylindricalPlanetGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CylindricalPlanetGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6345,
        _6364,
        _6310,
        _6366,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearDynamicAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearDynamicAnalysis")


class CylindricalPlanetGearDynamicAnalysis(_6332.CylindricalGearDynamicAnalysis):
    """CylindricalPlanetGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGearDynamicAnalysis")

    class _Cast_CylindricalPlanetGearDynamicAnalysis:
        """Special nested class for casting CylindricalPlanetGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
            parent: "CylindricalPlanetGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6332.CylindricalGearDynamicAnalysis":
            return self._parent._cast(_6332.CylindricalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6345.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6364.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6310.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
        ) -> "CylindricalPlanetGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearDynamicAnalysis._Cast_CylindricalPlanetGearDynamicAnalysis":
        return self._Cast_CylindricalPlanetGearDynamicAnalysis(self)
