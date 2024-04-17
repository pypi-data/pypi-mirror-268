"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._645 import CalculationError
    from ._646 import ChartType
    from ._647 import GearPointCalculationError
    from ._648 import MicroGeometryDefinitionMethod
    from ._649 import MicroGeometryDefinitionType
    from ._650 import PlungeShaverCalculation
    from ._651 import PlungeShaverCalculationInputs
    from ._652 import PlungeShaverGeneration
    from ._653 import PlungeShaverInputsAndMicroGeometry
    from ._654 import PlungeShaverOutputs
    from ._655 import PlungeShaverSettings
    from ._656 import PointOfInterest
    from ._657 import RealPlungeShaverOutputs
    from ._658 import ShaverPointCalculationError
    from ._659 import ShaverPointOfInterest
    from ._660 import VirtualPlungeShaverOutputs
else:
    import_structure = {
        "_645": ["CalculationError"],
        "_646": ["ChartType"],
        "_647": ["GearPointCalculationError"],
        "_648": ["MicroGeometryDefinitionMethod"],
        "_649": ["MicroGeometryDefinitionType"],
        "_650": ["PlungeShaverCalculation"],
        "_651": ["PlungeShaverCalculationInputs"],
        "_652": ["PlungeShaverGeneration"],
        "_653": ["PlungeShaverInputsAndMicroGeometry"],
        "_654": ["PlungeShaverOutputs"],
        "_655": ["PlungeShaverSettings"],
        "_656": ["PointOfInterest"],
        "_657": ["RealPlungeShaverOutputs"],
        "_658": ["ShaverPointCalculationError"],
        "_659": ["ShaverPointOfInterest"],
        "_660": ["VirtualPlungeShaverOutputs"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculationError",
    "ChartType",
    "GearPointCalculationError",
    "MicroGeometryDefinitionMethod",
    "MicroGeometryDefinitionType",
    "PlungeShaverCalculation",
    "PlungeShaverCalculationInputs",
    "PlungeShaverGeneration",
    "PlungeShaverInputsAndMicroGeometry",
    "PlungeShaverOutputs",
    "PlungeShaverSettings",
    "PointOfInterest",
    "RealPlungeShaverOutputs",
    "ShaverPointCalculationError",
    "ShaverPointOfInterest",
    "VirtualPlungeShaverOutputs",
)
