#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yuchen He
@contact: heyuchen@tgqs.net
@version: 1.0.0
@file: TripleGate.py
@time: 2024/1/16 17:05
"""
from numba import njit, prange
def ActOn_State(psi, num_qubits, Gate_type, Gate_pos, *Angles):
    """

    :param psi:
    :param num_qubits:
    :param Gate_type:
    :param Gate_pos:
    :param Angles:
    :return:
    """

    # todo 目前只有Toffoli门
    j2 = sorted(Gate_pos)[2]  # 高位比特，不区分控制位与目标位
    j1 = sorted(Gate_pos)[1]  # 中间位比特，不区分控制位与目标位
    j0 = sorted(Gate_pos)[0]  # 低位比特，不区分控制位与目标位
    # j0<j1<j2
    i1_plus = 2 ** j0
    i2_plus = 2 ** j1
    i3_plus = 2 ** j0 + 2 ** j1
    i4_plus = 2 ** j2
    i5_plus = 2 ** j2 + 2 ** j0
    i6_plus = 2 ** j2 + 2 ** j1
    i7_plus = 2 ** j2 + 2 ** j1 + 2 ** j0
    delta3 = 2 ** (j2 + 1)
    delta2 = 2 ** (j1 + 1)
    delta1 = 2 ** (j0 + 1)
    max3 = 2 ** num_qubits - 2 ** (j2 + 1)
    max2 = 2 ** j2 - 2 ** (j1 + 1)
    max1 = 2 ** j1 - 2 ** (j0 + 1)
    max0 = 2 ** j0 - 1

    for k in prange(0, max3 + 1, delta3):
        for l in prange(0, max2 + 1, delta2):
            for m in prange(0, max1 + 1, delta1):
                for n in prange(0, max0 + 1):
                    i0 = m | l | k | n  # to get index of a(*...*0_j2*...*0_j1*...*0_j0*...*)
                    i1 = i0 | i1_plus  # to get index of a(*...*0_j2*...*0_j1*...*1_j0*...*)
                    i2 = i0 | i2_plus  # to get index of a(*...*0_j2*...*1_j1*...*0_j0*...*)
                    i3 = i0 | i3_plus  # to get index of a(*...*0_j2*...*1_j1*...*1_j0*...*)
                    i4 = i0 | i4_plus  # to get index of a(*...*1_j2*...*0_j1*...*0_j0*...*)
                    i5 = i0 | i5_plus  # to get index of a(*...*1_j2*...*0_j1*...*1_j0*...*)
                    i6 = i0 | i6_plus  # to get index of a(*...*1_j2*...*1_j1*...*0_j0*...*)
                    i7 = i0 | i7_plus  # to get index of a(*...*1_j2*...*1_j1*...*1_j0*...*)
                    if Gate_type == 'ccx':
                        # use rule to update matrix element of state
                        if Gate_pos[0] < Gate_pos[2] and Gate_pos[1] < Gate_pos[2]:
                            # case: control_q: q1,q0(q0,q1), target_q: q2 
                            # 011 -> 111 , 111 -> 011
                            psi[i3], psi[i7] = psi[i7], psi[i3]

                        elif Gate_pos[2] < Gate_pos[0] and Gate_pos[2] < Gate_pos[1]:
                            # case: control_q: q2q1(q1q2), target_q: q0
                            # 110 -> 111, 111-> 110
                            psi[i6], psi[i7] = psi[i7], psi[i6]

                        elif (Gate_pos[2] > Gate_pos[0] and Gate_pos[2] < Gate_pos[1]) or (
                                Gate_pos[2] > Gate_pos[1] and Gate_pos[2] < Gate_pos[0]):
                            # case: control_q: q0q2(q2q0), target_q: q1
                            # 101 -> 111 , 111 -> 101
                            psi[i5], psi[i7] = psi[i7], psi[i5]
                    elif Gate_type == "cswap":
                        if Gate_pos[0] < min(Gate_pos[1], Gate_pos[2]):
                            psi[i3], psi[i5] = psi[i5], psi[i3]
                        elif Gate_pos[1] < min(Gate_pos[0], Gate_pos[2]):
                            psi[i3], psi[i6] = psi[i6], psi[i3]
                        elif Gate_pos[2] < min(Gate_pos[0], Gate_pos[1]):
                            psi[i6], psi[i5] = psi[i5], psi[i6]
    return psi
