"""FinishToothThicknessDesignSpecification"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.cylindrical import _1092
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FINISH_TOOTH_THICKNESS_DESIGN_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "FinishToothThicknessDesignSpecification",
)


__docformat__ = "restructuredtext en"
__all__ = ("FinishToothThicknessDesignSpecification",)


Self = TypeVar("Self", bound="FinishToothThicknessDesignSpecification")


class FinishToothThicknessDesignSpecification(_1092.ToothThicknessSpecificationBase):
    """FinishToothThicknessDesignSpecification

    This is a mastapy class.
    """

    TYPE = _FINISH_TOOTH_THICKNESS_DESIGN_SPECIFICATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FinishToothThicknessDesignSpecification"
    )

    class _Cast_FinishToothThicknessDesignSpecification:
        """Special nested class for casting FinishToothThicknessDesignSpecification to subclasses."""

        def __init__(
            self: "FinishToothThicknessDesignSpecification._Cast_FinishToothThicknessDesignSpecification",
            parent: "FinishToothThicknessDesignSpecification",
        ):
            self._parent = parent

        @property
        def tooth_thickness_specification_base(
            self: "FinishToothThicknessDesignSpecification._Cast_FinishToothThicknessDesignSpecification",
        ) -> "_1092.ToothThicknessSpecificationBase":
            return self._parent._cast(_1092.ToothThicknessSpecificationBase)

        @property
        def finish_tooth_thickness_design_specification(
            self: "FinishToothThicknessDesignSpecification._Cast_FinishToothThicknessDesignSpecification",
        ) -> "FinishToothThicknessDesignSpecification":
            return self._parent

        def __getattr__(
            self: "FinishToothThicknessDesignSpecification._Cast_FinishToothThicknessDesignSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "FinishToothThicknessDesignSpecification.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "FinishToothThicknessDesignSpecification._Cast_FinishToothThicknessDesignSpecification":
        return self._Cast_FinishToothThicknessDesignSpecification(self)
