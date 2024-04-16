from __future__ import annotations

from desssign.loads.wind.enums import FlatRoofType

# mypy: ignore-errors


FLAT_ROOF_SHARP_EAVES = {
    "F": {"c_pe10": -1.8, "c_pe1": -2.5},
    "G": {"c_pe10": -1.2, "c_pe1": -2.0},
    "H": {"c_pe10": -0.7, "c_pe1": -1.2},
    "I": {
        "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        "-": {"c_pe10": -0.2, "c_pe1": -0.2},
    },
}

FLAT_ROOF_PARAPETS = {
    0.025: {
        "F": {"c_pe10": -1.6, "c_pe1": -2.2},
        "G": {"c_pe10": -1.1, "c_pe1": -1.8},
        "H": {"c_pe10": -0.7, "c_pe1": -1.2},
        "I": {
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
            "-": {"c_pe10": -0.2, "c_pe1": -0.2},
        },
    },
    0.050: {
        "F": {"c_pe10": -1.4, "c_pe1": -2.0},
        "G": {"c_pe10": -0.9, "c_pe1": -1.6},
        "H": {"c_pe10": -0.7, "c_pe1": -1.2},
        "I": {
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
            "-": {"c_pe10": -0.2, "c_pe1": -0.2},
        },
    },
    0.100: {
        "F": {"c_pe10": -1.2, "c_pe1": -1.8},
        "G": {"c_pe10": -0.8, "c_pe1": -1.4},
        "H": {"c_pe10": -0.7, "c_pe1": -1.2},
        "I": {
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
            "-": {"c_pe10": -0.2, "c_pe1": -0.2},
        },
    },
}


def linear_interpolation(x: float, x1: float, x2: float, y1: float, y2: float) -> float:
    """
    Linear interpolation formula to find y for a given x.

    :param x: The x value for which y is to be found.
    :param x1: The x value of the first point.
    :param x2: The x value of the second point.
    :param y1: The y value of the first point.
    :param y2: The y value of the second point.
    :return: The interpolated y value.
    """
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)


def get_flat_roof_coefficient(
    flat_roof_type: str | FlatRoofType,
    zone_key: str,
    coefficient_label: str,
    sign: str | None = None,
    ratio: float | None = None,
) -> float:
    """
    Get the external pressure coefficient for flat roofs with sharp eaves or with parapets.

    :param flat_roof_type: The type of flat roof, either 'sharp_eaves' or 'with_parapets'.
    :param zone_key: The zone key for the external pressure coefficient.
    :param coefficient_label: The label of the coefficient to be retrieved, either 'c_pu10' or 'c_pu1'.
    :param sign: The sign of the coefficient, either '+' (pressure) or '-' (suction).
    :param ratio: The ratio of the height of the parapet to the height of the building.
    """
    if flat_roof_type == FlatRoofType.SHARP_EAVES:
        coefficients_data = FLAT_ROOF_SHARP_EAVES
        area_data = coefficients_data.get(zone_key, {})

        # Check for nested data within the area
        if sign and isinstance(area_data, dict) and sign in area_data:
            area_data = area_data[sign]

        return area_data.get(coefficient_label)

    elif flat_roof_type == FlatRoofType.WITH_PARAPETS:
        coefficients_data = FLAT_ROOF_PARAPETS
    else:
        raise ValueError(
            "The 'flat_roof_type' parameter must be either 'sharp_eaves' or 'with_parapets'."
        )

    if ratio is not None:
        sorted_keys = sorted(coefficients_data.keys())

        if (
            ratio < sorted_keys[0]
        ):  # Use the lowest boundary value if ratio is below the minimum
            ratio = sorted_keys[0]
        elif (
            ratio > sorted_keys[-1]
        ):  # Use the highest boundary value if ratio is above the maximum
            ratio = sorted_keys[-1]

        lower_key = None
        upper_key = None

        for key in sorted_keys:
            if key <= ratio:
                lower_key = key
            if key >= ratio and upper_key is None:
                upper_key = key
            if lower_key and upper_key:
                break

        # Extract data for interpolation or direct use
        lower_data = coefficients_data[lower_key][zone_key]
        upper_data = coefficients_data[upper_key][zone_key]

        # Check for nested data (sub-areas)
        if sign and isinstance(lower_data, dict) and sign in lower_data:
            lower_data = lower_data[sign]
            upper_data = upper_data[sign]

        if (
            lower_key == ratio or lower_key == upper_key
        ):  # Exact match or only one key available
            return lower_data[coefficient_label]

        # Perform interpolation for the specific coefficient
        return linear_interpolation(
            ratio,
            lower_key,
            upper_key,
            lower_data[coefficient_label],
            upper_data[coefficient_label],
        )
    else:
        raise ValueError(
            "The ratio parameter must be provided for flat roofs with parapets."
        )


