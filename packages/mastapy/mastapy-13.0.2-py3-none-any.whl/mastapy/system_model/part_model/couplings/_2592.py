"""CouplingHalf"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2471
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import (
        _2586,
        _2589,
        _2595,
        _2597,
        _2598,
        _2604,
        _2609,
        _2612,
        _2613,
        _2614,
        _2616,
        _2618,
    )
    from mastapy.system_model.part_model import _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalf",)


Self = TypeVar("Self", bound="CouplingHalf")


class CouplingHalf(_2471.MountableComponent):
    """CouplingHalf

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalf")

    class _Cast_CouplingHalf:
        """Special nested class for casting CouplingHalf to subclasses."""

        def __init__(self: "CouplingHalf._Cast_CouplingHalf", parent: "CouplingHalf"):
            self._parent = parent

        @property
        def mountable_component(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2471.MountableComponent":
            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "CouplingHalf._Cast_CouplingHalf") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "CouplingHalf._Cast_CouplingHalf") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def clutch_half(self: "CouplingHalf._Cast_CouplingHalf") -> "_2586.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.ClutchHalf)

        @property
        def concept_coupling_half(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2589.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.ConceptCouplingHalf)

        @property
        def cvt_pulley(self: "CouplingHalf._Cast_CouplingHalf") -> "_2595.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2597.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "CouplingHalf._Cast_CouplingHalf") -> "_2598.Pulley":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.Pulley)

        @property
        def rolling_ring(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2604.RollingRing":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.RollingRing)

        @property
        def spring_damper_half(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2609.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.SpringDamperHalf)

        @property
        def synchroniser_half(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2612.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2612

            return self._parent._cast(_2612.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2613.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2613

            return self._parent._cast(_2613.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2614.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2614

            return self._parent._cast(_2614.SynchroniserSleeve)

        @property
        def torque_converter_pump(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2616.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2616

            return self._parent._cast(_2616.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "CouplingHalf._Cast_CouplingHalf",
        ) -> "_2618.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.TorqueConverterTurbine)

        @property
        def coupling_half(self: "CouplingHalf._Cast_CouplingHalf") -> "CouplingHalf":
            return self._parent

        def __getattr__(self: "CouplingHalf._Cast_CouplingHalf", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalf.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bore.setter
    @enforce_parameter_types
    def bore(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Bore = value

    @property
    def diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Diameter = value

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "CouplingHalf._Cast_CouplingHalf":
        return self._Cast_CouplingHalf(self)
