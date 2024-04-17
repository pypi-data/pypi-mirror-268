"""BeltDriveSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3351,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "BeltDriveSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.static_loads import _6830
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3295,
        _3253,
        _3332,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="BeltDriveSteadyStateSynchronousResponseOnAShaft")


class BeltDriveSteadyStateSynchronousResponseOnAShaft(
    _3351.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
):
    """BeltDriveSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BeltDriveSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
            parent: "BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3351.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3351.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3253.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3332.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(_3332.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3295.CVTSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3295,
            )

            return self._parent._cast(_3295.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "BeltDriveSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BeltDriveSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6830.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft(self)
