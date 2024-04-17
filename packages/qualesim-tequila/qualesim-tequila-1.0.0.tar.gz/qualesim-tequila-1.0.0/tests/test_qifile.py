from qualesim.plugin import *
from qualesim.host import *
import unittest


class Constructor(unittest.TestCase):
    def test_adder(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testqifile/adder.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            func_int = sim.recv()["func_int"]
            a = 0
            for i in func_int["a_int"]:
                a = a >> 1 + i
            b = 0
            for i in func_int["b_int"]:
                b = b >> 1 + i
            ans = 0
            for i in func_int["ans_int"]:
                ans = ans >> 1 + i
            assert a + b == ans

    def test_bell(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testqifile/bell.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            func_int = sim.recv()["func_int"]
            assert func_int["c1"][0] == func_int["c2"][0]

    def test_mod(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testqifile/mod.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            func_int = sim.recv()["func_int"]
            assert func_int["a"][0] % func_int["b"][0] == func_int["c"][0]

    def test_pwm(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testqifile/pwm.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            func_int = sim.recv()["func_int"]
            assert (func_int["a"][0] ** func_int["n"][0]) % func_int["N"][
                0
            ] == func_int["res"][0]


if __name__ == "__main__":
    suite = unittest.TestSuite()  # 实例化TestSuite
    suite.addTest(Constructor("test_test"))  # 添加测试用例
    runner = unittest.TextTestRunner()  # 实例化TextTestRunner
    runner.run(suite)  # 传入suite并执行测试用例
