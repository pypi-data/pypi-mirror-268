"""CylindricalGearSetCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3184,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3039,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3171,
        _3172,
        _3208,
        _3222,
        _3124,
        _3203,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CylindricalGearSetCompoundSteadyStateSynchronousResponse")


class CylindricalGearSetCompoundSteadyStateSynchronousResponse(
    _3184.GearSetCompoundSteadyStateSynchronousResponse
):
    """CylindricalGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CylindricalGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
            parent: "CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3184.GearSetCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3184.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(_3203.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3208.PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3208,
            )

            return self._parent._cast(
                _3208.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "CylindricalGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CylindricalGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2533.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

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
    ) -> "List[_3039.CylindricalGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalGearSetSteadyStateSynchronousResponse]

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
    def cylindrical_gears_compound_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3171.CylindricalGearCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.CylindricalGearCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_compound_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3172.CylindricalGearMeshCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.CylindricalGearMeshCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3039.CylindricalGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalGearSetSteadyStateSynchronousResponse]

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
    ) -> "CylindricalGearSetCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponse(self)
