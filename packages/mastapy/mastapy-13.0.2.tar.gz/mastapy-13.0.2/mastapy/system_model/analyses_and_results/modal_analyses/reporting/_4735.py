"""SingleModeResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4727
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_MODE_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "SingleModeResults",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4731


__docformat__ = "restructuredtext en"
__all__ = ("SingleModeResults",)


Self = TypeVar("Self", bound="SingleModeResults")


class SingleModeResults(_4727.DesignEntityModalAnalysisGroupResults):
    """SingleModeResults

    This is a mastapy class.
    """

    TYPE = _SINGLE_MODE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SingleModeResults")

    class _Cast_SingleModeResults:
        """Special nested class for casting SingleModeResults to subclasses."""

        def __init__(
            self: "SingleModeResults._Cast_SingleModeResults",
            parent: "SingleModeResults",
        ):
            self._parent = parent

        @property
        def design_entity_modal_analysis_group_results(
            self: "SingleModeResults._Cast_SingleModeResults",
        ) -> "_4727.DesignEntityModalAnalysisGroupResults":
            return self._parent._cast(_4727.DesignEntityModalAnalysisGroupResults)

        @property
        def single_mode_results(
            self: "SingleModeResults._Cast_SingleModeResults",
        ) -> "SingleModeResults":
            return self._parent

        def __getattr__(self: "SingleModeResults._Cast_SingleModeResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SingleModeResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mode_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModeFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def mode_id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModeID

        if temp is None:
            return 0

        return temp

    @property
    def all_rigidly_connected_groups(
        self: Self,
    ) -> "List[_4731.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis]

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
    ) -> "List[_4731.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis]

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
    ) -> "List[_4731.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis]

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
    ) -> "List[_4731.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis]

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
    def cast_to(self: Self) -> "SingleModeResults._Cast_SingleModeResults":
        return self._Cast_SingleModeResults(self)
