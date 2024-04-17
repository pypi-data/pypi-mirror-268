from qualesim.plugin import *
from qualesim.host import *
import unittest
from pathlib import Path
from tests.with_sim import MTestDQCSimQi
from tests.with_sim import MTestDQCSimInst

cur_dir = Path(__file__).parent
test_qi_file_dir = cur_dir / "testqifile"


def bit2int(bits: list):
    bits.reverse()
    s = "".join([str(bit) for bit in bits])
    return int(s, 2)


def test_bit2int():
    assert bit2int([1, 0, 0, 0]) == 1
    assert bit2int([0, 1, 0, 0]) == 2
    assert bit2int([0, 0, 1, 0]) == 4
    assert bit2int([0, 0, 0, 1]) == 8
    assert bit2int([0, 1, 0, 1]) == 10
    print("all bit2int tests have passed.")


class TestQiFile(unittest.TestCase):
    def test_test(self):
        with MTestDQCSimQi(test_qi_file_dir / "test.qi") as res:
            print(res)

    def test_adder(self):
        with MTestDQCSimQi(test_qi_file_dir / "adder.qi") as res:
            for i in res["res"]["quantum"][1]:
                a = bit2int(i[0:4])
                b = bit2int(i[4:8])
                ans = bit2int(i[8:])
                assert a + b == ans

    def test_bell(self):
        with MTestDQCSimQi(test_qi_file_dir / "bell.qi") as res:
            for i in res["res"]["quantum"][1]:
                assert i[0] == i[1]

    def test_mod(self):
        with MTestDQCSimQi(test_qi_file_dir / "mod.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] % func_int["b"][0] == func_int["c"][0]

    def test_pwm(self):
        with MTestDQCSimQi(test_qi_file_dir / "pwm.qi") as res:
            func_int = res["func_int"]
            assert (func_int["a"][0] ** func_int["n"][0]) % func_int["N"][
                0
            ] == func_int["res"][0]

    def test_get_str(self):
        with MTestDQCSimQi(test_qi_file_dir / "get_str.qi") as res:
            func_int = res["func_int"]
            s = 0
            for i in range(len(func_int["re"]) - 1, -1, -1):
                s = s * 2 + func_int["re"][i]
            assert s == func_int["a"][0]

    def test_find_r(self):
        with MTestDQCSimQi(test_qi_file_dir / "find_r.qi") as res:
            func_int = res["func_int"]
            base1 = func_int["base"][1]
            base0 = func_int["base"][0]
            n = func_int["n"][0]
            assert func_int["res"][0] == 2**n / (base1 - base0)

    def test_gcd(self):
        with MTestDQCSimQi(test_qi_file_dir / "gcd.qi") as res:
            func_int = res["func_int"]
            a = func_int["a"][0]
            b = func_int["b"][0]
            while b != 0:
                tmp = a
                a = b
                b = tmp % b
            assert a == func_int["res"][0]

    def test_prep_num_qubits(self):
        with MTestDQCSimQi(test_qi_file_dir / "prep_num_qubits.qi") as res:
            func_int = res["func_int"]
            func_qubit = res["func_qubit"]
            qubit_measure = res["qubit_measure"]
            assert qubit_measure[func_qubit["b"][0]][0] == func_int["b_idx"][0]
            assert qubit_measure[func_qubit["b"][1]][0] == func_int["b_idx"][1]
            assert qubit_measure[func_qubit["b"][2]][0] == func_int["b_idx"][2]
            assert qubit_measure[func_qubit["b"][3]][0] == func_int["b_idx"][3]

    # def test_add_qft(self):
    #    with MTestDQCSimInst(test_qi_file_dir / "add_qft.qi") as res:
    #        func_qubit = res["func_qubit"]
    #        qubit_measure = res["qubit_measure"]
    #        assert -0.2 < qubit_measure[func_qubit["locs"][0]][1] - 0.5 < 0.2
    #        assert -0.2 < qubit_measure[func_qubit["locs"][1]][1] - 0.5 < 0.2
    #        assert -0.2 < qubit_measure[func_qubit["locs"][2]][1] - 0.5 < 0.2
    #
    # def test_add_qfts(self):
    #    with MTestDQCSimInst(test_qi_file_dir / "add_qfts.qi") as res:
    #        func_qubit = res["func_qubit"]
    #        qubit_measure = res["qubit_measure"]
    #        assert -0.2 < qubit_measure[func_qubit["locs"][0]][1] - 0.5 < 0.2
    #        assert -0.2 < qubit_measure[func_qubit["locs"][1]][1] - 0.5 < 0.2
    #        assert -0.2 < qubit_measure[func_qubit["locs"][2]][1] - 0.5 < 0.2
    #
    # def test_add_qftd(self):
    #    with MTestDQCSimInst(test_qi_file_dir / "add_qftd.qi") as res:
    #        func_qubit = res["func_qubit"]
    #        qubit_measure = res["qubit_measure"]
    #        assert qubit_measure[func_qubit["locs"][0]][0] == 0
    #        assert qubit_measure[func_qubit["locs"][1]][0] == 0
    #        assert qubit_measure[func_qubit["locs"][2]][0] == 0
    #
    # def test_add_qftds(self):
    #    with MTestDQCSimInst(test_qi_file_dir / "add_qftds.qi") as res:
    #        func_qubit = res["func_qubit"]
    #        qubit_measure = res["qubit_measure"]
    #        assert qubit_measure[func_qubit["locs"][0]][0] == 0
    #        assert qubit_measure[func_qubit["locs"][1]][0] == 0
    #        assert -0.2 < qubit_measure[func_qubit["locs"][2]][1] - 0.5 < 0.2
    #
    # def test_add_Q_Add(self):
    #    with MTestDQCSimInst(test_qi_file_dir / "add_Q_Add.qi") as res:
    #        func_qubit = res["func_qubit"]
    #        qubit_measure = res["qubit_measure"]
    #        print(qubit_measure)
    #        # assert qubit_measure[func_qubit["locs"][0]][0] == 0
    #        # assert qubit_measure[func_qubit["locs"][1]][0] == 0
    #        # assert -0.2 < qubit_measure[func_qubit["locs"][2]][1] - 0.5 < 0.2
    #
    # def test_add_Q_Minus(self):
    #    with MTestDQCSimInst(test_qi_file_dir / "add_Q_Minus.qi") as res:
    #        func_qubit = res["func_qubit"]
    #        qubit_measure = res["qubit_measure"]
    #        print(qubit_measure)
    #        # assert qubit_measure[func_qubit["locs"][0]][0] == 0
    #        # assert qubit_measure[func_qubit["locs"][1]][0] == 0
    #        # assert -0.2 < qubit_measure[func_qubit["locs"][2]][1] - 0.5 < 0.2

    def test_changeable_list(self):
        with MTestDQCSimQi(test_qi_file_dir / "changeable_list.qi") as res:
            for i in res["res"]["quantum"][1]:
                assert i[0] == i[1]
            for i in res["res"]["classical"]:
                assert i["r"][1] == i["r"][2]
                assert i["res_i_0"][0] == i["res_i_0"][1]


if __name__ == "__main__":
    TestQiFile().test_changeable_list()
