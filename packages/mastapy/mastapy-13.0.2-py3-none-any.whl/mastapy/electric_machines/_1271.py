"""ElectricMachineMeshingOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MESHING_OPTIONS = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "ElectricMachineMeshingOptions"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1251
    from mastapy.nodal_analysis import _61


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineMeshingOptions",)


Self = TypeVar("Self", bound="ElectricMachineMeshingOptions")


class ElectricMachineMeshingOptions(_1272.ElectricMachineMeshingOptionsBase):
    """ElectricMachineMeshingOptions

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_MESHING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineMeshingOptions")

    class _Cast_ElectricMachineMeshingOptions:
        """Special nested class for casting ElectricMachineMeshingOptions to subclasses."""

        def __init__(
            self: "ElectricMachineMeshingOptions._Cast_ElectricMachineMeshingOptions",
            parent: "ElectricMachineMeshingOptions",
        ):
            self._parent = parent

        @property
        def electric_machine_meshing_options_base(
            self: "ElectricMachineMeshingOptions._Cast_ElectricMachineMeshingOptions",
        ) -> "_1272.ElectricMachineMeshingOptionsBase":
            return self._parent._cast(_1272.ElectricMachineMeshingOptionsBase)

        @property
        def fe_meshing_options(
            self: "ElectricMachineMeshingOptions._Cast_ElectricMachineMeshingOptions",
        ) -> "_61.FEMeshingOptions":
            from mastapy.nodal_analysis import _61

            return self._parent._cast(_61.FEMeshingOptions)

        @property
        def electric_machine_meshing_options(
            self: "ElectricMachineMeshingOptions._Cast_ElectricMachineMeshingOptions",
        ) -> "ElectricMachineMeshingOptions":
            return self._parent

        def __getattr__(
            self: "ElectricMachineMeshingOptions._Cast_ElectricMachineMeshingOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineMeshingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def air_gap_element_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AirGapElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @air_gap_element_size.setter
    @enforce_parameter_types
    def air_gap_element_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AirGapElementSize = value

    @property
    def air_gap_partition(self: Self) -> "_1251.AirGapPartition":
        """mastapy.electric_machines.AirGapPartition"""
        temp = self.wrapped.AirGapPartition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.AirGapPartition"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1251", "AirGapPartition"
        )(value)

    @air_gap_partition.setter
    @enforce_parameter_types
    def air_gap_partition(self: Self, value: "_1251.AirGapPartition"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.AirGapPartition"
        )
        self.wrapped.AirGapPartition = value

    @property
    def conductor_element_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ConductorElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @conductor_element_size.setter
    @enforce_parameter_types
    def conductor_element_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ConductorElementSize = value

    @property
    def magnet_element_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MagnetElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @magnet_element_size.setter
    @enforce_parameter_types
    def magnet_element_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MagnetElementSize = value

    @property
    def number_of_element_layers_in_air_gap(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfElementLayersInAirGap

        if temp is None:
            return 0

        return temp

    @number_of_element_layers_in_air_gap.setter
    @enforce_parameter_types
    def number_of_element_layers_in_air_gap(self: Self, value: "int"):
        self.wrapped.NumberOfElementLayersInAirGap = (
            int(value) if value is not None else 0
        )

    @property
    def rotor_element_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RotorElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rotor_element_size.setter
    @enforce_parameter_types
    def rotor_element_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RotorElementSize = value

    @property
    def slot_element_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SlotElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @slot_element_size.setter
    @enforce_parameter_types
    def slot_element_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SlotElementSize = value

    @property
    def stator_element_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.StatorElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @stator_element_size.setter
    @enforce_parameter_types
    def stator_element_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.StatorElementSize = value

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineMeshingOptions._Cast_ElectricMachineMeshingOptions":
        return self._Cast_ElectricMachineMeshingOptions(self)
