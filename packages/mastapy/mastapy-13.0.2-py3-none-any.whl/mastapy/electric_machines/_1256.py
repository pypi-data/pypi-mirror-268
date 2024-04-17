"""CADRotor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines import _1300
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_ROTOR = python_net_import("SMT.MastaAPI.ElectricMachines", "CADRotor")

if TYPE_CHECKING:
    from mastapy.electric_machines import _1255


__docformat__ = "restructuredtext en"
__all__ = ("CADRotor",)


Self = TypeVar("Self", bound="CADRotor")


class CADRotor(_1300.Rotor):
    """CADRotor

    This is a mastapy class.
    """

    TYPE = _CAD_ROTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADRotor")

    class _Cast_CADRotor:
        """Special nested class for casting CADRotor to subclasses."""

        def __init__(self: "CADRotor._Cast_CADRotor", parent: "CADRotor"):
            self._parent = parent

        @property
        def rotor(self: "CADRotor._Cast_CADRotor") -> "_1300.Rotor":
            return self._parent._cast(_1300.Rotor)

        @property
        def cad_rotor(self: "CADRotor._Cast_CADRotor") -> "CADRotor":
            return self._parent

        def __getattr__(self: "CADRotor._Cast_CADRotor", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADRotor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def importing_full_rotor(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ImportingFullRotor

        if temp is None:
            return False

        return temp

    @importing_full_rotor.setter
    @enforce_parameter_types
    def importing_full_rotor(self: Self, value: "bool"):
        self.wrapped.ImportingFullRotor = bool(value) if value is not None else False

    @property
    def number_of_imported_poles(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfImportedPoles

        if temp is None:
            return 0

        return temp

    @number_of_imported_poles.setter
    @enforce_parameter_types
    def number_of_imported_poles(self: Self, value: "int"):
        self.wrapped.NumberOfImportedPoles = int(value) if value is not None else 0

    @property
    def number_of_magnet_layers(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfMagnetLayers

        if temp is None:
            return 0

        return temp

    @number_of_magnet_layers.setter
    @enforce_parameter_types
    def number_of_magnet_layers(self: Self, value: "int"):
        self.wrapped.NumberOfMagnetLayers = int(value) if value is not None else 0

    @property
    def offset_of_additional_line_used_for_estimating_kair(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OffsetOfAdditionalLineUsedForEstimatingKair

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @offset_of_additional_line_used_for_estimating_kair.setter
    @enforce_parameter_types
    def offset_of_additional_line_used_for_estimating_kair(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OffsetOfAdditionalLineUsedForEstimatingKair = value

    @property
    def magnet_layers(self: Self) -> "List[_1255.CADMagnetsForLayer]":
        """List[mastapy.electric_machines.CADMagnetsForLayer]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagnetLayers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "CADRotor._Cast_CADRotor":
        return self._Cast_CADRotor(self)
