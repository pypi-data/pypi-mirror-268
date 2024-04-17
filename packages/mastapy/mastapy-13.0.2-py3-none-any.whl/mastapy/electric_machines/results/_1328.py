"""DynamicForceResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.electric_machines.harmonic_load_data import _1385
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_RESULTS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "DynamicForceResults"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1520
    from mastapy.electric_machines.harmonic_load_data import _1390, _1387


__docformat__ = "restructuredtext en"
__all__ = ("DynamicForceResults",)


Self = TypeVar("Self", bound="DynamicForceResults")


class DynamicForceResults(_1385.ElectricMachineHarmonicLoadDataBase):
    """DynamicForceResults

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicForceResults")

    class _Cast_DynamicForceResults:
        """Special nested class for casting DynamicForceResults to subclasses."""

        def __init__(
            self: "DynamicForceResults._Cast_DynamicForceResults",
            parent: "DynamicForceResults",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data_base(
            self: "DynamicForceResults._Cast_DynamicForceResults",
        ) -> "_1385.ElectricMachineHarmonicLoadDataBase":
            return self._parent._cast(_1385.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(
            self: "DynamicForceResults._Cast_DynamicForceResults",
        ) -> "_1390.SpeedDependentHarmonicLoadData":
            from mastapy.electric_machines.harmonic_load_data import _1390

            return self._parent._cast(_1390.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "DynamicForceResults._Cast_DynamicForceResults",
        ) -> "_1387.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1387

            return self._parent._cast(_1387.HarmonicLoadDataBase)

        @property
        def dynamic_force_results(
            self: "DynamicForceResults._Cast_DynamicForceResults",
        ) -> "DynamicForceResults":
            return self._parent

        def __getattr__(
            self: "DynamicForceResults._Cast_DynamicForceResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicForceResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitations(self: Self) -> "List[_1520.FourierSeries]":
        """List[mastapy.math_utility.FourierSeries]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "DynamicForceResults._Cast_DynamicForceResults":
        return self._Cast_DynamicForceResults(self)
