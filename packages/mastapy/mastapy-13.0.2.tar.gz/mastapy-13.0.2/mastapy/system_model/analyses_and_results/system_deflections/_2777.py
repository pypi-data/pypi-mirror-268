"""KlingelnbergCycloPalloidConicalGearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.power_flows import _4111
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2780,
        _2783,
        _2768,
        _2814,
        _2693,
        _2793,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetSystemDeflection",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetSystemDeflection")


class KlingelnbergCycloPalloidConicalGearSetSystemDeflection(
    _2733.ConicalGearSetSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2733.ConicalGearSetSystemDeflection":
            return self._parent._cast(_2733.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2768.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(_2768.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2814.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2693.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2693,
            )

            return self._parent._cast(_2693.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2780.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(
                _2780.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "_2783.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(
                _2783.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetSystemDeflection(self)
