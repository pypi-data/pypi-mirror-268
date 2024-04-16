from desssign.loads.snow.enums import SnowZone
from desssign.loads.snow.enums import Topography

EXPOSURE_COEFFICIENTS = {
    Topography.WINDSWEPT: 0.8,
    Topography.NORMAL: 1.0,
    Topography.SHELTERED: 1.2,
}

SNOW_LOAD_ON_THE_GROUND = {
    SnowZone.I: 0.7,
    SnowZone.II: 1.0,
    SnowZone.III: 1.5,
    SnowZone.IV: 2.0,
    SnowZone.V: 2.5,
    SnowZone.VI: 3.0,
    SnowZone.VII: 4.0,
    SnowZone.VIII: 0.0,
}
