"""CycloidalAssembly"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalAssembly"
)

if TYPE_CHECKING:
    from mastapy.cycloidal import _1460
    from mastapy.system_model.part_model.cycloidal import _2577, _2576
    from mastapy.system_model.part_model import _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssembly",)


Self = TypeVar("Self", bound="CycloidalAssembly")


class CycloidalAssembly(_2483.SpecialisedAssembly):
    """CycloidalAssembly

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalAssembly")

    class _Cast_CycloidalAssembly:
        """Special nested class for casting CycloidalAssembly to subclasses."""

        def __init__(
            self: "CycloidalAssembly._Cast_CycloidalAssembly",
            parent: "CycloidalAssembly",
        ):
            self._parent = parent

        @property
        def specialised_assembly(
            self: "CycloidalAssembly._Cast_CycloidalAssembly",
        ) -> "_2483.SpecialisedAssembly":
            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "CycloidalAssembly._Cast_CycloidalAssembly",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "CycloidalAssembly._Cast_CycloidalAssembly") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "CycloidalAssembly._Cast_CycloidalAssembly",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cycloidal_assembly(
            self: "CycloidalAssembly._Cast_CycloidalAssembly",
        ) -> "CycloidalAssembly":
            return self._parent

        def __getattr__(self: "CycloidalAssembly._Cast_CycloidalAssembly", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalAssembly.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cycloidal_assembly_design(self: Self) -> "_1460.CycloidalAssemblyDesign":
        """mastapy.cycloidal.CycloidalAssemblyDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalAssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_pins(self: Self) -> "_2577.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPins

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def known_designs(self: Self) -> "List[_1460.CycloidalAssemblyDesign]":
        """List[mastapy.cycloidal.CycloidalAssemblyDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KnownDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_disc(self: Self) -> "_2576.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc"""
        method_result = self.wrapped.AddDisc()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def design_named(self: Self, name: "str") -> "_1460.CycloidalAssemblyDesign":
        """mastapy.cycloidal.CycloidalAssemblyDesign

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.DesignNamed(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def remove_disc_from_designs(self: Self, disc_id: "int"):
        """Method does not return.

        Args:
            disc_id (int)
        """
        disc_id = int(disc_id)
        self.wrapped.RemoveDiscFromDesigns(disc_id if disc_id else 0)

    @enforce_parameter_types
    def set_active_cycloidal_assembly_design(
        self: Self, cycloidal_assembly_design: "_1460.CycloidalAssemblyDesign"
    ):
        """Method does not return.

        Args:
            cycloidal_assembly_design (mastapy.cycloidal.CycloidalAssemblyDesign)
        """
        self.wrapped.SetActiveCycloidalAssemblyDesign(
            cycloidal_assembly_design.wrapped if cycloidal_assembly_design else None
        )

    @enforce_parameter_types
    def try_remove_design(
        self: Self, design: "_1460.CycloidalAssemblyDesign"
    ) -> "bool":
        """bool

        Args:
            design (mastapy.cycloidal.CycloidalAssemblyDesign)
        """
        method_result = self.wrapped.TryRemoveDesign(design.wrapped if design else None)
        return method_result

    @property
    def cast_to(self: Self) -> "CycloidalAssembly._Cast_CycloidalAssembly":
        return self._Cast_CycloidalAssembly(self)
