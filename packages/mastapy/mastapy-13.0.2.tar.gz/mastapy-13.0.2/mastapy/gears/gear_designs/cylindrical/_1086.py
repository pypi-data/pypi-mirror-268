"""TiffAnalysisSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIFF_ANALYSIS_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "TiffAnalysisSettings"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.gears.gear_designs.cylindrical import _1055


__docformat__ = "restructuredtext en"
__all__ = ("TiffAnalysisSettings",)


Self = TypeVar("Self", bound="TiffAnalysisSettings")


class TiffAnalysisSettings(
    _1593.IndependentReportablePropertiesBase["TiffAnalysisSettings"]
):
    """TiffAnalysisSettings

    This is a mastapy class.
    """

    TYPE = _TIFF_ANALYSIS_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TiffAnalysisSettings")

    class _Cast_TiffAnalysisSettings:
        """Special nested class for casting TiffAnalysisSettings to subclasses."""

        def __init__(
            self: "TiffAnalysisSettings._Cast_TiffAnalysisSettings",
            parent: "TiffAnalysisSettings",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "TiffAnalysisSettings._Cast_TiffAnalysisSettings",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def tiff_analysis_settings(
            self: "TiffAnalysisSettings._Cast_TiffAnalysisSettings",
        ) -> "TiffAnalysisSettings":
            return self._parent

        def __getattr__(
            self: "TiffAnalysisSettings._Cast_TiffAnalysisSettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TiffAnalysisSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_findley_analysis(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeFindleyAnalysis

        if temp is None:
            return False

        return temp

    @include_findley_analysis.setter
    @enforce_parameter_types
    def include_findley_analysis(self: Self, value: "bool"):
        self.wrapped.IncludeFindleyAnalysis = (
            bool(value) if value is not None else False
        )

    @property
    def include_residual_stresses(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeResidualStresses

        if temp is None:
            return False

        return temp

    @include_residual_stresses.setter
    @enforce_parameter_types
    def include_residual_stresses(self: Self, value: "bool"):
        self.wrapped.IncludeResidualStresses = (
            bool(value) if value is not None else False
        )

    @property
    def include_shot_peening(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeShotPeening

        if temp is None:
            return False

        return temp

    @include_shot_peening.setter
    @enforce_parameter_types
    def include_shot_peening(self: Self, value: "bool"):
        self.wrapped.IncludeShotPeening = bool(value) if value is not None else False

    @property
    def measured_residual_stress_profile_property(
        self: Self,
    ) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.MeasuredResidualStressProfileProperty

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @measured_residual_stress_profile_property.setter
    @enforce_parameter_types
    def measured_residual_stress_profile_property(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.MeasuredResidualStressProfileProperty = value.wrapped

    @property
    def number_of_rotations_for_findley(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfRotationsForFindley

        if temp is None:
            return 0

        return temp

    @number_of_rotations_for_findley.setter
    @enforce_parameter_types
    def number_of_rotations_for_findley(self: Self, value: "int"):
        self.wrapped.NumberOfRotationsForFindley = (
            int(value) if value is not None else 0
        )

    @property
    def shot_peening_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShotPeeningDepth

        if temp is None:
            return 0.0

        return temp

    @shot_peening_depth.setter
    @enforce_parameter_types
    def shot_peening_depth(self: Self, value: "float"):
        self.wrapped.ShotPeeningDepth = float(value) if value is not None else 0.0

    @property
    def shot_peening_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShotPeeningFactor

        if temp is None:
            return 0.0

        return temp

    @shot_peening_factor.setter
    @enforce_parameter_types
    def shot_peening_factor(self: Self, value: "float"):
        self.wrapped.ShotPeeningFactor = float(value) if value is not None else 0.0

    @property
    def strain_at_mid_case_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StrainAtMidCaseDepth

        if temp is None:
            return 0.0

        return temp

    @strain_at_mid_case_depth.setter
    @enforce_parameter_types
    def strain_at_mid_case_depth(self: Self, value: "float"):
        self.wrapped.StrainAtMidCaseDepth = float(value) if value is not None else 0.0

    @property
    def strain_at_surface(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StrainAtSurface

        if temp is None:
            return 0.0

        return temp

    @strain_at_surface.setter
    @enforce_parameter_types
    def strain_at_surface(self: Self, value: "float"):
        self.wrapped.StrainAtSurface = float(value) if value is not None else 0.0

    @property
    def core_material_properties(self: Self) -> "_1055.HardenedMaterialProperties":
        """mastapy.gears.gear_designs.cylindrical.HardenedMaterialProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoreMaterialProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def surface_material_properties(self: Self) -> "_1055.HardenedMaterialProperties":
        """mastapy.gears.gear_designs.cylindrical.HardenedMaterialProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceMaterialProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "TiffAnalysisSettings._Cast_TiffAnalysisSettings":
        return self._Cast_TiffAnalysisSettings(self)
