from typing import Union
from qualesim.plugin import *
from qualesim.host import *
from pyquiet.qir.QiProg import *
from pyquiet.qir.qModule.StdInstructions import QuietStdInstruction
from pyquiet.qir import QiVariable, VariableDecl, QiList
from pyquiet.qir.Variable import QuietVariable
from pyquiet.qir.Type import QuietType
from typing import List
from antlr4 import *
import numpy as np


class QiDataStack:
    def __init__(self) -> None:
        self.func_qubit = dict()
        self.func_int = dict()
        self.func_double = dict()
        self.free_list = []
        self.func_name = ""
        ## qubit_measure <--> self.qubit_measure[self.func_qubit[name][index]] = (value, prob)
        self.qubit_measure = dict()
        self.changeable_list = dict()
        self.qubit_list = dict()
        self.matrix_list = dict()
        self.qubit_now = []
        self.state_vector = []
        self.res_qubit = []
        self.res_qubit_m = []
        self.res_dict = []
        self.PC = 0


def check_type(var, types):
    try:
        if isinstance(var, types):
            return True
        else:
            return False
    except:
        if hasattr(types, "__origin__") and types.__origin__ == Union:
            for t in types.__args__:
                if isinstance(var, t):
                    return True
    return False


def is_type_single_gate(instr: QuietStdInstruction, func_data: QiDataStack):
    gate_list = ["H", "X", "Y", "Z", "S", "T", "Sdag", "Tdag"]
    operation_name = instr.opname
    if operation_name not in gate_list:
        return False
    instr_type = 0
    instr_dest = instr.qubit.name
    instr_index = 0
    instr_matrix = [j for i in instr.matrix for j in i]
    mat_matrix = instr.matrix
    if isinstance(instr.qubit, QiVariable):
        instr_type = 1
        instr_index, instr_dest = QiVar_index_name(instr.qubit, func_data)
    else:
        instr_type = 2
    return instr_type, instr_dest, instr_index, instr_matrix, mat_matrix


def is_type_ctrl_two_gate(instr: QuietStdInstruction, func_data: QiDataStack):
    gate_list = ["CNOT", "CZ"]
    operation_name = instr.opname
    if operation_name not in gate_list:
        return False
    instr_matrix = [j for i in instr.matrix[2:, 2:] for j in i]
    mat_matrix = instr.matrix
    instr_dest_index, instr_dest, instr_ctrl_index, instr_ctrl = QiVar2_index_name(
        instr.t_qubit, instr.c_qubit, func_data
    )
    return (
        instr_dest,
        instr_dest_index,
        instr_ctrl,
        instr_ctrl_index,
        instr_matrix,
        mat_matrix,
    )


def is_type_ctrl_phase_two_gate(instr: QuietStdInstruction, func_data: QiDataStack):
    gate_list = ["CP", "CRz"]
    operation_name = instr.opname
    if operation_name not in gate_list:
        return False
    angel_list_row = instr.angle
    angel_list = []
    for i in range(len(angel_list_row)):
        if isinstance(angel_list_row[i], QiVariable):
            if str(angel_list_row[i].type) == "int":
                index, name = QiVar_index_name(angel_list_row[i], func_data)
                angel_list.append(func_data.func_int[name][index])
            elif str(angel_list_row[i].type) == "double":
                index, name = QiVar_index_name(angel_list_row[i], func_data)
                angel_list.append(func_data.func_double[name][index])
        else:
            angel_list.append(angel_list_row[i])
    if operation_name == "CP":
        instr_matrix = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, np.exp(1j * angel_list[0])],
            ]
        )
    if operation_name == "CRz":
        instr_matrix = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, np.exp(-1j * angel_list[0] / 2), 0],
                [0, 0, 0, np.exp(1j * angel_list[0] / 2)],
            ]
        )
    mat_matrix = instr_matrix
    instr_matrix = [j for i in instr_matrix[2:, 2:] for j in i]
    instr_dest_index, instr_dest, instr_ctrl_index, instr_ctrl = QiVar2_index_name(
        instr.t_qubit, instr.c_qubit, func_data
    )
    return (
        instr_dest,
        instr_dest_index,
        instr_ctrl,
        instr_ctrl_index,
        instr_matrix,
        mat_matrix,
    )


def is_type_two_gate(instr: QuietStdInstruction, func_data: QiDataStack):
    gate_list = ["SWAP"]
    operation_name = instr.opname
    if operation_name not in gate_list:
        return False
    instr_matrix = [j for i in instr.matrix for j in i]
    mat_matrix = instr.matrix
    instr_dest_index, instr_dest, instr_ctrl_index, instr_ctrl = QiVar2_index_name(
        instr.t_qubit, instr.c_qubit, func_data
    )
    return (
        instr_dest,
        instr_dest_index,
        instr_ctrl,
        instr_ctrl_index,
        instr_matrix,
        mat_matrix,
    )


