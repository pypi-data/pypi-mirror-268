"""CouplingHalfLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6933
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingHalfLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2592
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6842,
        _6848,
        _6865,
        _6939,
        _6949,
        _6956,
        _6966,
        _6976,
        _6978,
        _6979,
        _6983,
        _6984,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfLoadCase",)


Self = TypeVar("Self", bound="CouplingHalfLoadCase")


class CouplingHalfLoadCase(_6933.MountableComponentLoadCase):
    """CouplingHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfLoadCase")

    class _Cast_CouplingHalfLoadCase:
        """Special nested class for casting CouplingHalfLoadCase to subclasses."""

        def __init__(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
            parent: "CouplingHalfLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6842.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6848.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConceptCouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6865.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6865

            return self._parent._cast(_6865.CVTPulleyLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6939.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.PartToPartShearCouplingHalfLoadCase)

        @property
        def pulley_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6949.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.PulleyLoadCase)

        @property
        def rolling_ring_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6956.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.RollingRingLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6966.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.SpringDamperHalfLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6976.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6978.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6978

            return self._parent._cast(_6978.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6979.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6983.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "_6984.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.TorqueConverterTurbineLoadCase)

        @property
        def coupling_half_load_case(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase",
        ) -> "CouplingHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2592.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingHalfLoadCase._Cast_CouplingHalfLoadCase":
        return self._Cast_CouplingHalfLoadCase(self)
