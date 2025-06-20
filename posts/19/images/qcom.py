from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import UnitaryGate
import numpy as np
import matplotlib.pyplot as plt

U = np.array([[0, 1], [1, 0]])
my_gate = UnitaryGate(U, label="A")
cu_gate = my_gate.control()

qr1 = QuantumRegister(1, name="|kn⟩")
# qr2 = QuantumRegister(1, name="|x2⟩")
qc = QuantumCircuit(qr1)
qc.h(0)

fig = qc.draw("mpl")
fig.savefig("circuit1.svg")