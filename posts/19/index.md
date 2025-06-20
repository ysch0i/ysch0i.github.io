<link rel="stylesheet" href="https://ysch0i.github.io/style.css" />
<div class="centered-container">
<div id="header"></div>
<script>
  fetch('https://ysch0i.github.io/header.html')
    .then(res => res.text())
    .then(data => {
      document.getElementById('header').innerHTML = data;
    });
</script>
<br>


# Fourier Transform with Quantum Computer II

퀀텀 컴퓨터 잘되면 좋겠다.


## 1. Basis transform with qubit


[Fourier Transform with Quantum Computer I](https://ysch0i.github.io/posts/16/) 에서 우리는 아래와 같은 basis transform을 해야 한다는 것을 알았다.

$$\begin{align}
\ket{k} &\mapsto \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} \omega_N^{jk} \ket{j} \\
&= \frac{1}{\sqrt{N}} \left(\ket{0} + e^{i2\pi [0.k_n]} \ket{1}      \right) \otimes \left(\ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1}      \right) \otimes \cdots \otimes \left(\ket{0} + e^{i2\pi [0.k_1 k_2 \cdots k_n]  } \ket{1}      \right)
\end{align}$$


여기서 $\omega_N = e^{i2\pi/N}$, $k$는 $0$부터 $N-1$까지의 범위를 가지는 정수, $k_j$는 0 또는 1이며 아래의 식을 만족한다.

$$\begin{align}
(k)_{10} = (k_1 k_2 \cdots k_n)_2
\end{align}$$

$$\begin{align}
k &= 2^{n-1} k_1 + 2^{n-2} k_2 +  \cdots + k_n \\ 

&= \sum_{m=1}^n 2^{n-m} k_m
\end{align}$$

$\ket{k} = \ket{k_1k_2 \cdots k_n} = \ket{k_1} \otimes \ket{k_2} \otimes \cdots \otimes \ket{k_n}$이므로 이를 식 (2)에 대입하면, 

$$\begin{align}
\ket{k_1} \otimes \ket{k_2} & \otimes \cdots \otimes \ket{k_n} \\
&\mapsto 
\frac{1}{\sqrt{N}} \left(\ket{0} + e^{i2\pi [0.k_n]} \ket{1}      \right) \otimes \left(\ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1}      \right) \otimes \cdots \otimes \left(\ket{0} + e^{i2\pi [0.k_1 k_2 \cdots k_n]  } \ket{1}      \right)
\end{align}$$

가 된다. 따라서 basis transform을 qubit의 관점에서 보면,


$$\begin{align}
\ket{k_1} \mapsto \ket{0} + e^{i2\pi [0.k_n]} \ket{1} 
\end{align}$$

$$\begin{align}
\ket{k_2} \mapsto \ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1} 
\end{align}$$

$$\cdots$$

$$\begin{align}
\ket{k_n} \mapsto \ket{0} + e^{i2\pi [0.k_1 k_2 \cdots k_n] } \ket{1}    
\end{align}$$

가 된다(정규화 상수 생략). 즉, 우리는 퀀텀 컴퓨터 회로를 통해 첫 번째 qubit을 식 (8)로, $\cdots$ $n$ 번째 qubit을 식 (10)으로 변환해야 한다.

하지만, 식 (8)-(10)의 변환은 어렵다. 따라서 quantum Fourier transform 에서는 아래와 같은 변환을 한 뒤, SWAP gate로 순서를 뒤집는다.

$$\begin{align}
\ket{k_1} \mapsto \ket{0} + e^{i2\pi [0.k_1 k_2 k_3 \cdots k_n] } \ket{1}    



\end{align}$$

$$\begin{align}
\ket{k_2} \mapsto \ket{0} + e^{i2\pi [0.k_2 k_3 \cdots k_n] } \ket{1}   
\end{align}$$

$$\cdots$$

$$\begin{align}
\ket{k_n} \mapsto \ket{0} + e^{i2\pi [0.k_n]} \ket{1} 
\end{align}$$


<br>

## 2. 회로 설계

