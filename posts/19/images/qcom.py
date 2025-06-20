from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import UnitaryGate
import numpy as np
import matplotlib.pyplot as plt

U = np.array([[0, 1], [1, 0]])
my_gate = UnitaryGate(U, label="R2")
cu_gate = my_gate.control()

qr1 = QuantumRegister(1, name="|kn-1⟩")
qr2 = QuantumRegister(1, name="|kn⟩")
qc = QuantumCircuit(qr1, qr2)
qc.h(0) 

qc.append(cu_gate, [qr2[0], qr1[0]])
qc.h(1) 
fig = qc.draw("mpl")
fig.savefig("circuit2.svg")