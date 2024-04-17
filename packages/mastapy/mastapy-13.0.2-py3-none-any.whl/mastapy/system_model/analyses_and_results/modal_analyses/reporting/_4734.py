"""SingleExcitationResultsModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4727
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_EXCITATION_RESULTS_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "SingleExcitationResultsModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4730


__docformat__ = "restructuredtext en"
__all__ = ("SingleExcitationResultsModalAnalysis",)


Self = TypeVar("Self", bound="SingleExcitationResultsModalAnalysis")


class SingleExcitationResultsModalAnalysis(_4727.DesignEntityModalAnalysisGroupResults):
    """SingleExcitationResultsModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGLE_EXCITATION_RESULTS_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SingleExcitationResultsModalAnalysis")

    class _Cast_SingleExcitationResultsModalAnalysis:
        """Special nested class for casting SingleExcitationResultsModalAnalysis to subclasses."""

        def __init__(
            self: "SingleExcitationResultsModalAnalysis._Cast_SingleExcitationResultsModalAnalysis",
            parent: "SingleExcitationResultsModalAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_modal_analysis_group_results(
            self: "SingleExcitationResultsModalAnalysis._Cast_SingleExcitationResultsModalAnalysis",
        ) -> "_4727.DesignEntityModalAnalysisGroupResults":
            return self._parent._cast(_4727.DesignEntityModalAnalysisGroupResults)

        @property
        def single_excitation_results_modal_analysis(
            self: "SingleExcitationResultsModalAnalysis._Cast_SingleExcitationResultsModalAnalysis",
        ) -> "SingleExcitationResultsModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SingleExcitationResultsModalAnalysis._Cast_SingleExcitationResultsModalAnalysis",
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
        self: Self, instance_to_wrap: "SingleExcitationResultsModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicIndex

        if temp is None:
            return 0

        return temp

    @property
    def all_rigidly_connected_groups(
        self: Self,
    ) -> (
        "List[_4730.RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis]"
    ):
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllRigidlyConnectedGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigidly_connected_groups_with_significant_energy(
        self: Self,
    ) -> (
        "List[_4730.RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis]"
    ):
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedGroupsWithSignificantEnergy

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigidly_connected_groups_with_significant_kinetic_energy(
        self: Self,
    ) -> (
        "List[_4730.RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis]"
    ):
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedGroupsWithSignificantKineticEnergy

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigidly_connected_groups_with_significant_strain_energy(
        self: Self,
    ) -> (
        "List[_4730.RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis]"
    ):
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedGroupsWithSignificantStrainEnergy

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SingleExcitationResultsModalAnalysis._Cast_SingleExcitationResultsModalAnalysis":
        return self._Cast_SingleExcitationResultsModalAnalysis(self)