먼저, 식 (13)의 변환은 쉽다. 잘 안보인다면 $k_n$에 0, 1을 대입해보면 된다. 

$k_n = 0$이면,

$$\begin{align}
\ket{0} &\mapsto \ket{0} + e^{i2\pi [0.0]} \ket{1} \\
&= \ket{0} + \ket{1}
\end{align}$$

$k_n = 1$이면,

$$\begin{align}
\ket{1} &\mapsto \ket{0} + e^{i2\pi [0.1]} \ket{1} \\
&= \ket{0} + e^{i2\pi 2^{-1}} \ket{1} \\
&= \ket{0} + e^{i\pi} \ket{1} \\
&= \ket{0} - \ket{1}

\end{align}$$

따라서 식 (13)의 변환은 

$$\begin{align}
\begin{bmatrix}
a \\
b 
\end{bmatrix} \mapsto \begin{bmatrix}
a+b \\
a-b
\end{bmatrix}
\end{align}$$

이다. 이게 뭘까? 바로 Hadamard gate 이다. 따라서 $n$ 번째 qubit의 변환은 Hadamard gate 하나로 표현된다 (앞으로 정규화 상수 생략).

$$\begin{align}
H \ket{k_n} = \ket{0} + e^{i2\pi [0.k_n]} \ket{1} 
\end{align}$$



<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/circuit1.svg" width="150px" style="display: block; margin: 0 auto;" />
</figure>


다음으로 $n-1$ 번째 qubit을 변환해보자. 


$$\begin{align}
\ket{k_{n-1}} \mapsto \ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1} 
\end{align}$$

일단 먼저 Hadamard gate를 통과시키면,

$$\begin{align}
H \ket{k_{n-1}} = \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} 
\end{align}$$

가 된다. 이제

$$\begin{align}
 \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} \mapsto \ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1} 
\end{align}$$

을 해주면 된다. 앞에서와 마찬가지로 $k_n$에 0, 1을 대입해보자. 

$k_n = 0$이면,

$$\begin{align}
 \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} \mapsto \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} 
\end{align}$$


아무 변화가 없다. $k_n = 1$이면,

$$\begin{align}
 \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} &\mapsto \ket{0} + e^{i2\pi [0.k_{n-1}1]} \ket{1} \\
 &= \ket{0} + e^{i2\pi ([0.k_{n-1}] + 2^{-2})} \ket{1} \\
&= \ket{0} + e^{i2\pi[0.k_{n-1}]} e^{i2\pi / 2^2} \ket{1} \\
\end{align}$$

즉, 식 (28)의 변환은 $\ket{1}$에 $e^{i2\pi / 2^2}$ 가 곱해지므로 아래와 같은 행렬 $R_2$로 표현할 수 있다.

$$\begin{align}
R_2 = \begin{bmatrix}
1 & 0 \\
0 & e^{i2\pi / 2^2}
\end{bmatrix}

\end{align}$$


식 (25), (28)을 종합하면, $n-1$ 번째 qubit은 $n$ 번째 qubit이 $\ket{0}$이면, 아무런 변화가 없고, $n$ 번째 qubit이 $\ket{1}$이면, $R_2$ gate가 가해진다. 이게 뭘까? 바로 controlled gate 이다. 

따라서 식 (23)의 Hadamard gate, 식 (24)의 controlled gate 를 종합하면 $n-1$ 번째 qubit의 변환은 아래와 같이 표현된다 ($n$ 번째 qubit의 변환도 같이 표현).

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/circuit2.svg" width="300px" style="display: block; margin: 0 auto;" />
</figure>


이렇게 계속 반복하면 된다. 예들 들어 qubit이 3개라면 

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/circuit3.svg" width="450px" style="display: block; margin: 0 auto;" />
</figure>

가 된다. 여기서 $R_k$ gate는

$$\begin{align}
R_k = \begin{bmatrix}
1 & 0 \\
0 & e^{i2\pi / 2^k}
\end{bmatrix}

\end{align}$$


이다. 마지막으로 SWAP gate을 통해 qubit의 순서를 반대로 바꿔주면 quantum Fourier transform 회로가 완성된다.

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/circuit4.svg" width="500px" style="display: block; margin: 0 auto;" />
</figure>

