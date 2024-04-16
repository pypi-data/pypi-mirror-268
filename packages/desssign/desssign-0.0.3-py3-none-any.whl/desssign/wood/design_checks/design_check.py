from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from desssign.wood.enums import CheckResult

if TYPE_CHECKING:
    import numpy.typing as npt


class Check:
    """Abstract class for design checks."""

    def __init__(
        self,
        code: str,
        paragraph: str,
        equation_number: str,
    ) -> None:
        """Init the Check object."""
        self.code = code
        self.paragraph = paragraph
        self.equation_number = equation_number

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        raise NotImplementedError("Method 'usage' must be implemented.")

    @property
    def max_usage(self) -> float:
        """Maximum usage of the material."""
        return float(np.max(self.usages))

    @property
    def result(self) -> CheckResult:
        """Overall design result."""
        if self.max_usage <= 1.0:
            return CheckResult(CheckResult.PASS)
        return CheckResult(CheckResult.FAIL)


class TensionParallelToTheGrainCheck(Check):
    """
    Class for checking tension parallel to the grain.

    EN 1995-1-1, 6.1.2, eq. (6.1)

    :param sigma_t0d: Design tensile stresses parallel to the grain along the member.
    :param f_t0d: Design tension strength parallel to the grain.
    """

    def __init__(
        self,
        sigma_t0d: npt.NDArray[np.float64],
        f_t0d: float,
    ) -> None:
        """Init the TensionParallelToTheGrain object."""
        super().__init__("EN 1995-1-1", "6.1.2", "6.1")
        self.sigma_t0d = sigma_t0d
        self.f_t0d = f_t0d

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        return np.abs(self.sigma_t0d) / self.f_t0d


class CompressionParallelToTheGrainCheck(Check):
    """
    Class for checking compression parallel to the grain.

    EN 1995-1-1, 6.1.4, 6.2

    :param sigma_c0d: Design compressive stresses parallel to the grain along the member.
    :param f_c0d: Design compressive strength parallel to the grain.
    """

    def __init__(
        self,
        sigma_c0d: npt.NDArray[np.float64],
        f_c0d: float,
    ) -> None:
        """Init the CompressionParallelToTheGrain object."""
        super().__init__("EN 1995-1-1", "6.1.4", "6.2")
        self.sigma_c0d = sigma_c0d
        self.f_c0d = f_c0d

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        return np.abs(self.sigma_c0d) / self.f_c0d


class BendingCheck(Check):
    """
    Class for checking bending.

    EN 1995-1-1, 6.1.5, eq. 6.11 & 6.12

    :param sigma_myd: Design bending stresses about the principal y-axis along the member.
    :param sigma_mzd: Design bending stresses about the principal z-axis along the member.
    :param f_myd: Design bending strength about the principal y-axis.
    :param f_mzd: Design bending strength about the principal z-axis.
    :param k_m: Factor considering re-distribution of bending stresses
                in cross-section.
    """

    def __init__(
        self,
        sigma_myd: npt.NDArray[np.float64],
        sigma_mzd: npt.NDArray[np.float64],
        f_myd: float,
        f_mzd: float,
        k_m: float = 0.7,  # TODO: 0.7 for rectangular cross-section, else 1.0
    ) -> None:
        """Init the Bending object."""
        super().__init__("EN 1995-1-1", "6.1.6", "6.11, 6.12")
        self.sigma_myd = sigma_myd
        self.sigma_mzd = sigma_mzd
        self.f_myd = f_myd
        self.f_mzd = f_mzd
        self.k_m = k_m

        self.eq_6_11 = (
            np.abs(self.sigma_myd) / self.f_myd
            + self.k_m * np.abs(self.sigma_mzd) / self.f_mzd
        )
        self.eq_6_12 = (
            self.k_m * np.abs(self.sigma_myd) / self.f_myd
            + np.abs(self.sigma_mzd) / self.f_mzd
        )

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        return np.maximum(self.eq_6_11, self.eq_6_12)


class ShearCheck(Check):
    """
    Class for checking shear stress.

    EN 1995-1-1, 6.1.7, eq. 6.13

    :param tau_d: Design shear stresses along the member.
    :param f_vd: Design shear strength.
    """

    def __init__(
        self,
        tau_d: npt.NDArray[np.float64],
        f_vd: float,
    ) -> None:
        """Init the Shear object."""
        super().__init__("EN 1995-1-1", "6.1.7", "6.13")
        self.tau_d = tau_d
        self.f_vd = f_vd

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        return np.abs(self.tau_d) / self.f_vd


