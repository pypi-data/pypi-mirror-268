"""CylindricalGearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5447
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CylindricalGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.static_loads import _6870
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5437,
        _5472,
        _5412,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearMultibodyDynamicsAnalysis")


class CylindricalGearMultibodyDynamicsAnalysis(_5447.GearMultibodyDynamicsAnalysis):
    """CylindricalGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMultibodyDynamicsAnalysis"
    )

    class _Cast_CylindricalGearMultibodyDynamicsAnalysis:
        """Special nested class for casting CylindricalGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
            parent: "CylindricalGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_multibody_dynamics_analysis(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_5447.GearMultibodyDynamicsAnalysis":
            return self._parent._cast(_5447.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_5472.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_5412.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "_5437.CylindricalPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(
                _5437.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
        ) -> "CylindricalGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2532.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6870.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMultibodyDynamicsAnalysis._Cast_CylindricalGearMultibodyDynamicsAnalysis":
        return self._Cast_CylindricalGearMultibodyDynamicsAnalysis(self)
