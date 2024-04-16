from __future__ import annotations

from framesss.pre.material import Material

from desssign.loads.enums import LoadDurationClass
from desssign.wood.constants import get_modification_factor
from desssign.wood.constants import get_partial_factor
from desssign.wood.enums import ServiceClass
from desssign.wood.enums import WoodType
from desssign.wood.strength_classes import WOOD_STRENGTH_CLASSES


class WoodMaterial(Material):
    """
    Class for structural wood material.

    Inherits from Material class and adds specific properties of wood.

    :param strength_class: Strength class of the wood material.
    :param service_class: Service class of the wood material.
    """

    def __init__(
        self,
        strength_class: str,
        service_class: int | ServiceClass,
    ) -> None:
        """Init the WoodMaterial object."""
        if strength_class not in WOOD_STRENGTH_CLASSES:
            raise ValueError(f"Invalid strength class: {strength_class}")

        self.strength_class = strength_class
        self.wood_type = (
            WoodType.SOLID_TIMBER
        )  # TODO: Add wood type to strength classes
        self.service_class = ServiceClass(service_class)

        wood_properties = WOOD_STRENGTH_CLASSES[strength_class]

        self.f_mk = wood_properties["f_mk"]

        self.f_t0k = wood_properties["f_t0k"]
        self.f_t90k = wood_properties["f_t90k"]
        self.f_c0k = wood_properties["f_c0k"]
        self.f_c90k = wood_properties["f_c90k"]
        self.f_vk = wood_properties["f_vk"]
        self.E_m0mean = wood_properties["E_m0mean"]
        self.E_m0k = wood_properties["E_m0k"]
        self.E_m90mean = wood_properties["E_m90mean"]
        self.G_mean = wood_properties["G_mean"]
        self.rho_k = wood_properties["rho_k"]
        self.rho_mean = wood_properties["rho_mean"]

        poisson = self.E_m0mean / (2 * self.G_mean) - 1

        super().__init__(
            label=strength_class,
            elastic_modulus=self.E_m0k,
            poissons_ratio=poisson,
            thermal_expansion_coefficient=0.5e-6,  # According to EN 1995-1-5, table C.1
            density=self.rho_mean,
        )

    def __repr__(self) -> str:
        """Return the string representation of the WoodMaterial object."""
        return f"WoodMaterial({self.strength_class})"

    @property
    def gamma_m(self) -> float:
        """Partial factor according to EN 1995-1-1, table 2.5."""
        return get_partial_factor(self.wood_type)

    def get_design_value(
        self,
        characteristic_value: float,
        load_duration_class: str | LoadDurationClass,
    ) -> float:
        """
        Return the design value of a characteristic value.

        EN 1995-1-1, 2.4.1, eq. (2.14)

        :param characteristic_value: Characteristic value.
        :param load_duration_class: Load duration class.
        :return: Design value.
        """
        load_duration_class = LoadDurationClass(load_duration_class)

        k_mod = get_modification_factor(
            self.wood_type, self.service_class, load_duration_class
        )
        return k_mod * characteristic_value / self.gamma_m

    @property
    def beta_c(self) -> float:
        """Factor for members within the straightness limits defined in Section 10 of EN 1995-1-1."""
        if self.wood_type == WoodType.SOLID_TIMBER:
            return 0.2
        elif self.wood_type == WoodType.GLUED_LAMINATED_TIMBER:
            return 0.1
        elif self.wood_type == WoodType.LVL:
            return 0.1
        else:
            raise AttributeError(f"Invalid wood type: {self.wood_type}")
