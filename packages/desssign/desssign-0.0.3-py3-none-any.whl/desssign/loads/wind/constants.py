from desssign.loads.wind.enums import TerrainCategory
from desssign.loads.wind.enums import WindZone

# Fundamental value of basic wind velocity (v_b0) in m/s.
FUNDAMENTAL_VALUE_OF_BASIC_WIND_VELOCITY: dict[str, float] = {
    WindZone.I: 22.5,
    WindZone.II: 25.0,
    WindZone.III: 27.5,
    WindZone.IV: 30.0,
    WindZone.V: 36.0,
}

# Directional factor (c_dir)
DIRECTIONAL_FACTOR: float = 1.0

# Seasonal factor (c_season)
SEASONAL_FACTOR: float = 1.0

# Density of air (rho_air) in kg/m³.
AIR_DENSITY: float = 1.25

# Roughness length (z_0) in m, according to EN 1991-1-4, table 4.1.
ROUGHNESS_LENGTH: dict[str, float] = {
    TerrainCategory.O: 0.003,
    TerrainCategory.I: 0.01,
    TerrainCategory.II: 0.05,
    TerrainCategory.III: 0.3,
    TerrainCategory.IV: 1.0,
}

# Minimum height (z_min) in m, according to EN 1991-1-4, table 4.1.
MINIMUM_HEIGHT: dict[str, float] = {
    TerrainCategory.O: 1.0,
    TerrainCategory.I: 1.0,
    TerrainCategory.II: 2.0,
    TerrainCategory.III: 5.0,
    TerrainCategory.IV: 10.0,
}
