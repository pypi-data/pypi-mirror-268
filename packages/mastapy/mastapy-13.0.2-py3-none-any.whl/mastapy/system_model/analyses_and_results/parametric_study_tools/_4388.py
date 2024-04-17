"""MonteCarloDistribution"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MONTE_CARLO_DISTRIBUTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "MonteCarloDistribution",
)


__docformat__ = "restructuredtext en"
__all__ = ("MonteCarloDistribution",)


Self = TypeVar("Self", bound="MonteCarloDistribution")


class MonteCarloDistribution(Enum):
    """MonteCarloDistribution

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MONTE_CARLO_DISTRIBUTION

    NORMAL_DISTRIBUTION = 1
    UNIFORM_DISTRIBUTION = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MonteCarloDistribution.__setattr__ = __enum_setattr
MonteCarloDistribution.__delattr__ = __enum_delattr
