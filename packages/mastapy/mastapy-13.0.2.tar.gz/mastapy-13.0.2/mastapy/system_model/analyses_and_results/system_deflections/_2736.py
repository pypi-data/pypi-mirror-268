"""ConnectorSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.analyses_and_results.system_deflections import _2790
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConnectorSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.math_utility.measured_vectors import _1571
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2765,
        _2706,
        _2792,
        _2809,
        _2723,
        _2793,
    )
    from mastapy.system_model.fe import _2392
    from mastapy.system_model.analyses_and_results.power_flows import _4076
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorSystemDeflection",)


Self = TypeVar("Self", bound="ConnectorSystemDeflection")


class ConnectorSystemDeflection(_2790.MountableComponentSystemDeflection):
    """ConnectorSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorSystemDeflection")

    class _Cast_ConnectorSystemDeflection:
        """Special nested class for casting ConnectorSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
            parent: "ConnectorSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_system_deflection(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_system_deflection(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_2706.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BearingSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_2792.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.OilSealSystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "_2809.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.ShaftHubConnectionSystemDeflection)

        @property
        def connector_system_deflection(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection",
        ) -> "ConnectorSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def convergence_delta_energy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConvergenceDeltaEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_force_on_inner(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearForceOnInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def moment_on_inner(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentOnInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2454.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_on_outer_support_in_lcs(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceOnOuterSupportInLCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_on_outer_support_in_wcs(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceOnOuterSupportInWCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_fe_part(self: Self) -> "_2765.FEPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterFEPart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_fe_substructure_nodes(self: Self) -> "List[_2392.FESubstructureNode]":
        """List[mastapy.system_model.fe.FESubstructureNode]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterFESubstructureNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4076.ConnectorPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConnectorPowerFlow

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
    ) -> "ConnectorSystemDeflection._Cast_ConnectorSystemDeflection":
        return self._Cast_ConnectorSystemDeflection(self)