class TorsionCheck(Check):
    """
    Class for checking torsion.

    EN 1995-1-1, 6.1.8, eq. 6.14

    :param t_tord: Design torsional stresses along the member.
    :param f_vd: Design shear strength.
    :param k_shape: Factor depending on the shape of the cross-section.
    """

    def __init__(
        self,
        t_tord: npt.NDArray[np.float64],
        f_vd: float,
        k_shape: float,
    ) -> None:
        """Init the Torsion object."""
        super().__init__("EN 1995-1-1", "6.1.8", "6.14")
        self.t_tord = t_tord
        self.f_vd = f_vd
        self.k_shape = k_shape

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        return np.abs(self.t_tord) / self.k_shape * self.f_vd


class CombinedBendingAndAxialTensionCheck(Check):
    """
    Class for checking combined bending and axial tension.

    EN 1995-1-1, 6.2.3, eq. 6.17

    :param sigma_t0d: Design tensile stresses parallel to the grain along the member.
    :param sigma_myd: Design bending stresses about the principal y-axis along the member.
    :param sigma_mzd: Design bending stresses about the principal z-axis along the member.
    :param f_t0d: Design tension strength parallel to the grain.
    :param f_myd: Design bending strength about the principal y-axis.
    :param f_mzd: Design bending strength about the principal z-axis.
    :param k_m: Factor considering re-distribution of bending stresses in cross-section.
    """

    def __init__(
        self,
        sigma_t0d: npt.NDArray[np.float64],
        sigma_myd: npt.NDArray[np.float64],
        sigma_mzd: npt.NDArray[np.float64],
        f_t0d: float,
        f_myd: float,
        f_mzd: float,
        k_m: float = 0.7,  # TODO: 0.7 for rectangular cross-section, else 1.0
    ) -> None:
        """Init the CombinedBendingAndAxialTension object."""
        super().__init__("EN 1995-1-1", "6.2.3", "6.17, 6.18")
        self.sigma_t0d = sigma_t0d
        self.sigma_myd = sigma_myd
        self.sigma_mzd = sigma_mzd
        self.f_t0d = f_t0d
        self.f_myd = f_myd
        self.f_mzd = f_mzd
        self.k_m = k_m

        tension = np.abs(self.sigma_t0d) / self.f_t0d
        bending_y = np.abs(self.sigma_myd) / self.f_myd
        bending_z = np.abs(self.sigma_mzd) / self.f_mzd

        self.eq_6_17: npt.NDArray[np.float64] = (
            tension + bending_y + self.k_m * bending_z
        )
        self.eq_6_18: npt.NDArray[np.float64] = (
            tension + self.k_m * bending_y + bending_z
        )

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        return np.maximum(self.eq_6_17, self.eq_6_18)


class CombinedBendingAndAxialCompressionCheck(Check):
    """
    Class for checking combined bending and axial compression.

    EN 1995-1-1, 6.2.4, eq. 6.19, 6.20

    :param sigma_c0d: Design compressive stresses parallel to the grain along the member.
    :param sigma_myd: Design bending stresses about the principal y-axis along the member.
    :param sigma_mzd: Design bending stresses about the principal z-axis along the member.
    :param f_c0d: Design compressive strength parallel to the grain.
    :param f_myd: Design bending strength about the principal y-axis.
    :param f_mzd: Design bending strength about the principal z-axis.
    :param k_m: Factor considering re-distribution of bending stresses in cross-section.
    """

    def __init__(
        self,
        sigma_c0d: npt.NDArray[np.float64],
        sigma_myd: npt.NDArray[np.float64],
        sigma_mzd: npt.NDArray[np.float64],
        f_c0d: float,
        f_myd: float,
        f_mzd: float,
        k_m: float = 0.7,  # TODO: 0.7 for rectangular cross-section, else 1.0
    ) -> None:
        """Init the CombinedBendingAndAxialCompression object."""
        super().__init__("EN 1995-1-1", "6.2.4", "6.19, 6.20")
        self.sigma_c0d = sigma_c0d
        self.sigma_myd = sigma_myd
        self.sigma_mzd = sigma_mzd
        self.f_c0d = f_c0d
        self.f_myd = f_myd
        self.f_mzd = f_mzd
        self.k_m = k_m

        compression = (np.abs(self.sigma_c0d) / self.f_c0d) ** 2
        bending_y = np.abs(self.sigma_myd) / self.f_myd
        bending_z = np.abs(self.sigma_mzd) / self.f_mzd

        self.eq_6_19: npt.NDArray[np.float64] = (
            compression + bending_y + self.k_m * bending_z
        )
        self.eq_6_20: npt.NDArray[np.float64] = (
            compression + self.k_m * bending_y + bending_z
        )

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        return np.maximum(self.eq_6_19, self.eq_6_20)


