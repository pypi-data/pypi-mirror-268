"""RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4731
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_FOR_SINGLE_EXCITATION_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
        "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
    )
)


__docformat__ = "restructuredtext en"
__all__ = ("RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",)


Self = TypeVar(
    "Self", bound="RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis"
)


class RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis(
    _4731.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
):
    """RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis

    This is a mastapy class.
    """

    TYPE = _RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_FOR_SINGLE_EXCITATION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
    )

    class _Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis:
        """Special nested class for casting RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis to subclasses."""

        def __init__(
            self: "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
            parent: "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
        ):
            self._parent = parent

        @property
        def rigidly_connected_design_entity_group_for_single_mode_modal_analysis(
            self: "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
        ) -> "_4731.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis":
            return self._parent._cast(
                _4731.RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
            )

        @property
        def rigidly_connected_design_entity_group_for_single_excitation_modal_analysis(
            self: "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
        ) -> "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
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
        instance_to_wrap: "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reference_speed_of_crossing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceSpeedOfCrossing

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis":
        return self._Cast_RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis(
            self
        )
