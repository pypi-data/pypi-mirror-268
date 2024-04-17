"""CylindricalGearSetSystemDeflectionWithLTCAResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2750
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearSetSystemDeflectionWithLTCAResults",
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _863
    from mastapy.system_model.analyses_and_results.system_deflections import (
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
__all__ = ("CylindricalGearSetSystemDeflectionWithLTCAResults",)


Self = TypeVar("Self", bound="CylindricalGearSetSystemDeflectionWithLTCAResults")


class CylindricalGearSetSystemDeflectionWithLTCAResults(
    _2750.CylindricalGearSetSystemDeflection
):
    """CylindricalGearSetSystemDeflectionWithLTCAResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetSystemDeflectionWithLTCAResults"
    )

    class _Cast_CylindricalGearSetSystemDeflectionWithLTCAResults:
        """Special nested class for casting CylindricalGearSetSystemDeflectionWithLTCAResults to subclasses."""

        def __init__(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
            parent: "CylindricalGearSetSystemDeflectionWithLTCAResults",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_system_deflection(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_2750.CylindricalGearSetSystemDeflection":
            return self._parent._cast(_2750.CylindricalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_2768.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(_2768.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_2814.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_2693.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2693,
            )

            return self._parent._cast(_2693.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
        ) -> "CylindricalGearSetSystemDeflectionWithLTCAResults":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults",
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
        instance_to_wrap: "CylindricalGearSetSystemDeflectionWithLTCAResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_ltca_results(
        self: Self,
    ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearSetLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def advanced_ltca_results_only_first_planetary_mesh(
        self: Self,
    ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearSetLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedLTCAResultsOnlyFirstPlanetaryMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def basic_ltca_results(
        self: Self,
    ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearSetLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def basic_ltca_results_only_first_planetary_mesh(
        self: Self,
    ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearSetLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicLTCAResultsOnlyFirstPlanetaryMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetSystemDeflectionWithLTCAResults._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults":
        return self._Cast_CylindricalGearSetSystemDeflectionWithLTCAResults(self)
