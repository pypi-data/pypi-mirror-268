"""FaceGearSetParetoOptimiser"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_set_pareto_optimiser import _915
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_FACE_GEAR_SET_PARETO_OPTIMISER = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser", "FaceGearSetParetoOptimiser"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _999
    from mastapy.gears.gear_set_pareto_optimiser import _909


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetParetoOptimiser",)


Self = TypeVar("Self", bound="FaceGearSetParetoOptimiser")


class FaceGearSetParetoOptimiser(_915.GearSetParetoOptimiser):
    """FaceGearSetParetoOptimiser

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_PARETO_OPTIMISER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetParetoOptimiser")

    class _Cast_FaceGearSetParetoOptimiser:
        """Special nested class for casting FaceGearSetParetoOptimiser to subclasses."""

        def __init__(
            self: "FaceGearSetParetoOptimiser._Cast_FaceGearSetParetoOptimiser",
            parent: "FaceGearSetParetoOptimiser",
        ):
            self._parent = parent

        @property
        def gear_set_pareto_optimiser(
            self: "FaceGearSetParetoOptimiser._Cast_FaceGearSetParetoOptimiser",
        ) -> "_915.GearSetParetoOptimiser":
            return self._parent._cast(_915.GearSetParetoOptimiser)

        @property
        def design_space_search_base(
            self: "FaceGearSetParetoOptimiser._Cast_FaceGearSetParetoOptimiser",
        ) -> "_909.DesignSpaceSearchBase":
            pass

            from mastapy.gears.gear_set_pareto_optimiser import _909

            return self._parent._cast(_909.DesignSpaceSearchBase)

        @property
        def face_gear_set_pareto_optimiser(
            self: "FaceGearSetParetoOptimiser._Cast_FaceGearSetParetoOptimiser",
        ) -> "FaceGearSetParetoOptimiser":
            return self._parent

        def __getattr__(
            self: "FaceGearSetParetoOptimiser._Cast_FaceGearSetParetoOptimiser",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetParetoOptimiser.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_space_search_strategy(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignSpaceSearchStrategy.SelectedItemName

        if temp is None:
            return ""

        return temp

    @design_space_search_strategy.setter
    @enforce_parameter_types
    def design_space_search_strategy(self: Self, value: "str"):
        self.wrapped.DesignSpaceSearchStrategy.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def design_space_search_strategy_duty_cycle(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignSpaceSearchStrategyDutyCycle.SelectedItemName

        if temp is None:
            return ""

        return temp

    @design_space_search_strategy_duty_cycle.setter
    @enforce_parameter_types
    def design_space_search_strategy_duty_cycle(self: Self, value: "str"):
        self.wrapped.DesignSpaceSearchStrategyDutyCycle.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def selected_candidate_geometry(self: Self) -> "_999.FaceGearSetDesign":
        """mastapy.gears.gear_designs.face.FaceGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedCandidateGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_candidate_gear_sets(self: Self) -> "List[_999.FaceGearSetDesign]":
        """List[mastapy.gears.gear_designs.face.FaceGearSetDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllCandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def candidate_gear_sets(self: Self) -> "List[_999.FaceGearSetDesign]":
        """List[mastapy.gears.gear_designs.face.FaceGearSetDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetParetoOptimiser._Cast_FaceGearSetParetoOptimiser":
        return self._Cast_FaceGearSetParetoOptimiser(self)
