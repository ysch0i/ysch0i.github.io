from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt


# QFT
# prepare signal
fSignal = [1, 2, 3, 4, 5, 6, 7, 8]
normSignal = np.linalg.norm(fSignal)
fSignal /= normSignal

prepared_statevector = Statevector(fSignal)

# quantum circuit
qr1 = QuantumRegister(1, name="|k1⟩")                       # qubit1
qr2 = QuantumRegister(1, name="|k2⟩")                       # qubit2
qr3 = QuantumRegister(1, name="|k3⟩")                       # qubit3
cbits = ClassicalRegister(3, "c")                           # classical register : used to save measured values 
qc = QuantumCircuit(qr1, qr2, qr3, cbits)
qc.initialize(prepared_statevector, range(0,3))

U2 = np.array([[1, 0], [0, np.exp(1j*2*np.pi/2**2)]])       # R2 gate
my_gate2 = UnitaryGate(U2, label="R2")
cu_gate2 = my_gate2.control()

U3 = np.array([[1, 0], [0, np.exp(1j*2*np.pi/2**3)]])       # R3 gate
my_gate3 = UnitaryGate(U3, label="R3")
cu_gate3 = my_gate3.control()

qc.swap(0, 2)                                               # for qiskit qubit ordering

qc.h(qr1[0]) 
qc.append(cu_gate2, [qr2[0], qr1[0]])
qc.append(cu_gate3, [qr3[0], qr1[0]])
qc.h(qr2[0]) 
qc.append(cu_gate2, [qr3[0], qr2[0]])
qc.h(qr3[0]) 

qc.measure(qr1, cbits[0])
qc.measure(qr2, cbits[1])
qc.measure(qr3, cbits[2])
# qc.draw("mpl")


# emulate quantum computer
simulator = AerSimulator()
qc= transpile(qc, simulator)
result = simulator.run(qc, shots=10000).result()

counts = result.get_counts(qc)
fig = plot_histogram(counts)
fig.savefig("hist2.svg")


# DFT
omega = np.exp(1j*2*np.pi/8)
dft = [0,0,0,0,0,0,0,0]

for k in range(8):
    for j in range(8):
        dft[k] += omega**(j*k)*fSignal[j]

plt.figure()
plt.bar(range(len(np.abs(dft))), np.abs(dft))
plt.savefig("hist3.svg")


