"""BearingDetailConfiguration"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.configurations import _2625
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_CONFIGURATION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Configurations", "BearingDetailConfiguration"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingDetailConfiguration",)


Self = TypeVar("Self", bound="BearingDetailConfiguration")


class BearingDetailConfiguration(
    _2625.PartDetailConfiguration[
        "_2624.BearingDetailSelection", "_2446.Bearing", "_2137.BearingDesign"
    ]
):
    """BearingDetailConfiguration

    This is a mastapy class.
    """

    TYPE = _BEARING_DETAIL_CONFIGURATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingDetailConfiguration")

    class _Cast_BearingDetailConfiguration:
        """Special nested class for casting BearingDetailConfiguration to subclasses."""

        def __init__(
            self: "BearingDetailConfiguration._Cast_BearingDetailConfiguration",
            parent: "BearingDetailConfiguration",
        ):
            self._parent = parent

        @property
        def part_detail_configuration(
            self: "BearingDetailConfiguration._Cast_BearingDetailConfiguration",
        ) -> "_2625.PartDetailConfiguration":
            return self._parent._cast(_2625.PartDetailConfiguration)

        @property
        def bearing_detail_configuration(
            self: "BearingDetailConfiguration._Cast_BearingDetailConfiguration",
        ) -> "BearingDetailConfiguration":
            return self._parent

        def __getattr__(
            self: "BearingDetailConfiguration._Cast_BearingDetailConfiguration",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingDetailConfiguration.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BearingDetailConfiguration._Cast_BearingDetailConfiguration":
        return self._Cast_BearingDetailConfiguration(self)
