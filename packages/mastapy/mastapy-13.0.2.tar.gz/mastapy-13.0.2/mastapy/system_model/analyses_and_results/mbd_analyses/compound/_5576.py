"""CouplingHalfCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5614
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CouplingHalfCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5425
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5560,
        _5565,
        _5579,
        _5619,
        _5625,
        _5629,
        _5641,
        _5651,
        _5652,
        _5653,
        _5656,
        _5657,
        _5562,
        _5616,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundMultibodyDynamicsAnalysis")


class CouplingHalfCompoundMultibodyDynamicsAnalysis(
    _5614.MountableComponentCompoundMultibodyDynamicsAnalysis
):
    """CouplingHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingHalfCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
            parent: "CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5614.MountableComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5614.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(_5562.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5560.ClutchHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(_5560.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5565.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(
                _5565.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5579.CVTPulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5579,
            )

            return self._parent._cast(_5579.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5619.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(
                _5619.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5625.PulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5625,
            )

            return self._parent._cast(_5625.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.RollingRingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5641.SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5651.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5652.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5652,
            )

            return self._parent._cast(
                _5652.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5653.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5656.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5657.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "CouplingHalfCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CouplingHalfCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5425.CouplingHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CouplingHalfMultibodyDynamicsAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5425.CouplingHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CouplingHalfMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis(self)