def is_type_1QRotation_gate(instr: QuietStdInstruction, func_data: QiDataStack):
    gate_list = ["Rx", "Ry", "Rz", "Rxy", "U4"]
    operation_name = instr.opname
    if operation_name not in gate_list:
        return False
    instr_type = 0
    instr_dest = instr.qubit.name
    instr_index = 0
    angel_list_row = instr.angle
    angel_list = []
    for i in range(len(angel_list_row)):
        if isinstance(angel_list_row[i], QiVariable):
            if str(angel_list_row[i].type) == "int":
                index, name = QiVar_index_name(angel_list_row[i], func_data)
                angel_list.append(func_data.func_int[name][index])
            elif str(angel_list_row[i].type) == "double":
                index, name = QiVar_index_name(angel_list_row[i], func_data)
                angel_list.append(func_data.func_double[name][index])
        else:
            angel_list.append(angel_list_row[i])

    if operation_name == "Rx":
        instr_matrix = np.array(
            [
                [
                    np.cos(angel_list[0] / 2),
                    -1j * np.sin(angel_list[0] / 2),
                ],
                [
                    -1j * np.sin(angel_list[0] / 2),
                    np.cos(angel_list[0] / 2),
                ],
            ]
        )
    elif operation_name == "Ry":
        instr_matrix = np.array(
            [
                [np.cos(angel_list[0] / 2), -np.sin(angel_list[0] / 2)],
                [np.sin(angel_list[0] / 2), np.cos(angel_list[0] / 2)],
            ]
        )
    elif operation_name == "Rz":
        instr_matrix = np.array(
            [
                [np.exp(-1j * angel_list[0] / 2), 0],
                [0, np.exp(1j * angel_list[0] / 2)],
            ]
        )
    elif operation_name == "Rxy":
        instr_matrix = np.array(
            [
                [
                    np.cos(angel_list[0] / 2),
                    -1j * np.exp(-1j * angel_list[1]) * np.sin(angel_list[0] / 2),
                ],
                [
                    -1j * np.exp(1j * angel_list[1]) * np.sin(angel_list[0] / 2),
                    np.cos(angel_list[0] / 2),
                ],
            ]
        )
    elif operation_name == "U4":
        instr_matrix = np.array(
            [
                [
                    np.exp(1j * (angel_list[0] - angel_list[1] / 2 - angel_list[3] / 2))
                    * np.cos(angel_list[2] / 2),
                    -np.exp(
                        1j * (angel_list[0] - angel_list[1] / 2 + angel_list[3] / 2)
                    )
                    * np.sin(angel_list[2] / 2),
                ],
                [
                    np.exp(1j * (angel_list[0] + angel_list[1] / 2 - angel_list[3] / 2))
                    * np.sin(angel_list[2] / 2),
                    np.exp(1j * (angel_list[0] + angel_list[1] / 2 + angel_list[3] / 2))
                    * np.cos(angel_list[2] / 2),
                ],
            ]
        )
    mat_matrix = instr_matrix
    instr_matrix = [j for i in instr_matrix for j in i]

    if isinstance(instr.qubit, QiVariable):
        instr_type = 1
        instr_index, instr_dest = QiVar_index_name(instr.qubit, func_data)
    else:
        instr_type = 2
    return instr_type, instr_dest, instr_index, instr_matrix, mat_matrix


## Get QiVariable's name and index
def QiVar_index_name(var: QiVariable, func_data: QiDataStack):
    index = 0
    if var.is_vector:
        if isinstance(var.index, str):
            index = func_data.func_int[var.index][0]
        else:
            index = var.index
        if var.name in func_data.changeable_list.keys():
            if func_data.changeable_list[var.name] == "int":
                l = len(func_data.func_int[var.name])
                if l <= index:
                    func_data.func_int[var.name] = func_data.func_int[var.name] + [
                        0
                    ] * (index - l + 1)
            elif func_data.changeable_list[var.name] == "double":
                l = len(func_data.func_double[var.name])
                if l <= index:
                    func_data.func_double[var.name] = func_data.func_double[
                        var.name
                    ] + [0.0] * (index - l + 1)
    return index, var.name


def QiVar2_index_name(var1: QiVariable, var2: QiVariable, func_data: QiDataStack):
    index1, name1 = QiVar_index_name(var1, func_data)
    index2, name2 = QiVar_index_name(var2, func_data)
    return index1, name1, index2, name2


## Ctrl word
def ctrl_word(instr, func_data: QiDataStack):
    ctrl_qubit = []
    if instr.ctrl_word.ctrl:
        for var in instr.ctrl_word.ctrl_qubits:
            index, name = QiVar_index_name(var, func_data)
            ctrl_qubit.append(func_data.func_qubit[name][index])
    return ctrl_qubit


## We use the str instead of the isinstance function to avoid fatal.
def check_var_type(qtype: QuietType):
    if str(qtype) == "qubit":
        return 1
    if str(qtype) == "int":
        return 2
    if str(qtype) == "double":
        return 3
    return 0


## function init
def func_initial(
    args_in: List[VariableDecl],
    args_out: List[VariableDecl],
    qi_input: list,
    qi_output: List[QuietVariable],
):
    func_data: QiDataStack = QiDataStack()
    for i in range(len(args_in)):
        name = args_in[i].var.name
        i_type = check_var_type(args_in[i].type)
        if i_type == 1:
            func_data.func_qubit[name] = qi_input[i]
        elif i_type == 2:
            func_data.func_int[name] = qi_input[i]
            if isinstance(args_in[i].var, QiList) and args_in[i].var.size == 0:
                func_data.changeable_list[name] = str(args_in[i].type)
        elif i_type == 3:
            func_data.func_double[name] = qi_input[i]
            if isinstance(args_in[i].var, QiList) and args_in[i].var.size == 0:
                func_data.changeable_list[name] = str(args_in[i].type)
    for i in range(len(args_out)):
        name = args_out[i].var.name
        size = 1
        if isinstance(args_out[i].var, QiList):
            if args_out[i].var.size != 0:
                size = args_out[i].var.size
            else:
                size = qi_output[i].size
                if size == 0:
                    func_data.changeable_list[name] = str(args_out[i].type)
        i_type = check_var_type(args_out[i].type)
        if i_type == 2:
            func_data.func_int[name] = [0] * size
        elif i_type == 3:
            func_data.func_double[name] = [0.0] * size
    return func_data
