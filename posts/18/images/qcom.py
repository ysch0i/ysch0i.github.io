from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import UnitaryGate
import numpy as np
import matplotlib.pyplot as plt

U = np.array([[0, 1], [1, 0]])
my_gate = UnitaryGate(U, label="A")

qr = QuantumRegister(1, name="|x1⟩")
qc = QuantumCircuit(qr)
qc.append(my_gate, [0])

fig = qc.draw("mpl")
fig.savefig("circuit.svg")