MONOPITCH_ROOF_COEFFICIENTS_0 = {
    5: {
        "F": {
            "-": {"c_pe10": -1.7, "c_pe1": -2.5},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
        "G": {
            "-": {"c_pe10": -1.2, "c_pe1": -2.0},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
        "H": {
            "-": {"c_pe10": -0.6, "c_pe1": -1.2},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
    },
    15: {
        "F": {
            "-": {"c_pe10": -0.9, "c_pe1": -2.0},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
        "G": {
            "-": {"c_pe10": -0.8, "c_pe1": -1.5},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
        "H": {
            "-": {"c_pe10": -0.3, "c_pe1": -0.3},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
    },
    30: {
        "F": {
            "-": {"c_pe10": -0.5, "c_pe1": -1.5},
            "+": {"c_pe10": +0.7, "c_pe1": +0.7},
        },
        "G": {
            "-": {"c_pe10": -0.5, "c_pe1": -1.5},
            "+": {"c_pe10": +0.7, "c_pe1": +0.7},
        },
        "H": {
            "-": {"c_pe10": -0.2, "c_pe1": -0.2},
            "+": {"c_pe10": +0.4, "c_pe1": +0.4},
        },
    },
    45: {
        "F": {
            "-": {"c_pe10": -0.0, "c_pe1": -0.0},
            "+": {"c_pe10": +0.7, "c_pe1": +0.7},
        },
        "G": {
            "-": {"c_pe10": -0.0, "c_pe1": -0.0},
            "+": {"c_pe10": +0.7, "c_pe1": +0.7},
        },
        "H": {
            "-": {"c_pe10": -0.0, "c_pe1": -0.0},
            "+": {"c_pe10": +0.6, "c_pe1": +0.6},
        },
    },
    60: {
        "F": {"c_pe10": +0.7, "c_pe1": +0.7},
        "G": {"c_pe10": +0.7, "c_pe1": +0.7},
        "H": {"c_pe10": +0.7, "c_pe1": +0.7},
    },
    75: {
        "F": {"c_pe10": +0.8, "c_pe1": +0.8},
        "G": {"c_pe10": +0.8, "c_pe1": +0.8},
        "H": {"c_pe10": +0.8, "c_pe1": +0.8},
    },
}

MONOPITCH_ROOF_COEFFICIENTS_180 = {
    5: {
        "F": {"c_pe10": -2.3, "c_pe1": -2.5},
        "G": {"c_pe10": -1.3, "c_pe1": -2.0},
        "H": {"c_pe10": -0.8, "c_pe1": -1.2},
    },
    15: {
        "F": {"c_pe10": -2.5, "c_pe1": -2.8},
        "G": {"c_pe10": -1.3, "c_pe1": -2.0},
        "H": {"c_pe10": -0.9, "c_pe1": -1.2},
    },
    30: {
        "F": {"c_pe10": -1.1, "c_pe1": -2.3},
        "G": {"c_pe10": -0.8, "c_pe1": -1.5},
        "H": {"c_pe10": -0.8, "c_pe1": -0.8},
    },
    45: {
        "F": {"c_pe10": -0.6, "c_pe1": -1.3},
        "G": {"c_pe10": -0.5, "c_pe1": -0.5},
        "H": {"c_pe10": -0.7, "c_pe1": -0.7},
    },
    60: {
        "F": {"c_pe10": -0.5, "c_pe1": -1.0},
        "G": {"c_pe10": -0.5, "c_pe1": -0.5},
        "H": {"c_pe10": -0.5, "c_pe1": -0.5},
    },
    75: {
        "F": {"c_pe10": -0.5, "c_pe1": -1.0},
        "G": {"c_pe10": -0.5, "c_pe1": -0.5},
        "H": {"c_pe10": -0.5, "c_pe1": -0.5},
    },
}

MONOPITCH_ROOF_COEFFICIENTS_90 = {
    5: {
        "F_up": {"c_pe10": -2.1, "c_pe1": -2.6},
        "F_low": {"c_pe10": -2.1, "c_pe1": -2.4},
        "G": {"c_pe10": -1.8, "c_pe1": -2.0},
        "H": {"c_pe10": -0.6, "c_pe1": -1.2},
        "I": {"c_pe10": -0.5, "c_pe1": -0.5},
    },
    15: {
        "F_up": {"c_pe10": -2.4, "c_pe1": -2.9},
        "F_low": {"c_pe10": -1.6, "c_pe1": -2.4},
        "G": {"c_pe10": -1.9, "c_pe1": -2.5},
        "H": {"c_pe10": -0.8, "c_pe1": -1.2},
        "I": {"c_pe10": -0.7, "c_pe1": -1.2},
    },
    30: {
        "F_up": {"c_pe10": -2.1, "c_pe1": -2.9},
        "F_low": {"c_pe10": -1.3, "c_pe1": -2.0},
        "G": {"c_pe10": -1.5, "c_pe1": -2.0},
        "H": {"c_pe10": -1.0, "c_pe1": -1.3},
        "I": {"c_pe10": -0.8, "c_pe1": -1.2},
    },
    45: {
        "F_up": {"c_pe10": -1.5, "c_pe1": -2.4},
        "F_low": {"c_pe10": -1.3, "c_pe1": -2.0},
        "G": {"c_pe10": -1.4, "c_pe1": -2.0},
        "H": {"c_pe10": -1.0, "c_pe1": -1.3},
        "I": {"c_pe10": -0.9, "c_pe1": -1.2},
    },
    60: {
        "F_up": {"c_pe10": -1.2, "c_pe1": -2.0},
        "F_low": {"c_pe10": -1.2, "c_pe1": -2.0},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -1.0, "c_pe1": -1.3},
        "I": {"c_pe10": -0.7, "c_pe1": -1.2},
    },
    75: {
        "F_up": {"c_pe10": -1.2, "c_pe1": -2.0},
        "F_low": {"c_pe10": -1.2, "c_pe1": -2.0},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -1.0, "c_pe1": -1.3},
        "I": {"c_pe10": -0.5, "c_pe1": -0.5},
    },
}

DUOPITCH_ROOF_COEFFICIENTS_0 = {
    -45: {
        "F": {"c_pe10": -0.6, "c_pe1": -0.6},
        "G": {"c_pe10": -0.6, "c_pe1": -0.6},
        "H": {"c_pe10": -0.8, "c_pe1": -0.8},
        "I": {"c_pe10": -0.7, "c_pe1": -0.7},
        "J": {"c_pe10": -1.0, "c_pe1": -1.5},
    },
    -30: {
        "F": {"c_pe10": -1.1, "c_pe1": -2.0},
        "G": {"c_pe10": -0.8, "c_pe1": -1.5},
        "H": {"c_pe10": -0.8, "c_pe1": -0.8},
        "I": {"c_pe10": -0.6, "c_pe1": -0.6},
        "J": {"c_pe10": -0.8, "c_pe1": -1.4},
    },
    -15: {
        "F": {"c_pe10": -2.5, "c_pe1": -2.8},
        "G": {"c_pe10": -1.3, "c_pe1": -2.0},
        "H": {"c_pe10": -0.9, "c_pe1": -1.2},
        "I": {"c_pe10": -0.5, "c_pe1": -0.5},
        "J": {"c_pe10": -0.7, "c_pe1": -1.2},
    },
    -5: {
        "F": {"c_pe10": -2.3, "c_pe1": -2.5},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -0.8, "c_pe1": -1.2},
        "I": {
            "-": {"c_pe10": -0.6, "c_pe1": -0.6},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
        "J": {
            "-": {"c_pe10": -0.6, "c_pe1": -0.6},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
    },
    0: {
        "F": {"c_pe10": -1.8, "c_pe1": -2.5},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -0.7, "c_pe1": -1.2},
        "I": {
            "-": {"c_pe10": -0.2, "c_pe1": -0.2},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
        "J": {
            "-": {"c_pe10": -0.6, "c_pe1": -0.6},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
    },
    5: {
        "F": {
            "-": {"c_pe10": -1.7, "c_pe1": -2.5},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
        "G": {
            "-": {"c_pe10": -1.2, "c_pe1": -2.0},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
        "H": {
            "-": {"c_pe10": -0.6, "c_pe1": -1.2},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
        "I": {
            "-": {"c_pe10": -0.6, "c_pe1": -0.6},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
        "J": {
            "-": {"c_pe10": -0.6, "c_pe1": -0.6},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
    },
    15: {
        "F": {
            "-": {"c_pe10": -0.9, "c_pe1": -2.0},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
        "G": {
            "-": {"c_pe10": -0.8, "c_pe1": -1.5},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
        "H": {
            "-": {"c_pe10": -0.3, "c_pe1": -0.3},
            "+": {"c_pe10": +0.2, "c_pe1": +0.2},
        },
        "I": {
            "-": {"c_pe10": -0.4, "c_pe1": -0.4},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
        "J": {
            "-": {"c_pe10": -1.0, "c_pe1": -1.5},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
    },
    30: {
        "F": {
            "-": {"c_pe10": -0.5, "c_pe1": -1.5},
            "+": {"c_pe10": +0.7, "c_pe1": +0.7},
        },
        "G": {
            "-": {"c_pe10": -0.5, "c_pe1": -1.5},
            "+": {"c_pe10": +0.7, "c_pe1": +0.7},
        },
        "H": {
            "-": {"c_pe10": -0.2, "c_pe1": -0.2},
            "+": {"c_pe10": +0.4, "c_pe1": +0.4},
        },
        "I": {
            "-": {"c_pe10": -0.4, "c_pe1": -0.4},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
        "J": {
            "-": {"c_pe10": -0.5, "c_pe1": -0.5},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
    },
    45: {
        "F": {
            "-": {"c_pe10": -0.0, "c_pe1": -0.0},
            "+": {"c_pe10": +0.7, "c_pe1": +0.7},
        },
        "G": {
            "-": {"c_pe10": -0.0, "c_pe1": -0.0},
            "+": {"c_pe10": +0.7, "c_pe1": +0.7},
        },
        "H": {
            "-": {"c_pe10": -0.0, "c_pe1": -0.0},
            "+": {"c_pe10": +0.6, "c_pe1": +0.6},
        },
        "I": {
            "-": {"c_pe10": -0.2, "c_pe1": -0.2},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
        "J": {
            "-": {"c_pe10": -0.3, "c_pe1": -0.3},
            "+": {"c_pe10": +0.0, "c_pe1": +0.0},
        },
    },
    60: {
        "F": {"c_pe10": +0.7, "c_pe1": +0.7},
        "G": {"c_pe10": +0.7, "c_pe1": +0.7},
        "H": {"c_pe10": +0.7, "c_pe1": +0.7},
        "I": {"c_pe10": -0.2, "c_pe1": -0.2},
        "J": {"c_pe10": -0.3, "c_pe1": -0.3},
    },
    75: {
        "F": {"c_pe10": +0.8, "c_pe1": +0.8},
        "G": {"c_pe10": +0.8, "c_pe1": +0.8},
        "H": {"c_pe10": +0.8, "c_pe1": +0.8},
        "I": {"c_pe10": -0.2, "c_pe1": -0.2},
        "J": {"c_pe10": -0.3, "c_pe1": -0.3},
    },
}

DUOPITCH_ROOF_COEFFICIENTS_90 = {
    -45: {
        "F": {"c_pe10": -1.4, "c_pe1": -2.0},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -1.0, "c_pe1": -1.3},
        "I": {"c_pe10": -0.9, "c_pe1": -1.2},
    },
    -30: {
        "F": {"c_pe10": -1.5, "c_pe1": -2.1},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -1.0, "c_pe1": -1.3},
        "I": {"c_pe10": -0.9, "c_pe1": -1.2},
    },
    -15: {
        "F": {"c_pe10": -1.9, "c_pe1": -2.5},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -0.8, "c_pe1": -1.2},
        "I": {"c_pe10": -0.8, "c_pe1": -1.2},
    },
    -5: {
        "F": {"c_pe10": -1.8, "c_pe1": -2.5},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -0.7, "c_pe1": -1.2},
        "I": {"c_pe10": -0.6, "c_pe1": -1.2},
    },
    5: {
        "F": {"c_pe10": -1.6, "c_pe1": -2.2},
        "G": {"c_pe10": -1.3, "c_pe1": -2.0},
        "H": {"c_pe10": -0.7, "c_pe1": -1.2},
        "I": {"c_pe10": -0.6, "c_pe1": -0.6},
    },
    15: {
        "F": {"c_pe10": -1.3, "c_pe1": -2.0},
        "G": {"c_pe10": -1.3, "c_pe1": -2.0},
        "H": {"c_pe10": -0.6, "c_pe1": -1.2},
        "I": {"c_pe10": -0.5, "c_pe1": -0.5},
    },
    30: {
        "F": {"c_pe10": -1.1, "c_pe1": -1.5},
        "G": {"c_pe10": -1.4, "c_pe1": -2.0},
        "H": {"c_pe10": -0.8, "c_pe1": -1.2},
        "I": {"c_pe10": -0.5, "c_pe1": -0.5},
    },
    45: {
        "F": {"c_pe10": -1.1, "c_pe1": -1.5},
        "G": {"c_pe10": -1.4, "c_pe1": -2.0},
        "H": {"c_pe10": -0.9, "c_pe1": -1.2},
        "I": {"c_pe10": -0.5, "c_pe1": -0.5},
    },
    60: {
        "F": {"c_pe10": -1.1, "c_pe1": -1.5},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -0.8, "c_pe1": -1.0},
        "I": {"c_pe10": -0.5, "c_pe1": -0.5},
    },
    75: {
        "F": {"c_pe10": -1.1, "c_pe1": -1.5},
        "G": {"c_pe10": -1.2, "c_pe1": -2.0},
        "H": {"c_pe10": -0.8, "c_pe1": -1.0},
        "I": {"c_pe10": -0.5, "c_pe1": -0.5},
    },
}


def get_duopitch_roof_coefficient(
    zone_key: str,
    coefficient_label: str,
    sign: str,
    pitch_angle: float,
    wind_direction: str,
) -> float:
    """
    Get the external pressure coefficient for duopitch roofs.

    :param zone_key: The zone key for the external pressure coefficient.
    :param coefficient_label: The label of the coefficient to be retrieved, either 'c_pe10' or 'c_pe1'.
    :param sign: The sign of the coefficient, either '+' (pressure) or '-' (suction).
    :param pitch_angle: The pitch angle of the roof.
    :param wind_direction: The wind direction, either 'x' or 'y'.
    """
    if wind_direction == "x":
        coefficients_data = DUOPITCH_ROOF_COEFFICIENTS_0
    elif wind_direction == "y":
        coefficients_data = DUOPITCH_ROOF_COEFFICIENTS_90
    else:
        raise ValueError(
            f"Direction must be either 'x' or 'y', not: '{wind_direction}'."
        )

    # Find nearest pitch angles for interpolation
    sorted_keys = sorted(coefficients_data.keys())
    lower_key = max(
        [k for k in sorted_keys if k <= pitch_angle], default=sorted_keys[0]
    )
    upper_key = min(
        [k for k in sorted_keys if k >= pitch_angle], default=sorted_keys[-1]
    )

    # Get the data for lower and upper keys
    lower_data = coefficients_data[lower_key][zone_key]
    upper_data = coefficients_data[upper_key][zone_key]

    # Determine if sign-specific data is available and retrieve it
    if sign and isinstance(lower_data, dict) and sign in lower_data:
        lower_val = lower_data[sign][coefficient_label]
        upper_val = upper_data[sign][coefficient_label]
    else:
        lower_val = lower_data[coefficient_label]
        upper_val = upper_data[coefficient_label]

    # Perform interpolation if necessary
    if lower_key == upper_key:
        return lower_val  # Return directly if it's an exact match
    else:
        return linear_interpolation(
            pitch_angle, lower_key, upper_key, lower_val, upper_val
        )
