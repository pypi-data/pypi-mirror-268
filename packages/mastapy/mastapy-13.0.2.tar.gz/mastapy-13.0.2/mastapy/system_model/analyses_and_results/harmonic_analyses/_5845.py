"""VirtualComponentHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "VirtualComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.system_deflections import _2843
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5792,
        _5793,
        _5804,
        _5805,
        _5844,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentHarmonicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentHarmonicAnalysis")


class VirtualComponentHarmonicAnalysis(_5794.MountableComponentHarmonicAnalysis):
    """VirtualComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentHarmonicAnalysis")

    class _Cast_VirtualComponentHarmonicAnalysis:
        """Special nested class for casting VirtualComponentHarmonicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
            parent: "VirtualComponentHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5792.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5793.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5793,
            )

            return self._parent._cast(_5793.MeasurementComponentHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5804.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(_5804.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5805.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.PowerLoadHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "_5844.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5844,
            )

            return self._parent._cast(_5844.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
        ) -> "VirtualComponentHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2486.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2843.VirtualComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentHarmonicAnalysis._Cast_VirtualComponentHarmonicAnalysis":
        return self._Cast_VirtualComponentHarmonicAnalysis(self)
