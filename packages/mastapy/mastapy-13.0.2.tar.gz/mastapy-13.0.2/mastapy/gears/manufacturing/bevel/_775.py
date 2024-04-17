"""AbstractTCA"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_TCA = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "AbstractTCA"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1166
    from mastapy.gears.manufacturing.bevel import _798


__docformat__ = "restructuredtext en"
__all__ = ("AbstractTCA",)


Self = TypeVar("Self", bound="AbstractTCA")


class AbstractTCA(_0.APIBase):
    """AbstractTCA

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_TCA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractTCA")

    class _Cast_AbstractTCA:
        """Special nested class for casting AbstractTCA to subclasses."""

        def __init__(self: "AbstractTCA._Cast_AbstractTCA", parent: "AbstractTCA"):
            self._parent = parent

        @property
        def ease_off_based_tca(
            self: "AbstractTCA._Cast_AbstractTCA",
        ) -> "_798.EaseOffBasedTCA":
            from mastapy.gears.manufacturing.bevel import _798

            return self._parent._cast(_798.EaseOffBasedTCA)

        @property
        def abstract_tca(self: "AbstractTCA._Cast_AbstractTCA") -> "AbstractTCA":
            return self._parent

        def __getattr__(self: "AbstractTCA._Cast_AbstractTCA", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractTCA.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_transmission_error_with_respect_to_wheel(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTransmissionErrorWithRespectToWheel

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_transmission_error_with_respect_to_wheel(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeakTransmissionErrorWithRespectToWheel

        if temp is None:
            return 0.0

        return temp

    @property
    def conical_mesh_misalignments(self: Self) -> "_1166.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshMisalignments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "AbstractTCA._Cast_AbstractTCA":
        return self._Cast_AbstractTCA(self)
