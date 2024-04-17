"""PlanetaryGearSetCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5586
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5480
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5597,
        _5635,
        _5537,
        _5616,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundMultibodyDynamicsAnalysis")


class PlanetaryGearSetCompoundMultibodyDynamicsAnalysis(
    _5586.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
):
    """PlanetaryGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5586.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5586.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5597.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(_5597.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5635.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5537.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5537,
            )

            return self._parent._cast(
                _5537.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5480.PlanetaryGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PlanetaryGearSetMultibodyDynamicsAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5480.PlanetaryGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PlanetaryGearSetMultibodyDynamicsAnalysis]

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
    ) -> "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_PlanetaryGearSetCompoundMultibodyDynamicsAnalysis(self)
