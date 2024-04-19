"""
@author: Yuchen He
@contact: heyuchen@tgqs.net
@version: 1.0.0
@file: DoubleGate.py
@time: 2024/1/16 17:05
"""
import numpy as np
from numba import njit, prange
import cmath as cm

def ActOn_State(psi, num_qubits, Gate_type, Gate_pos, *Angles):
    # Gate_pos[0]:control bit
    j1 = sorted(Gate_pos)[1]  # 高位比特，不区分控制位与目标位
    # Gate_pos[1]:target bit
    j0 = sorted(Gate_pos)[0]  # 低位比特，不区分控制位与目标位

    i1_plus = 2 ** j0  #
    i2_plus = 2 ** j1  #
    i3_plus = 2 ** j0 + 2 ** j1  # for i3 = i0 + i3_plus
    delta2 = 2 ** (j1 + 1)
    delta1 = 2 ** (j0 + 1)
    max2 = 2 ** num_qubits - delta2
    max1 = 2 ** j1 - delta1
    max0 = 2 ** j0 - 1

    for k in prange(0, max2 + 1, delta2):
        for l in prange(0, max1 + 1, delta1):
            for m in prange(0, max0 + 1):
                i0 = m | l | k  # to get a(*...*0_j1*...*0_j0*...)
                i1 = i0 | i1_plus  # to get a(*...*0_j1*...*1_j0*...)
                i2 = i0 | i2_plus  # to get a(*...*1_j1*...*0_j0*...)
                i3 = i0 | i3_plus  # to get a(*...*1_j1*...*1_j0*...)
                if Gate_type == 'cx':
                        if Gate_pos[0] > Gate_pos[1]:
                            psi[i2],  psi[i3] =  psi[i3],  psi[i2]
                        else:
                            psi[i1],  psi[i3] =  psi[i3],  psi[i1]
                elif Gate_type == 'swap':
                        psi[i1], psi[i2] = psi[i2],  psi[i1]
                elif Gate_type == 'iswap':
                        psi[i1], psi[i2] = 1j * psi[i2], 1j * psi[i1]
                elif Gate_type == 'cz':
                        psi[i3] = -1.0 * psi[i3]
                elif Gate_type == 'cp':
                        psi[i3] = cm.exp(1j * Angles[0]) * psi[i3]
                elif Gate_type == 'rxx':
                        psi[i0], psi[i3] = cm.cos(Angles[0] / 2.0) *  psi[i0] + (-1j) * cm.sin(
                            Angles[0] / 2.0) *  psi[i3], \
                                                    cm.cos(Angles[0] / 2.0) *  psi[i3] + (-1j) * cm.sin(
                                                        Angles[0] / 2.0) *  psi[i0]
                        psi[i1], psi[i2] = cm.cos(Angles[0] / 2.0) * psi[i1] + (-1j) * cm.sin(
                            Angles[0] / 2.0) *  psi[i2], \
                                                    cm.cos(Angles[0] / 2.0) * psi[i2] + (-1j) * cm.sin(
                                                        Angles[0] / 2.0) * psi[i1]
                elif Gate_type == 'ryy':
                        psi[i0], psi[i3] = cm.cos(Angles[0] / 2.0) * psi[i0] + 1j * cm.sin(
                            Angles[0] / 2.0) *  psi[i3], \
                                                    cm.cos(Angles[0] / 2.0) * psi[i3] + 1j * cm.sin(
                                                        Angles[0] / 2.0) *  psi[i0]
                        psi[i1], psi[i2] = cm.cos(Angles[0] / 2.0) *  psi[i1] + (-1j) * cm.sin(
                            Angles[0] / 2.0) *  psi[i2], \
                                                    cm.cos(Angles[0] / 2.0) * psi[i2] + (-1j) * cm.sin(
                                                        Angles[0] / 2.0) * psi[i1]

                elif Gate_type == 'rzz':
                        psi[i0], psi[i1],  psi[i2],  psi[i3] = cm.exp(-0.5j * Angles[0]) *  psi[
                            i0], cm.exp(0.5j * Angles[0]) *  psi[i1], \
                                                                                    cm.exp(0.5j * Angles[0]) *  psi[
                                                                                        i2], cm.exp(-0.5j * Angles[0]) * \
                                                                                    psi[i3]

    return psi
