"""CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7247,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7056,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7170,
        _7175,
        _7229,
        _7251,
        _7266,
        _7149,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class CouplingCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """CouplingCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CouplingCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7247.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7170.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7170,
            )

            return self._parent._cast(
                _7170.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7175.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7175,
            )

            return self._parent._cast(
                _7175.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7229.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7251.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7251,
            )

            return self._parent._cast(
                _7251.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7266.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7266,
            )

            return self._parent._cast(
                _7266.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7056.CouplingAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CouplingAdvancedTimeSteppingAnalysisForModulation]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7056.CouplingAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CouplingAdvancedTimeSteppingAnalysisForModulation]

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
    def cast_to(
        self: Self,
    ) -> "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
