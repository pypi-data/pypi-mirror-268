from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from desssign.loads.snow.enums import SnowZone
    from desssign.loads.snow.enums import Topography

from desssign.loads.snow.constants import EXPOSURE_COEFFICIENTS
from desssign.loads.snow.constants import SNOW_LOAD_ON_THE_GROUND


def calculate_shape_coefficient(
    roof_pitch_angle: float, is_prevented_sliding: bool = False
) -> float:
    """
    Calculate the shape coefficient for snow load calculations.

    This function takes in account only monopitched and pitched roofs.

    :param roof_pitch_angle: The angle of pitch of the roof in degrees.
    :param is_prevented_sliding: Whether the snow is prevented from sliding off the roof.
                                 Where snow fences or other obstructions exist or where
                                 the lower edge of the roof is terminated with a parapet.
    :return: The shape coefficients.
    """
    if is_prevented_sliding:
        return 0.8
    else:
        if 0 <= roof_pitch_angle <= 30:
            return 0.8
        elif 30 < roof_pitch_angle < 60:
            return 0.8 * (60 - roof_pitch_angle) / 30
        else:
            return 0.0


def calculate_snow_load_on_the_roof(
    roof_pitch_angle: float,
    snow_zone: str | SnowZone,
    topography: str | Topography,
    thermal_coefficient: float = 1.0,
    is_prevented_sliding: bool = False,
) -> float:
    """
    Calculate the snow load on the roof according to EN 1991-1-3.

    :param roof_pitch_angle: The angle of pitch of the roof in degrees.
    :param snow_zone: The snow zone according to CZ NA.
    :param topography: The topography considering future development around the site.
    :param thermal_coefficient: The thermal coefficient.
    :param is_prevented_sliding: Whether the snow is prevented from sliding off the roof.
                                 Where snow fences or other obstructions exist or where
                                 the lower edge of the roof is terminated with a parapet.
    """
    mu_1 = calculate_shape_coefficient(roof_pitch_angle, is_prevented_sliding)
    c_e = EXPOSURE_COEFFICIENTS[topography]
    c_t = thermal_coefficient
    s_k = SNOW_LOAD_ON_THE_GROUND[snow_zone]

    return mu_1 * c_e * c_t * s_k
