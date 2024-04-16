from __future__ import annotations

from typing import TYPE_CHECKING

from desssign.loads.wind.external_pressure_coefficients import (
    get_duopitch_roof_coefficient,
)
from desssign.loads.wind.external_pressure_coefficients import get_flat_roof_coefficient
from desssign.loads.wind.wind_load import WindLoad

if TYPE_CHECKING:
    from desssign.loads.wind.enums import FlatRoofType
    from desssign.loads.wind.enums import TerrainCategory
    from desssign.loads.wind.enums import WindZone


class Roof:
    """
    Abstract class for roofs.

    :ivar zone: Wind zone.
    :ivar terrain_category: Terrain category.
    :ivar b_x: Width of the building in the x-direction.
    :ivar b_y: Width of the building in the y-direction.
    """

    def __init__(
        self,
        zone: str | WindZone,
        terrain_category: str | TerrainCategory,
        b_x: float,
        b_y: float,
    ) -> None:
        """Init the Roof class."""
        self.zone = zone
        self.terrain_category = terrain_category
        self.b_x = b_x
        self.b_y = b_y


class FlatRoof(Roof):
    """
    Class for flat roofs.

    :ivar roof_type: Type of the flat roof.
    :ivar zone: Wind zone.
    :ivar terrain_category: Terrain category.
    :ivar b_x: Width of the building in the x-direction.
    :ivar b_y: Width of the building in the y-direction.
    :ivar h: Height of the building.
    :ivar h_p: Height of the parapet.
    :ivar wind_load: Instance of the :class:`WindLoad` class.
    """

    def __init__(
        self,
        roof_type: str | FlatRoofType,
        zone: str | WindZone,
        terrain_category: str | TerrainCategory,
        b_x: float,
        b_y: float,
        h: float,
        h_p: float = 0.0,
    ) -> None:
        """Init the FlatRoof class."""
        super().__init__(zone, terrain_category, b_x, b_y)
        self.roof_type = roof_type
        self.h = h
        self.h_p = h_p
        self.wind_load = WindLoad(self.zone, self.terrain_category, self.z_e)

    @property
    def z_e(self) -> float:
        """Reference height."""
        return self.h + self.h_p

    def get_roof_zones(
        self, b: float, d: float, sign: str, direction: str
    ) -> list[RoofZone]:
        """
        Get roof zones for a flat roof.

        :param b: Crosswind dimension of the building.
        :param d: Length of the building.
        :param sign: Sign of the coefficients, '+' (pressure), '-' (suction).
        :param direction: Wind direction, 'x' or 'y'.
        """
        e = min(b, 2 * self.h)
        ratio = self.h_p / self.h if self.h_p != 0.0 else None
        c_pe = {}
        for zone_label in ["F", "G", "H", "I"]:
            c_pe[zone_label] = get_flat_roof_coefficient(
                self.roof_type, zone_label, "c_pe10", sign=sign, ratio=ratio
            )

        if direction.lower() == "x":
            zones = [
                RoofZone(
                    "F",
                    0.0,
                    0.0,
                    e / 10,
                    e / 4,
                    c_pe["F"],
                    c_pe["F"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "G",
                    0.0,
                    e / 4,
                    e / 10,
                    b - 2 * e / 4,
                    c_pe["G"],
                    c_pe["G"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "F",
                    0.0,
                    b - e / 4,
                    e / 10,
                    e / 4,
                    c_pe["F"],
                    c_pe["F"] * self.wind_load.q_p,
                ),
            ]
            if d - e / 2 > 0:
                zones.append(
                    RoofZone(
                        "H",
                        e / 10,
                        0.0,
                        e / 2 - e / 10,
                        b,
                        c_pe["H"],
                        c_pe["H"] * self.wind_load.q_p,
                    )
                )
                zones.append(
                    RoofZone(
                        "I",
                        e / 2,
                        0.0,
                        d - e / 2,
                        b,
                        c_pe["I"],
                        c_pe["I"] * self.wind_load.q_p,
                    )
                )
            else:
                zones.append(
                    RoofZone(
                        "H",
                        e / 10,
                        0.0,
                        d - e / 10,
                        b,
                        c_pe["H"],
                        c_pe["H"] * self.wind_load.q_p,
                    )
                )

        elif direction.lower() == "y":
            zones = [
                RoofZone(
                    "F",
                    0.0,
                    0.0,
                    e / 4,
                    e / 10,
                    c_pe["F"],
                    c_pe["F"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "G",
                    e / 4,
                    0.0,
                    b - 2 * e / 4,
                    e / 10,
                    c_pe["G"],
                    c_pe["G"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "F",
                    b - e / 4,
                    0.0,
                    e / 4,
                    e / 10,
                    c_pe["F"],
                    c_pe["F"] * self.wind_load.q_p,
                ),
            ]

            if d - e / 2 > 0:
                zones.append(
                    RoofZone(
                        "H",
                        0.0,
                        e / 10,
                        b,
                        e / 2 - e / 10,
                        c_pe["H"],
                        c_pe["H"] * self.wind_load.q_p,
                    )
                )
                zones.append(
                    RoofZone(
                        "I",
                        0.0,
                        e / 2,
                        b,
                        d - e / 2,
                        c_pe["I"],
                        c_pe["I"] * self.wind_load.q_p,
                    )
                )
            else:
                zones.append(
                    RoofZone(
                        "H",
                        0.0,
                        e / 10,
                        b,
                        d - e / 10,
                        c_pe["H"],
                        c_pe["H"] * self.wind_load.q_p,
                    )
                )

        else:
            raise ValueError(
                f"Direction must be either 'x' or 'y', not: '{direction}'."
            )
        return zones

    @property
    def zones_x_neg_pos(self) -> list[RoofZone]:
        """Wind zones for wind in x-direction with pressure on the left and suction on the 'I' zone."""
        return self.get_roof_zones(self.b_y, self.b_x, "+", "x")

    @property
    def zones_x_neg_neg(self) -> list[RoofZone]:
        """Wind zones for wind in x-direction with pressure everywhere."""
        return self.get_roof_zones(self.b_y, self.b_x, "-", "x")

    @property
    def zones_y_neg_pos(self) -> list[RoofZone]:
        """Wind zones for wind in y-direction with pressure on the left and suction on the 'I' zone."""
        return self.get_roof_zones(self.b_x, self.b_y, "+", "y")

    @property
    def zones_y_neg_neg(self) -> list[RoofZone]:
        """Wind zones for wind in y-direction with pressure everywhere."""
        return self.get_roof_zones(self.b_x, self.b_y, "-", "y")


class MonopitchRoof(Roof):
    """
    Class for monopitched roofs.

    :ivar zone: Wind zone.
    :ivar terrain_category: Terrain category.
    :ivar b_x: Width of the building in the x-direction.
    :ivar b_y: Width of the building in the y-direction.
    :ivar h: Height of the building.
    :ivar wind_load: Instance of the :class:`WindLoad` class.
    """

    def __init__(
        self,
        zone: str | WindZone,
        terrain_category: str | TerrainCategory,
        b_x: float,
        b_y: float,
        h: float,
    ) -> None:
        """Init the MonopitchedRoof class."""
        super().__init__(zone, terrain_category, b_x, b_y)
        self.h = h
        self.wind_load = WindLoad(self.zone, self.terrain_category, self.z_e)
        raise NotImplementedError("MonopitchedRoof class is not implemented yet.")

    @property
    def z_e(self) -> float:
        """Reference height."""
        return self.h


class DuopitchRoof(Roof):
    """
    Class for duopitched roofs.

    The ridge is considered parallel to the y-axis.

    :ivar zone: Wind zone.
    :ivar terrain_category: Terrain category.
    :ivar b_x: Width of the building in the x-direction.
    :ivar b_y: Width of the building in the y-direction.
    :ivar h: Height of the building.
    :ivar pitch_angle: Pitch angle of the roof.
    """

    def __init__(
        self,
        zone: str | WindZone,
        terrain_category: str | TerrainCategory,
        b_x: float,
        b_y: float,
        h: float,
        pitch_angle: float,
    ) -> None:
        """Init the DuopitchRoof class."""
        super().__init__(zone, terrain_category, b_x, b_y)
        self.h = h
        self.pitch_angle = pitch_angle
        self.wind_load = WindLoad(self.zone, self.terrain_category, self.z_e)

    @property
    def z_e(self) -> float:
        """Reference height."""
        return self.h

    def get_roof_zones(
        self,
        b: float,
        d: float,
        signs: list[str],
        wind_direction: str,
    ) -> list[RoofZone]:
        """
        Get wind zones for a duopitch roof.

        :param b: Crosswind dimension of the building.
        :param d: Length of the building.
        :param signs: Signs of the coefficients, '+' (pressure), '-' (suction).
        :param wind_direction: Wind direction, 'x' or 'y'.
        """
        e = min(b, 2 * self.h)

        c_pe = {}

        zone_keys = ["F", "G", "H", "I"]
        zone_signs = [signs[0]] * 3 + [signs[1]] * 1
        if wind_direction == "x":
            zone_keys.append("J")
            zone_signs.append(signs[1])

        for zone_key, sign in zip(zone_keys, zone_signs):
            c_pe[zone_key] = get_duopitch_roof_coefficient(
                zone_key, "c_pe10", sign, self.pitch_angle, wind_direction
            )

        if wind_direction.lower() == "x":
            zones = [
                RoofZone(
                    "F",
                    0.0,
                    0.0,
                    e / 10,
                    e / 4,
                    c_pe["F"],
                    c_pe["F"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "G",
                    0.0,
                    e / 4,
                    e / 10,
                    b - 2 * e / 4,
                    c_pe["G"],
                    c_pe["G"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "F",
                    0.0,
                    b - e / 4,
                    e / 10,
                    e / 4,
                    c_pe["F"],
                    c_pe["F"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "H",
                    e / 10,
                    0.0,
                    d / 2 - e / 10,
                    b,
                    c_pe["H"],
                    c_pe["H"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "J",
                    d / 2,
                    0.0,
                    e / 10,
                    b,
                    c_pe["J"],
                    c_pe["J"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "I",
                    d / 2 + e / 10,
                    0.0,
                    d / 2 - e / 10,
                    b,
                    c_pe["I"],
                    c_pe["I"] * self.wind_load.q_p,
                ),
            ]

        elif wind_direction.lower() == "y":
            zones = [
                RoofZone(
                    "F",
                    0.0,
                    0.0,
                    e / 4,
                    e / 10,
                    c_pe["F"],
                    c_pe["F"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "G",
                    e / 4,
                    0.0,
                    b / 2 - e / 4,
                    e / 10,
                    c_pe["G"],
                    c_pe["G"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "G",
                    b / 2,
                    0.0,
                    b / 2 - e / 4,
                    e / 10,
                    c_pe["G"],
                    c_pe["G"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "F",
                    b - e / 4,
                    0.0,
                    e / 4,
                    e / 10,
                    c_pe["F"],
                    c_pe["F"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "H",
                    0.0,
                    e / 10,
                    b / 2,
                    e / 2 - e / 10,
                    c_pe["H"],
                    c_pe["H"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "H",
                    b / 2,
                    e / 10,
                    b / 2,
                    e / 2 - e / 10,
                    c_pe["H"],
                    c_pe["H"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "I",
                    0.0,
                    e / 2,
                    b / 2,
                    d - e / 2,
                    c_pe["I"],
                    c_pe["I"] * self.wind_load.q_p,
                ),
                RoofZone(
                    "I",
                    b / 2,
                    e / 2,
                    b / 2,
                    d - e / 2,
                    c_pe["I"],
                    c_pe["I"] * self.wind_load.q_p,
                ),
            ]

        else:
            raise ValueError(
                f"Direction must be either 'x' or 'y', not: '{wind_direction}'."
            )

        return zones

    @property
    def zones_x_neg_neg(self) -> list[RoofZone] | None:
        """Wind zones for wind in x-direction with pressure on both sides of the roof."""
        if 45.0 < self.pitch_angle <= 75.0:
            return None

        return self.get_roof_zones(self.b_y, self.b_x, ["-", "-"], "x")

    @property
    def zones_wind_x_neg_pos(self) -> list[RoofZone] | None:
        """Wind zones for wind in x-direction with pressure on the left and suction on the right side of the roof."""
        if not (-5.0 <= self.pitch_angle <= 45.0):
            return None

        return self.get_roof_zones(self.b_y, self.b_x, ["-", "+"], "x")

    @property
    def zones_wind_x_pos_neg(self) -> list[RoofZone] | None:
        """Wind zones for wind in x-direction with suction on the left and pressure on the right side of the roof."""
        if not (5.0 <= self.pitch_angle <= 75.0):
            return None

        return self.get_roof_zones(self.b_y, self.b_x, ["+", "-"], "x")

    @property
    def zones_wind_x_pos_pos(self) -> list[RoofZone] | None:
        """Wind zones for wind in x-direction with pressure on both sides of the roof."""
        if not (5.0 <= self.pitch_angle <= 45.0):
            return None

        return self.get_roof_zones(self.b_y, self.b_x, ["+", "+"], "x")

    @property
    def zones_wind_y(self) -> list[RoofZone] | None:
        """Wind zones for wind in y-direction."""
        return self.get_roof_zones(self.b_x, self.b_y, ["-", "-"], "y")


class RoofZone:
    """
    Class representing a roof zone.

    :ivar roof_zone: Label of the roof zone.
    :ivar x_bl: X coordinate of the bottom-left corner.
    :ivar y_bl: Y coordinate of the bottom-left corner.
    :ivar b_x: Width of the zone in the x-direction.
    :ivar b_y: Width of the zone in the y-direction.
    :ivar c_pe: External pressure coefficient.
    :ivar w_e: Wind pressure.
    """

    def __init__(
        self,
        roof_zone: str,
        x_bl: float,
        y_bl: float,
        b_x: float,
        b_y: float,
        c_pe: float,
        w_e: float,
    ) -> None:
        """Init the RoofZone class."""
        self.roof_zone = roof_zone
        self.c_pe = c_pe
        self.w_e = w_e

        self.x_bl = x_bl
        self.y_bl = y_bl
        self.b_x = b_x
        self.b_y = b_y

        self.geometry = calculate_rectangle_points(x_bl, y_bl, b_x, b_y)

    def __str__(self) -> str:
        """Return a string representation of the RoofZone class."""
        return f"RoofZone({self.roof_zone}, {self.geometry}, {self.c_pe}, {self.w_e})"


def calculate_rectangle_points(
    x_bl: float, y_bl: float, dx: float, dy: float
) -> list[list[float]]:
    """
    Calculate corner points of a rectangle.

    :param x_bl: X coordinate of the bottom-left corner.
    :param y_bl: Y coordinate of the bottom-left corner.
    :param dx: Width of the rectangle.
    :param dy: Height of the rectangle.
    :return: A list of corner points of the rectangle.
    """
    return [[x_bl, y_bl], [x_bl + dx, y_bl], [x_bl + dx, y_bl + dy], [x_bl, y_bl + dy]]
