"""CouplingSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2814
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CouplingSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.power_flows import _4079
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2721,
        _2727,
        _2796,
        _2820,
        _2838,
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
__all__ = ("CouplingSystemDeflection",)


Self = TypeVar("Self", bound="CouplingSystemDeflection")


class CouplingSystemDeflection(_2814.SpecialisedAssemblySystemDeflection):
    """CouplingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingSystemDeflection")

    class _Cast_CouplingSystemDeflection:
        """Special nested class for casting CouplingSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
            parent: "CouplingSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2814.SpecialisedAssemblySystemDeflection":
            return self._parent._cast(_2814.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2693.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2693,
            )

            return self._parent._cast(_2693.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2721.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ClutchSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2727.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConceptCouplingSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2796.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.PartToPartShearCouplingSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2820.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.SpringDamperSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "_2838.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.TorqueConverterSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "CouplingSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2591.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4079.CouplingPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CouplingPowerFlow

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
    ) -> "CouplingSystemDeflection._Cast_CouplingSystemDeflection":
        return self._Cast_CouplingSystemDeflection(self)
