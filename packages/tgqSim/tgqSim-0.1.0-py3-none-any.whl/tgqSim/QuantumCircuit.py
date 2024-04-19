#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Yuchen He
@contact: heyuchen@tgqs.net
@version: 1.0.1
@file: QuantumCircuit.py
@time: 2024/1/16 17:16
"""
from GateSimulation import SingleGate, DoubleGate, TripleGate
from typing import Union
import random, os, ctypes
import numpy as np
import draw_circuit_tools as tools
import matplotlib.pyplot as plt
import GPUtil
# from numba import njit, prange

class Float2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float),
                ("y", ctypes.c_float)]

class GateInfo(ctypes.Structure):
    _fields_ = [
        ("gateName", ctypes.c_char_p),
        ("actionPos", ctypes.POINTER(ctypes.c_int)),
        ("theta", ctypes.c_float)
    ]


class Qubit:
    def __init__(self, name=None, idx=None, pos=None):
        self.label = 'p' if not name else name
        self.name = f'p_{idx+100}' if not name else f"{name}_{idx}"
        self.pos = pos + idx
        self.idx = idx

    # def __getattr__(self, item):
    #     if item == self.name:
    #         return self.idx
    #     if item == self.label+"["+str(self.pos)+"]":
    #         return self.idx

    def __str__(self):
        return str(self.name)


class SimulationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class QuantumCircuit:
    def __init__(self, qbit_number=None):
        self.qbit_list = [] if not qbit_number else self.add_qubits(number=qbit_number)
        self.cbit_list = []
        self.gate_list = []
        self.qbit_register = {}
        self.base_single_gate = ['h', 'x', 'y', 'z', 'rx', 'ry', 'rz', 'u3', 's', 'sdg', 't', 'tdg']
        self.base_double_gate = ['cx', 'swap', 'iswap', 'cz', 'cp', 'rxx', 'ryy', 'rzz']
        self.base_triple_gate = ['ccx', 'cswap']
        self.width = 0
        self.state = []
        self.circuit_diag = []
        self.isgpu = False
        self.deviceid = []

    def add_qubits(self, number: int, name: str = 'p'):
        """
        添加量子比特
        :param number: 比特数量
        :param name: 比特名称
        :return:
        """
        self.width += number
        if name not in self.qbit_register:
            self.qbit_register.update({name: number})
            sub_list = [Qubit(name=name, idx=i, pos=i+self.width) for i in range(number)]
        else:
            former_number = self.qbit_register[name]
            self.qbit_register.update({name: number+former_number})
            sub_list = [Qubit(name=name, idx=i+former_number, pos=i+self.width) for i in range(number)]
        self.qbit_list.append(sub_list)

    def add_single_gate(self, gate_pos: Union[int, str], *gate_info):
        """
        添加单比特门序列
        :param gate_pos:
        :param gate_info: 门类型，门参数
        :return:
        """
        if isinstance(gate_pos, int):
            gatename = gate_info[0].upper()
            self.circuit_diag.append([(gatename, gate_pos)])
        else:
            self.circuit_diag.append([(gatename, int(gate_pos))])
        return self.gate_list.append((gate_pos, gate_info))
        # todo 通过比特名称访问
        # if isinstance(gate_pos, str):
        #     return self.gate_list.append((gate_pos, gate_type))

    def add_double_gate(self, gate_pos_0, gate_pos_1, *gate_info):
        """
        添加两比特门序列
        :param gate_pos_0: 控制位
        :param gate_pos_1: 目标位
        :param gate_info: 门类型，门参数
        :return:
        """
        if gate_info[0] in ["rxx", 'ryy', 'rzz', 'iswap', 'syc']:
            self.circuit_diag.append([(gate_info[0].upper(), (gate_pos_1, gate_pos_0))])
        else:
            self.circuit_diag.append([(gate_info[0].upper(), gate_pos_1, gate_pos_0)])
        return self.gate_list.append(([gate_pos_0, gate_pos_1], gate_info))

    def add_triple_gate(self, gate_pos, *gate_info):
        """
        添加三比特门序列
        :param gate_pos:
        :param gate_info:
        :return:
        """
        self.circuit_diag.append([(gate_info[0].upper(), gate_pos[2], gate_pos[0], gate_pos[1])])
        return self.gate_list.append((gate_pos, gate_info))
    
    def setdevice(self, deviceList: Union[int, list]):
        gpus = GPUtil.getGPUs()
        gpuidList = [gpu.id for gpu in gpus]
        if isinstance(deviceList, int):
            deviceList = [deviceList]
        for deviceid in deviceList:
            if deviceid not in gpuidList:
                raise ValueError("设置设备ID不存在")
        self.isgpu = True
        self.deviceid = deviceList
    
    def _run_with_device(self):
        # 未测试
        dll_path = os.path.abspath('./lib/tgq_simulator.so')
        lib = ctypes.CDLL(dll_path)
        lib.execute_circuit.argtypes = [
            ctypes.POINTER(Float2),
            ctypes.POINTER(GateInfo),
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int
        ]
        gateInfo = []
        for (gate_pos, gate_info) in self.gate_list:
            if isinstance(gate_pos, int):
                length = 2
                gate_pos = [gate_pos]
            elif isinstance(gate_pos, list):
                length = len(gate_pos) + 1
            else:
                raise TypeError("Type of gate_pos must be int or list")
            gate_obj = GateInfo()
            actionPos = gate_pos + [-1]
            gate_obj.actionPos = (ctypes.c_int * length)(*actionPos)
            if len(gate_info) > 0:
                gate_obj.gateName = gate_info[0].encode(encoding='utf-8')
            if len(gate_info) > 1:
                gate_obj.theta = gate_info[1]
            gateInfo.append(gate_obj)
        gateInfoCData = (GateInfo * len(gateInfo))(*gateInfo)
        initial_state = [Float2(1.0, 0.0) if i == 0 else Float2(0.0, 0.0) for i in range(2 ** self.width)]
        psi = (Float2 * len(initial_state))(*initial_state)
        lib.execute_circuit(psi, gateInfoCData, len(gateInfo), self.width, self.deviceid[0])
        for i, ele in enumerate(psi):
            self.state[i] = ele.x + 1j * ele.y

    def run_statevector(self):
        """
        根据线路的门序列计算末态的量子态
        :return:
        """
        self.state = [1 if a == 0 else 0 for a in range(2**self.width)]
        if not self.isgpu:
            for (gate_pos, gate_info) in self.gate_list:
                gate_type = gate_info[0]
                angle = tuple(gate_info[1:])
                if gate_type in self.base_single_gate:
                    self.state = SingleGate.ActOn_State(self.state, self.width, gate_type, gate_pos, *angle)

                elif gate_type in self.base_double_gate:
                    set_gate_pos = set(gate_pos)
                    if len(set_gate_pos) != len(gate_pos):
                        raise SimulationError(f"Gate position cannot be the same: {gate_pos[0]}, {gate_pos[1]}")
                    self.state = DoubleGate.ActOn_State(self.state, self.width, gate_type, gate_pos, *angle)
                elif gate_type in self.base_triple_gate:
                    set_gate_pos = set(gate_pos)
                    if len(set_gate_pos) != len(gate_pos):
                        raise SimulationError(f"Gate position cannot be the same: "
                                            f"{gate_pos[0]}, {gate_pos[1]} and {gate_pos[2]}")
                    self.state = TripleGate.ActOn_State(self.state, self.width, gate_type, gate_pos, *angle)
                else:
                    raise SimulationError(f"Unkown gate type: {gate_type}")
        else:
            self._run_with_device()
    
    def random_circuit(self, num_qubits, num_gates: Union[int, list]):
        """
        生成随机线路
        :param num_qubits:
        :param num_gates: 门数量，列表表示单比特，多比特门数量
        :return:
        """
        self.width = num_qubits
        if isinstance(num_gates, int):
            base_gate_list = self.base_single_gate + self.base_double_gate + self.base_triple_gate
            for _ in range(num_gates):
                gate_type = np.random.choice(base_gate_list)
                angle = np.random.uniform(-2*np.pi, 2*np.pi, size=3)
                if gate_type in self.base_single_gate:
                    gate_pos = np.random.choice(np.array(range(num_qubits)), size=1)[0]
                elif gate_type in self.base_double_gate:
                    gate_pos = random.sample(range(num_qubits), 2)
                    gate_pos = list(gate_pos)
                elif gate_type in self.base_triple_gate:
                    gate_pos = random.sample(range(num_qubits), 3)
                    gate_pos = list(gate_pos)
                else:
                    gate_pos = None
                self.gate_list.append([gate_pos, tuple([gate_type]) + tuple(angle)])
        elif isinstance(num_gates, list):
            single_gate_num = num_gates[0]
            multiple_gate_num = num_gates[1]
            for _ in range(single_gate_num):
                gate_type = np.random.choice(self.base_single_gate)
                angle = np.random.uniform(-2*np.pi, 2*np.pi, size=3)
                gate_pos = np.random.choice(np.array(range(num_qubits)), size=1)[0]
                self.gate_list.append([gate_pos, tuple([gate_type]) + tuple(angle)])
            for _ in range(multiple_gate_num):
                base_gate_list = self.base_double_gate+self.base_triple_gate
                gate_type = np.random.choice(base_gate_list)
                angle = np.random.uniform(-2 * np.pi, 2 * np.pi, size=3)
                if gate_type in self.base_double_gate:
                    gate_pos = random.sample(range(num_qubits), 2)
                    gate_pos = list(gate_pos)
                elif gate_type in self.base_triple_gate:
                    gate_pos = random.sample(range(num_qubits), 3)
                    gate_pos = list(gate_pos)
                else:
                    gate_pos = None
                self.gate_list.append([gate_pos, tuple([gate_type]) + tuple(angle)])
                random.shuffle(self.gate_list)

    def h(self, qbit: Union[int, str]):
        return self.add_single_gate(qbit, 'h')

    def x(self, qbit):
        return self.add_single_gate(qbit, 'x')

    def y(self, qbit):
        return self.add_single_gate(qbit, 'y')

    def z(self, qbit):
        return self.add_single_gate(qbit, 'z')

    def rx(self, qbit, theta):
        return self.add_single_gate(qbit, 'rx', theta)

    def ry(self, qbit, theta):
        return self.add_single_gate(qbit, 'ry', theta)

    def rz(self, qbit: Union[int, str], theta):
        return self.add_single_gate(qbit, 'rz', theta)

    def u3(self, qbit, *theta):
        return self.add_single_gate(qbit, 'u3', *theta)
    
    def s(self, qbit:Union[int, str]):
        return self.add_single_gate(qbit, 's')
    
    def sdg(self, qbit:Union[int, str]):
        return self.add_single_gate(qbit, 'sdg')
    
    def t(self, qbit:Union[int, str]):
        return self.add_single_gate(qbit, 't')
    
    def tdg(self, qbit:Union[int, str]):
        return self.add_single_gate(qbit, 'tdg')

    def cx(self, control_qubit, target_qubit):
        return self.add_double_gate(control_qubit, target_qubit, 'cx')

    def swap(self, qubit_1, qubit_2):
        return self.add_double_gate(qubit_1, qubit_2, 'swap')

    def iswap(self, qubit_1, qubit_2):
        return self.add_double_gate(qubit_1, qubit_2, 'iswap')

    def cz(self, control_qubit, target_qubit):
        return self.add_double_gate(control_qubit, target_qubit, 'cz')

    def cp(self, control_qubit, target_qubit, theta):
        return self.add_double_gate(control_qubit, target_qubit, 'cp', theta)

    def rxx(self, qubit_1, qubit_2, theta):
        return self.add_double_gate(qubit_1, qubit_2, 'rxx', theta)

    def ryy(self, qubit_1, qubit_2, theta):
        return self.add_double_gate(qubit_1, qubit_2, 'ryy', theta)

    def rzz(self, qubit_1, qubit_2, theta):
        return self.add_double_gate(qubit_1, qubit_2, 'rzz', theta)

    def ccx(self, control_qubits: list, target_qubits: int):
        return self.add_triple_gate(control_qubits+[target_qubits], 'ccx')
    
    def show_quantum_circuit(self, plot_labels=True, **kwargs):
        """Use Matplotlib to plot a quantum circuit.
        kwargs    Can override plot_parameters
        """
        labels = []
        inits = {}
        for i in range(self.width):
            labels.append(f"q_{i}")
            inits[f"q_{i}"] = i
        plot_params = dict(scale = 1.0, fontsize = 14.5, linewidth = 2.0, 
                            control_radius = 0.05, not_radius = 0.15, 
                            swap_delta = 0.08, label_buffer = 0.8, 
                            rectangle_delta = 0.3, box_pad=0.2)
        plot_params.update(kwargs)
        scale = plot_params['scale']
        
        # Create labels from gates. This will become slow if there are a lot 
        #  of gates, in which case move to an ordered dictionary
        if not labels:
            labels = []
            for i,gate in tools.enumerate_gates(self.circuit_diag, schedule=True):
                for label in gate[1:]:
                    if label not in labels:
                        labels.append(label)
        
        nq = len(labels)
        nt = len(self.circuit_diag)
        wire_grid = np.arange(0.0, nq*scale, scale, dtype=float)
        gate_grid = np.arange(0.0, nt*scale, scale, dtype=float)
        gate_grid_index = [0.0 for _ in range(nq)]
        # print(gate_grid_index)
        
        fig,ax = tools.setup_figure(nq,nt,gate_grid,wire_grid,plot_params)

        measured = tools.measured_wires(self.circuit_diag, labels, schedule=True)
        tools.draw_wires(ax, nq, gate_grid, wire_grid, plot_params, 'k', measured)
        
        if plot_labels: 
            tools.draw_labels(ax, labels, inits, gate_grid, wire_grid, plot_params, 'k')

        tools.draw_gates(ax, self.circuit_diag, labels, gate_grid_index, wire_grid, plot_params, measured, schedule=True)
        plt.show()
        # return ax
    
    def measure(self, measure_bits_list: Union[list, int]=None, shots: int=1000)->dict:
        """
        测量们
        Args:
            measure_bits_list: 测量比特列表，传入比特位置或列表位置
            shots: 测量次数
        Returns:
            返回测量结果
        """
        # 首先通过执行操作得到所有的状态
        self.run_statevector()
        state = np.array(self.state)
        prob = np.real(state.conjugate() * state)
        count = {format(i, f'0{self.width}b'): prob[i] for i in range(len(prob))}
        distribution = {}

        if isinstance(measure_bits_list, int):
            measure_bits_list = [measure_bits_list]
        if measure_bits_list is None: # 若为空默认测量所有可能
            distribution = count
        
        # 计算测量分布
        for p in count.keys():
            # key = ''.join(p[pos - 1] for pos in measure_bits_list)
            key = ''.join(p[pos] for pos in measure_bits_list)
            if count[p] == 0:
                continue
            if key not in distribution:
                distribution[key] = count[p]
            else:
                distribution[key] += count[p]
        # 根据分布抽样概率
        result = {}
        cumulate = 0
        sample = np.random.uniform(0,1, size=shots)
        for key in distribution.keys():
            new_cumulate = cumulate + distribution[key]
            result[key] = sum((cumulate<=sample) & (sample<new_cumulate))
            cumulate = new_cumulate
        return result



# 下面这段代码仅限测试使用，不会参与实际工程
if __name__ == '__main__':
    nQubits = 9
    qc = QuantumCircuit()
    qc.add_qubits(nQubits, name='qft')
    for i in range(nQubits):
        if nQubits - 2 == i:
            qc.x(i)
        else:
            qc.h(i)
    for i in range(nQubits - 1, -1, -1):
        for j in range(i, -1, -1):
            if j == i:
                qc.h(j)
            else:
                qc.cp(control_qubit=j, target_qubit=i, theta=np.pi / (2 ** (i - j)))
    qc.x(0)
    for i in range(0, nQubits // 2):
        qc.swap(qubit_1=i, qubit_2=nQubits - 1 - i)
    qc.run_statevector()
    print(qc.state)
    print(len(qc.state))
    measure_pos = sorted([1, 0, 2], reverse=True)
    print(qc.measure(measure_bits_list=measure_pos))
    # qc.show_quantum_circuit()    
