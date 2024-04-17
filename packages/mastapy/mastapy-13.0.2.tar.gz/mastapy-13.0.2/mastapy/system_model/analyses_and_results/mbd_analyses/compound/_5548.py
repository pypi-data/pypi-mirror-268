"""BevelDifferentialGearCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5553
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5551,
        _5552,
        _5541,
        _5569,
        _5595,
        _5614,
        _5562,
        _5616,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundMultibodyDynamicsAnalysis")


class BevelDifferentialGearCompoundMultibodyDynamicsAnalysis(
    _5553.BevelGearCompoundMultibodyDynamicsAnalysis
):
    """BevelDifferentialGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
            parent: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5553.BevelGearCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5553.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5541.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(
                _5541.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5569.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(
                _5569.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5595.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5595,
            )

            return self._parent._cast(_5595.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5614.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(
                _5614.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(_5562.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5551.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(
                _5551.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5552.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5552,
            )

            return self._parent._cast(
                _5552.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
        ) -> "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2522.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5398.BevelDifferentialGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5398.BevelDifferentialGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BevelDifferentialGearCompoundMultibodyDynamicsAnalysis(self)
