from qualesim.plugin import *
from qualesim.host import *
from pyquiet.qir.QiProg import *
from pyquiet.QiParser.QiParser import QiParser
from pyquiet.qir.qModule.IntInstruction import QuietImInstruction
from pyquiet.qir.qModule.FloatInstructions import QuietFmInstruction
from pyquiet.qir.qbody.Function import QiLabelTable
from pyquiet.qir import (
    FunctionCall,
    QiDefineGate,
    QiVariable,
    QiList,
    DoubleType,
    IntType,
    QiProgram,
)
from typing import List
from antlr4 import *
from .utils import *
from pathlib import Path


@plugin("QUIET-S", "DDL", "0.0.2")
class QUIETs(Frontend):
    """QUIETs frontend plugin. Must be implemented with the input *.qi file"""

    # ==========================================================================
    # Init the plugin
    # ==========================================================================
    def __init__(self, filename, host_arb_ifaces=None, upstream_arb_ifaces=None):
        """Create the QUIETs Frontend plugin with the input filename.

        Args:
            filename (*.qi): filename is the input qi file to be simulated.
            host_arb_ifaces (_type_, optional): the argument is lists
            of strings representing the supported interface IDs. Defaults to None.
            upstream_arb_ifaces (_type_, optional): the argument is lists
            of strings representing the supported interface IDs. Defaults to None.
        """
        super().__init__(host_arb_ifaces, upstream_arb_ifaces)

        # use ensure_path to transform the str(filename) to Path(filename).

        self.parser: QiParser = QiParser()
        self.parser.handle_parser(filename)

        # parse the input file into QiProgram, you can refer to self.parse below.
        self.qiprog: QiProgram = self.parser.prog

        # get the body section of self.qiprog which stores the instructions of qifile.
        self.qibody: QiBodySection = self.qiprog.body_section

        # get the main section. Defaults to None.
        self.qimain: QiFunction = None

    # ==========================================================================
    # Handle run the plugin
    # ==========================================================================
    def handle_run(self, **kwards):
        """Here is the handle_run function, it will control the simulation with different
        inputs.

        Args:
            **kwards: We use keyword parameters as input, now we have
                measure_mod="one_shot" and num_shots=int /
                measure_mod="state_vector" /
                measure_mod="Matrix"

        Returns:
            ArbData: Return the ArbData to the upstream plugin. You can call the res with
            key-value form.
        """
        # determine whether to simulate the file based on the presence of the main function.
        try:
            # measure_mod default is one_shot and num_shots default is 1.
            measure_mod = "one_shot"
            if "measure_mod" in kwards.keys():
                measure_mod = kwards["measure_mod"]
            num_shots = 1
            if "num_shots" in kwards.keys():
                num_shots = kwards["num_shots"]
            get_prob = False
            if "get_probability" in kwards.keys():
                get_prob = kwards["get_probability"]

            # call the run_with_exemode with measure_mod and num_shots.
            arb = self.run_with_exemode(measure_mod, num_shots, get_prob)
            return arb
        except:
            self.info("There is no start!")

    def run_with_exemode(self, measure_mod: str, num_shots=1, get_prob=False):
        """Run the simulation with different exemode.
        if the measure_mod is one_shot, num_shots=2, the output is:
            {'quantum': (['q1', 'q2', 'q3'], [[1, 0, 0],
                                              [1, 0, 0]]),
            'classical': [{'c1': [1], 'c2': [0], 'c3': [0]},
                          {'c1': [1], 'c2': [0], 'c3': [0]}]}
            the classical result and quantum result is one-to-one correspondence.
        if the measure_mod is state_vector, the output is:
            {{['q1', 'q2', 'q3']:'[(0.4999999999999998+0j), 0j,
                                   (0.4999999999999998+0j), 0j,
                                   0j, (0.4999999999999998+0j),
                                   0j, (0.4999999999999998+0j)]'}}
        if the measure_mod is matrix, the output is:
            [{matrix1:[qubit_list1]}, {matrix2:[qubit_list2]}]

        Args:
            measure_mod (str): one_shot / state_vector / matrix
            num_shots (int, optional): if measure_mod = one_shot, num_shots would work.
            Defaults to 1.
            get_prob (bool): default False to accelerate the one_shot and state_vector's
            speed.

        Returns:
            arb (ArbData): Returns ArbData to the handle_run function.
        """
        # get the start and output of the qifile.
        self.qimain = self.qiprog.main_func()
        qi_output: List[QuietVariable] = []
        for ii in self.qimain.get_output_args():
            qi_output.append(ii.var)

        # construct the output of different exemode.
        qubit_value = []
        classical_value = []
        if measure_mod not in ["one_shot", "state_vector", "Matrix"]:
            get_prob = True
        res, ret = self.function_run(self.qimain, [], qi_output, measure_mod, get_prob)
        qubit_value.append(res.res_dict)
        classical_value.append(ret)
        if measure_mod == "one_shot" and num_shots > 1:
            for ii in range(num_shots - 1):
                res, ret = self.function_run(
                    self.qimain, [], qi_output, measure_mod, get_prob
                )
                qubit_value.append(res.res_dict)
                classical_value.append(ret)
        one_shot = dict()
        one_shot["classical"] = classical_value
        one_shot["quantum"] = (res.res_qubit_m, qubit_value)
        state_vector = res.state_vector
        if measure_mod == "one_shot":
            fn = one_shot
        elif measure_mod == "state_vector":
            fn = state_vector
        elif measure_mod == "Matrix":
            fn = res.matrix_list
        else:
            fn = []
        # construct the ret ArbData.
        arb = ArbData(
            func_qubit=res.func_qubit,
            func_int=res.func_int,
            func_double=res.func_double,
            qubit_measure=res.qubit_measure,
            res=fn,
        )
        return arb

    def function_run(
        self,
        qi_function: QiFunction,
        qi_input: list,
        qi_output: List[QuietVariable],
        measure_mod="one_shot",
        get_prob=False,
    ):
        """Here is the function_run, we simulate the quiet-s instructions here.

        Args:
            qi_function (QiFunction): the start is main_func, and when it comes to
                                      FunctionCall instructions, it will call the subfunction
                                      here.
            qi_input (list): the list of function's input, it will bind the value of the input.
            qi_output (List[QuietVariable]): the output of QiFunction's __output_args.
            measure_mod (str, optional): measure_mod is one_shot /state_vector Matrix/. Defaults
                                         to "one_shot".
            Mat (list, optional): store the circuit matrix. Defaults to [].

        Returns:
            main:
                func_data (QiDataStack): if the simulated function is 'main' function, the function returns the func_data as output
                ret (dict): if the simulated function is 'main' function, the ret stores the "main"'s output.
            sub_function:
                output_int (dict): sub_function's return int value.
                output_double: sub_function's return double value.
        """
        # initial the func_data using the input and output.

        args_func_input: List[VariableDecl] = qi_function.get_input_args()
        args_func_output: List[VariableDecl] = qi_function.get_output_args()
        func_data: QiDataStack = func_initial(
            args_func_input, args_func_output, qi_input, qi_output
        )
        func_data.func_name = qi_function.func_name
        func_data.matrix_list[func_data.func_name] = []
        measure_flag = 0

        # bind the index for formal parameters and arguments.
        output_index = dict()
        for i in range(len(qi_output)):
            if isinstance(qi_output[i], QiVariable):
                index, name = QiVar_index_name(qi_output[i], func_data)
            else:
                name = qi_output[i].name
                index = -1
            output_index[name] = (args_func_output[i].var.name, index)
        func_label = qi_function.label_table()
        # start the simulation.
        func_body = qi_function.body
        while func_data.PC < len(func_body):
            instr = func_body[func_data.PC]
            # variable declaration
            if isinstance(instr, VariableDecl):
                self.function_var_decl(instr, func_data)

            # function call, and measure is a special form of function call instructions.
            elif isinstance(instr, FunctionCall):
                if instr.name == "measure":
                    measure_flag = 1
                    self.function_measure_res(
                        func_body, func_data, measure_mod, get_prob
                    )
                else:
                    func_data.matrix_list[func_data.func_name].append(
                        "call func " + str(instr)
                    )
                    self.function_call(instr, func_data)

            ## QUIET-s Instructions
            elif isinstance(instr, QiDefineGate):
                self.qu_defined_gate(instr, func_data)
            elif check_type(instr, QuietStdInstruction):
                self.qu_std_instr(instr, func_data)
            elif check_type(instr, QuietFmInstruction):
                self.qu_fm_instr(instr, func_data)
            elif check_type(instr, QuietImInstruction):
                self.qu_im_instr(instr, func_data, func_label)
            func_data.PC = func_data.PC + 1
        # free the temporary qubit.

        # construct the output of the function.
        output_int = dict()
        output_double = dict()
        for i in qi_output:
            if isinstance(i.type, IntType):
                if isinstance(i, QiList):
                    output_int[i.name] = (
                        func_data.func_int[output_index[i.name][0]],
                        -1,
                    )
                else:
                    output_int[i.name] = (
                        func_data.func_int[output_index[i.name][0]],
                        output_index[i.name][1],
                    )
            if isinstance(i.type, DoubleType):
                if isinstance(i, QiList):
                    output_double[i.name] = (
                        func_data.func_double[output_index[i.name][0]],
                        -1,
                    )
                else:
                    output_double[i.name] = (
                        func_data.func_double[output_index[i.name][0]],
                        output_index[i.name][1],
                    )
        # construct the main return.
        if qi_function.func_name == "main":
            # classical output.
            out_int = dict()
            for i in output_int.keys():
                out_int[i] = output_int[i][0]
            out_double = dict()
            for i in output_double.keys():
                out_double[i] = output_double[i][0]
            ret = dict(**out_int, **out_double)

            res_state_vector = dict()
            res_cls = dict()
            res_sv = dict()
            # quantum output.
            for ml in func_data.func_qubit.keys():
                if len(func_data.func_qubit[ml]) == 1:
                    try:
                        func_data.qubit_measure[func_data.func_qubit[ml][0]] = (self.get_measurement(func_data.func_qubit[ml][0]).value,self.get_measurement(func_data.func_qubit[ml][0])["probability"],self.get_measurement(func_data.func_qubit[ml][0])["state_vector"])
                    except:
                        pass
                else:
                    for mi in range(len(func_data.func_qubit[ml])):
                        try:
                            func_data.qubit_measure[func_data.func_qubit[ml][mi]] = (self.get_measurement(func_data.func_qubit[ml][mi]).value,self.get_measurement(func_data.func_qubit[ml][mi])["probability"],self.get_measurement(func_data.func_qubit[ml][mi])["state_vector"])
                        except:
                            pass
            for jj in func_data.qubit_measure.keys():
                func_data.res_dict.append(func_data.qubit_measure[jj][0])
                for ii in func_data.func_qubit.keys():
                    if (
                        len(func_data.func_qubit[ii]) == 1
                        and func_data.func_qubit[ii][0] == jj
                    ):
                        res_cls[ii] = func_data.qubit_measure[jj][0]
                        func_data.res_qubit_m.append(ii)
                    elif len(func_data.func_qubit[ii]) != 1:
                        for ik in range(len(func_data.func_qubit[ii])):
                            if func_data.func_qubit[ii][ik] == jj:
                                res_cls[
                                    str(ii) + "[" + str(ik) + "]"
                                ] = func_data.qubit_measure[jj][0]
                                func_data.res_qubit_m.append(
                                    str(ii) + "[" + str(ik) + "]"
                                )
            for ii in func_data.func_qubit.keys():
                for jj in range(len(func_data.func_qubit[ii])):
                    if (
                        func_data.func_qubit[ii][jj]
                        not in func_data.qubit_measure.keys()
                    ):
                        if len(func_data.func_qubit[ii]) == 1:
                            func_data.res_qubit.append(ii)
                        else:
                            func_data.res_qubit.append(str(ii) + "[" + str(jj) + "]")
            res_state_vector["classical"] = res_cls
            if measure_mod == "state_vector":
                if measure_flag == 1:
                    res_state_vector["quantum"] = (
                        func_data.res_qubit,
                        eval(func_data.state_vector)[1],
                    )
                else:
                    if len(func_data.free_list) == 0:
                        res_state_vector["quantum"] = [1]
                    else:
                        tar = func_data.func_qubit[func_data.free_list[0]][0]
                        self.measure(
                            tar,
                            arb=ArbData(measure_mod="measureforres"),
                        )
                        res_state_vector["quantum"] = (
                            func_data.res_qubit,
                            eval(self.get_measurement(tar)["state_vector"])[1],
                        )
                if 2 ** len(res_state_vector["quantum"][0]) != len(
                    res_state_vector["quantum"][1]
                ):
                    self.info(
                        "here is untraced qubit, and may rise a bug when exemod is statevector in quantumsim backend!"
                    )
            func_data.state_vector = str(res_state_vector)
            for i in func_data.free_list:
                self.free(func_data.func_qubit[i])
            return func_data, ret

        for i in func_data.free_list:
            self.free(func_data.func_qubit[i])
        return output_int, output_double, func_data.matrix_list

    def function_var_decl(self, instr: VariableDecl, func_data: QiDataStack):
        """The function_var_decl is to handle VariableDecl instructions.

        Args:
            instr (VariableDecl): the input instruction.
            func_data (QiDataStack): func_data is to store the datas of simulation.
        """
        # get the name and size.
        var_size = 1
        var_name = instr.var.name
        if isinstance(instr.var, QiList):
            var_size = instr.var.size

        # store it into different dict depend on the type of variables.
        i_type = check_var_type(instr.type)
        if i_type == 1:
            # the qubit allocated should be added into qubit_list when it is not be measured.
            # the qubit allocated in the function should be added into free_list.
            func_data.func_qubit[var_name] = self.allocate(var_size)
            func_data.qubit_list[var_name] = [-1] * var_size
            func_data.free_list.append(var_name)
            for i in range(var_size):
                if var_size == 1:
                    func_data.qubit_now.append(var_name)
                else:
                    func_data.qubit_now.append(var_name + "[" + str(i) + "]")
        elif i_type == 2:
            func_data.func_int[var_name] = [0] * var_size
        elif i_type == 3:
            func_data.func_double[var_name] = [0.0] * var_size

    def function_measure_res(
        self, func_body: list, func_data: QiDataStack, measure_mod: str, get_prob=False
    ):
        """the function will return measure result.

        Args:
            func_body (list): func_body is the list of instructions, you can refer to the next
                              instruction using PC.
            func_data (QiDataStack): func_data is to store the datas of simulation.
            measure_mod (str): measure_mod is one_shot /state_vector Matrix/. Defaults
                               to "one_shot".
        """
        # contact the measure input and output.
        measure_inputs: List[QuietVariable] = []
        measure_outputs: List[QuietVariable] = []
        func_data.PC, measure_inputs, measure_outputs = self.func_measure(
            func_body, func_data.PC, measure_inputs, measure_outputs
        )

        # the input should not be repeated, so we use the
        measure_list = []
        for it in measure_inputs:
            if isinstance(it, QiVariable):
                index, name = QiVar_index_name(it, func_data)
                measure_list = measure_list + [func_data.func_qubit[name][index]]
            else:
                measure_list = measure_list + func_data.func_qubit[it.name]
        qubit_measure_list = dict()
        for i in range(len(measure_list)):
            if measure_list[i] in qubit_measure_list.keys():
                qubit_measure_list[measure_list[i]] = (
                    qubit_measure_list[measure_list[i]] + 1
                )
            else:
                qubit_measure_list[measure_list[i]] = 1
        measure_targets = list(qubit_measure_list.keys())
        self.measure(
            measure_targets,
            arb=ArbData(measure_mod=measure_mod, get_probability=get_prob),
        )

        # sv is the statevector from backend, it includes the rest of qubits unmeasured.
        sv = self.get_measurement(measure_list[0])["state_vector"]

        # store the measure result into datastack.
        count = 0
        for j in range(len(measure_outputs)):
            it = measure_outputs[j]
            name = it.name
            pr = []
            if str(it.type) == "int":
                if isinstance(it, QiList):
                    for i in range(it.size):
                        func_data.func_int[name][i] = self.get_measurement(
                            measure_list[count]
                        ).value
                        self.f(func_data, measure_list, count)
                        count = count + 1
                    pr = func_data.func_int[name]
                else:
                    index, name = QiVar_index_name(it, func_data)
                    func_data.func_int[name][index] = self.get_measurement(
                        measure_list[count]
                    ).value
                    self.f(func_data, measure_list, count)
                    count = count + 1
                    pr = func_data.func_int[name][index]
            elif str(it.type) == "double":
                if isinstance(it, QiList):
                    for i in range(it.size):
                        func_data.func_double[name][i] = self.get_measurement(
                            measure_list[count]
                        ).value
                        self.f(func_data, measure_list, count)
                        count = count + 1
                    pr = func_data.func_double[name]
                else:
                    index, name = QiVar_index_name(it, func_data)
                    func_data.func_double[name][index] = self.get_measurement(
                        measure_list[count]
                    ).value
                    self.f(func_data, measure_list, count)
                    count = count + 1
                    pr = func_data.func_double[name][index]

            # store the qubit measure value in func_data.qubit_list.
            if isinstance(measure_inputs[j], QiList):
                func_data.qubit_list[measure_inputs[j].name] = pr
            else:
                index, name = QiVar_index_name(measure_inputs[j], func_data)
                func_data.qubit_list[name][index] = pr
        func_data.state_vector = sv

    def f(self, func_data: QiDataStack, measure_list: list, count: int):
        """store the measure result into datastack.

        Args:
            func_data (QiDataStack): func_data is to store the datas of simulation.
            measure_list (list): measure_list is the list of measure qubit's index.
            count (int): the index.
        """
        try:
            func_data.qubit_measure[measure_list[count]] = (
                self.get_measurement(measure_list[count]).value,
                self.get_measurement(measure_list[count])["probability"],
                self.get_measurement(measure_list[count])["state_vector"],
            )
        except:
            func_data.qubit_measure[measure_list[count]] = (
                self.get_measurement(measure_list[count]).value,
                self.get_measurement(measure_list[count])["probability"],
            )

    def func_measure(
        self,
        func_body: list,
        PC: int,
        measure_inputs: List[QuietVariable],
        measure_outputs: List[QuietVariable],
    ):
        """the func_measure is to handle the continuous measure instructions, the function
        will contact these measure instructions together to measure at once.

        Args:
            func_body (list): func_body is the list of instructions, you can refer to the next
                              instruction using PC.
            PC (int): the index of instructions.
            measure_inputs (List[QuietVariable]): the input qubit.
            measure_outputs (List[QuietVariable]): the measure res.

        Returns:
            PC (int): PC indicated the current index of instructions.
            measure_inputs (List[QuietVariable]): the input of measure.
            measure_outputs (List[QuietVariable]): the output of measure.
        """
        flag = 0
        instr: FunctionCall = func_body[PC]

        # the measure option needs equal inputs and outputs.
        if isinstance(instr.inputs[0], QiList) and isinstance(instr.outputs[0], QiList):
            if instr.inputs[0].size != instr.outputs[0].size:
                self.error("measure input list is not equal to the output!")
            else:
                flag = 1
        elif isinstance(instr.inputs[0], QiVariable) and isinstance(
            instr.outputs[0], QiVariable
        ):
            flag = 1
        else:
            self.error("measure input and output are not the same!")
        measure_inputs.append(instr.inputs[0])
        measure_outputs.append(instr.outputs[0])

        # the step below will contract the continuous measure option.
        if (
            flag == 1
            and PC + 1 < len(func_body)
            and isinstance(func_body[PC + 1], FunctionCall)
            and func_body[PC + 1].name == "measure"
        ):
            PC, measure_inputs, measure_outputs = self.func_measure(
                func_body, PC + 1, measure_inputs, measure_outputs
            )
        return PC, measure_inputs, measure_outputs

    def function_call(self, instr: FunctionCall, func_data: QiDataStack):
        """function_call is to handle the FunctionCall instructions.

        Args:
            instr (FunctionCall): the instructions, we can get the function, input and output from instr.
            func_data (QiDataStack): func_data is to store the datas of simulation.
        """

        # handle the input list, and save the input value into inputlist.
        inputlist = []
        for i in instr.inputs:
            if isinstance(i, QiList):
                if str(i.type) == "qubit":
                    inputlist.append(func_data.func_qubit[i.name])
                elif str(i.type) == "int":
                    inputlist.append(func_data.func_int[i.name])
                elif str(i.type) == "double":
                    inputlist.append(func_data.func_double[i.name])
            elif isinstance(i, QiVariable):
                index, name = QiVar_index_name(i, func_data)
                l = []
                if str(i.type) == "qubit":
                    l.append(func_data.func_qubit[name][index])
                    inputlist.append(l)
                elif str(i.type) == "int":
                    l.append(func_data.func_int[name][index])
                    inputlist.append(l)
                elif str(i.type) == "double":
                    l.append(func_data.func_double[name][index])
                    inputlist.append(l)
            elif isinstance(i, list):
                inputlist.append(i)
            elif isinstance(i, (int,float)):
                inputlist.append([i])
        # get the called function from self.qibody.
        sub_func = None
        for func in self.qibody.functions:
            if func.func_name == instr.name:
                sub_func = func
                break

        # when the sub_func is not None, the function can be simulated.
        if sub_func is not None:
            outputlist_int: dict = dict()
            outputlist_double: dict = dict()
            outputlist_int, outputlist_double, mt = self.function_run(
                sub_func, inputlist, instr.outputs
            )
            for key in mt.keys():
                if key not in func_data.matrix_list:
                    func_data.matrix_list[key] = mt[key]

            # bind the output with the output value in outputlist_int and outputlist_double.
            for key in outputlist_int.keys():
                if outputlist_int[key][1] == -1:
                    func_data.func_int[key] = outputlist_int[key][0]
                else:
                    index = outputlist_int[key][1]
                    func_data.func_int[key][index] = outputlist_int[key][0][0]
            for key in outputlist_double.keys():
                if outputlist_double[key][1] == -1:
                    func_data.func_double[key] = outputlist_double[key][0]
                else:
                    index = outputlist_double[key][1]
                    func_data.func_double[key][index] = outputlist_double[key][0][0]
        else:
            self.info("No such function")

    def qu_defined_gate(self, instr: QiDefineGate, func_data: QiDataStack):
        """qu_defined_gate is to handle the defined gate instructions.

        Args:
            instr (QiDefineGate): the QiDefineGate instruction, the matrix is defined in the .gate section.
            func_data (QiDataStack): func_data is to store the datas of simulation.
        """
        # get the ctrl_qubit.
        ctrl_qubit = ctrl_word(instr, func_data)

        # get the matrix and qubits.
        s = ""
        if len(ctrl_qubit) != 0:
            s = s + "ctrl qubits " + str(ctrl_qubit)
        s = s + str(instr.matrix) + " on qubits " + str(instr.qubits[0])
        if len(instr.qubits) == 2:
            s = s + ", " + str(instr.qubits[1])
        func_data.matrix_list[func_data.func_name].append(s)

        # get the matrix of the defined gate.
        matrix = [j for i in instr.matrix for j in i]

        # len(instr.qubits) == 1 handles the single qubit gate operation.
        if len(instr.qubits) == 1:
            var = instr.qubits[0]
            if isinstance(var, QiVariable):
                index, name = QiVar_index_name(var, func_data)
                self.unitary(
                    func_data.func_qubit[name][index],
                    matrix,
                    ctrl_qubit,
                )

            # when the gate is single qubit gate, it can be applyed into a qubit QiList, and it is the same as applying the gate to all qubit in the QiList.
            elif isinstance(var, QiList):
                for q in func_data.func_qubit[var.name]:
                    self.unitary(
                        q,
                        matrix,
                        ctrl_qubit,
                    )
        elif len(instr.qubits) == 2:
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.qubits[0], instr.qubits[1], func_data
            )

            self.unitary(
                [
                    func_data.func_qubit[name1][index1],
                    func_data.func_qubit[name2][index2],
                ],
                matrix,
                ctrl_qubit,
            )

    def qu_std_instr(self, instr: QuietStdInstruction, func_data: QiDataStack):
        """handle the quiet std instructions.

        Args:
            instr (QuietStdInstruction): QuietStdInstruction, including common sigle qubit gate, two qubit gate and U4 gate.
            func_data (QiDataStack): func_data is to store the datas of simulation.
        """
        # get ctrl qubit if instr has.
        ctrl_qubit = ctrl_word(instr, func_data)

        # handle single gate
        if is_type_single_gate(instr, func_data):
            (
                instr_type,
                instr_dest,
                instr_index,
                instr_matrix,
                mat_matrix,
            ) = is_type_single_gate(instr, func_data)
            if instr_type == 1:
                self.unitary(
                    func_data.func_qubit[instr_dest][instr_index],
                    instr_matrix,
                    ctrl_qubit,
                )
            else:
                for q in func_data.func_qubit[instr_dest]:
                    self.unitary(q, instr_matrix, ctrl_qubit)
            qu = str(instr.qubit)

        # handle ctrl two qubit gate such as CNOT, CZ
        elif is_type_ctrl_two_gate(instr, func_data):
            (
                instr_dest,
                instr_dest_index,
                instr_ctrl,
                instr_ctrl_index,
                instr_matrix,
                mat_matrix,
            ) = is_type_ctrl_two_gate(instr, func_data)
            self.unitary(
                func_data.func_qubit[instr_dest][instr_dest_index],
                instr_matrix,
                [func_data.func_qubit[instr_ctrl][instr_ctrl_index]] + ctrl_qubit,
            )
            qu = str(instr.c_qubit) + ", " + str(instr.t_qubit)

        # handle ctrl two qubit gate with phase such as CP, CRz
        elif is_type_ctrl_phase_two_gate(instr, func_data):
            (
                instr_dest,
                instr_dest_index,
                instr_ctrl,
                instr_ctrl_index,
                instr_matrix,
                mat_matrix,
            ) = is_type_ctrl_phase_two_gate(instr, func_data)
            self.unitary(
                func_data.func_qubit[instr_dest][instr_dest_index],
                instr_matrix,
                [func_data.func_qubit[instr_ctrl][instr_ctrl_index]] + ctrl_qubit,
            )
            qu = str(instr.c_qubit) + ", " + str(instr.t_qubit)

        # handle two qubit gate such as SWAP
        elif is_type_two_gate(instr, func_data):
            (
                instr_dest,
                instr_dest_index,
                instr_ctrl,
                instr_ctrl_index,
                instr_matrix,
                mat_matrix,
            ) = is_type_two_gate(instr, func_data)
            self.unitary(
                [
                    func_data.func_qubit[instr_ctrl][instr_ctrl_index],
                    func_data.func_qubit[instr_dest][instr_dest_index],
                ],
                instr_matrix,
                ctrl_qubit,
            )
            qu = str(instr.c_qubit) + ", " + str(instr.t_qubit)

        # handle 1QRotation_gate such as "Rx", "Ry", "Rz", "Rxy", "U4"
        elif is_type_1QRotation_gate(instr, func_data):
            (
                instr_type,
                instr_dest,
                instr_index,
                instr_matrix,
                mat_matrix,
            ) = is_type_1QRotation_gate(instr, func_data)
            if instr_type == 1:
                self.unitary(
                    func_data.func_qubit[instr_dest][instr_index],
                    instr_matrix,
                    ctrl_qubit,
                )
            else:
                for q in func_data.func_qubit[instr_dest]:
                    self.unitary(q, instr_matrix, ctrl_qubit)
            qu = str(instr.qubit)

        # get the matrix list.
        s = ""
        if len(ctrl_qubit) != 0:
            s = s + "ctrl qubits " + str(ctrl_qubit)
        s = s + str(mat_matrix) + " on qubits " + qu
        func_data.matrix_list[func_data.func_name].append(s)

    def qu_fm_instr(self, instr: QuietFmInstruction, func_data: QiDataStack):
        """handle the quiet float instructions.

        Args:
            instr (QuietFmInstruction): QuietFmInstruction
            func_data (QiDataStack): func_data is to store the datas of simulation.
        """
        if instr.opname == "ldd":
            index, name = QiVar_index_name(instr.dst, func_data)
            func_data.func_double[name][index] = instr.imm
        elif instr.opname == "movd":
            if isinstance(instr.dst, QiList):
                func_data.func_double[instr.dst.name] = func_data.func_double[
                    instr.src.name
                ]
            else:
                index1, name1, index2, name2 = QiVar2_index_name(
                    instr.dst, instr.src, func_data
                )
                func_data.func_double[name1][index1] = func_data.func_double[name2][
                    index2
                ]
        elif instr.opname == "addd":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_double[name][index] = (
                func_data.func_double[name1][index1]
                + func_data.func_double[name2][index2]
            )
        elif instr.opname == "subd":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_double[name][index] = (
                func_data.func_double[name1][index1]
                - func_data.func_double[name2][index2]
            )
        elif instr.opname == "muld":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_double[name][index] = (
                func_data.func_double[name1][index1]
                * func_data.func_double[name2][index2]
            )
        elif instr.opname == "divd":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_double[name][index] = (
                func_data.func_double[name1][index1]
                / func_data.func_double[name2][index2]
            )
        elif instr.opname == "adddi":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.dst, instr.src1, func_data
            )
            func_data.func_double[name1][index1] = (
                func_data.func_double[name2][index2] + instr.src2
            )
        elif instr.opname == "subdi":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.dst, instr.src1, func_data
            )
            func_data.func_double[name1][index1] = (
                func_data.func_double[name2][index2] - instr.src2
            )
        elif instr.opname == "muldi":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.dst, instr.src1, func_data
            )
            func_data.func_double[name1][index1] = (
                func_data.func_double[name2][index2] * instr.src2
            )
        elif instr.opname == "divdi":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.dst, instr.src1, func_data
            )
            func_data.func_double[name1][index1] = (
                func_data.func_double[name2][index2] / instr.src2
            )

    def qu_im_instr(
        self,
        instr: QuietImInstruction,
        func_data: QiDataStack,
        func_lable: QiLabelTable,
    ):
        """handle the quiet int instructions.

        Args:
            instr (QuietImInstruction): QuietImInstruction
            func_data (QiDataStack): func_data is to store the datas of simulation.
            func_lable (QiLabelTable): the lable is for jump instructions.
        """
        if instr.opname == "jump":
            func_data.PC = func_lable.index(instr.destination_label) - 1
        elif instr.opname == "ld":
            index, name = QiVar_index_name(instr.dst, func_data)
            func_data.func_int[name][index] = instr.imm
        elif instr.opname == "mov":
            if isinstance(instr.dst, QiList):
                func_data.func_int[instr.dst.name] = func_data.func_int[instr.src.name]
            else:
                index1, name1, index2, name2 = QiVar2_index_name(
                    instr.dst, instr.src, func_data
                )
                func_data.func_int[name1][index1] = func_data.func_int[name2][index2]
        elif instr.opname == "lnot":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.dst, instr.src, func_data
            )
            func_data.func_int[name1][index1] = ~func_data.func_int[name2][index2]
        elif instr.opname == "land":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] & func_data.func_int[name2][index2]
            )
        elif instr.opname == "lor":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] | func_data.func_int[name2][index2]
            )
        elif instr.opname == "lxor":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] ^ func_data.func_int[name2][index2]
            )
        elif instr.opname == "add":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] + func_data.func_int[name2][index2]
            )
        elif instr.opname == "sub":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] - func_data.func_int[name2][index2]
            )
        elif instr.opname == "mul":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] * func_data.func_int[name2][index2]
            )
        elif instr.opname == "div":
            index, name = QiVar_index_name(instr.dst, func_data)
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] // func_data.func_int[name2][index2]
            )
        elif instr.opname == "addi":
            index, name, index1, name1 = QiVar2_index_name(
                instr.dst, instr.src1, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] + instr.src2
            )
        elif instr.opname == "subi":
            index, name, index1, name1 = QiVar2_index_name(
                instr.dst, instr.src1, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] - instr.src2
            )
        elif instr.opname == "muli":
            index, name, index1, name1 = QiVar2_index_name(
                instr.dst, instr.src1, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] * instr.src2
            )
        elif instr.opname == "divi":
            index, name, index1, name1 = QiVar2_index_name(
                instr.dst, instr.src1, func_data
            )
            func_data.func_int[name][index] = (
                func_data.func_int[name1][index1] // instr.src2
            )
        elif instr.opname == "bne":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            s1 = func_data.func_int[name1][index1]
            s2 = func_data.func_int[name2][index2]
            if s1 != s2:
                func_data.PC = func_lable.index(instr.dst_label) - 1
        elif instr.opname == "beq":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            s1 = func_data.func_int[name1][index1]
            s2 = func_data.func_int[name2][index2]
            if s1 == s2:
                func_data.PC = func_lable.index(instr.dst_label) - 1
        elif instr.opname == "bgt":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            s1 = func_data.func_int[name1][index1]
            s2 = func_data.func_int[name2][index2]
            if s1 > s2:
                func_data.PC = func_lable.index(instr.dst_label) - 1
        elif instr.opname == "bge":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            s1 = func_data.func_int[name1][index1]
            s2 = func_data.func_int[name2][index2]
            if s1 >= s2:
                func_data.PC = func_lable.index(instr.dst_label) - 1
        elif instr.opname == "blt":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            s1 = func_data.func_int[name1][index1]
            s2 = func_data.func_int[name2][index2]
            if s1 < s2:
                func_data.PC = func_lable.index(instr.dst_label) - 1
        elif instr.opname == "ble":
            index1, name1, index2, name2 = QiVar2_index_name(
                instr.src1, instr.src2, func_data
            )
            s1 = func_data.func_int[name1][index1]
            s2 = func_data.func_int[name2][index2]
            if s1 <= s2:
                func_data.PC = func_lable.index(instr.dst_label) - 1
