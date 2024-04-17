"""HarmonicLoadDataMotorCADImport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.analyses_and_results.static_loads import _6911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_MOTOR_CAD_IMPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataMotorCADImport",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6910


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataMotorCADImport",)


Self = TypeVar("Self", bound="HarmonicLoadDataMotorCADImport")


class HarmonicLoadDataMotorCADImport(
    _6911.HarmonicLoadDataImportFromMotorPackages[
        "_6891.ElectricMachineHarmonicLoadMotorCADImportOptions"
    ]
):
    """HarmonicLoadDataMotorCADImport

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_MOTOR_CAD_IMPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicLoadDataMotorCADImport")

    class _Cast_HarmonicLoadDataMotorCADImport:
        """Special nested class for casting HarmonicLoadDataMotorCADImport to subclasses."""

        def __init__(
            self: "HarmonicLoadDataMotorCADImport._Cast_HarmonicLoadDataMotorCADImport",
            parent: "HarmonicLoadDataMotorCADImport",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_import_from_motor_packages(
            self: "HarmonicLoadDataMotorCADImport._Cast_HarmonicLoadDataMotorCADImport",
        ) -> "_6911.HarmonicLoadDataImportFromMotorPackages":
            return self._parent._cast(_6911.HarmonicLoadDataImportFromMotorPackages)

        @property
        def harmonic_load_data_import_base(
            self: "HarmonicLoadDataMotorCADImport._Cast_HarmonicLoadDataMotorCADImport",
        ) -> "_6910.HarmonicLoadDataImportBase":
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(_6910.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_motor_cad_import(
            self: "HarmonicLoadDataMotorCADImport._Cast_HarmonicLoadDataMotorCADImport",
        ) -> "HarmonicLoadDataMotorCADImport":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataMotorCADImport._Cast_HarmonicLoadDataMotorCADImport",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicLoadDataMotorCADImport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def derive_rotor_forces_from_stator_loads(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DeriveRotorForcesFromStatorLoads

        if temp is None:
            return False

        return temp

    @derive_rotor_forces_from_stator_loads.setter
    @enforce_parameter_types
    def derive_rotor_forces_from_stator_loads(self: Self, value: "bool"):
        self.wrapped.DeriveRotorForcesFromStatorLoads = (
            bool(value) if value is not None else False
        )

    def select_motor_cad_file(self: Self):
        """Method does not return."""
        self.wrapped.SelectMotorCADFile()

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicLoadDataMotorCADImport._Cast_HarmonicLoadDataMotorCADImport":
        return self._Cast_HarmonicLoadDataMotorCADImport(self)
