"""ThermoElasticFactor"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THERMO_ELASTIC_FACTOR = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "ThermoElasticFactor"
)


__docformat__ = "restructuredtext en"
__all__ = ("ThermoElasticFactor",)


Self = TypeVar("Self", bound="ThermoElasticFactor")


class ThermoElasticFactor(_1612.MeasurementBase):
    """ThermoElasticFactor

    This is a mastapy class.
    """

    TYPE = _THERMO_ELASTIC_FACTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ThermoElasticFactor")

    class _Cast_ThermoElasticFactor:
        """Special nested class for casting ThermoElasticFactor to subclasses."""

        def __init__(
            self: "ThermoElasticFactor._Cast_ThermoElasticFactor",
            parent: "ThermoElasticFactor",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "ThermoElasticFactor._Cast_ThermoElasticFactor",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def thermo_elastic_factor(
            self: "ThermoElasticFactor._Cast_ThermoElasticFactor",
        ) -> "ThermoElasticFactor":
            return self._parent

        def __getattr__(
            self: "ThermoElasticFactor._Cast_ThermoElasticFactor", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ThermoElasticFactor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ThermoElasticFactor._Cast_ThermoElasticFactor":
        return self._Cast_ThermoElasticFactor(self)
