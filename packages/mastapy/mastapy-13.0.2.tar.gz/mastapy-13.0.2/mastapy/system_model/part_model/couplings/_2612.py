"""SynchroniserHalf"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model.couplings import _2613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserHalf"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2611, _2592
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalf",)


Self = TypeVar("Self", bound="SynchroniserHalf")


class SynchroniserHalf(_2613.SynchroniserPart):
    """SynchroniserHalf

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHalf")

    class _Cast_SynchroniserHalf:
        """Special nested class for casting SynchroniserHalf to subclasses."""

        def __init__(
            self: "SynchroniserHalf._Cast_SynchroniserHalf", parent: "SynchroniserHalf"
        ):
            self._parent = parent

        @property
        def synchroniser_part(
            self: "SynchroniserHalf._Cast_SynchroniserHalf",
        ) -> "_2613.SynchroniserPart":
            return self._parent._cast(_2613.SynchroniserPart)

        @property
        def coupling_half(
            self: "SynchroniserHalf._Cast_SynchroniserHalf",
        ) -> "_2592.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2592

            return self._parent._cast(_2592.CouplingHalf)

        @property
        def mountable_component(
            self: "SynchroniserHalf._Cast_SynchroniserHalf",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "SynchroniserHalf._Cast_SynchroniserHalf",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "SynchroniserHalf._Cast_SynchroniserHalf") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "SynchroniserHalf._Cast_SynchroniserHalf",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def synchroniser_half(
            self: "SynchroniserHalf._Cast_SynchroniserHalf",
        ) -> "SynchroniserHalf":
            return self._parent

        def __getattr__(self: "SynchroniserHalf._Cast_SynchroniserHalf", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserHalf.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def area_of_cone_with_minimum_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreaOfConeWithMinimumArea

        if temp is None:
            return 0.0

        return temp

    @property
    def blocker_chamfer_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BlockerChamferAngle

        if temp is None:
            return 0.0

        return temp

    @blocker_chamfer_angle.setter
    @enforce_parameter_types
    def blocker_chamfer_angle(self: Self, value: "float"):
        self.wrapped.BlockerChamferAngle = float(value) if value is not None else 0.0

    @property
    def blocker_chamfer_coefficient_of_friction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BlockerChamferCoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @blocker_chamfer_coefficient_of_friction.setter
    @enforce_parameter_types
    def blocker_chamfer_coefficient_of_friction(self: Self, value: "float"):
        self.wrapped.BlockerChamferCoefficientOfFriction = (
            float(value) if value is not None else 0.0
        )

    @property
    def blocker_chamfer_pcd(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BlockerChamferPCD

        if temp is None:
            return 0.0

        return temp

    @blocker_chamfer_pcd.setter
    @enforce_parameter_types
    def blocker_chamfer_pcd(self: Self, value: "float"):
        self.wrapped.BlockerChamferPCD = float(value) if value is not None else 0.0

    @property
    def cone_side(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConeSide

        if temp is None:
            return ""

        return temp

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
    def number_of_surfaces(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSurfaces

        if temp is None:
            return 0

        return temp

    @number_of_surfaces.setter
    @enforce_parameter_types
    def number_of_surfaces(self: Self, value: "int"):
        self.wrapped.NumberOfSurfaces = int(value) if value is not None else 0

    @property
    def total_area_of_cones(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalAreaOfCones

        if temp is None:
            return 0.0

        return temp

    @property
    def cones(self: Self) -> "List[_2611.SynchroniserCone]":
        """List[mastapy.system_model.part_model.couplings.SynchroniserCone]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "SynchroniserHalf._Cast_SynchroniserHalf":
        return self._Cast_SynchroniserHalf(self)
