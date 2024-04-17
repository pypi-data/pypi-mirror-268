"""GearRootFilletStressResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_ROOT_FILLET_STRESS_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearRootFilletStressResults"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _841, _842, _829, _834


__docformat__ = "restructuredtext en"
__all__ = ("GearRootFilletStressResults",)


Self = TypeVar("Self", bound="GearRootFilletStressResults")


class GearRootFilletStressResults(_0.APIBase):
    """GearRootFilletStressResults

    This is a mastapy class.
    """

    TYPE = _GEAR_ROOT_FILLET_STRESS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearRootFilletStressResults")

    class _Cast_GearRootFilletStressResults:
        """Special nested class for casting GearRootFilletStressResults to subclasses."""

        def __init__(
            self: "GearRootFilletStressResults._Cast_GearRootFilletStressResults",
            parent: "GearRootFilletStressResults",
        ):
            self._parent = parent

        @property
        def conical_gear_root_fillet_stress_results(
            self: "GearRootFilletStressResults._Cast_GearRootFilletStressResults",
        ) -> "_829.ConicalGearRootFilletStressResults":
            from mastapy.gears.ltca import _829

            return self._parent._cast(_829.ConicalGearRootFilletStressResults)

        @property
        def cylindrical_gear_root_fillet_stress_results(
            self: "GearRootFilletStressResults._Cast_GearRootFilletStressResults",
        ) -> "_834.CylindricalGearRootFilletStressResults":
            from mastapy.gears.ltca import _834

            return self._parent._cast(_834.CylindricalGearRootFilletStressResults)

        @property
        def gear_root_fillet_stress_results(
            self: "GearRootFilletStressResults._Cast_GearRootFilletStressResults",
        ) -> "GearRootFilletStressResults":
            return self._parent

        def __getattr__(
            self: "GearRootFilletStressResults._Cast_GearRootFilletStressResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearRootFilletStressResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_line_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLineIndex

        if temp is None:
            return 0

        return temp

    @property
    def columns(self: Self) -> "List[_841.GearFilletNodeStressResultsColumn]":
        """List[mastapy.gears.ltca.GearFilletNodeStressResultsColumn]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Columns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rows(self: Self) -> "List[_842.GearFilletNodeStressResultsRow]":
        """List[mastapy.gears.ltca.GearFilletNodeStressResultsRow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearRootFilletStressResults._Cast_GearRootFilletStressResults":
        return self._Cast_GearRootFilletStressResults(self)
