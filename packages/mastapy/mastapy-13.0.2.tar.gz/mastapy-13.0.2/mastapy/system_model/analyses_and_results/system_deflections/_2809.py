"""ShaftHubConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2736
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ShaftHubConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.detailed_rigid_connectors.rating import _1443
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.power_flows import _4140
    from mastapy.bearings.bearing_results import _1948
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2858,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2790,
        _2723,
        _2793,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionSystemDeflection",)


Self = TypeVar("Self", bound="ShaftHubConnectionSystemDeflection")


class ShaftHubConnectionSystemDeflection(_2736.ConnectorSystemDeflection):
    """ShaftHubConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnectionSystemDeflection")

    class _Cast_ShaftHubConnectionSystemDeflection:
        """Special nested class for casting ShaftHubConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
            parent: "ShaftHubConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def connector_system_deflection(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_2736.ConnectorSystemDeflection":
            return self._parent._cast(_2736.ConnectorSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_system_deflection(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
        ) -> "ShaftHubConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def limiting_friction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitingFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def node_pair_separations(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairSeparations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_radial_forces_on_inner(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeRadialForcesOnInner

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_deflection_left_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflectionLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_deflection_right_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflectionRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_deflection_tooth_centre(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflectionToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_force_left_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForceLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_force_right_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForceRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_force_tooth_centre(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForceToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_stiffness_left_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_stiffness_right_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def normal_stiffness_tooth_centre(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def number_of_major_diameter_contacts(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfMajorDiameterContacts

        if temp is None:
            return 0

        return temp

    @property
    def number_of_teeth_in_contact(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTeethInContact

        if temp is None:
            return 0

        return temp

    @property
    def tangential_force_left_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForceLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def tangential_force_right_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForceRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def tangential_force_tooth_centre(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForceToothCentre

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def tangential_force_on_spline(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForceOnSpline

        if temp is None:
            return 0.0

        return temp

    @property
    def will_spline_slip(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WillSplineSlip

        if temp is None:
            return False

        return temp

    @property
    def component_design(self: Self) -> "_2606.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_1443.ShaftHubConnectionRating":
        """mastapy.detailed_rigid_connectors.rating.ShaftHubConnectionRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6958.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4140.ShaftHubConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ShaftHubConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_matrix_in_local_coordinate_system(
        self: Self,
    ) -> "_1948.BearingStiffnessMatrixReporter":
        """mastapy.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMatrixInLocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stiffness_matrix_in_unrotated_coordinate_system(
        self: Self,
    ) -> "_1948.BearingStiffnessMatrixReporter":
        """mastapy.bearings.bearing_results.BearingStiffnessMatrixReporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMatrixInUnrotatedCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank_contacts(self: Self) -> "List[_2858.SplineFlankContactReporting]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.SplineFlankContactReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def right_flank_contacts(self: Self) -> "List[_2858.SplineFlankContactReporting]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.SplineFlankContactReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def tip_contacts(self: Self) -> "List[_2858.SplineFlankContactReporting]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.SplineFlankContactReporting]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftHubConnectionSystemDeflection._Cast_ShaftHubConnectionSystemDeflection":
        return self._Cast_ShaftHubConnectionSystemDeflection(self)
