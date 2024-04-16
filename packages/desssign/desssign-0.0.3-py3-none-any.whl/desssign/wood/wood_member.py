from __future__ import annotations

import math
from typing import TYPE_CHECKING

from framesss.pre.member_1d import Member1D

from desssign.wood.design_checks.member_1d_checks import Member1DChecks

if TYPE_CHECKING:
    import numpy as np
    import numpy.typing as npt
    from framesss.enums import BeamConnection
    from framesss.enums import Element1DType
    from framesss.fea.analysis.analysis import Analysis
    from framesss.fea.node import Node

    from desssign.loads.load_case_combination import DesignLoadCaseCombination
    from desssign.wood.wood_section import WoodRectangularSection


class WoodMember1D(Member1D):
    """
    Class for 1D wood member.

    Inherits from `Member1D` class and adds specific properties of wood.

    param label: A user-defined identifier for the member.
    :param element_type: Specifies the type of the element ('navier', 'timoshenko').
    :param nodes: The nodes at the ends of the member.
    :param section: The cross-section of the member.
    :param hinges: Defines the type of connections at the start and the end of the  member
                   (e.g., fixed, hinged, or semirigid) to model the rotational stiffness accurately.
    :param auxiliary_vector_xy_plane: An auxiliary vector in local xy-plane that defines the local
                                      coordinate system of the member.
    :param analysis: The :class:`Analysis` object.
    """

    section: WoodRectangularSection  # Explicit type annotation, so that mypy can check the type

    def __init__(
        self,
        label: str,
        element_type: str | Element1DType,
        nodes: list[Node],
        section: WoodRectangularSection,
        hinges: list[str] | list[BeamConnection],
        auxiliary_vector_xy_plane: npt.NDArray[np.float64],
        analysis: Analysis,
    ) -> None:
        """Init the WoodMember1D object."""
        super().__init__(
            label=label,
            element_type=element_type,
            nodes=nodes,
            section=section,
            hinges=hinges,
            auxiliary_vector_xy_plane=auxiliary_vector_xy_plane,
            analysis=analysis,
        )

        self.design_checks = Member1DChecks(self)

        self.is_prevented_lateral_displacement_at_compressive_edge = False
        self.is_prevented_torsional_rotation_at_supports = False

    @property
    def L_cr_y(self) -> float:
        """Critical length for buckling in y-axis."""
        # TODO: Implement the critical length for buckling in y-axis
        return float(self.length)

    @property
    def L_cr_z(self) -> float:
        """Critical length for buckling in z-axis."""
        # TODO: Implement the critical length for buckling in z-axis
        return float(self.length)

    @property
    def lambda_y(self) -> float:
        """Slenderness ratio in y-axis."""
        return self.L_cr_y / self.section.i_y

    @property
    def lambda_z(self) -> float:
        """Slenderness ratio in z-axis."""
        return self.L_cr_z / self.section.i_z

    @property
    def lambda_rel_y(self) -> float:
        """
        Relative slenderness ratio in y-axis.

        EN 1995-1-1, 6.3.2(1), eq. (6.21)
        """
        return (
            self.lambda_y
            / math.pi
            * math.sqrt(self.section.material.f_c0k / self.section.material.E_m0k)
        )

    @property
    def lambda_rel_z(self) -> float:
        """
        Relative slenderness ratio in z-axis.

        EN 1995-1-1, 6.3.2(1), eq. (6.22)
        """
        return (
            self.lambda_z
            / math.pi
            * math.sqrt(self.section.material.f_c0k / self.section.material.E_m0k)
        )

    @property
    def k_y(self) -> float:
        """
        Instability factor.

        EN 1995-1-1, 6.3.2(3), eq. (6.27)
        """
        beta_c = self.section.material.beta_c
        lambda_rel_y = self.lambda_rel_y
        return 0.5 * (1 + beta_c * (lambda_rel_y - 0.3) + lambda_rel_y**2)

    @property
    def k_z(self) -> float:
        """
        Instability factor.

        EN 1995-1-1, 6.3.2(3), eq. (6.28)
        """
        beta_c = self.section.material.beta_c
        lambda_rel_z = self.lambda_rel_z
        return 0.5 * (1 + beta_c * (lambda_rel_z - 0.3) + lambda_rel_z**2)

    @property
    def k_cy(self) -> float:
        """
        Instability factor.

        EN 1995-1-1, 6.3.2(3), eq. (6.25)
        """
        return 1.0 / (self.k_y + math.sqrt(self.k_y**2 - self.lambda_rel_y**2))

    @property
    def k_cz(self) -> float:
        """
        Instability factor.

        EN 1995-1-1, 6.3.2(3), eq. (6.26)
        """
        return 1.0 / (self.k_z + math.sqrt(self.k_z**2 - self.lambda_rel_z**2))

    @property
    def l_ef(self) -> float:
        """
        Effective length of the member subjected to bending.

        EN 1995-1-1, 6.3.3(3), Table 6.1
        """
        # TODO: Implement the effective length of the member subjected to bending
        return float(0.9 * self.length + 2 * self.section.height_z)

    @property
    def sigma_m_crit(self) -> float:
        """
        Critical bending stress.

        EN 1995-1-1, 6.3.3(3), eq. (6.32)
        """
        b = self.section.height_y
        E = self.section.material.E_m0k
        h = self.section.height_z
        l_ef = self.l_ef
        return 0.78 * b**2 * E / (h * l_ef)

    @property
    def lambda_rel_m(self) -> float:
        """
        Relative slenderness for bending.

        EN 1995-1-1, 6.3.3(2), eq. (6.30)
        """
        return math.sqrt(self.section.material.f_mk / self.sigma_m_crit)

    @property
    def k_crit(self) -> float:
        """
        Factor used for lateral buckling.

        EN 1995-1-1, 6.3.3(4), eq. (6.34)
        EN 1995-1-1, 6.3.3(5)
        """
        if (
            self.is_prevented_lateral_displacement_at_compressive_edge
            and self.is_prevented_torsional_rotation_at_supports
        ):
            return 1.0

        if self.lambda_rel_m <= 0.75:
            return 1.0
        elif 0.75 < self.lambda_rel_m <= 1.4:
            return 1.56 - 0.75 * self.lambda_rel_m
        else:
            return 1 / self.lambda_rel_m**2

    def perform_uls_checks(
        self, load_combinations: list[DesignLoadCaseCombination]
    ) -> None:
        """Perform the design checks."""
        self.design_checks.perform_uls_checks(load_combinations)
