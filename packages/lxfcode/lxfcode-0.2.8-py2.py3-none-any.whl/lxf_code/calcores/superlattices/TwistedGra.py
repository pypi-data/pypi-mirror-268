from ..hamiltonians.tb_h import (
    TightTBGHa,
    TightAAtTTGHa,
    TightABtTTGHa,
    TightAtATTGHa,
    TightAtBTTGHa,
)
import numpy as np

# import matplotlib.pyplot as plt
from ..pubmeth.consts import *
from ..hamiltonians.conti_h import ContiTBGHa, EffABtHa
from typing import Literal
from ..bands.bands_cal import BandsCal
from ..bands.bands_plot import BandsPlot
from ..raman.raman_cal import RamanCal
from ..raman.raman_plot import RamanPlot
from ..abc.abmoire import ABContiGraMoires, ABMoHa, ABTBHa
from ..pubmeth.pubmeth import Line
from ..superlattices.comm_stru import (
    CommTBGStru,
    CommAAtTTGStru,
    CommABtTTGStru,
    CommAtATTGStru,
    CommAtBTTGStru,
)
from ..superlattices.stru_plot import StruPlot
from ..jdos.jdos_cal import JdosCal
from ..jdos.jdos_plot import JdosPlot
from ..dos.dos_cal import DosCal
from ..dos.dos_plot import DosPlot


class ContiTBG(ABContiGraMoires):
    def __init__(
        self,
        twist_angle: float,
        haInst: ABMoHa = ContiTBGHa,
        vFcoeff: float = 1,
        a0: float = 2.46,
        kshells: int = 7,
        w_inter=118,
    ) -> None:
        super().__init__(twist_angle, haInst, vFcoeff, a0, kshells, w_inter)
        self.mat_name = "Twisted Bilayer Graphene"

    def bands(
        self,
        path: list[Literal["K_t", "K_b", "M", "Gamma"]] = ["K_t", "K_b", "Gamma", "M"],
        suffix="",
        ylim=None,
        density=100,
    ):
        bds_title = "Band structures of {:.2f}$\degree$ {}".format(
            self.twist_angle, self.mat_name
        )
        h: ABMoHa = self.hInst(self)

        bcals = BandsCal(h, path=path, suffix=suffix, p_density=density)
        bplot = BandsPlot(bcals)
        bplot.plot(title_name=bds_title, ylim=ylim)

    def raman(
        self,
        density=70,
        calcores=3,
        ffolder="",
        update_eles=False,
        bds_num=5,
        disable_elet=False,
        gamma=100,
        plot_over_eop=False,
    ) -> RamanPlot:
        h: ABMoHa = self.hInst(self)
        rcals = RamanCal(
            h, density=density, cal_corenum=calcores, bds_num=bds_num, gamma=gamma
        )
        rplot = RamanPlot(rcals, ffolder=ffolder, disable_elet=disable_elet)

        if plot_over_eop:
            ri_overeop, e_range = rplot.raman_eop_plot()
            ri_overeop_sum = ri_overeop.sum(axis=1).sum(axis=1)
            ri_modules = abs(ri_overeop_sum) ** 2
            Line(
                [e_range] * 2, [np.real(ri_overeop_sum), np.imag(ri_overeop_sum)]
            ).multiplot(
                "realimag_overeop",
                ["real part", "imaginary part"],
                "E (meV)",
                "Raman intensity",
                "Raman over photon energy",
                xlim=[1200, 3000],
            )
            Line(e_range, ri_modules).plot(
                "ri_overeop",
                "E (meV)",
                "Raman intensity",
                "Raman over photon energy",
                xlim=[1200, 3000],
            )

        pexisted = rplot.rFileInst.existed()[0]
        if (not pexisted) or update_eles:
            rplot.plot(update_elet=update_eles)
        return rplot

    def jdos(
        self,
        density=70,
        broadening=1,
        vc_num=3,
        calcores=3,
        update_npy=False,
        cal_hint=False,
        e_range=np.linspace(100, 2500, 200),
        large_scal_cal=False,
    ):
        h: ABMoHa = self.hInst(self)

        jcals = JdosCal(
            h,
            density,
            broadening=broadening,
            cal_corenum=calcores,
            vc_num=vc_num,
            cal_hint=cal_hint,
            e_range=e_range,
            large_scale_cal=large_scal_cal,
        )
        jplot = JdosPlot(jcals, update_npy=update_npy)

        jplot.plot()
        return

    def dos(
        self,
        density=70,
        broadening=1,
        calcores=3,
        update_npy=False,
        cal_hint=False,
        e_range=np.linspace(-2000, 2500, 200),
        large_scal_cal=False,
    ):
        h: ABMoHa = self.hInst(self)

        dcals = DosCal(
            h,
            density,
            dos_broadening=broadening,
            cal_corenum=calcores,
            cal_hint=cal_hint,
            e_range=e_range,
            large_scale_cal=large_scal_cal,
        )
        dosplot = DosPlot(dcals, update_npy=update_npy)

        dosplot.plot()
        return


