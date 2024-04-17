"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._734 import CutterSimulationCalc
    from ._735 import CylindricalCutterSimulatableGear
    from ._736 import CylindricalGearSpecification
    from ._737 import CylindricalManufacturedRealGearInMesh
    from ._738 import CylindricalManufacturedVirtualGearInMesh
    from ._739 import FinishCutterSimulation
    from ._740 import FinishStockPoint
    from ._741 import FormWheelGrindingSimulationCalculator
    from ._742 import GearCutterSimulation
    from ._743 import HobSimulationCalculator
    from ._744 import ManufacturingOperationConstraints
    from ._745 import ManufacturingProcessControls
    from ._746 import RackSimulationCalculator
    from ._747 import RoughCutterSimulation
    from ._748 import ShaperSimulationCalculator
    from ._749 import ShavingSimulationCalculator
    from ._750 import VirtualSimulationCalculator
    from ._751 import WormGrinderSimulationCalculator
else:
    import_structure = {
        "_734": ["CutterSimulationCalc"],
        "_735": ["CylindricalCutterSimulatableGear"],
        "_736": ["CylindricalGearSpecification"],
        "_737": ["CylindricalManufacturedRealGearInMesh"],
        "_738": ["CylindricalManufacturedVirtualGearInMesh"],
        "_739": ["FinishCutterSimulation"],
        "_740": ["FinishStockPoint"],
        "_741": ["FormWheelGrindingSimulationCalculator"],
        "_742": ["GearCutterSimulation"],
        "_743": ["HobSimulationCalculator"],
        "_744": ["ManufacturingOperationConstraints"],
        "_745": ["ManufacturingProcessControls"],
        "_746": ["RackSimulationCalculator"],
        "_747": ["RoughCutterSimulation"],
        "_748": ["ShaperSimulationCalculator"],
        "_749": ["ShavingSimulationCalculator"],
        "_750": ["VirtualSimulationCalculator"],
        "_751": ["WormGrinderSimulationCalculator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterSimulationCalc",
    "CylindricalCutterSimulatableGear",
    "CylindricalGearSpecification",
    "CylindricalManufacturedRealGearInMesh",
    "CylindricalManufacturedVirtualGearInMesh",
    "FinishCutterSimulation",
    "FinishStockPoint",
    "FormWheelGrindingSimulationCalculator",
    "GearCutterSimulation",
    "HobSimulationCalculator",
    "ManufacturingOperationConstraints",
    "ManufacturingProcessControls",
    "RackSimulationCalculator",
    "RoughCutterSimulation",
    "ShaperSimulationCalculator",
    "ShavingSimulationCalculator",
    "VirtualSimulationCalculator",
    "WormGrinderSimulationCalculator",
)
