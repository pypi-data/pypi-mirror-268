"""CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7085,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2353
    from mastapy.system_model.analyses_and_results.system_deflections import _2737
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7041,
        _7046,
        _7101,
        _7123,
        _7138,
        _7054,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"
)


class CouplingConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """CouplingConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CouplingConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7054.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7041.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7046.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7101.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7101,
            )

            return self._parent._cast(
                _7101.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7123.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7138.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7138,
            )

            return self._parent._cast(
                _7138.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    ) -> "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
