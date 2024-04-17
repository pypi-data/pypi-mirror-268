"""CouplingMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5497
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CouplingMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5409,
        _5415,
        _5478,
        _5503,
        _5518,
        _5384,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingMultibodyDynamicsAnalysis")


class CouplingMultibodyDynamicsAnalysis(
    _5497.SpecialisedAssemblyMultibodyDynamicsAnalysis
):
    """CouplingMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingMultibodyDynamicsAnalysis")

    class _Cast_CouplingMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
            parent: "CouplingMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_5497.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5497.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_5384.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_5409.ClutchMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ClutchMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_5415.ConceptCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_5478.PartToPartShearCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(
                _5478.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_5503.SpringDamperMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(_5503.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "_5518.TorqueConverterMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "CouplingMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CouplingMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2591.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis":
        return self._Cast_CouplingMultibodyDynamicsAnalysis(self)
