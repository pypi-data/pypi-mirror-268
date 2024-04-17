"""RollingRing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.couplings import _2592
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRing"
)

if TYPE_CHECKING:
    from mastapy.gears import _336
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("RollingRing",)


Self = TypeVar("Self", bound="RollingRing")


class RollingRing(_2592.CouplingHalf):
    """RollingRing

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRing")

    class _Cast_RollingRing:
        """Special nested class for casting RollingRing to subclasses."""

        def __init__(self: "RollingRing._Cast_RollingRing", parent: "RollingRing"):
            self._parent = parent

        @property
        def coupling_half(
            self: "RollingRing._Cast_RollingRing",
        ) -> "_2592.CouplingHalf":
            return self._parent._cast(_2592.CouplingHalf)

        @property
        def mountable_component(
            self: "RollingRing._Cast_RollingRing",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "RollingRing._Cast_RollingRing") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "RollingRing._Cast_RollingRing") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "RollingRing._Cast_RollingRing",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def rolling_ring(self: "RollingRing._Cast_RollingRing") -> "RollingRing":
            return self._parent

        def __getattr__(self: "RollingRing._Cast_RollingRing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AverageDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @average_diameter.setter
    @enforce_parameter_types
    def average_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AverageDiameter = value

    @property
    def is_internal(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsInternal

        if temp is None:
            return False

        return temp

    @is_internal.setter
    @enforce_parameter_types
    def is_internal(self: Self, value: "bool"):
        self.wrapped.IsInternal = bool(value) if value is not None else False

    @property
    def largest_end(self: Self) -> "_336.Hand":
        """mastapy.gears.Hand"""
        temp = self.wrapped.LargestEnd

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.Hand")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._336", "Hand")(value)

    @largest_end.setter
    @enforce_parameter_types
    def largest_end(self: Self, value: "_336.Hand"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.Hand")
        self.wrapped.LargestEnd = value

    @property
    def cast_to(self: Self) -> "RollingRing._Cast_RollingRing":
        return self._Cast_RollingRing(self)
