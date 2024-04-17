"""PlanetaryGearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7331
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PlanetaryGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7343,
        _7382,
        _7278,
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PlanetaryGearSetAdvancedSystemDeflection")


class PlanetaryGearSetAdvancedSystemDeflection(
    _7331.CylindricalGearSetAdvancedSystemDeflection
):
    """PlanetaryGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetAdvancedSystemDeflection"
    )

    class _Cast_PlanetaryGearSetAdvancedSystemDeflection:
        """Special nested class for casting PlanetaryGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
            parent: "PlanetaryGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_7331.CylindricalGearSetAdvancedSystemDeflection":
            return self._parent._cast(_7331.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_7343.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(_7343.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_7382.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(_7382.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_7278.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(_7278.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
        ) -> "PlanetaryGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2549.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetAdvancedSystemDeflection._Cast_PlanetaryGearSetAdvancedSystemDeflection":
        return self._Cast_PlanetaryGearSetAdvancedSystemDeflection(self)
