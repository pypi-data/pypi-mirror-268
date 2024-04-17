"""ConicalGearSetHarmonicLoadData"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6903
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConicalGearSetHarmonicLoadData",
)

if TYPE_CHECKING:
    from mastapy.gears import _352
    from mastapy.math_utility import _1520
    from mastapy.electric_machines.harmonic_load_data import _1387


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetHarmonicLoadData",)


Self = TypeVar("Self", bound="ConicalGearSetHarmonicLoadData")


class ConicalGearSetHarmonicLoadData(_6903.GearSetHarmonicLoadData):
    """ConicalGearSetHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_HARMONIC_LOAD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetHarmonicLoadData")

    class _Cast_ConicalGearSetHarmonicLoadData:
        """Special nested class for casting ConicalGearSetHarmonicLoadData to subclasses."""

        def __init__(
            self: "ConicalGearSetHarmonicLoadData._Cast_ConicalGearSetHarmonicLoadData",
            parent: "ConicalGearSetHarmonicLoadData",
        ):
            self._parent = parent

        @property
        def gear_set_harmonic_load_data(
            self: "ConicalGearSetHarmonicLoadData._Cast_ConicalGearSetHarmonicLoadData",
        ) -> "_6903.GearSetHarmonicLoadData":
            return self._parent._cast(_6903.GearSetHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "ConicalGearSetHarmonicLoadData._Cast_ConicalGearSetHarmonicLoadData",
        ) -> "_1387.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1387

            return self._parent._cast(_1387.HarmonicLoadDataBase)

        @property
        def conical_gear_set_harmonic_load_data(
            self: "ConicalGearSetHarmonicLoadData._Cast_ConicalGearSetHarmonicLoadData",
        ) -> "ConicalGearSetHarmonicLoadData":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetHarmonicLoadData._Cast_ConicalGearSetHarmonicLoadData",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetHarmonicLoadData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def te_specification_type(self: Self) -> "_352.TESpecificationType":
        """mastapy.gears.TESpecificationType"""
        temp = self.wrapped.TESpecificationType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.TESpecificationType")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._352", "TESpecificationType"
        )(value)

    @te_specification_type.setter
    @enforce_parameter_types
    def te_specification_type(self: Self, value: "_352.TESpecificationType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.TESpecificationType"
        )
        self.wrapped.TESpecificationType = value

    @property
    def excitations(self: Self) -> "List[_1520.FourierSeries]":
        """List[mastapy.math_utility.FourierSeries]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def read_data_from_gleason_gemsxml(self: Self):
        """Method does not return."""
        self.wrapped.ReadDataFromGleasonGEMSXML()

    def read_data_from_ki_mo_sxml(self: Self):
        """Method does not return."""
        self.wrapped.ReadDataFromKIMoSXML()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetHarmonicLoadData._Cast_ConicalGearSetHarmonicLoadData":
        return self._Cast_ConicalGearSetHarmonicLoadData(self)
