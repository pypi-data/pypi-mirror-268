from .dos_cal import DosCal, DefinedFuncs
from ..filesop.filesave import FilesSave
import matplotlib.pyplot as plt
import numpy as np


class DosPlot:
    def __init__(self, dosCal: DosCal, ffolder="", update_npy=False) -> None:
        self.dosCalInst = dosCal

        self._supp_info = "../{}/{}_{}_{}".format(
            ffolder,
            self.dosCalInst.haInst.__class__.__name__,
            self.dosCalInst.haInst.sigs,
            self.dosCalInst.density,
        )

        self.dosFolderInst = FilesSave("DOS/dos") + self._supp_info
        self.dos_info = "dos_{}".format(self.dosCalInst.broadening)
        self.e_info = "eig_e"

        self.update_npy = update_npy

    def _load(self):
        if self.dosFolderInst.exist_npy(self.dos_info) and (not self.update_npy):
            print("Loading existing npy file...")
            dos = self.dosFolderInst.load_npy(self.dos_info)
        else:
            print("Calculating...")
            if self.dosFolderInst.exist_npy(self.e_info):
                print("Using the existing npy file...")
                eig_e = self.dosFolderInst.load_npy(self.e_info)
                if not self.dosCalInst.large_scal_cal:
                    dos = DefinedFuncs.deltaF_arct(
                        eig_e, self.dosCalInst.e_range, a=self.dosCalInst.broadening
                    )
                else:
                    print("Large scale calculations...")
                    dos = []
                    for ele_e in self.dosCalInst.e_range:
                        ele_jdos = DefinedFuncs.deltaF_arct(
                            eig_e, ele_e, a=self.dosCalInst.broadening
                        )
                        ele_jdos = np.sum(ele_jdos)
                        dos.append(ele_jdos)
                    dos = np.array(dos)
            else:
                print("calculating...")
                eig_e, dos = self.dosCalInst.calculate()
            self.dosFolderInst.save_npy(self.dos_info, dos)
            self.dosFolderInst.save_npy(self.e_info, eig_e)
        return dos

    def plot(self):
        dos = self._load()
        if not self.dosCalInst.large_scal_cal:
            dos: np.ndarray = dos.sum(axis=-1).sum(axis=-1)
        else:
            print("The array is already reduced to one dimension: ", dos.shape)
            pass
        fig, ax_dos = plt.subplots()
        ax_dos.plot(self.dosCalInst.e_range, dos)
        ax_dos.set_aspect("auto")
        ax_dos.set_xlabel("E (meV)", fontsize=12)
        ax_dos.set_ylabel("DOS", fontsize=12)
        ax_dos.set_title("", fontsize=14)
        ax_dos.set_xlim(ax_dos.get_xlim())
        ax_dos.set_ylim(ax_dos.get_ylim())
        self.dosFolderInst.save_fig(
            fig, fname="dos_{}".format(self.dosCalInst.broadening)
        )

        return


class JdosFiles:
    def __init__(self) -> None:
        pass
