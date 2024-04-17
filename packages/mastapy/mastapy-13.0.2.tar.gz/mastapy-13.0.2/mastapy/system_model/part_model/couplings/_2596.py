"""PartToPartShearCoupling"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2591
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCoupling"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2355
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCoupling",)


Self = TypeVar("Self", bound="PartToPartShearCoupling")


class PartToPartShearCoupling(_2591.Coupling):
    """PartToPartShearCoupling

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartToPartShearCoupling")

    class _Cast_PartToPartShearCoupling:
        """Special nested class for casting PartToPartShearCoupling to subclasses."""

        def __init__(
            self: "PartToPartShearCoupling._Cast_PartToPartShearCoupling",
            parent: "PartToPartShearCoupling",
        ):
            self._parent = parent

        @property
        def coupling(
            self: "PartToPartShearCoupling._Cast_PartToPartShearCoupling",
        ) -> "_2591.Coupling":
            return self._parent._cast(_2591.Coupling)

        @property
        def specialised_assembly(
            self: "PartToPartShearCoupling._Cast_PartToPartShearCoupling",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "PartToPartShearCoupling._Cast_PartToPartShearCoupling",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(
            self: "PartToPartShearCoupling._Cast_PartToPartShearCoupling",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "PartToPartShearCoupling._Cast_PartToPartShearCoupling",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def part_to_part_shear_coupling(
            self: "PartToPartShearCoupling._Cast_PartToPartShearCoupling",
        ) -> "PartToPartShearCoupling":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCoupling._Cast_PartToPartShearCoupling", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartToPartShearCoupling.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part_to_part_shear_coupling_connection(
        self: Self,
    ) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartToPartShearCouplingConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PartToPartShearCoupling._Cast_PartToPartShearCoupling":
        return self._Cast_PartToPartShearCoupling(self)