class ColumnStabilityCheck(Check):
    """
    Class for checking column stability.

    EN 1995-1-1, 6.3, eq. 6.23, 6.24

    :param sigma_c0d: Design compressive stresses parallel to the grain along the member.
    :param sigma_myd: Design bending stresses about the principal y-axis along the member.
    :param sigma_mzd: Design bending stresses about the principal z-axis along the member.
    :param f_c0d: Design compressive strength parallel to the grain.
    :param f_myd: Design bending strength about the principal y-axis.
    :param f_mzd: Design bending strength about the principal z-axis.
    :param k_cy: Instability factor for the y-axis.
    :param k_cz: Instability factor for the z-axis.
    :param k_m: Factor considering re-distribution of bending stresses in cross-section.
    """

    def __init__(
        self,
        sigma_c0d: npt.NDArray[np.float64],
        sigma_myd: npt.NDArray[np.float64],
        sigma_mzd: npt.NDArray[np.float64],
        f_c0d: float,
        f_myd: float,
        f_mzd: float,
        k_cy: float,
        k_cz: float,
        k_m: float,
    ) -> None:
        """Init the ColumnStabilityCheck object."""
        super().__init__("EN 1995-1-1", "6.3", "6.23, 6.24")
        self.sigma_c0d = sigma_c0d
        self.sigma_myd = sigma_myd
        self.sigma_mzd = sigma_mzd
        self.f_c0d = f_c0d
        self.f_myd = f_myd
        self.f_mzd = f_mzd
        self.k_cy = k_cy
        self.k_cz = k_cz
        self.k_m = k_m

        compression = (np.abs(self.sigma_c0d) / self.f_c0d) ** 2
        bending_y = np.abs(self.sigma_myd) / self.f_myd
        bending_z = np.abs(self.sigma_mzd) / self.f_mzd

        self.eq_6_23: npt.NDArray[np.float64] = (
            compression / k_cy + bending_y + self.k_m * bending_z
        )
        self.eq_6_24: npt.NDArray[np.float64] = (
            compression / k_cz + self.k_m * bending_y + bending_z
        )

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        return np.maximum(self.eq_6_23, self.eq_6_24)


class BeamStabilityCheck(Check):
    """
    Class for checking beam stability.

    EN 1995-1-1, 6.3, eq. 6.35

    :param sigma_c0d: Design compressive stresses parallel to the grain along the member.
    :param sigma_myd: Design bending stresses about the principal y-axis along the member.
    :param f_c0d: Design compressive strength parallel to the grain.
    :param f_myd: Design bending strength about the principal y-axis.
    :param k_crit: Factor which takes into account the reduced bending strength due to lateral buckling.
    :param k_cz: Instability factor for the z-axis.
    """

    def __init__(
        self,
        sigma_c0d: npt.NDArray[np.float64],
        sigma_myd: npt.NDArray[np.float64],
        f_c0d: float,
        f_myd: float,
        k_crit: float,
        k_cz: float,
    ) -> None:
        """Init the BeamStabilityCheck object."""
        super().__init__("EN 1995-1-1", "6.3", "6.35")
        self.sigma_c0d = sigma_c0d
        self.sigma_myd = sigma_myd
        self.f_c0d = f_c0d
        self.f_myd = f_myd
        self.k_crit = k_crit
        self.k_cz = k_cz

        compression = np.abs(self.sigma_c0d) / (self.k_cz * self.f_c0d)
        bending = (np.abs(self.sigma_myd) / (self.k_crit * self.f_myd)) ** 2

        self.eq_6_35: npt.NDArray[np.float64] = compression + bending

    @property
    def usages(self) -> npt.NDArray[np.float64]:
        """Usages of the material at every point along the member."""
        return self.eq_6_35
