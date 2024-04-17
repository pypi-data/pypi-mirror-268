from qualesim.plugin import *
from qualesim.host import *
import unittest
from pathlib import Path
from tests.with_sim import MTestDQCSimInst

cur_dir = Path(__file__).parent
test_qi_file_dir = cur_dir / "testgate"


class TestGates(unittest.TestCase):
    def test_H_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "h.qi") as res:
            func_qubit = res["func_qubit"]
            qubit_measure = res["qubit_measure"]
            assert -0.2 < (qubit_measure[func_qubit["q"][0]][1] - 0.5) < 0.2

    def test_X_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "x.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 1
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1.0) < 1e-5

    def test_Y_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "y.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 0
            # the res state should be [(1/sqrt(2))(-sin(angle[0]/2)-cos(angle[0]/2))j,
            #                          (1/sqrt(2))(-sin(angle[0]/2)+cos(angle[0]/2))j]
            assert -0.1 < (qubit_measure[func_qubit["q"][0]][1] - 0.933) < 0.1

    def test_Z_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "z.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 0
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1.0) < 1e-5

    def test_T_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "t.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 0
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1.0) < 1e-5

    def test_S_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "s.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 0
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1.0) < 1e-5

    def test_Sdag_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "sdag.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 0
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1.0) < 1e-5

    def test_Tdag_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "tdag.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 0
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1.0) < 1e-5

    def test_CNOT_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "cnot.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c2"][0] == 1
            assert -1e-5 < (qubit_measure[func_qubit["q2"][0]][1] - 1.0) < 1e-5

    def test_CZ_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "cz.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c2"][0] == 0
            assert -1e-5 < (qubit_measure[func_qubit["q2"][0]][1] - 1.0) < 1e-5

    def test_CP_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "cp.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c2"][0] == 0
            assert -1e-5 < (qubit_measure[func_qubit["q2"][0]][1] - 1.0) < 1e-5

    def test_CRz_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "crz.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c2"][0] == 1
            assert -1e-5 < (qubit_measure[func_qubit["q2"][0]][1] - 1) < 1e-5

    def test_SWAP_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "swap.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c1"][0] == 0
            assert func_int["c2"][0] == 1
            assert -1e-5 < (qubit_measure[func_qubit["q1"][0]][1] - 1.0) < 1e-5
            assert -1e-5 < (qubit_measure[func_qubit["q2"][0]][1] - 1.0) < 1e-5

    def test_Rx_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "rx.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 1
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1) < 1e-5

    def test_Ry_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "ry.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 1
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1) < 1e-5

    def test_Rz_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "rz.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 1
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1) < 1e-5

    def test_Rxy_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "rxy.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert -0.2 < (qubit_measure[func_qubit["q"][0]][1] - 0.5) < 0.2

    ## The matrix is not unitary!
    def test_U4_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "u4.qi") as res:
            func_qubit = res["func_qubit"]
            qubit_measure = res["qubit_measure"]
            assert -0.2 < (qubit_measure[func_qubit["q"][0]][1] - 0.5) < 0.2

    def test_CTRL(self):
        with MTestDQCSimInst(test_qi_file_dir / "ctrlH.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c"][0] == 0
            assert -0.2 < (qubit_measure[func_qubit["q2"][0]][1] - 0.75) < 0.2

    def test_defined_gate(self):
        with MTestDQCSimInst(test_qi_file_dir / "definegate.qi") as res:
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
            assert func_int["c1"][0] == 1
            assert func_int["c2"][0] == 1
            assert -1e-5 < (qubit_measure[func_qubit["q"][0]][1] - 1) < 1e-5
            assert -1e-5 < (qubit_measure[func_qubit["q2"][0]][1] - 1) < 1e-5


if __name__ == "__main__":
    TestGates().test_U4_gate()
