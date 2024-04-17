"""CouplingLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6843,
        _6849,
        _6940,
        _6967,
        _6982,
        _6815,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingLoadCase",)


Self = TypeVar("Self", bound="CouplingLoadCase")


class CouplingLoadCase(_6961.SpecialisedAssemblyLoadCase):
    """CouplingLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingLoadCase")

    class _Cast_CouplingLoadCase:
        """Special nested class for casting CouplingLoadCase to subclasses."""

        def __init__(
            self: "CouplingLoadCase._Cast_CouplingLoadCase", parent: "CouplingLoadCase"
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6843.ClutchLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.ClutchLoadCase)

        @property
        def concept_coupling_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6849.ConceptCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConceptCouplingLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6940.PartToPartShearCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(_6940.PartToPartShearCouplingLoadCase)

        @property
        def spring_damper_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6967.SpringDamperLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.SpringDamperLoadCase)

        @property
        def torque_converter_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6982.TorqueConverterLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.TorqueConverterLoadCase)

        @property
        def coupling_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "CouplingLoadCase":
            return self._parent

        def __getattr__(self: "CouplingLoadCase._Cast_CouplingLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingLoadCase.TYPE"):
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
    def cast_to(self: Self) -> "CouplingLoadCase._Cast_CouplingLoadCase":
        return self._Cast_CouplingLoadCase(self)
