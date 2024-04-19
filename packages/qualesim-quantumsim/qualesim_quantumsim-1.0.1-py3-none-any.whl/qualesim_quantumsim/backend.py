from qualesim.plugin import *
from qualesim.common import *
from qualesim_quantumsim.qubit import Qubit
import struct
import numpy as np
from quantumsim.dm_np import DensityNP
# import copy


@plugin("QuantumSim interface for QuaLeSim", "Dingdong Liu", "0.0.1")
class QuantumSimInterface(Backend):
    # QuantumSim's SparseDM object doesn't support adding or removing qubits.
    # However, any qubits that haven't been entangled yet are purely classical.
    # Therefore, we can just allocate a large number of qubits at startup and
    # use those when we need them. This is that large number.
    MAX_QUBITS = 1000

    def __init__(self):
        super().__init__()

        # quantumsim.ptm module reference.
        self.ptm = None

        # quantumsim.sparsedm.SparseDM object representing the system.
        self.sdm = None

        # numpy module reference.
        self.np = None

        # store the classical value
        self.cls_dict = dict()

        # Indices of qubits that are free/live within self.sdm.
        self.free_qs_qubits = set(range(self.MAX_QUBITS))
        self.live_qs_qubits = set()

        # Qubit data for each upstream qubit.
        self.qubits = {}

    """def copy(self):
        return copy.deepcopy(self)"""

    def handle_init(self, cmds):
        # Interpret commands.
        self.t1 = None
        self.t2 = None
        for cmd in cmds:
            if cmd.iface == "quantumsim":
                if cmd.oper == "error":
                    if "t1" in cmd:
                        self.t1 = cmd["t1"]
                    if "t2" in cmd:
                        self.t2 = cmd["t2"]
                else:
                    raise ValueError("Unknown ArbCmd %s.%s" % (cmd.iface, cmd.oper))

        # Loading QuantumSim can take some time, so defer to initialize
        # callback. We also have logging at that point in time, so it should
        # provide a nice UX.
        self.debug("Trying to load QuantumSim...")
        import quantumsim.ptm as ptm

        self.ptm = ptm
        import quantumsim.sparsedm as sdm

        self.sdm = sdm.SparseDM(self.MAX_QUBITS)
        import numpy as np

        self.np = np
        self.info(
            "QuantumSim loaded {}using CUDA acceleration",
            "" if sdm.using_gpu else "*without* ",
        )

    def handle_allocate(self, qubit_refs, cmds):
        # Allow t1 and t2 to be overwritten on a per-qubit basis.
        t1 = self.t1
        t2 = self.t2
        for cmd in cmds:
            if cmd.iface == "quantumsim":
                if cmd.oper == "error":
                    if "t1" in cmd:
                        t1 = cmd["t1"]
                    if "t2" in cmd:
                        t2 = cmd["t2"]
                else:
                    raise ValueError("Unknown ArbCmd %s.%s" % (cmd.iface, cmd.oper))

        for qubit_ref in qubit_refs:
            self.qubits[qubit_ref] = Qubit(self, qubit_ref, t1=t1, t2=t2)

    def handle_free(self, qubit_refs):
        for qubit_ref in qubit_refs:
            qubit = self.qubits.pop(qubit_ref)

            # Measure the qubit to make sure it's freed in the SDM.
            qubit.measure()
        self.cls_dict = dict()

    def handle_measurement_gate(self, qubit_refs, basis, arb):
        """_summary_

        Args:
            qubit_refs (_type_): _description_
            basis (_type_): _description_
            arb (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            List [Measurement(
                    qubit_refs[it],
                    cls_list[it],
                    struct.pack("<d", 1),
                    probability=1,
                    state_vector=state_res,
                    one_shot=msmts,
                )]
        """
        # for mixed instr, QuaLeSim only need to handle the measure_mod,
        # the one_shot module's num_shot is to handle in the frontend.
        # the different measure mod is to define the different Measurement.
        # QuantumSim is default one_shot. and it is same as quiets's one-shot
        if "measure_mod" in arb:
            measure_mod = arb["measure_mod"]
        else:
            measure_mod = "one_shot"

        if "num_shots" in arb:
            num_shots = arb["num_shots"]
        else:
            num_shots = 1

        # Determine the hermitian of the basis for rotating back after
        # measuring.
        basis_hermetian = [
            basis[0].real - basis[0].imag * 1j,
            basis[2].real - basis[2].imag * 1j,
            basis[1].real - basis[1].imag * 1j,
            basis[3].real - basis[3].imag * 1j,
        ]

        # Perform the measurements.
        measurements = []
        msg = dict()
        msmt = []
        state_res_before = self._dm_to_vec(self.sdm.full_dm.to_array())
        st = dict()
        res_l = []
        for qubit_ref in qubit_refs:
            st[qubit_ref] = self._partial_trace(self.sdm.full_dm, qubit_ref - 1)
            self.handle_unitary_gate([qubit_ref], basis_hermetian, None)
            qubit: Qubit = self.qubits[qubit_ref]
            qubit.apply_pending_error()
            if qubit.qs_ref is not None:
                p0, p1 = qubit.qsi.sdm.peak_measurement(qubit.qs_ref)
                trace = p0 + p1
                p0 /= trace
                p1 /= trace
                qubit.classical = int(qubit.qsi.random_float() < p1)
                qubit.qsi.sdm.project_measurement(
                    qubit.qs_ref, int(bool(qubit.classical))
                )
                qubit.qsi.sdm.renormalize()
                if qubit.classical:
                    p = p1
                else:
                    p = p0
            msg[qubit_ref] = (qubit.classical, p)
            self.cls_dict[qubit_ref] = qubit.classical
            res_l.append(qubit.classical)
        msmt.append(res_l)

        if measure_mod == "measureforres":
            state_res = str([self.cls_dict, state_res_before])
            for qubit_ref in qubit_refs:
                measurements.append(
                    Measurement(
                        qubit_ref,
                        msg[qubit_ref][0],
                        struct.pack("<d", msg[qubit_ref][1]),
                        probability=msg[qubit_ref][1],
                        state_vector=state_res,
                        one_shot=msmt,
                    )
                )
                self.handle_unitary_gate([qubit_ref], basis, None)
        else:
            for qubit_ref in qubit_refs:
                state_res = str([self.cls_dict, st[qubit_ref]])
                measurements.append(
                    Measurement(
                        qubit_ref,
                        msg[qubit_ref][0],
                        struct.pack("<d", msg[qubit_ref][1]),
                        probability=msg[qubit_ref][1],
                        state_vector=state_res,
                        one_shot=msmt,
                    )
                )
                self.handle_unitary_gate([qubit_ref], basis, None)
        return measurements

    def _dm_to_vec(self, dm_array):
        """Method turning a pure state density matrix into state vector."""
        num_col = dm_array.shape[1]  # Number of columns
        # The target state vector got from normalizing the column with the largest norm.
        # Mathematically, a colunm with non-zero norm is enough, but in real computer *some almost zero number is not zero*.
        # Thus, we choose the-largest-norm column to get away from that situation.
        state_vec = None
        cur_max_norm = 0
        for i in range(0, num_col):
            col_vec = dm_array[:, i]
            # This norm is just the norm of the current col's common (one-of-amplitude)* factor
            norm = np.linalg.norm(col_vec)
            if norm > cur_max_norm:
                state_vec = col_vec / norm
                cur_max_norm = norm
        return list(state_vec)

    def _partial_trace(self, full_dm, qubits_ref):
        """Method for partial trace of a density matrix."""
        dm_array = full_dm.to_array()
        num_qubits = int(np.log2(dm_array.shape[0]))  # Total number of qubits
        qubits_to_trace = [i for i in range(num_qubits) if i != qubits_ref]
        num_qubits_to_trace = len(qubits_to_trace)  # Number of qubits to trace out

        # Compute the dimensions of the reduced density matrix
        reduced_dm_dim = 2**(num_qubits - num_qubits_to_trace)

        # Initialize the reduced density matrix
        reduced_dm = np.zeros((reduced_dm_dim, reduced_dm_dim), dtype=np.complex128)

        # Compute the indices of the qubits to keep
        qubits_to_keep = sorted(set(range(num_qubits)) - set(qubits_to_trace))

        # Iterate over all elements of the full density matrix
        for i in range(2**num_qubits):
            # Compute the indices of the corresponding element in the reduced density matrix
            reduced_dm_index = tuple(np.array([i >> q & 1 for q in qubits_to_keep]))

            # Update the corresponding element in the reduced density matrix
            reduced_dm[reduced_dm_index] += dm_array[i, i]
        return self._dm_to_vec(reduced_dm)


    def handle_prepare_gate(self, qubit_refs, basis, _arb):
        measurements = []
        for qubit_ref in qubit_refs:
            self.qubits[qubit_ref].prep()
            self.handle_unitary_gate([qubit_ref], basis, None)
        return measurements

    def handle_unitary_gate(self, qubit_refs, unitary_matrix, _arb):
        # Convert the incoming matrix to a numpy array.
        unitary_matrix = self.np.reshape(
            self.np.array(unitary_matrix), (2 ** len(qubit_refs),) * 2
        )

        # Print what we're doing.
        self.debug(
            "gate on %s:\n%s"
            % (", ".join(map("q{}".format, qubit_refs)), unitary_matrix)
        )

        # Apply pending idling gates and get QuantumSim references.
        qs_refs = []
        for qubit_ref in qubit_refs:
            qubit = self.qubits[qubit_ref]
            qubit.ensure_in_sdm()
            qubit.apply_pending_error()
            qs_refs.append(qubit.qs_ref)

        # Convert the Z-basis unitary matrix to the corresponding Pauli transfer
        # matrix in QuantumSim's 0xy1 basis.
        tensor = self.ptm.single_tensor
        for _ in range(len(qubit_refs) - 1):
            tensor = self.np.kron(tensor, self.ptm.single_tensor)
        ptm = self.np.einsum(
            "xab, bc, ycd, ad -> xy",
            tensor,
            unitary_matrix,
            tensor,
            unitary_matrix.conj(),
        ).real

        # Apply the ptm.
        if len(qubit_refs) == 1:
            self.sdm.apply_ptm(qs_refs[0], ptm)
            self.sdm.ensure_dense(qs_refs[0])
            self.sdm.combine_and_apply_single_ptm(qs_refs[0])
        elif len(qubit_refs) == 2:
            self.sdm.ensure_dense(qs_refs[0])
            self.sdm.ensure_dense(qs_refs[1])
            self.sdm.combine_and_apply_single_ptm(qs_refs[0])
            self.sdm.combine_and_apply_single_ptm(qs_refs[1])
            self.sdm.apply_two_ptm(qs_refs[1], qs_refs[0], ptm)
        else:
            raise RuntimeError(
                "QuantumSim can only handle one- and two-qubit gates. "
                + "{} is too many.".format(len(qubit_refs))
            )

    def handle_advance(self, cycles):
        for qubit in self.qubits.values():
            qubit.idle(cycles)
