from __future__ import annotations

import math
from typing import TYPE_CHECKING

from framesss.pre.section import RectangularSection

from desssign.wood.enums import WoodType

if TYPE_CHECKING:
    from desssign.wood.wood_material import WoodMaterial


class WoodRectangularSection(RectangularSection):
    """
    Class for wood rectangular section.

    Inherits from `RectangularSection` class and adds specific properties of wood.

    :param label: Label of the section.
    :param b: Width of the section.
    :param h: Height of the section.
    :param material: Wood material of the section.
    """

    material: WoodMaterial  # Explicit type annotation, so that mypy can check the type

    def __init__(
        self,
        label: str,
        b: float,
        h: float,
        material: WoodMaterial,
    ) -> None:
        super().__init__(label, b, h, material)

    @property
    def i_y(self) -> float:
        """Radius of gyration to the y-axis."""
        return math.sqrt(self.inertia_y / self.area_y)

    @property
    def i_z(self) -> float:
        """Radius of gyration to the z-axis."""
        return math.sqrt(self.inertia_z / self.area_z)

    @property
    def W_y(self) -> float:
        """Elastic section modulus to the y-axis."""
        return self.inertia_y / (0.5 * self.height_z)

    @property
    def W_z(self) -> float:
        """Elastic section modulus to the z-axis."""
        return self.inertia_z / (0.5 * self.height_y)

    @property
    def k_m(self) -> float:
        """
        Factor considering re-distribution of bending stresses in a cross-section.

        EN 1995-1-1, 6.1.6(2)
        """
        if (
            self.material.wood_type == WoodType.SOLID_TIMBER
            or self.material.wood_type == WoodType.GLUED_LAMINATED_TIMBER
            or self.material.wood_type == WoodType.LVL
        ):
            return 0.7
        else:
            return 1.0

    @property
    def k_cr(self) -> float:
        """
        Crack factor for shear resistance.

        EN 1995-1-1, 6.1.7 (2), eq. (6.13a)
        """
        if self.material.wood_type == WoodType.SOLID_TIMBER:
            return 0.67
        elif self.material.wood_type == WoodType.GLUED_LAMINATED_TIMBER:
            return 0.67
        else:
            return 1.0

    def get_k_h(self, type_of_stress: str) -> float:
        """
        Depth factor.

        EN 1995-1-1, 3.2(3):
            For rectangular solid timber with a characteristic timber density `rho_k` <= 700 kg/m3,
            the reference depth in bending or width (maximum cross-sectional dimension) in tension
            is 150 mm. For depths in bending or widths in tension of solid timber less than 150 mm
            the characteristic values for `f_mk` and `f_t0k` may be increased by the factor `k_h`.

        :param type_of_stress: Type of stress, either 'bending' or 'tension'.
        """
        if self.material.rho_k > 700:
            return 1.0

        if type_of_stress.lower() == "bending":
            h = self.height_z
        elif type_of_stress.lower() == "tension":
            h = max(self.height_z, self.height_y)
        else:
            raise AttributeError(
                f"Invalid type of stress: '{type_of_stress}'. Use either 'bending' or 'tension'."
            )

        if h <= 0:
            raise ValueError(
                "Height or width of the section must be greater than zero."
            )

        return float(min((150 / h) ** 0.2, 1.3))
