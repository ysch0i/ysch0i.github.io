from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import UnitaryGate
import numpy as np
import matplotlib.pyplot as plt

U = np.array([[0, 1], [1, 0]])
my_gate2 = UnitaryGate(U, label="R2")
cu_gate2 = my_gate2.control()


my_gate3 = UnitaryGate(U, label="R3")
cu_gate3 = my_gate3.control()

qr1 = QuantumRegister(1, name="|k1⟩")
qr2 = QuantumRegister(1, name="|k2⟩")
qr3 = QuantumRegister(1, name="|k3⟩")
qc = QuantumCircuit(qr1, qr2, qr3)


qc.h(0) 
qc.append(cu_gate2, [qr2[0], qr1[0]])
qc.append(cu_gate3, [qr3[0], qr1[0]])
qc.h(1) 
qc.append(cu_gate2, [qr3[0], qr2[0]])
qc.h(2) 
fig = qc.draw("mpl")
qc.swap(0, 2)
fig.savefig("circuit4.svg")