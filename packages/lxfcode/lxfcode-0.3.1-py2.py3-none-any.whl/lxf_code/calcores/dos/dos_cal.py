from ..abc.abmoire import ABMoHa
from ..abc.abcal import ABCal
from ..pubmeth.pubmeth import DefinedFuncs

from ..multical.multicorecal import MultiCal
import sys

import numpy as np


class DosCal(ABCal):
    def __init__(
        self,
        haInst: ABMoHa,
        density: int = 70,
        cal_corenum: int = 3,
        e_range=np.linspace(-2000, 200, 300),
        dos_broadening=1,
        cal_hint=False,
        large_scale_cal=False,
    ) -> None:
        super().__init__(haInst, density, cal_corenum)

        self.e_range = e_range
        self.broadening = dos_broadening

        self.cal_hint = cal_hint
        self.large_scal_cal = large_scale_cal

    def energies_cal(self, k_arr):
        h = self.haInst.h(k_arr)

        eig_vals = np.real(np.linalg.eig(h)[0])

        eig_vals.sort()

        return np.real(eig_vals)

    def calculate(self):
        k_arrs = self.kps_in_BZ()[0]

        eig_vals = MultiCal(
            self.energies_cal,
            k_arrs,
            [],
            core=self.calcoren,
            disable_hint=(not self.cal_hint),
        ).calculate()

        eig_vals = np.array(eig_vals)

        if not self.large_scal_cal:
            dos = DefinedFuncs.deltaF_arct(eig_vals, self.e_range, a=self.broadening)
        else:
            print("Large scale calculations...")
            dos = []
            for ele_e in self.e_range:
                ele_dos = DefinedFuncs.deltaF_arct(eig_vals, ele_e, a=self.broadening)
                ele_dos = np.sum(ele_dos)
                dos.append(ele_dos)
            dos = np.array(dos)

        print("Shape of the joint energy matrix: ", dos.shape)
        print("Size of joint energy (MB): ", sys.getsizeof(dos) / 1024**2)

        return eig_vals, dos  # eigen_values_mat, dos_results
