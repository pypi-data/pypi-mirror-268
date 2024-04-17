"""CylindricalMeshedGearLoadDistributionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_CONTACT_RESULT_TYPE = python_net_import("SMT.MastaAPI.Gears.LTCA", "ContactResultType")
_CYLINDRICAL_MESHED_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "CylindricalMeshedGearLoadDistributionAnalysis"
)
_BOOLEAN = python_net_import("System", "Boolean")
_INT_32 = python_net_import("System", "Int32")

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _859
    from mastapy.gears.cylindrical import _1217, _1216, _1215, _1214
    from mastapy.gears.ltca import _830
    from mastapy.math_utility import _1522


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshedGearLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="CylindricalMeshedGearLoadDistributionAnalysis")


class CylindricalMeshedGearLoadDistributionAnalysis(_0.APIBase):
    """CylindricalMeshedGearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESHED_GEAR_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalMeshedGearLoadDistributionAnalysis"
    )

    class _Cast_CylindricalMeshedGearLoadDistributionAnalysis:
        """Special nested class for casting CylindricalMeshedGearLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "CylindricalMeshedGearLoadDistributionAnalysis._Cast_CylindricalMeshedGearLoadDistributionAnalysis",
            parent: "CylindricalMeshedGearLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_meshed_gear_load_distribution_analysis(
            self: "CylindricalMeshedGearLoadDistributionAnalysis._Cast_CylindricalMeshedGearLoadDistributionAnalysis",
        ) -> "CylindricalMeshedGearLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshedGearLoadDistributionAnalysis._Cast_CylindricalMeshedGearLoadDistributionAnalysis",
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
        instance_to_wrap: "CylindricalMeshedGearLoadDistributionAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_patch_edge_loading_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPatchEdgeLoadingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_patch_offset_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPatchOffsetFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_patch_tip_loading_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPatchTipLoadingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def is_loaded_on_tip(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoadedOnTip

        if temp is None:
            return False

        return temp

    @property
    def maximum_principal_root_stress_compression(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPrincipalRootStressCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_principal_root_stress_tension(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPrincipalRootStressTension

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_compression(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumVonMisesRootStressCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_tension(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumVonMisesRootStressTension

        if temp is None:
            return 0.0

        return temp

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
    def nominal_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_of_effective_face_width_utilized(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageOfEffectiveFaceWidthUtilized

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_of_effective_profile_utilized(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageOfEffectiveProfileUtilized

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_of_potential_contact_area_loaded(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageOfPotentialContactAreaLoaded

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_of_potential_contact_area_utilized(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageOfPotentialContactAreaUtilized

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_scaled_by_application_and_dynamic_factors(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueScaledByApplicationAndDynamicFactors

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_load_distribution_analysis(
        self: Self,
    ) -> "_859.CylindricalGearLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearLoadDistributionAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def other_gear_load_distribution_analysis(
        self: Self,
    ) -> "_859.CylindricalGearLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OtherGearLoadDistributionAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worst_contact_charts(
        self: Self,
    ) -> "_1217.CylindricalGearWorstLTCAContactCharts":
        """mastapy.gears.cylindrical.CylindricalGearWorstLTCAContactCharts

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstContactCharts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worst_contact_charts_as_text_files(
        self: Self,
    ) -> "_1216.CylindricalGearWorstLTCAContactChartDataAsTextFile":
        """mastapy.gears.cylindrical.CylindricalGearWorstLTCAContactChartDataAsTextFile

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstContactChartsAsTextFiles

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_charts(self: Self) -> "List[_1215.CylindricalGearLTCAContactCharts]":
        """List[mastapy.gears.cylindrical.CylindricalGearLTCAContactCharts]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactCharts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def contact_charts_as_text_files(
        self: Self,
    ) -> "List[_1214.CylindricalGearLTCAContactChartDataAsTextFile]":
        """List[mastapy.gears.cylindrical.CylindricalGearLTCAContactChartDataAsTextFile]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartsAsTextFiles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def contact_patch_as_text(
        self: Self,
        result_type: "_830.ContactResultType",
        include_tip_contact: "bool",
        file_name_with_path: "str",
        start_rotation_index: "int" = 0,
    ):
        """Method does not return.

        Args:
            result_type (mastapy.gears.ltca.ContactResultType)
            include_tip_contact (bool)
            file_name_with_path (str)
            start_rotation_index (int, optional)
        """
        result_type = conversion.mp_to_pn_enum(
            result_type, "SMT.MastaAPI.Gears.LTCA.ContactResultType"
        )
        include_tip_contact = bool(include_tip_contact)
        file_name_with_path = str(file_name_with_path)
        start_rotation_index = int(start_rotation_index)
        self.wrapped.ContactPatchAsText(
            result_type,
            include_tip_contact if include_tip_contact else False,
            file_name_with_path if file_name_with_path else "",
            start_rotation_index if start_rotation_index else 0,
        )

    @enforce_parameter_types
    def contact_patch(
        self: Self,
        result_type: "_830.ContactResultType",
        include_tip_contact: "bool",
        start_rotation_index: "int" = 0,
    ) -> "_1522.GriddedSurface":
        """mastapy.math_utility.GriddedSurface

        Args:
            result_type (mastapy.gears.ltca.ContactResultType)
            include_tip_contact (bool)
            start_rotation_index (int, optional)
        """
        result_type = conversion.mp_to_pn_enum(
            result_type, "SMT.MastaAPI.Gears.LTCA.ContactResultType"
        )
        include_tip_contact = bool(include_tip_contact)
        start_rotation_index = int(start_rotation_index)
        method_result = self.wrapped.ContactPatch.Overloads[
            _CONTACT_RESULT_TYPE, _BOOLEAN, _INT_32
        ](
            result_type,
            include_tip_contact if include_tip_contact else False,
            start_rotation_index if start_rotation_index else 0,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def contact_patch_detailed(
        self: Self,
        result_type: "_830.ContactResultType",
        number_of_face_width_steps: "int",
        number_of_roll_distance_steps: "int",
        start_rotation_index: "int" = 0,
    ) -> "_1522.GriddedSurface":
        """mastapy.math_utility.GriddedSurface

        Args:
            result_type (mastapy.gears.ltca.ContactResultType)
            number_of_face_width_steps (int)
            number_of_roll_distance_steps (int)
            start_rotation_index (int, optional)
        """
        result_type = conversion.mp_to_pn_enum(
            result_type, "SMT.MastaAPI.Gears.LTCA.ContactResultType"
        )
        number_of_face_width_steps = int(number_of_face_width_steps)
        number_of_roll_distance_steps = int(number_of_roll_distance_steps)
        start_rotation_index = int(start_rotation_index)
        method_result = self.wrapped.ContactPatch.Overloads[
            _CONTACT_RESULT_TYPE, _INT_32, _INT_32, _INT_32
        ](
            result_type,
            number_of_face_width_steps if number_of_face_width_steps else 0,
            number_of_roll_distance_steps if number_of_roll_distance_steps else 0,
            start_rotation_index if start_rotation_index else 0,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalMeshedGearLoadDistributionAnalysis._Cast_CylindricalMeshedGearLoadDistributionAnalysis":
        return self._Cast_CylindricalMeshedGearLoadDistributionAnalysis(self)
