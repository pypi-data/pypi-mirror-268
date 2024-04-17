"""RadialInternalClearanceTolerance"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model import _2466
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RADIAL_INTERNAL_CLEARANCE_TOLERANCE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "RadialInternalClearanceTolerance"
)


__docformat__ = "restructuredtext en"
__all__ = ("RadialInternalClearanceTolerance",)


Self = TypeVar("Self", bound="RadialInternalClearanceTolerance")


class RadialInternalClearanceTolerance(_2466.InternalClearanceTolerance):
    """RadialInternalClearanceTolerance

    This is a mastapy class.
    """

    TYPE = _RADIAL_INTERNAL_CLEARANCE_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RadialInternalClearanceTolerance")

    class _Cast_RadialInternalClearanceTolerance:
        """Special nested class for casting RadialInternalClearanceTolerance to subclasses."""

        def __init__(
            self: "RadialInternalClearanceTolerance._Cast_RadialInternalClearanceTolerance",
            parent: "RadialInternalClearanceTolerance",
        ):
            self._parent = parent

        @property
        def internal_clearance_tolerance(
            self: "RadialInternalClearanceTolerance._Cast_RadialInternalClearanceTolerance",
        ) -> "_2466.InternalClearanceTolerance":
            return self._parent._cast(_2466.InternalClearanceTolerance)

        @property
        def radial_internal_clearance_tolerance(
            self: "RadialInternalClearanceTolerance._Cast_RadialInternalClearanceTolerance",
        ) -> "RadialInternalClearanceTolerance":
            return self._parent

        def __getattr__(
            self: "RadialInternalClearanceTolerance._Cast_RadialInternalClearanceTolerance",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RadialInternalClearanceTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "RadialInternalClearanceTolerance._Cast_RadialInternalClearanceTolerance":
        return self._Cast_RadialInternalClearanceTolerance(self)
