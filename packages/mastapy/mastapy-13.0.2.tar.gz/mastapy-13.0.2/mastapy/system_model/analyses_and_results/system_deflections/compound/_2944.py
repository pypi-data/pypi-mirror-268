"""PlanetaryGearSetCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.system_deflections.compound import _2908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "PlanetaryGearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2920,
        _2959,
        _2859,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundSystemDeflection",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundSystemDeflection")


class PlanetaryGearSetCompoundSystemDeflection(
    _2908.CylindricalGearSetCompoundSystemDeflection
):
    """PlanetaryGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundSystemDeflection"
    )

    class _Cast_PlanetaryGearSetCompoundSystemDeflection:
        """Special nested class for casting PlanetaryGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
            parent: "PlanetaryGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "_2908.CylindricalGearSetCompoundSystemDeflection":
            return self._parent._cast(_2908.CylindricalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "_2920.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(_2920.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "_2959.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "_2859.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "PlanetaryGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection":
        return self._Cast_PlanetaryGearSetCompoundSystemDeflection(self)
