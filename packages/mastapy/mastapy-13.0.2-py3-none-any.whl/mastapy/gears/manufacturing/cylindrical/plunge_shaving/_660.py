"""VirtualPlungeShaverOutputs"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _654
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_PLUNGE_SHAVER_OUTPUTS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "VirtualPlungeShaverOutputs",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _718


__docformat__ = "restructuredtext en"
__all__ = ("VirtualPlungeShaverOutputs",)


Self = TypeVar("Self", bound="VirtualPlungeShaverOutputs")


class VirtualPlungeShaverOutputs(_654.PlungeShaverOutputs):
    """VirtualPlungeShaverOutputs

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_PLUNGE_SHAVER_OUTPUTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualPlungeShaverOutputs")

    class _Cast_VirtualPlungeShaverOutputs:
        """Special nested class for casting VirtualPlungeShaverOutputs to subclasses."""

        def __init__(
            self: "VirtualPlungeShaverOutputs._Cast_VirtualPlungeShaverOutputs",
            parent: "VirtualPlungeShaverOutputs",
        ):
            self._parent = parent

        @property
        def plunge_shaver_outputs(
            self: "VirtualPlungeShaverOutputs._Cast_VirtualPlungeShaverOutputs",
        ) -> "_654.PlungeShaverOutputs":
            return self._parent._cast(_654.PlungeShaverOutputs)

        @property
        def virtual_plunge_shaver_outputs(
            self: "VirtualPlungeShaverOutputs._Cast_VirtualPlungeShaverOutputs",
        ) -> "VirtualPlungeShaverOutputs":
            return self._parent

        def __getattr__(
            self: "VirtualPlungeShaverOutputs._Cast_VirtualPlungeShaverOutputs",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualPlungeShaverOutputs.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_modification_on_conjugate_shaver_chart_left_flank(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadModificationOnConjugateShaverChartLeftFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def lead_modification_on_conjugate_shaver_chart_right_flank(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadModificationOnConjugateShaverChartRightFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def shaver(self: Self) -> "_718.CylindricalGearShaver":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearShaver

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaver

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualPlungeShaverOutputs._Cast_VirtualPlungeShaverOutputs":
        return self._Cast_VirtualPlungeShaverOutputs(self)
