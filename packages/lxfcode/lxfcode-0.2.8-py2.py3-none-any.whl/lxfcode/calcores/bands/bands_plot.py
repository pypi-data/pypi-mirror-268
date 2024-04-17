import matplotlib.pyplot as plt
from ..filesop.filesave import FilesSave
from typing import Literal
from .bands_cal import BandsCal
import numpy as np


plt.rc("font", family="Times New Roman")  # change the font of plot
plt.rcParams["mathtext.fontset"] = "stix"


class BandsPlot:
    fontsize = 12
    titlesize = 14

    def __init__(self, bandsInst: BandsCal) -> None:
        self.bandsInst = bandsInst
        pass

    def ylim_bounds(
        self,
        energies: np.ndarray,
        symmetry: Literal["middle", "bottom", "top"] = "middle",
    ):
        if symmetry == "middle":
            # print("shape: ", energies.shape)
            vmax = np.max(
                energies[:, energies.shape[1] // 2 - 3 : energies.shape[1] // 2 + 3]
            )
            vmin = np.min(
                energies[:, energies.shape[1] // 2 - 3 : energies.shape[1] // 2 + 3]
            )
        return [vmin, vmax]

    def plot(
        self,
        title_name: str,
        line_style: Literal["k-", "r-", "k--", "r--"] = "k-",
        figsize: tuple = (7, 5),
        lw=2,
        ylim=None,
    ) -> np.ndarray:
        energies, xlabel_x = self.bandsInst.calculate()

        ##  shift all the energies symmetrical to the zero energies
        energies = energies - np.median(energies)

        fig, ax_e = plt.subplots(figsize=figsize)
        ax_e.plot(energies, line_style, linewidth=lw)
        ax_e.set_aspect("auto")
        ax_e.set_xticks(
            xlabel_x,
            [
                r"$\{}$".format(ele) if ele == "Gamma" else r"${}$".format(ele)
                for ele in self.bandsInst.path
            ],
            fontsize=self.fontsize,
        )
        ax_e.set_ylabel("E (meV)", fontsize=self.fontsize)
        ax_e.set_title(title_name, fontsize=self.titlesize)
        ax_e.set_xlim(ax_e.get_xlim())
        if ylim is None:
            ylim = self.ylim_bounds(energies)
        ax_e.set_ylim(ylim)
        FilesSave("Bands").save_fig(fig, self.bandsInst.fname)
        plt.close()

        return energies