<br>



## 3. 구현

위에서 살펴본 회로를 통해 실제로 3-qubit system에서 quantum Fourier transform을 하는 과정을 알아보자. 사실 3-qubit이면 데이터가 8개라 Fourier transform이라 하기 민망하긴 하다. 그래도 시각화를 위해 3-qubit system을 사용한다.

우리의 목표는 데이터 $x_0$, $x_1$, $\cdots$, $x_7$이 주어졌을 때, discrete Fourier transform된 데이터 $\xi_0$, $\xi_1$, $\cdots$, $\xi_7$를 얻는 것이다.


$$\begin{align}
\begin{bmatrix}
x_0 \\
x_1 \\
\vdots \\
x_7
\end{bmatrix}  \mapsto 
\begin{bmatrix}
\xi_0 \\ \xi_1 \\  \vdots \\ \xi_7
\end{bmatrix}  
\end{align}$$


IBM의 qskit package를 사용하여 quantum Fourier transform을 구현해보겠다. 먼저, 초기의 상태를 


$$\begin{align}
\ket{x}&=x_0 \ket{0} + x_1 \ket{1} + \cdots x_7 \ket{7} \\
&= x_0 \ket{000} + x_1 \ket{001} + \cdots x_7 \ket{111}
\end{align}$$

로 initialize 한다. 여기서는 $[x_0, x_1, \cdots, x_7] = [1,2,\cdots 8]$로 initialize 하였다. 

```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

fSignal = [1, 2, 3, 4, 5, 6, 7, 8]
normSignal = np.linalg.norm(fSignal)
fSignal /= normSignal

prepared_statevector = Statevector(fSignal)

qr1 = QuantumRegister(1, name="|k1⟩")
qr2 = QuantumRegister(1, name="|k2⟩")
qr3 = QuantumRegister(1, name="|k3⟩")
cbits = ClassicalRegister(3, "c")
qc = QuantumCircuit(qr1, qr2, qr3, cbits)
qc.initialize(prepared_statevector, range(0,3))

qc.measure(qr1, cbits[0])
qc.measure(qr2, cbits[1])
qc.measure(qr3, cbits[2])

simulator = AerSimulator()
qc= transpile(qc, simulator)
result = simulator.run(qc, shots=10000).result()

counts = result.get_counts(qc)
fig = plot_histogram(counts)
fig.savefig("hist1.svg")
```

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/hist1.svg" width="500px" style="display: block; margin: 0 auto;" />
</figure>

그 결과 각 state가 나타날 확률이 $|x_i|^2$에 비례하는 것을 확인 할 수 있었다.

이후, 위에서 구현한 회로를 구성한 뒤, 각 state가 나타날 확률을 다시 측정한다.

```python
U2 = np.array([[1, 0], [0, np.exp(1j*2*np.pi/2**2)]])
my_gate2 = UnitaryGate(U2, label="R2")
cu_gate2 = my_gate2.control()

U3 = np.array([[1, 0], [0, np.exp(1j*2*np.pi/2**3)]])
my_gate3 = UnitaryGate(U3, label="R3")
cu_gate3 = my_gate3.control()

qc.swap(0, 2)

qc.h(qr1[0]) 
qc.append(cu_gate2, [qr2[0], qr1[0]])
qc.append(cu_gate3, [qr3[0], qr1[0]])
qc.h(qr2[0]) 
qc.append(cu_gate2, [qr3[0], qr2[0]])
qc.h(qr3[0]) 
```

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/hist2.svg" width="500px" style="display: block; margin: 0 auto;" />
</figure>


위의 그림에서 각 state가 나타날 확률이 $|\xi_i|^2$을 의미한다. 결과가 맞는지 확인하기 위해 classical 컴퓨터의 discrete Fourier transform과 비교해보자. 같은 signal에 대해 discrete Fourier transform을 진행하였을 때 결과는 아래 그림과 같다.

