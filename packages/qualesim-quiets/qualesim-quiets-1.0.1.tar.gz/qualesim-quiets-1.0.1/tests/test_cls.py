from qualesim.plugin import *
from qualesim.host import *
import unittest
from pathlib import Path
from tests.with_sim import MTestDQCSimInst

cur_dir = Path(__file__).parent
test_qi_file_dir = cur_dir / "testclsfile"


class TestClsFile(unittest.TestCase):
    def test_Ld(self):
        with MTestDQCSimInst(test_qi_file_dir / "ld.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 3
            assert func_int["c"][0] == 5

    def test_Mov(self):
        with MTestDQCSimInst(test_qi_file_dir / "mov.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 10
            assert func_int["c"][0] == 10

    def test_Lnot(self):
        with MTestDQCSimInst(test_qi_file_dir / "lnot.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == -11
            assert func_int["a"][0] == ~func_int["b"][0]
            assert ~func_int["a"][0] == func_int["b"][0]

    def test_Land(self):
        with MTestDQCSimInst(test_qi_file_dir / "land.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 6
            assert func_int["c"][0] == 2
            assert func_int["a"][0] & func_int["b"][0] == func_int["c"][0]

    def test_Lor(self):
        with MTestDQCSimInst(test_qi_file_dir / "lor.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 6
            assert func_int["c"][0] == 14
            assert func_int["a"][0] | func_int["b"][0] == func_int["c"][0]

    def test_Lxor(self):
        with MTestDQCSimInst(test_qi_file_dir / "lxor.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 6
            assert func_int["c"][0] == 12
            assert func_int["a"][0] ^ func_int["b"][0] == func_int["c"][0]

    def test_Add(self):
        with MTestDQCSimInst(test_qi_file_dir / "add.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 6
            assert func_int["c"][0] == 16
            assert func_int["a"][0] + func_int["b"][0] == func_int["c"][0]

    def test_Sub(self):
        with MTestDQCSimInst(test_qi_file_dir / "sub.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 6
            assert func_int["c"][0] == 4
            assert func_int["a"][0] - func_int["b"][0] == func_int["c"][0]

    def test_Mul(self):
        with MTestDQCSimInst(test_qi_file_dir / "mul.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 4
            assert func_int["b"][0] == 6
            assert func_int["c"][0] == 24
            assert func_int["a"][0] * func_int["b"][0] == func_int["c"][0]

    def test_Div(self):
        with MTestDQCSimInst(test_qi_file_dir / "div.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 24
            assert func_int["b"][0] == 6
            assert func_int["c"][0] == 4
            assert func_int["d"][0] == 1
            assert func_int["a"][0] // func_int["b"][0] == func_int["c"][0]
            assert func_int["b"][0] // func_int["c"][0] == func_int["d"][0]

    def test_Addi(self):
        with MTestDQCSimInst(test_qi_file_dir / "addi.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["c"][0] == 13
            assert func_int["a"][0] + 3 == func_int["c"][0]

    def test_Subi(self):
        with MTestDQCSimInst(test_qi_file_dir / "subi.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["c"][0] == 4
            assert func_int["a"][0] - 6 == func_int["c"][0]

    def test_Muli(self):
        with MTestDQCSimInst(test_qi_file_dir / "muli.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 4
            assert func_int["c"][0] == 24
            assert func_int["a"][0] * 6 == func_int["c"][0]

    def test_Divi(self):
        with MTestDQCSimInst(test_qi_file_dir / "divi.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 24
            assert func_int["c"][0] == 4
            assert func_int["a"][0] // 6 == func_int["c"][0]

    def test_Jump(self):
        with MTestDQCSimInst(test_qi_file_dir / "jump.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 6
            assert func_int["c"][0] == 16

    def test_Bne(self):
        with MTestDQCSimInst(test_qi_file_dir / "bne.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 60
            assert func_int["c"][0] == 16
            assert func_int["d"][0] == 10

    def test_Beq(self):
        with MTestDQCSimInst(test_qi_file_dir / "beq.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 6
            assert func_int["c"][0] == 16
            assert func_int["d"][0] == 10

    def test_Bgt(self):
        with MTestDQCSimInst(test_qi_file_dir / "bgt.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 10

    def test_Bge(self):
        with MTestDQCSimInst(test_qi_file_dir / "bge.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 11

    def test_Blt(self):
        with MTestDQCSimInst(test_qi_file_dir / "blt.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 10

    def test_Ble(self):
        with MTestDQCSimInst(test_qi_file_dir / "ble.qi") as res:
            func_int = res["func_int"]
            assert func_int["a"][0] == 10
            assert func_int["b"][0] == 11

    def test_Ldd(self):
        with MTestDQCSimInst(test_qi_file_dir / "ldd.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 1.5
            assert func_double["b"][0] == 2.0
            assert func_double["c"][0] == 3.14

    def test_Movd(self):
        with MTestDQCSimInst(test_qi_file_dir / "movd.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 1.5
            assert func_double["b"][0] == 1.5
            assert func_double["c"][0] == 1.5

    def test_Addd(self):
        with MTestDQCSimInst(test_qi_file_dir / "addd.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 1.5
            assert func_double["b"][0] == 3.5
            assert func_double["c"][0] == 5
            assert func_double["a"][0] + func_double["b"][0] == func_double["c"][0]

    def test_Subd(self):
        with MTestDQCSimInst(test_qi_file_dir / "subd.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 3.14
            assert func_double["b"][0] == 2.04
            assert func_double["c"][0] == 1.1
            assert func_double["a"][0] - func_double["b"][0] == func_double["c"][0]

    def test_Muld(self):
        with MTestDQCSimInst(test_qi_file_dir / "muld.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 2.5
            assert func_double["b"][0] == 2
            assert func_double["c"][0] == 5
            assert func_double["a"][0] * func_double["b"][0] == func_double["c"][0]

    def test_Divd(self):
        with MTestDQCSimInst(test_qi_file_dir / "divd.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 10
            assert func_double["b"][0] == 4
            assert func_double["c"][0] == 2.5
            assert func_double["a"][0] / func_double["b"][0] == func_double["c"][0]

    def test_Adddi(self):
        with MTestDQCSimInst(test_qi_file_dir / "adddi.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 3.4
            assert func_double["c"][0] == 4
            assert func_double["a"][0] + 0.6 == func_double["c"][0]

    def test_Subdi(self):
        with MTestDQCSimInst(test_qi_file_dir / "subdi.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 3.4
            assert func_double["c"][0] == 2.8
            assert func_double["a"][0] - 0.6 == func_double["c"][0]

    def test_Muldi(self):
        with MTestDQCSimInst(test_qi_file_dir / "muldi.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 2.4
            assert func_double["c"][0] == 8.4
            assert func_double["a"][0] * 3.5 == func_double["c"][0]

    def test_Divdi(self):
        with MTestDQCSimInst(test_qi_file_dir / "divdi.qi") as res:
            func_double = res["func_double"]
            assert func_double["a"][0] == 2.4
            assert func_double["c"][0] == 4
            assert func_double["a"][0] / 0.6 == func_double["c"][0]


if __name__ == "__main__":
    TestClsFile().test_Beq()
