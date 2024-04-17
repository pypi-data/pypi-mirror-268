from qualesim.plugin import *
from qualesim.common import *
import struct

import numpy as np


def bitwise_reverse_sort(lst, k):
    sorted_lst = []
    for i in range(len(lst)):
        sorted_lst.append(lst[int("0b" + bin(i)[2:].zfill(k)[::-1], 2)])
    return sorted_lst


@plugin("Tequila interface", "Liu Dingdong", "0.0.1")
class TequilaInterface(Backend):
    """Tequila Backend for DQCsim."""

    # ==========================================================================
    # Init the plugin
    # ==========================================================================
    def __init__(self):
        """init the Tequila Backend

        self.qubits: the index of qubits.
        """
        super().__init__()

        # self.circuit is to store the circuit, we apply the quantum gate to it.
        self.circuit = None

        self.states = None
        self.gate = None

        # self.qubits is the index of qubits.
        self.qubits = {}
        self.typ = "CQInstr"

        self.cls_dict = dict()

        # self.qubits_ismeasured = {}
        # self.qubits_ismeasured_value = {}

    def handle_init(self, cmds):
        """handle_init the backend plugin with the given cmds.
        Here we initial the circuit to qubit(1,0) since the proj_norm func has
        bugs with projecting it into an empty circuit.

        Args:
            cmds (ArbCmd): send ArbCmd to the backend plugin.

        Raises:
            ValueError: Unknown ArbCmd
        """
        # Interpret commands.

        # < ======================================================================
        # < ======================================================================
        # no live time in the tequila backend! so the codes below is of no sense.
        self.t1 = None
        self.t2 = None
        for cmd in cmds:
            if cmd.iface == "tequila":
                if cmd.oper == "error":
                    continue
                else:
                    raise ValueError("Unknown ArbCmd %s.%s" % (cmd.iface, cmd.oper))
        # < ======================================================================
        # no live time in the tequila backend! so the codes above is of no sense.
        # < ======================================================================

        # Loading Tequila can take some time, so defer to initialize
        # callback. We also have logging at that point in time, so it should
        # provide a nice UX.
        # TODO maybe i should move the import module here later.
        self.debug("Trying to load Tequila...")
        import tequila.states as states

        self.states = states
        import tequila.gates as gates

        self.gate = gates

        # use qubit to store the circuit, we can use cat_qubits to add new qubits
        self.circuit = self.states.qubit(1)
        self.info("Tequila loaded...")

    # ==========================================================================
    # Handle run the plugin
    # ==========================================================================
    def handle_allocate(self, qubit_refs, cmds):
        """handle_allocate is the handle function of frontend's self.allocate(size),
        You can use it to allocate new qubits here.

        Args:
            qubit_refs (list): a list of qubits' index, start from 1.
            cmds (ArbCmd): send ArbCmd to the backend plugin.
        """
        # we allocate the qubits below using qubit(1, 0) to init the qubit as state |0>.
        for qubit_ref in qubit_refs:
            qu = self.states.qubit(1, 0)
            self.circuit.add_qubits_on_back([qu])

            # the index of qubit_ref is store in self.qubits.
            self.qubits[qubit_ref] = self.circuit.n - 1

            # self.qubits_ismeasured is unused.
            # self.qubits_ismeasured[qubit_ref] = 0

    def handle_free(self, qubit_refs):
        """use trace to proj the qubits into base to free it.
        now we should proj the qubit_ref in the end of program.
        using arb in the handle_measure to proj may be better.

        Args:
            qubit_refs (list): a list of qubit to be free.
        """
        basis = [1, 0, 0, 1]
        self.cls_dict = dict()
        self.handle_measurement_gate(
            qubit_refs, basis, arb=ArbData(measure_mod="free", typ=self.typ)
        )

    def handle_measurement_gate(self, qubit_refs, basis, arb):
        if "typ" in arb:
            typ = arb["typ"]
            self.typ = typ
            if typ == "PQInstr":
                msmt = self.handle_measurement_gate_qcis(qubit_refs, basis, arb)
                return msmt
            elif typ == "CQInstr":
                msmt = self.handle_measurement_gate_quiets(qubit_refs, basis, arb)
                return msmt
        else:
            msmt = self.handle_measurement_gate_quiets(qubit_refs, basis, arb)
            return msmt

    def handle_measurement_gate_qcis(self, qubit_refs, basis, arb):
        state_res = ""
        if "measure_mod" in arb:
            measure_mod = arb["measure_mod"]
        else:
            measure_mod = "one_shot"
        if "num_shots" in arb:
            num_shots = arb["num_shots"]
        else:
            num_shots = 1

        # store the measurements: List[Measurement]
        measurements = []

        # cls_list is to store the measure value for output and project.
        cls_list = []

        # measure_targets is the qubit index of qubit_refs.
        measure_targets = []
        for i in qubit_refs:
            measure_targets.append(self.qubits[i])

        # get the statevector before measure.
        # TODO the state_res should be rerange, deprecate parentheses.
        # if measure_mod == "measureforres":
        circuit = self.states.qubit(self.circuit.n, self.circuit.data)
        loc = [0]
        bse = [0]
        for i in self.cls_dict.keys():
            loc.append(self.qubits[i])
            bse.append(self.cls_dict[i])
        circuit.proj_norm(loc, bse)
        state_res_before = bitwise_reverse_sort(
            [i[0] for i in circuit.vec().tolist()], circuit.n
        )
        state_res = str([self.cls_dict, state_res_before])
        # if measure_mod
        msmts = []
        if (
            measure_mod == "one_shot"
            or measure_mod == "state_vector"
            or measure_mod == "free"
        ):
            for i in range(num_shots):
                """meas_rej returns result in a dict format: {'11000': 2, '00100': 3}"""
                bit_str_res = list(self.circuit.meas_rej(measure_targets, 1).keys())[0]
                res = [int(bit_str_res[i], 2) for i in range(len(measure_targets))]
                msmts.append(res)
            # use meas_rej to measure the one_shot and state_vector measure_mod
            measure_res = self.circuit.meas_rej(measure_targets, 1)
            for key in measure_res.keys():
                for j in range(len(key)):
                    cls_list.append(int(key[j]))
                    self.cls_dict[qubit_refs[j]] = int(key[j])
        else:
            # use others to handle other type of measure.
            repn = 1000
            if len(measure_targets) <= 3:
                measure_res = self.circuit.meas_minor(measure_targets, repn)
            else:
                measure_res = self.circuit.meas_mcmc(measure_targets, repn)

            # choose the max value as the cls_list to project.
            max_re = max(measure_res.values())
            for key in measure_res.keys():
                if measure_res[key] == max_re:
                    for j in key:
                        cls_list.append(int(j))
        if measure_mod == "state_vector":
           circuit = self.states.qubit(self.circuit.n, self.circuit.data)
           loc = [0]
           bse = [0]
           for i in self.cls_dict.keys():
               loc.append(self.qubits[i])
               bse.append(self.cls_dict[i])
           circuit.proj_norm(loc, bse)
           state_res_after = [i[0] for i in circuit.vec().tolist()]
           state_res = str([self.cls_dict, state_res_after])

        # handle free, use proj_norm to proj the circuit, and rerange the index of qubits.
        if measure_mod == "free":
            self.circuit.proj_norm(measure_targets, cls_list)
            for j in qubit_refs:
                for i in self.qubits.keys():
                    if i > j and self.qubits[i] != -1:
                        self.qubits[i] = self.qubits[i] - 1
                self.qubits[j] = -1
        # use proj_site to proj it into cls_list and retain the original index.
        else:
            for i in range(len(cls_list)):
                self.circuit.proj_site(measure_targets[i], cls_list[i])

        # form the Measurement and send it to upsteam plugins.
        for it in range(len(qubit_refs)):
            measurements.append(
                Measurement(
                    qubit_refs[it],
                    cls_list[it],
                    struct.pack("<d", 1),
                    probability=1,
                    state_vector=state_res,
                    state_vector_be=str([self.cls_dict, []]),
                    one_shot=msmts,
                )
            )
        return measurements

    def handle_measurement_gate_quiets(self, qubit_refs, basis, arb):
        """handle_measurement_gate is to handle the measure gate and free opration.

        Args:
            qubit_refs (list): a list of qubits, use self.qubits[qubit_ref] to get
                               the real index of qubit.
            basis (list): the basis matrix of measure.
            arb (ArbData): an ArbData is to get the measure_mod and others.

        Returns:
            measurements (List(Measurement)): the return value is a list of Measurement,
                                              and you can get the value, probability,
                                              qubit_measure_before and statevector here.
        """
        # < ======================================================================
        # methos is unused in the Tequila Backend. the codes below is of no sense.
        # < ======================================================================
        state_res = ""
        if "method" in arb:
            methods = arb["method"]
        else:
            methods = "random"
        if isinstance(methods, list):
            if len(methods) != len(qubit_refs):
                raise ValueError("method key does not have the right list size")
        elif isinstance(methods, str):
            methods = [methods] * len(qubit_refs)
        elif isinstance(methods, int):
            methods = [(methods >> i) & 1 for i in reversed(range(len(qubit_refs)))]
        else:
            raise ValueError("failed to parse method key")
        # < ======================================================================
        # methos is unused in the Tequila Backend. the codes above is of no sense.
        # < ======================================================================

        """ We have not define different measure basis here so the basis_hermetian
        is unused here.

        basis_hermetian = [
            basis[0].real - basis[0].imag * 1j,
            basis[2].real - basis[2].imag * 1j,
            basis[1].real - basis[1].imag * 1j,
            basis[3].real - basis[3].imag * 1j,
        ]
        """

        # get the measure_mod from input ArbData.
        if "measure_mod" in arb:
            measure_mod = arb["measure_mod"]
        else:
            measure_mod = "final_state"
        if "get_probability" in arb:
            get_prob = arb["get_probability"]
        else:
            get_prob = False

        # store the measurements: List[Measurement]
        measurements = []

        # cls_list is to store the measure value for output and project.
        cls_list = []

        # measure_targets is the qubit index of qubit_refs.
        measure_targets = []
        for i in qubit_refs:
            measure_targets.append(self.qubits[i])

        # get the statevector before measure.
        if measure_mod == "measureforres":
            circuit = self.states.qubit(self.circuit.n, self.circuit.data)
            loc = [0]
            bse = [0]
            for i in self.cls_dict.keys():
                loc.append(self.qubits[i])
                bse.append(self.cls_dict[i])
            circuit.proj_norm(loc, bse)
            state_res_before = bitwise_reverse_sort(
                [i[0] for i in circuit.vec().tolist()], circuit.n
            )
            state_res = str([self.cls_dict, state_res_before])

        # if measure_mod
        if (
            measure_mod == "one_shot"
            or measure_mod == "state_vector"
            or measure_mod == "free"
        ):
            # use meas_rej to measure the one_shot and state_vector measure_mod
            repn = 1
            measure_res = self.circuit.meas_rej(measure_targets, repn)
            for key in measure_res.keys():
                for j in range(len(key)):
                    cls_list.append(int(key[j]))
                    self.cls_dict[qubit_refs[j]] = int(key[j])
        else:
            # use others to handle other type of measure.
            repn = 1000
            if len(measure_targets) <= 3:
                measure_res = self.circuit.meas_minor(measure_targets, repn)
            else:
                measure_res = self.circuit.meas_mcmc(measure_targets, repn)

            # choose the max value as the cls_list to project.
            max_re = max(measure_res.values())
            for key in measure_res.keys():
                if measure_res[key] == max_re:
                    for j in key:
                        cls_list.append(int(j))

        if measure_mod == "state_vector":
            circuit = self.states.qubit(self.circuit.n, self.circuit.data)
            loc = [0]
            bse = [0]
            for i in self.cls_dict.keys():
                loc.append(self.qubits[i])
                bse.append(self.cls_dict[i])
            circuit.proj_norm(loc, bse)
            state_res_after = bitwise_reverse_sort(
                [i[0] for i in circuit.vec().tolist()], circuit.n
            )
            state_res = str([self.cls_dict, state_res_after])
        # handle free, use proj_norm to proj the circuit, and rerange the index of qubits.
        if measure_mod == "free":
            self.circuit.proj_norm(measure_targets, cls_list)
            for j in qubit_refs:
                for i in self.qubits.keys():
                    if i > j and self.qubits[i] != -1:
                        self.qubits[i] = self.qubits[i] - 1
                self.qubits[j] = -1

        # use proj_site to proj it into cls_list and retain the original index.
        else:
            for i in range(len(cls_list)):
                self.circuit.proj_site(measure_targets[i], cls_list[i])

        # form the Measurement and send it to upsteam plugins.
        for it in range(len(qubit_refs)):
            measurements.append(
                Measurement(
                    qubit_refs[it],
                    cls_list[it],
                    struct.pack("<d", 1),
                    probability=1,
                    state_vector=state_res,
                )
            )
        return measurements

    def handle_prepare_gate(self, qubit_refs, basis, _arb):
        """the prepare gate is about the initial of gates. now default is qubit(1,0) to
        construct a qubit .

        Args:
            qubit_refs (list): handle prepare gate, maybe the _arb can be used to prepare
                               other type of init state, now default is |0>.
            basis (list): basis default is matrix I.
            _arb (ArbData): maybe it can do other inputs latter.
        """
        for qubit_ref in qubit_refs:
            self.handle_unitary_gate([qubit_ref], basis, None)

    def handle_unitary_gate(self, qubit_refs, unitary_matrix, _arb):
        """handle unitary gate using the unitary_matrix.

        Args:
            qubit_refs (list): a list of qubits, use self.qubits[qubit_ref] to get
                               the real index of qubit.
            unitary_matrix (list): the matrix of gate applied into the qubit.
            _arb (ArbData): ArbData as inputs.
        """
        # create a gate from the input qubit_refs and unitary_matrix
        unitary_gate = self.gate.gate(len(qubit_refs))
        unitary_gate.mat2mpo(unitary_matrix)

        # print what we're doing in the debug method.
        unitary_matrix = np.reshape(
            np.array(unitary_matrix), (2 ** len(qubit_refs),) * 2
        )
        self.debug(
            "tequila gate on %s:\n%s"
            % (", ".join(map("q{}".format, qubit_refs)), unitary_matrix)
        )

        # get the locs from the input qubit_refs.
        locs = [self.qubits[i] for i in qubit_refs]

        # applying gate into qubits.
        self.circuit.apply(locs, unitary_gate)

    def handle_advance(self, cycles):
        """it is useless in tequila backend since there is no time limit."""
        pass
