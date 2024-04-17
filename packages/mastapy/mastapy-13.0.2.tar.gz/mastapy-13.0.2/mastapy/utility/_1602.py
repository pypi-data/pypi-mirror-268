"""PersistentSingleton"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERSISTENT_SINGLETON = python_net_import("SMT.MastaAPI.Utility", "PersistentSingleton")

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _68
    from mastapy.nodal_analysis.geometry_modeller_link import _163
    from mastapy.gears.materials import _599
    from mastapy.gears.ltca.cylindrical import _858
    from mastapy.gears.gear_designs.cylindrical import _1015
    from mastapy.utility import _1601, _1603, _1604
    from mastapy.utility.units_and_measurements import _1613
    from mastapy.utility.scripting import _1746
    from mastapy.utility.databases import _1834
    from mastapy.utility.cad_export import _1839
    from mastapy.bearings import _1906
    from mastapy.system_model.part_model import _2477


__docformat__ = "restructuredtext en"
__all__ = ("PersistentSingleton",)


Self = TypeVar("Self", bound="PersistentSingleton")


class PersistentSingleton(_0.APIBase):
    """PersistentSingleton

    This is a mastapy class.
    """

    TYPE = _PERSISTENT_SINGLETON
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PersistentSingleton")

    class _Cast_PersistentSingleton:
        """Special nested class for casting PersistentSingleton to subclasses."""

        def __init__(
            self: "PersistentSingleton._Cast_PersistentSingleton",
            parent: "PersistentSingleton",
        ):
            self._parent = parent

        @property
        def fe_user_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_68.FEUserSettings":
            from mastapy.nodal_analysis import _68

            return self._parent._cast(_68.FEUserSettings)

        @property
        def geometry_modeller_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_163.GeometryModellerSettings":
            from mastapy.nodal_analysis.geometry_modeller_link import _163

            return self._parent._cast(_163.GeometryModellerSettings)

        @property
        def gear_material_expert_system_factor_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_599.GearMaterialExpertSystemFactorSettings":
            from mastapy.gears.materials import _599

            return self._parent._cast(_599.GearMaterialExpertSystemFactorSettings)

        @property
        def cylindrical_gear_fe_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_858.CylindricalGearFESettings":
            from mastapy.gears.ltca.cylindrical import _858

            return self._parent._cast(_858.CylindricalGearFESettings)

        @property
        def cylindrical_gear_defaults(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_1015.CylindricalGearDefaults":
            from mastapy.gears.gear_designs.cylindrical import _1015

            return self._parent._cast(_1015.CylindricalGearDefaults)

        @property
        def per_machine_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_1601.PerMachineSettings":
            from mastapy.utility import _1601

            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def program_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_1603.ProgramSettings":
            from mastapy.utility import _1603

            return self._parent._cast(_1603.ProgramSettings)

        @property
        def pushbullet_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_1604.PushbulletSettings":
            from mastapy.utility import _1604

            return self._parent._cast(_1604.PushbulletSettings)

        @property
        def measurement_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_1613.MeasurementSettings":
            from mastapy.utility.units_and_measurements import _1613

            return self._parent._cast(_1613.MeasurementSettings)

        @property
        def scripting_setup(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_1746.ScriptingSetup":
            from mastapy.utility.scripting import _1746

            return self._parent._cast(_1746.ScriptingSetup)

        @property
        def database_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_1834.DatabaseSettings":
            from mastapy.utility.databases import _1834

            return self._parent._cast(_1834.DatabaseSettings)

        @property
        def cad_export_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_1839.CADExportSettings":
            from mastapy.utility.cad_export import _1839

            return self._parent._cast(_1839.CADExportSettings)

        @property
        def skf_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_1906.SKFSettings":
            from mastapy.bearings import _1906

            return self._parent._cast(_1906.SKFSettings)

        @property
        def planet_carrier_settings(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "_2477.PlanetCarrierSettings":
            from mastapy.system_model.part_model import _2477

            return self._parent._cast(_2477.PlanetCarrierSettings)

        @property
        def persistent_singleton(
            self: "PersistentSingleton._Cast_PersistentSingleton",
        ) -> "PersistentSingleton":
            return self._parent

        def __getattr__(
            self: "PersistentSingleton._Cast_PersistentSingleton", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PersistentSingleton.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def save(self: Self):
        """Method does not return."""
        self.wrapped.Save()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "PersistentSingleton._Cast_PersistentSingleton":
        return self._Cast_PersistentSingleton(self)
