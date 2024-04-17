from qualesim.plugin import *
from qualesim.host import *
import unittest


class Constructor(unittest.TestCase):
    def test_H_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/h.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            qubit_measure = res["qubit_measure"]
            assert -0.2 < (qubit_measure[func_qubit["q"][0]][1] - 0.5) < 0.2

    def test_X_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/x.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/x.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_Y_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/y.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/y.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_Z_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/z.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/z.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_T_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/t.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/t.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_S_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/s.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/s.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_Sdag_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/sdag.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/sdag.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_Tdag_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/tdag.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/tdag.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_CNOT_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/cnot.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/cnot.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q2"][0]][1]
                - qubit_masureq[func_qubitq["q2"][0]][1]
                < 1e-5
            )
            assert func_int["c2"][0] == func_intq["c2"][0]

    def test_CZ_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/cz.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/cz.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q2"][0]][1]
                - qubit_masureq[func_qubitq["q2"][0]][1]
                < 1e-5
            )
            assert func_int["c2"][0] == func_intq["c2"][0]

    def test_CP_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/cp.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/cp.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q2"][0]][1]
                - qubit_masureq[func_qubitq["q2"][0]][1]
                < 1e-5
            )
            assert func_int["c2"][0] == func_intq["c2"][0]

    def test_CRz_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/crz.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/crz.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q2"][0]][1]
                - qubit_masureq[func_qubitq["q2"][0]][1]
                < 1e-5
            )
            assert func_int["c2"][0] == func_intq["c2"][0]

    def test_SWAP_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/swap.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/swap.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert (
                qubit_measure[func_qubit["q1"][0]][1]
                == qubit_masureq[func_qubitq["q1"][0]][1]
            )
            assert (
                -1e-5
                < qubit_measure[func_qubit["q2"][0]][1]
                - qubit_masureq[func_qubitq["q2"][0]][1]
                < 1e-5
            )
            assert func_int["c1"][0] == func_intq["c1"][0]
            assert func_int["c2"][0] == func_intq["c2"][0]

    def test_Rx_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/rx.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/rx.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_Ry_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/ry.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/ry.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_Rz_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/rz.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/rz.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            func_intq = resq["func_int"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c"][0] == func_intq["c"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )

    def test_Rxy_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/rxy.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/rxy.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            qubit_masureq = resq["qubit_measure"]
            assert (
                -0.2
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 0.2
            )

    ## The matrix is not unitary!
    def test_U4_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/u4.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/u4.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_qubitq = resq["func_qubit"]
            qubit_masureq = resq["qubit_measure"]
            assert (
                -0.2
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 0.2
            )

    def test_CTRL(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/ctrlH.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/ctrlH.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_intq = resq["func_int"]
            func_qubitq = resq["func_qubit"]
            qubit_masureq = resq["qubit_measure"]
            if func_int["c"][0] == func_intq["c"][0]:
                assert (
                    -0.2
                    < qubit_measure[func_qubit["q2"][0]][1]
                    - qubit_masureq[func_qubitq["q2"][0]][1]
                    < 0.2
                )
            else:
                assert (
                    -0.2
                    < abs(
                        qubit_measure[func_qubit["q2"][0]][1]
                        - qubit_masureq[func_qubitq["q2"][0]][1]
                    )
                    - 0.5
                    < 0.2
                )

    def test_defined_gate(self):
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/definegate.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("tequila", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as sim:
            sim.run()
            res = sim.recv()
            func_qubit = res["func_qubit"]
            func_int = res["func_int"]
            qubit_measure = res["qubit_measure"]
        with Simulator(
            (
                "/home/liudingdong/gitee/dqcsim-tequila/tests/testgate/definegate.qi",
                {"verbosity": Loglevel.INFO},
            ),
            ("quantumsim", {"verbosity": Loglevel.INFO}),
            stderr_verbosity=Loglevel.INFO,
        ) as simq:
            simq.run()
            resq = simq.recv()
            func_intq = resq["func_int"]
            func_qubitq = resq["func_qubit"]
            qubit_masureq = resq["qubit_measure"]
            assert func_int["c1"][0] == func_intq["c1"][0]
            assert func_int["c2"][0] == func_intq["c2"][0]
            assert (
                -1e-5
                < qubit_measure[func_qubit["q"][0]][1]
                - qubit_masureq[func_qubitq["q"][0]][1]
                < 1e-5
            )
            assert (
                -1e-5
                < qubit_measure[func_qubit["q2"][0]][1]
                - qubit_masureq[func_qubitq["q2"][0]][1]
                < 1e-5
            )


if __name__ == "__main__":
    suite = unittest.TestSuite()  # 实例化TestSuite
    suite.addTest(Constructor("test_defined_gate"))  # 添加测试用例
    runner = unittest.TextTestRunner()  # 实例化TextTestRunner
    runner.run(suite)  # 传入suite并执行测试用例
