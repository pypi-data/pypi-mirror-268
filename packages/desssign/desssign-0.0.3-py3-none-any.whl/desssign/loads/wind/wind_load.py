from __future__ import annotations

from math import log

from desssign.loads.wind.constants import AIR_DENSITY
from desssign.loads.wind.constants import DIRECTIONAL_FACTOR
from desssign.loads.wind.constants import FUNDAMENTAL_VALUE_OF_BASIC_WIND_VELOCITY
from desssign.loads.wind.constants import MINIMUM_HEIGHT
from desssign.loads.wind.constants import ROUGHNESS_LENGTH
from desssign.loads.wind.constants import SEASONAL_FACTOR
from desssign.loads.wind.enums import TerrainCategory
from desssign.loads.wind.enums import WindZone


class WindLoad:
    """
    Class representing wind load according to EN 1991-1-4.

    :ivar zone: Wind zone.
    :ivar c_dir: Directional factor.
    :ivar c_season: Seasonal factor.
    :ivar rho_air: Density of air in kg/m³.
    """

    def __init__(
        self,
        zone: str | WindZone,
        terrain_category: str | TerrainCategory,
        z_e: float,
        area: float = 10.0,
        c_dir: float = DIRECTIONAL_FACTOR,
        c_season: float = SEASONAL_FACTOR,
        rho_air: float = AIR_DENSITY,
    ) -> None:
        self.zone = zone
        self.terrain_category = terrain_category
        self.z_e = z_e
        self.area = area

        self.c_dir = c_dir
        self.c_season = c_season
        self.rho_air = rho_air

    @property
    def v_b0(self) -> float:
        """
        Fundamental value of basic wind velocity in m/s according to EN 1991-1-4.

        :return: Fundamental value of basic wind velocity in m/s.
        """
        return FUNDAMENTAL_VALUE_OF_BASIC_WIND_VELOCITY[self.zone]

    @property
    def v_b(self) -> float:
        """
        Basic wind velocity in m/s according to EN 1991-1-4, eq. (4.1).

        The basic wind velocity is defined as function of wind direction and time of year
        at 10 m above the ground of terrain category II.

        :return: Basic wind velocity in m/s.
        """
        return self.c_dir * self.c_season * self.v_b0

    @property
    def q_b(self) -> float:
        """
        Basic velocity pressure in N/m² according to EN 1991-1-4, eq. (4.10).

        :return: Basic velocity pressure in N/m².
        """
        return 0.5 * self.rho_air * self.v_b**2

    @property
    def z_0(self) -> float:
        """Roughness length in m according to EN 1991-1-4, table 4.1."""
        return ROUGHNESS_LENGTH[self.terrain_category]

    @property
    def z_min(self) -> float:
        """Minimum height in m according to EN 1991-1-4, table 4.1."""
        return MINIMUM_HEIGHT[self.terrain_category]

    @property
    def z_max(self) -> float:
        """Maximum height in m according to EN 1991-1-4."""
        return 200.0

    @property
    def k_r(self) -> float:
        """
        Terrain factor.

        According to EN 1991-1-4, 4.3.2, eq. (4.5).
        """
        z_0II: float = ROUGHNESS_LENGTH[TerrainCategory.II]

        return 0.19 * (self.z_0 / z_0II) ** 0.07  # type: ignore[no-any-return]

    @property
    def k_l(self) -> float:
        """
        Turbulence factor.

        According to EN 1991-1-4, 4.4.1(1), note 2.
        """
        return 1.0

    @property
    def sigma_v(self) -> float:
        """Standard deviation of the turbulence in m/s according to EN 1991-1-4, 4.4(1), eq. (4.6)."""
        return self.k_r * self.v_b * self.k_l

    @property
    def c_o(self) -> float:
        """Orography factor."""
        return 1.0

    @property
    def c_r(self) -> float:
        """Roughness factor according to EN 1991-1-4, 4.3.2(1), eq. (4.4)."""
        if self.z_min <= self.z_e <= self.z_max:
            return self.k_r * log(self.z_e / self.z_0)
        elif self.z_e < self.z_min:
            return self.k_r * log(self.z_min / self.z_0)
        else:
            raise ValueError("Height above the maximum height is not supported.")

    @property
    def v_m(self) -> float:
        """Mean wind velocity in m/s according to EN 1991-1-4, 4.3.1 (1), eq. (4.3)."""
        return self.c_r * self.c_o * self.v_b

    @property
    def I_v(self) -> float:
        """Turbulence intensity according to EN 1991-1-4, 4.4.1(1), eq. (4.7)."""
        if self.z_min <= self.z_e <= self.z_max:
            return self.sigma_v / self.v_m
        elif self.z_e < self.z_min:
            return self.sigma_v / self.v_m
        else:
            raise ValueError("Height above the maximum height is not supported.")

    @property
    def q_p(self) -> float:
        """Peak velocity pressure in N/m² according to EN 1991-1-4, 4.5.1(1), eq. (4.8)."""
        return (1 + 7 * self.I_v) * 1 / 2 * self.rho_air * self.v_m**2

    @property
    def c_e(self) -> float:
        """Exposure factor according to EN 1991-1-4, 4.5.1(1), eq. (4.9)."""
        return self.q_p / self.q_b
