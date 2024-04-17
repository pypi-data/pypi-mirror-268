"""HarmonicLoadDataFluxImport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6907
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_FLUX_IMPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataFluxImport",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6919,
        _6911,
        _6910,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataFluxImport",)


Self = TypeVar("Self", bound="HarmonicLoadDataFluxImport")


class HarmonicLoadDataFluxImport(
    _6907.HarmonicLoadDataCSVImport[
        "_6888.ElectricMachineHarmonicLoadFluxImportOptions"
    ]
):
    """HarmonicLoadDataFluxImport

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_FLUX_IMPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicLoadDataFluxImport")

    class _Cast_HarmonicLoadDataFluxImport:
        """Special nested class for casting HarmonicLoadDataFluxImport to subclasses."""

        def __init__(
            self: "HarmonicLoadDataFluxImport._Cast_HarmonicLoadDataFluxImport",
            parent: "HarmonicLoadDataFluxImport",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_csv_import(
            self: "HarmonicLoadDataFluxImport._Cast_HarmonicLoadDataFluxImport",
        ) -> "_6907.HarmonicLoadDataCSVImport":
            return self._parent._cast(_6907.HarmonicLoadDataCSVImport)

        @property
        def harmonic_load_data_import_from_motor_packages(
            self: "HarmonicLoadDataFluxImport._Cast_HarmonicLoadDataFluxImport",
        ) -> "_6911.HarmonicLoadDataImportFromMotorPackages":
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.HarmonicLoadDataImportFromMotorPackages)

        @property
        def harmonic_load_data_import_base(
            self: "HarmonicLoadDataFluxImport._Cast_HarmonicLoadDataFluxImport",
        ) -> "_6910.HarmonicLoadDataImportBase":
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(_6910.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_flux_import(
            self: "HarmonicLoadDataFluxImport._Cast_HarmonicLoadDataFluxImport",
        ) -> "HarmonicLoadDataFluxImport":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataFluxImport._Cast_HarmonicLoadDataFluxImport",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicLoadDataFluxImport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_of_node_ring_from_flux_file(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterOfNodeRingFromFluxFile

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_diameter_reference(self: Self) -> "_6919.InnerDiameterReference":
        """mastapy.system_model.analyses_and_results.static_loads.InnerDiameterReference"""
        temp = self.wrapped.InnerDiameterReference

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.InnerDiameterReference",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.static_loads._6919",
            "InnerDiameterReference",
        )(value)

    @inner_diameter_reference.setter
    @enforce_parameter_types
    def inner_diameter_reference(self: Self, value: "_6919.InnerDiameterReference"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.InnerDiameterReference",
        )
        self.wrapped.InnerDiameterReference = value

    def select_flux_file(self: Self):
        """Method does not return."""
        self.wrapped.SelectFluxFile()

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicLoadDataFluxImport._Cast_HarmonicLoadDataFluxImport":
        return self._Cast_HarmonicLoadDataFluxImport(self)