class EffABt(ContiTBG):
    def __init__(
        self,
        twist_angle: float,
        haInst: ABMoHa = EffABtHa,
        vFcoeff: float = 1,
        a0: float = 2.46,
        kshells: int = 7,
        w_inter=118,
        tperp_coeff=1,
    ) -> None:
        super().__init__(twist_angle, haInst, vFcoeff, a0, kshells, w_inter)
        self.tperp_coeff = tperp_coeff

        self.mat_name = "ABt-Twisted Trilayer Graphene"


class TightTBG(CommTBGStru, ContiTBG):
    def __init__(
        self,
        m0: int,
        r: int,
        haInst: ABTBHa = TightTBGHa,
        a1: np.ndarray = np.array([np.sqrt(3) / 2, -1 / 2]),
        a2: np.ndarray = np.array([np.sqrt(3) / 2, 1 / 2]),
        a0: float = 2.46,
    ) -> None:
        super().__init__(m0, r, haInst, a1, a2, a0)

        self.mat_name = "Twisted Bilayer Graphene"

    def structure(self):
        h: TightTBGHa = self.hInst(self)
        strup = StruPlot(h.moInst)
        strup.plot()
        return


class TightAAtTTG(TightTBG, CommAAtTTGStru):
    def __init__(
        self,
        m0: int,
        r: int,
        haInst: ABTBHa = TightAAtTTGHa,
        a1: np.ndarray = np.array([np.sqrt(3) / 2, -1 / 2]),
        a2: np.ndarray = np.array([np.sqrt(3) / 2, 1 / 2]),
        a0: float = 2.46,
    ) -> None:
        super().__init__(m0, r, haInst, a1, a2, a0)
        self.mat_name = "AAt-TTG"


class TightAtATTG(TightTBG, CommAtATTGStru):
    def __init__(
        self,
        m0: int,
        r: int,
        haInst: ABTBHa = TightAtATTGHa,
        a1: np.ndarray = np.array([np.sqrt(3) / 2, -1 / 2]),
        a2: np.ndarray = np.array([np.sqrt(3) / 2, 1 / 2]),
        a0: float = 2.46,
    ) -> None:
        super().__init__(m0, r, haInst, a1, a2, a0)
        self.mat_name = "AtA-TTG"


class TightABtTTG(TightAAtTTG, CommABtTTGStru):
    def __init__(
        self,
        m0: int,
        r: int,
        haInst: ABTBHa = TightABtTTGHa,
        a1: np.ndarray = np.array([np.sqrt(3) / 2, -1 / 2]),
        a2: np.ndarray = np.array([np.sqrt(3) / 2, 1 / 2]),
        a0: float = 2.46,
    ) -> None:
        super().__init__(m0, r, haInst, a1, a2, a0)
        self.mat_name = "ABt-TTG"


class TightAtBTTG(TightTBG, CommAtBTTGStru):
    def __init__(
        self,
        m0: int,
        r: int,
        haInst: ABTBHa = TightAtBTTGHa,
        a1: np.ndarray = np.array([np.sqrt(3) / 2, -1 / 2]),
        a2: np.ndarray = np.array([np.sqrt(3) / 2, 1 / 2]),
        a0: float = 2.46,
    ) -> None:
        super().__init__(m0, r, haInst, a1, a2, a0)
        self.mat_name = "AtB-TTG"


def main():
    # tbg = TightTBG(3, 3).structure()
    EffABt(16.2, kshells=3).jdos(density=7, update_npy=True)

    pass
    # print(ttg.lindexes)
    # print(ttg.lindexes)

    # def h(self, k_arr):
    #     # r_arrs = self.equal_distarrs[self.minnorm_index]
    #     # equal_vppi = self.equal_vppi[self.minnorm_index]
    #     # equal_vpps = self.equal_vpps[self.minnorm_index]
    #     # equal_cos = self.equal_cos[self.minnorm_index]
    #     # print(np.argmin(nor))
    #     equal_cos = self.equal_cos.reshape((-1, len(self.moInst.expand_basis))).T
    #     equal_vppi = self.equal_vppi.reshape((-1, len(self.moInst.expand_basis))).T
    #     equal_vpps = self.equal_vpps.reshape((-1, len(self.moInst.expand_basis))).T
    #     phase_term: np.ndarray = np.exp(1j * k_arr @ self.equal_distarrs[:, :2].T)
    #     phase_term = phase_term.reshape(-1, len(self.moInst.expand_basis)).T
    #     h = phase_term * (
    #         equal_vppi * (1 - equal_cos**2) + equal_vpps * equal_cos**2
    #     )
    #     h = np.sum(h, axis=0)
    #     h = h.reshape((len(self.moInst.latwithin), len(self.moInst.latwithin)))
    #     row, col = np.diag_indices_from(h)
    #     h[row, col] = 0

    #     pass

    #     return h

    # ContiTBG(12).bands()
    # a = np.array([[1, 2, 3], [4, 5, 3], [5, 3, 4]])
    # b = np.array([[True, False, False], [False, True, True], [False, False, False]])
    # print(a[b])


if __name__ == "__main__":
    main()
