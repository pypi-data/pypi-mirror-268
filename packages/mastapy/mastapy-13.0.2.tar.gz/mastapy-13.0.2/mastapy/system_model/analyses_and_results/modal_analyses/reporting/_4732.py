"""RigidlyConnectedDesignEntityGroupModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results import _2660
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "RigidlyConnectedDesignEntityGroupModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.utility.modal_analysis import _1803


__docformat__ = "restructuredtext en"
__all__ = ("RigidlyConnectedDesignEntityGroupModalAnalysis",)


Self = TypeVar("Self", bound="RigidlyConnectedDesignEntityGroupModalAnalysis")


class RigidlyConnectedDesignEntityGroupModalAnalysis(_2660.DesignEntityGroupAnalysis):
    """RigidlyConnectedDesignEntityGroupModalAnalysis

    This is a mastapy class.
    """

    TYPE = _RIGIDLY_CONNECTED_DESIGN_ENTITY_GROUP_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RigidlyConnectedDesignEntityGroupModalAnalysis"
    )

    class _Cast_RigidlyConnectedDesignEntityGroupModalAnalysis:
        """Special nested class for casting RigidlyConnectedDesignEntityGroupModalAnalysis to subclasses."""

        def __init__(
            self: "RigidlyConnectedDesignEntityGroupModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupModalAnalysis",
            parent: "RigidlyConnectedDesignEntityGroupModalAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_group_analysis(
            self: "RigidlyConnectedDesignEntityGroupModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupModalAnalysis",
        ) -> "_2660.DesignEntityGroupAnalysis":
            return self._parent._cast(_2660.DesignEntityGroupAnalysis)

        @property
        def rigidly_connected_design_entity_group_modal_analysis(
            self: "RigidlyConnectedDesignEntityGroupModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupModalAnalysis",
        ) -> "RigidlyConnectedDesignEntityGroupModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RigidlyConnectedDesignEntityGroupModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupModalAnalysis",
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
        instance_to_wrap: "RigidlyConnectedDesignEntityGroupModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_frequencies_at_reference_speed(
        self: Self,
    ) -> "List[_1803.DesignEntityExcitationDescription]":
        """List[mastapy.utility.modal_analysis.DesignEntityExcitationDescription]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationFrequenciesAtReferenceSpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RigidlyConnectedDesignEntityGroupModalAnalysis._Cast_RigidlyConnectedDesignEntityGroupModalAnalysis":
        return self._Cast_RigidlyConnectedDesignEntityGroupModalAnalysis(self)
