"""MicroGeometryDesignSpaceSearch"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.gears.ltca.cylindrical import _859, _860, _863
from mastapy.gears.gear_set_pareto_optimiser import _909
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser", "MicroGeometryDesignSpaceSearch"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import _923
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1113


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryDesignSpaceSearch",)


Self = TypeVar("Self", bound="MicroGeometryDesignSpaceSearch")


class MicroGeometryDesignSpaceSearch(
    _909.DesignSpaceSearchBase[
        "_863.CylindricalGearSetLoadDistributionAnalysis",
        "_920.MicroGeometryDesignSpaceSearchCandidate",
    ]
):
    """MicroGeometryDesignSpaceSearch

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MicroGeometryDesignSpaceSearch")

    class _Cast_MicroGeometryDesignSpaceSearch:
        """Special nested class for casting MicroGeometryDesignSpaceSearch to subclasses."""

        def __init__(
            self: "MicroGeometryDesignSpaceSearch._Cast_MicroGeometryDesignSpaceSearch",
            parent: "MicroGeometryDesignSpaceSearch",
        ):
            self._parent = parent

        @property
        def design_space_search_base(
            self: "MicroGeometryDesignSpaceSearch._Cast_MicroGeometryDesignSpaceSearch",
        ) -> "_909.DesignSpaceSearchBase":
            return self._parent._cast(_909.DesignSpaceSearchBase)

        @property
        def micro_geometry_gear_set_design_space_search(
            self: "MicroGeometryDesignSpaceSearch._Cast_MicroGeometryDesignSpaceSearch",
        ) -> "_923.MicroGeometryGearSetDesignSpaceSearch":
            from mastapy.gears.gear_set_pareto_optimiser import _923

            return self._parent._cast(_923.MicroGeometryGearSetDesignSpaceSearch)

        @property
        def micro_geometry_design_space_search(
            self: "MicroGeometryDesignSpaceSearch._Cast_MicroGeometryDesignSpaceSearch",
        ) -> "MicroGeometryDesignSpaceSearch":
            return self._parent

        def __getattr__(
            self: "MicroGeometryDesignSpaceSearch._Cast_MicroGeometryDesignSpaceSearch",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MicroGeometryDesignSpaceSearch.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def run_all_planetary_meshes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RunAllPlanetaryMeshes

        if temp is None:
            return False

        return temp

    @run_all_planetary_meshes.setter
    @enforce_parameter_types
    def run_all_planetary_meshes(self: Self, value: "bool"):
        self.wrapped.RunAllPlanetaryMeshes = bool(value) if value is not None else False

    @property
    def select_gear(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis":
        """ListWithSelectedItem[mastapy.gears.ltca.cylindrical.CylindricalGearLoadDistributionAnalysis]"""
        temp = self.wrapped.SelectGear

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis",
        )(temp)

    @select_gear.setter
    @enforce_parameter_types
    def select_gear(self: Self, value: "_859.CylindricalGearLoadDistributionAnalysis"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SelectGear = value

    @property
    def select_mesh(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis":
        """ListWithSelectedItem[mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadDistributionAnalysis]"""
        temp = self.wrapped.SelectMesh

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis",
        )(temp)

    @select_mesh.setter
    @enforce_parameter_types
    def select_mesh(
        self: Self, value: "_860.CylindricalGearMeshLoadDistributionAnalysis"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SelectMesh = value

    @property
    def load_case_duty_cycle(
        self: Self,
    ) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearSetLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_candidate_micro_geometry(
        self: Self,
    ) -> "_1113.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedCandidateMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_candidate_gear_sets(
        self: Self,
    ) -> "List[_1113.CylindricalGearSetMicroGeometry]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry]

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
    def candidate_gear_sets(
        self: Self,
    ) -> "List[_1113.CylindricalGearSetMicroGeometry]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry]

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

    def add_chart(self: Self):
        """Method does not return."""
        self.wrapped.AddChart()

    def reset_charts(self: Self):
        """Method does not return."""
        self.wrapped.ResetCharts()

    @property
    def cast_to(
        self: Self,
    ) -> "MicroGeometryDesignSpaceSearch._Cast_MicroGeometryDesignSpaceSearch":
        return self._Cast_MicroGeometryDesignSpaceSearch(self)
