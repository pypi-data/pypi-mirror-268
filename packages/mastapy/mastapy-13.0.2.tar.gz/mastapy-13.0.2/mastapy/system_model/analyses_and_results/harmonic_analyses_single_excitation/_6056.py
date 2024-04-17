"""CVTBeltConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6025,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2280
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6082,
        _6051,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CVTBeltConnectionHarmonicAnalysisOfSingleExcitation")


class CVTBeltConnectionHarmonicAnalysisOfSingleExcitation(
    _6025.BeltConnectionHarmonicAnalysisOfSingleExcitation
):
    """CVTBeltConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTBeltConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6025.BeltConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6025.BeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6082.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6051.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2280.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CVTBeltConnectionHarmonicAnalysisOfSingleExcitation(self)
