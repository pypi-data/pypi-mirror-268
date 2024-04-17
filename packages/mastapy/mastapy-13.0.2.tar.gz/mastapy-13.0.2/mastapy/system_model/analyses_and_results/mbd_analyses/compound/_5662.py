"""WormGearSetCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "WormGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2559
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5527
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5660,
        _5661,
        _5635,
        _5537,
        _5616,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="WormGearSetCompoundMultibodyDynamicsAnalysis")


class WormGearSetCompoundMultibodyDynamicsAnalysis(
    _5597.GearSetCompoundMultibodyDynamicsAnalysis
):
    """WormGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearSetCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_WormGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting WormGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "WormGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5597.GearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5597.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5635.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5537.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5537,
            )

            return self._parent._cast(
                _5537.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "WormGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "WormGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2559.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2559.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5527.WormGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.WormGearSetMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gears_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5660.WormGearCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5661.WormGearMeshCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearMeshCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5527.WormGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.WormGearSetMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetCompoundMultibodyDynamicsAnalysis._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_WormGearSetCompoundMultibodyDynamicsAnalysis(self)
