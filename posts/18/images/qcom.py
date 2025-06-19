from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import UnitaryGate
import numpy as np
import matplotlib.pyplot as plt

U = np.array([[0, 1], [1, 0]])
my_gate = UnitaryGate(U, label="A")
cu_gate = my_gate.control()

qr1 = QuantumRegister(1, name="|x1⟩")
qr2 = QuantumRegister(1, name="|x2⟩")
qc = QuantumCircuit(qr1, qr2)
qc.append(cu_gate, [0,1])

fig = qc.draw("mpl")
fig.savefig("circuit2.svg")