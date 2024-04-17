"""DesignState"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups import _5666
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_STATE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups", "DesignState"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups import (
        _5669,
        _5670,
        _5668,
        _5667,
    )
    from mastapy.system_model.connections_and_sockets.couplings import _2349
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.static_loads import _6813


__docformat__ = "restructuredtext en"
__all__ = ("DesignState",)


Self = TypeVar("Self", bound="DesignState")


class DesignState(_5666.AbstractDesignStateLoadCaseGroup):
    """DesignState

    This is a mastapy class.
    """

    TYPE = _DESIGN_STATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignState")

    class _Cast_DesignState:
        """Special nested class for casting DesignState to subclasses."""

        def __init__(self: "DesignState._Cast_DesignState", parent: "DesignState"):
            self._parent = parent

        @property
        def abstract_design_state_load_case_group(
            self: "DesignState._Cast_DesignState",
        ) -> "_5666.AbstractDesignStateLoadCaseGroup":
            return self._parent._cast(_5666.AbstractDesignStateLoadCaseGroup)

        @property
        def abstract_static_load_case_group(
            self: "DesignState._Cast_DesignState",
        ) -> "_5668.AbstractStaticLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5668

            return self._parent._cast(_5668.AbstractStaticLoadCaseGroup)

        @property
        def abstract_load_case_group(
            self: "DesignState._Cast_DesignState",
        ) -> "_5667.AbstractLoadCaseGroup":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5667

            return self._parent._cast(_5667.AbstractLoadCaseGroup)

        @property
        def design_state(self: "DesignState._Cast_DesignState") -> "DesignState":
            return self._parent

        def __getattr__(self: "DesignState._Cast_DesignState", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignState.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutches(self: Self) -> "List[_5669.ClutchEngagementStatus]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.ClutchEngagementStatus]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_synchro_mounted_gears(
        self: Self,
    ) -> "List[_5670.ConceptSynchroGearEngagementStatus]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.ConceptSynchroGearEngagementStatus]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptSynchroMountedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def clutch_engagement_status_for(
        self: Self, clutch_connection: "_2349.ClutchConnection"
    ) -> "_5669.ClutchEngagementStatus":
        """mastapy.system_model.analyses_and_results.load_case_groups.ClutchEngagementStatus

        Args:
            clutch_connection (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        method_result = self.wrapped.ClutchEngagementStatusFor(
            clutch_connection.wrapped if clutch_connection else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def concept_synchro_gear_engagement_status_for(
        self: Self, gear: "_2532.CylindricalGear"
    ) -> "_5670.ConceptSynchroGearEngagementStatus":
        """mastapy.system_model.analyses_and_results.load_case_groups.ConceptSynchroGearEngagementStatus

        Args:
            gear (mastapy.system_model.part_model.gears.CylindricalGear)
        """
        method_result = self.wrapped.ConceptSynchroGearEngagementStatusFor(
            gear.wrapped if gear else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_load_case(
        self: Self, name: "str" = "New Static Load"
    ) -> "_6813.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Args:
            name (str, optional)
        """
        name = str(name)
        method_result = self.wrapped.CreateLoadCase(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def duplicate(self: Self, duplicate_static_loads: "bool" = True) -> "DesignState":
        """mastapy.system_model.analyses_and_results.load_case_groups.DesignState

        Args:
            duplicate_static_loads (bool, optional)
        """
        duplicate_static_loads = bool(duplicate_static_loads)
        method_result = self.wrapped.Duplicate(
            duplicate_static_loads if duplicate_static_loads else False
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "DesignState._Cast_DesignState":
        return self._Cast_DesignState(self)
