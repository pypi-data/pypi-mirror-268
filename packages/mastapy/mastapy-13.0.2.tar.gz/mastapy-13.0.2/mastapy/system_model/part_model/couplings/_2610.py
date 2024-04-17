"""Synchroniser"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Synchroniser"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2349
    from mastapy.system_model.part_model.couplings import _2614, _2612
    from mastapy.system_model.part_model import _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("Synchroniser",)


Self = TypeVar("Self", bound="Synchroniser")


class Synchroniser(_2483.SpecialisedAssembly):
    """Synchroniser

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Synchroniser")

    class _Cast_Synchroniser:
        """Special nested class for casting Synchroniser to subclasses."""

        def __init__(self: "Synchroniser._Cast_Synchroniser", parent: "Synchroniser"):
            self._parent = parent

        @property
        def specialised_assembly(
            self: "Synchroniser._Cast_Synchroniser",
        ) -> "_2483.SpecialisedAssembly":
            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "Synchroniser._Cast_Synchroniser",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "Synchroniser._Cast_Synchroniser") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "Synchroniser._Cast_Synchroniser",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def synchroniser(self: "Synchroniser._Cast_Synchroniser") -> "Synchroniser":
            return self._parent

        def __getattr__(self: "Synchroniser._Cast_Synchroniser", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Synchroniser.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_left_cone(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasLeftCone

        if temp is None:
            return False

        return temp

    @has_left_cone.setter
    @enforce_parameter_types
    def has_left_cone(self: Self, value: "bool"):
        self.wrapped.HasLeftCone = bool(value) if value is not None else False

    @property
    def has_right_cone(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasRightCone

        if temp is None:
            return False

        return temp

    @has_right_cone.setter
    @enforce_parameter_types
    def has_right_cone(self: Self, value: "bool"):
        self.wrapped.HasRightCone = bool(value) if value is not None else False

    @property
    def clutch_connection_left(self: Self) -> "_2349.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnectionLeft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def clutch_connection_right(self: Self) -> "_2349.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnectionRight

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hub_and_sleeve(self: Self) -> "_2614.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HubAndSleeve

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_cone(self: Self) -> "_2612.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftCone

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_cone(self: Self) -> "_2612.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightCone

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Synchroniser._Cast_Synchroniser":
        return self._Cast_Synchroniser(self)
