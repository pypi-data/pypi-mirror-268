"""ToothThicknessSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical import _1092
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_THICKNESS_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ToothThicknessSpecification"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1071


__docformat__ = "restructuredtext en"
__all__ = ("ToothThicknessSpecification",)


Self = TypeVar("Self", bound="ToothThicknessSpecification")


class ToothThicknessSpecification(_1092.ToothThicknessSpecificationBase):
    """ToothThicknessSpecification

    This is a mastapy class.
    """

    TYPE = _TOOTH_THICKNESS_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToothThicknessSpecification")

    class _Cast_ToothThicknessSpecification:
        """Special nested class for casting ToothThicknessSpecification to subclasses."""

        def __init__(
            self: "ToothThicknessSpecification._Cast_ToothThicknessSpecification",
            parent: "ToothThicknessSpecification",
        ):
            self._parent = parent

        @property
        def tooth_thickness_specification_base(
            self: "ToothThicknessSpecification._Cast_ToothThicknessSpecification",
        ) -> "_1092.ToothThicknessSpecificationBase":
            return self._parent._cast(_1092.ToothThicknessSpecificationBase)

        @property
        def readonly_tooth_thickness_specification(
            self: "ToothThicknessSpecification._Cast_ToothThicknessSpecification",
        ) -> "_1071.ReadonlyToothThicknessSpecification":
            from mastapy.gears.gear_designs.cylindrical import _1071

            return self._parent._cast(_1071.ReadonlyToothThicknessSpecification)

        @property
        def tooth_thickness_specification(
            self: "ToothThicknessSpecification._Cast_ToothThicknessSpecification",
        ) -> "ToothThicknessSpecification":
            return self._parent

        def __getattr__(
            self: "ToothThicknessSpecification._Cast_ToothThicknessSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ToothThicknessSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ToothThicknessSpecification._Cast_ToothThicknessSpecification":
        return self._Cast_ToothThicknessSpecification(self)
