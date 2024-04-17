"""BeltDriveCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2959
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BeltDriveCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.system_deflections import _2708
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2900,
        _2859,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BeltDriveCompoundSystemDeflection")


class BeltDriveCompoundSystemDeflection(
    _2959.SpecialisedAssemblyCompoundSystemDeflection
):
    """BeltDriveCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveCompoundSystemDeflection")

    class _Cast_BeltDriveCompoundSystemDeflection:
        """Special nested class for casting BeltDriveCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
            parent: "BeltDriveCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
        ) -> "_2959.SpecialisedAssemblyCompoundSystemDeflection":
            return self._parent._cast(_2959.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
        ) -> "_2859.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_compound_system_deflection(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
        ) -> "_2900.CVTCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.CVTCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
        ) -> "BeltDriveCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "BeltDriveCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2583.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2708.BeltDriveSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection]

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
    def assembly_analysis_cases(self: Self) -> "List[_2708.BeltDriveSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection]

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
    ) -> "BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection":
        return self._Cast_BeltDriveCompoundSystemDeflection(self)
