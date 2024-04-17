"""IndependentReportablePropertiesBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_REPORTABLE_PROPERTIES_BASE = python_net_import(
    "SMT.MastaAPI.Utility", "IndependentReportablePropertiesBase"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _301
    from mastapy.geometry import _312
    from mastapy.gears import _349
    from mastapy.gears.gear_designs.cylindrical import (
        _1024,
        _1055,
        _1063,
        _1064,
        _1067,
        _1068,
        _1076,
        _1084,
        _1086,
        _1090,
        _1094,
    )
    from mastapy.electric_machines import _1267
    from mastapy.electric_machines.load_cases_and_analyses import _1384
    from mastapy.math_utility.measured_data import _1573, _1574, _1575
    from mastapy.bearings.tolerances import _1925
    from mastapy.bearings.bearing_results import _1952
    from mastapy.bearings.bearing_results.rolling import _1983, _2077
    from mastapy.system_model.analyses_and_results.static_loads import _6819


__docformat__ = "restructuredtext en"
__all__ = ("IndependentReportablePropertiesBase",)


Self = TypeVar("Self", bound="IndependentReportablePropertiesBase")
T = TypeVar("T", bound="IndependentReportablePropertiesBase")


class IndependentReportablePropertiesBase(_0.APIBase, Generic[T]):
    """IndependentReportablePropertiesBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _INDEPENDENT_REPORTABLE_PROPERTIES_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_IndependentReportablePropertiesBase")

    class _Cast_IndependentReportablePropertiesBase:
        """Special nested class for casting IndependentReportablePropertiesBase to subclasses."""

        def __init__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
            parent: "IndependentReportablePropertiesBase",
        ):
            self._parent = parent

        @property
        def oil_pump_detail(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_301.OilPumpDetail":
            from mastapy.materials.efficiency import _301

            return self._parent._cast(_301.OilPumpDetail)

        @property
        def packaging_limits(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_312.PackagingLimits":
            from mastapy.geometry import _312

            return self._parent._cast(_312.PackagingLimits)

        @property
        def specification_for_the_effect_of_oil_kinematic_viscosity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_349.SpecificationForTheEffectOfOilKinematicViscosity":
            from mastapy.gears import _349

            return self._parent._cast(
                _349.SpecificationForTheEffectOfOilKinematicViscosity
            )

        @property
        def cylindrical_gear_micro_geometry_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1024.CylindricalGearMicroGeometrySettings":
            from mastapy.gears.gear_designs.cylindrical import _1024

            return self._parent._cast(_1024.CylindricalGearMicroGeometrySettings)

        @property
        def hardened_material_properties(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1055.HardenedMaterialProperties":
            from mastapy.gears.gear_designs.cylindrical import _1055

            return self._parent._cast(_1055.HardenedMaterialProperties)

        @property
        def ltca_load_case_modifiable_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1063.LTCALoadCaseModifiableSettings":
            from mastapy.gears.gear_designs.cylindrical import _1063

            return self._parent._cast(_1063.LTCALoadCaseModifiableSettings)

        @property
        def ltca_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1064.LTCASettings":
            from mastapy.gears.gear_designs.cylindrical import _1064

            return self._parent._cast(_1064.LTCASettings)

        @property
        def micropitting(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1067.Micropitting":
            from mastapy.gears.gear_designs.cylindrical import _1067

            return self._parent._cast(_1067.Micropitting)

        @property
        def muller_residual_stress_definition(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1068.MullerResidualStressDefinition":
            from mastapy.gears.gear_designs.cylindrical import _1068

            return self._parent._cast(_1068.MullerResidualStressDefinition)

        @property
        def scuffing(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1076.Scuffing":
            from mastapy.gears.gear_designs.cylindrical import _1076

            return self._parent._cast(_1076.Scuffing)

        @property
        def surface_roughness(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1084.SurfaceRoughness":
            from mastapy.gears.gear_designs.cylindrical import _1084

            return self._parent._cast(_1084.SurfaceRoughness)

        @property
        def tiff_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1086.TiffAnalysisSettings":
            from mastapy.gears.gear_designs.cylindrical import _1086

            return self._parent._cast(_1086.TiffAnalysisSettings)

        @property
        def tooth_flank_fracture_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1090.ToothFlankFractureAnalysisSettings":
            from mastapy.gears.gear_designs.cylindrical import _1090

            return self._parent._cast(_1090.ToothFlankFractureAnalysisSettings)

        @property
        def usage(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1094.Usage":
            from mastapy.gears.gear_designs.cylindrical import _1094

            return self._parent._cast(_1094.Usage)

        @property
        def eccentricity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1267.Eccentricity":
            from mastapy.electric_machines import _1267

            return self._parent._cast(_1267.Eccentricity)

        @property
        def temperatures(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1384.Temperatures":
            from mastapy.electric_machines.load_cases_and_analyses import _1384

            return self._parent._cast(_1384.Temperatures)

        @property
        def lookup_table_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1573.LookupTableBase":
            from mastapy.math_utility.measured_data import _1573

            return self._parent._cast(_1573.LookupTableBase)

        @property
        def onedimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1574.OnedimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1574

            return self._parent._cast(_1574.OnedimensionalFunctionLookupTable)

        @property
        def twodimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1575.TwodimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1575

            return self._parent._cast(_1575.TwodimensionalFunctionLookupTable)

        @property
        def roundness_specification(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1925.RoundnessSpecification":
            from mastapy.bearings.tolerances import _1925

            return self._parent._cast(_1925.RoundnessSpecification)

        @property
        def equivalent_load_factors(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1952.EquivalentLoadFactors":
            from mastapy.bearings.bearing_results import _1952

            return self._parent._cast(_1952.EquivalentLoadFactors)

        @property
        def iso14179_settings_per_bearing_type(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1983.ISO14179SettingsPerBearingType":
            from mastapy.bearings.bearing_results.rolling import _1983

            return self._parent._cast(_1983.ISO14179SettingsPerBearingType)

        @property
        def rolling_bearing_friction_coefficients(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_2077.RollingBearingFrictionCoefficients":
            from mastapy.bearings.bearing_results.rolling import _2077

            return self._parent._cast(_2077.RollingBearingFrictionCoefficients)

        @property
        def additional_acceleration_options(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_6819.AdditionalAccelerationOptions":
            from mastapy.system_model.analyses_and_results.static_loads import _6819

            return self._parent._cast(_6819.AdditionalAccelerationOptions)

        @property
        def independent_reportable_properties_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "IndependentReportablePropertiesBase":
            return self._parent

        def __getattr__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
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
        self: Self, instance_to_wrap: "IndependentReportablePropertiesBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase"
    ):
        return self._Cast_IndependentReportablePropertiesBase(self)
