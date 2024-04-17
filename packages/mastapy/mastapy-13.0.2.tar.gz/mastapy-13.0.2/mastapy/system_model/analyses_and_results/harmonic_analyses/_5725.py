"""CouplingConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2353
    from mastapy.system_model.analyses_and_results.system_deflections import _2737
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5708,
        _5714,
        _5797,
        _5823,
        _5839,
        _5723,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionHarmonicAnalysis")


class CouplingConnectionHarmonicAnalysis(
    _5782.InterMountableComponentConnectionHarmonicAnalysis
):
    """CouplingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionHarmonicAnalysis")

    class _Cast_CouplingConnectionHarmonicAnalysis:
        """Special nested class for casting CouplingConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
            parent: "CouplingConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_5782.InterMountableComponentConnectionHarmonicAnalysis":
            return self._parent._cast(
                _5782.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_5723.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_5708.ClutchConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ClutchConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_5714.ConceptCouplingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_5797.PartToPartShearCouplingConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5797,
            )

            return self._parent._cast(
                _5797.PartToPartShearCouplingConnectionHarmonicAnalysis
            )

        @property
        def spring_damper_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_5823.SpringDamperConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.SpringDamperConnectionHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "_5839.TorqueConverterConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "CouplingConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2353.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2737.CouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection

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
    ) -> "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis":
        return self._Cast_CouplingConnectionHarmonicAnalysis(self)