```python
omega = np.exp(1j*2*np.pi/8)
dft = [0,0,0,0,0,0,0,0]

for k in range(8):
    for j in range(8):
        dft[k] += omega**(j*k)*fSignal[j]

plt.bar(range(len(np.abs(dft))), np.abs(dft))
plt.savefig("hist3.svg")
```

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/hist3.svg" width="500px" style="display: block; margin: 0 auto;" />
</figure>

Quantum Fourier transform이 discrete Fourier transform과 같은 결과가 나왔음을 확인 할 수 있다. 

참고로, qiskit은 일반적으로 쓰는 노테이션과 qubit의 순서가 반대이다. 여기서는 일반적인 노테이션을 따라가기 위해 전체 회로 앞뒤에 swap gate를 넣었다. 전체 python 코드는 [여기](https://ysch0i.github.io/posts/19/images/qft_yschoi.py)에서 다운로드 할 수 있다.

<br>

## 4. 시간 복잡도

Dicrete Fourier transform 에서는 

$$\begin{align}
\begin{bmatrix}
\xi_0 \\ \xi_1 \\ \xi_2\\ \vdots \\ \xi_{N-1}
\end{bmatrix}  =\frac{1}{\sqrt{N}} \begin{bmatrix}
1 & 1 & 1               &  \cdots & 1 \\
1 & \omega & \omega^2      &  \cdots    &\omega ^{N-1}        \\
1 & \omega^2 & \omega^4 &  \cdots &\omega^{2(N-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots  \\
1 & \omega ^{N-1}  & \omega^{2(N-1)} & \cdots &\omega^{(N-1)(N-1)}

\end{bmatrix} \begin{bmatrix}
x_0 \\
x_1 \\
x_2 \\
\vdots \\
x_{N-1}
\end{bmatrix} 
\end{align}$$

를 계산하면 된다. 단순히 위의 행렬 연산을 한다면 시간 복잡도는 $O(N^2)$ 이고, FFT algorithm을 사용한다면 시간 복잡도는 $O(N\log N)$ 이 된다.


퀀텀 컴퓨터에서 시간 복잡도는 일반적으로 순차적으로 실행되어야 하는 gate layor의 개수가 된다. Quantum Fourier transform 회로를 보면 병렬로 연산할 수 있는 gate가 없으므로 단순히 gate의 개수가 시간복잡도가 된다.

위의 회로에서 qubit의 개수가 $n$개 라면 게이트의 수는 $n(n+1)/2$ 개 이므로 시간 복잡도는 $O(n^2)$ 이 된다. 이 때, $N = 2^n$ ($N$개의 데이터를 $n$개의 qubit으로 표현) 이므로 시간 복잡도를 $N$으로 나타내면 $O((\log N)^2)$이다.

정리하자면 classical 컴퓨터의 FFT는 $O(N\log N)$, 퀀텀 컴퓨터의 quantum Fourier transform은 $O((\log N)^2)$으로 퀀텀 컴퓨터가 어머어마하게 빠르다는 것을 알 수 있다.



<br>

## References

<sup>1</sup> L. Ruiz-Perez, and J. C. Garcia-Escartin, “Quantum arithmetic with the quantum Fourier transform,” [Quantum Inf Process](https://doi.org/10.1007/s11128-017-1603-1) **16**, 152 (2017).

<sup>2</sup> D. Camps, R. Van Beeumen, and C. Yang, “Quantum Fourier transform revisited,” [Numerical Linear Algebra App](https://doi.org/10.1002/nla.2331) **28**, e2331 (2021).


<sup>3</sup> M. A. Nielsen, and I. L. Chuang, *Quantum Computation and Quantum Information*, 10th anniversary edition (Cambridge university press, Cambridge, 2010).


<br>

---

2025.06.21 최예성 작성




<script src="https://utteranc.es/client.js"
        repo="ysch0i/ysch0i.github.io"
        issue-term="pathname"
        label="Comment"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
<div id="footer"></div>
<script>
  fetch('https://ysch0i.github.io/footer.html')
    .then(res => res.text())
    .then(html => {
      document.getElementById('footer').innerHTML = html;
    });
</script>
</div>