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


# Quantum Logic Gate

복잡한건 싫어. 최대한 간단하게 써보자.

## 1. Qubit

Classical 컴퓨터는 최소 연산 단위로 bit를 사용한다. Bit는 $0$ 또는 $1$의 값을 가진다. 반면 양자 컴퓨터는 최소 연산 단위로 qubit를 사용한다. Qubit는 $0$과 $1$이 중첩된 상태를 가진다.

그래도 우리는 양자에 익숙하니, 바로 노테이션으로 넘어가보자. 하나의 qubit $\ket{x_1}$은 아래와 같이 표현할 수 있다.


$$\begin{align}
\ket{x_1} = a \ket{0} + b \ket{1} = \begin{bmatrix}
a \\
b
\end{bmatrix}
\end{align}$$

여기서 $a$, $b$ 는 $a^*a + b^*b = 1$ 을 만족시키는 복소수이고, 

$$\begin{align}
\ket{0}  = \begin{bmatrix}
1\\
0
\end{bmatrix}\,\,\,\,\,\,\,\,\,\,\, \ket{1} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
\end{align}$$

이다. 

그럼 qubit이 2개면 어떨까? 두 qubit를 tensor product 하면 된다. 양자에서 tensor product는 단순히 두 state를 이어붙이는 것이다. 예를 들어 Born–Oppenheimer approximation이 만족하는 영역에서 분자의 state $\ket{\psi}$ 를 핵 $\ket{\chi}$과 전자 $\ket{\phi}$의 state의 곱으로 표현하는데,


$$\begin{align}
\ket{\psi} = \ket{\chi} \ket{\phi} = \ket{\chi} \otimes \ket{\phi}
\end{align}$$

여기서 곱이 tensor product 이다. 양자화학에서는 식 (3)의 중간 표현처럼 $\otimes$ 기호를 자주 생략하는 것 같다. 

같은 방법으로 두 qubit $\ket{x_1}$, $\ket{x_2}$의 tensor product는

$$\begin{align}
\ket{x_1x_2} = 
\ket{x_1}\otimes \ket{x_2} = \begin{bmatrix}
a_1\\
b_1
\end{bmatrix} \otimes \begin{bmatrix}
a_2\\
b_2
\end{bmatrix} = \begin{bmatrix}
a_1a_2 \\
a_1b_2 \\
b_1a_2 \\
b_1b_2
\end{bmatrix}
\end{align}$$

가 된다. 만약, $\ket{x_1} = \ket{0}$, $\ket{x_2} = \ket{0}$ 이면, $\ket{00}$ 으로 표기하고, 이를 행렬로 나타내면

$$\begin{align}
\ket{00}  = \begin{bmatrix}
1\\
0
\end{bmatrix} \otimes \begin{bmatrix}
1\\
0
\end{bmatrix} = \begin{bmatrix}
1\\
0\\
0\\
0
\end{bmatrix} = \ket{0}
\end{align}$$
이 된다. 비슷하게, 나머지 3가지 상태를 표현하면

$$\begin{align}
\ket{01} = \begin{bmatrix}
0\\
1\\
0\\
0
\end{bmatrix} = \ket{1}\,\,\,\,\,\,\ket{10} = \begin{bmatrix}
0\\
0\\
1\\
0
\end{bmatrix} = \ket{2}\,\,\,\,\,\,\ket{11} = \begin{bmatrix}
0\\
0\\
0\\
1
\end{bmatrix} = \ket{3}
\end{align}$$

가 된다. 이처럼 qubit이 2개인 경우에는 상태를 3가지 방법으로 표현할 수 있다. 


1. 이진법 이용 : $\ket{00}$, $\ket{01}$, $\ket{10}$, $\ket{11}$ 
   
2. 십진법 이용 : $\ket{0}$, $\ket{1}$, $\ket{2}$, $\ket{3}$

3. $4\times 1$ 행렬 이용


Qubit이 3개 이상이 경우에도 tensor product를 이용해 확장 할 수 있다.

<br>

## 2. Single-qubit gate

Classical 컴퓨터에 AND와 XOR 연산이 있는 것처럼 양자 컴퓨터에서는 quantum logic gate 가 있다. Single-qubit의 경우 quantum logic gate는 $2\times 2$ unitary matrix로 표현된다. 


예를 들어, 아래와 같은 matrix를 생각해보자.

$$\begin{align}
A = \begin{bmatrix}
p & q \\
r & s
\end{bmatrix}

\end{align}$$


$\ket{x_1} = a\ket{0} + b\ket{1}$의 상태를 가지는 qubit이 위의 $A$ gate를 통과하면,

$$\begin{align}
A\ket{x_1} = \begin{bmatrix}
p & q \\
r & s
\end{bmatrix} \begin{bmatrix}
a \\
b
\end{bmatrix} = \begin{bmatrix}
pa + qb \\
ra + sb
\end{bmatrix}
\end{align}$$

가 되고, 이를 그림으로는 아래와 같이 표현한다.

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/18/images/circuit.svg" width="150px" style="display: block; margin: 0 auto;" />
</figure>

아래는 자주 쓰이는 single-qubit gate 이다.

- Hadamard :

$$\begin{align}
H = \frac{1}{\sqrt{2}} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}

\end{align}$$


- Pauli-X,Y,Z :

$$\begin{align}
X =  \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}\,\,\,\,\,\,\,\,\,\,Y = \begin{bmatrix}
0 & -i \\
i & 0
\end{bmatrix}\,\,\,\,\,\,\,\,\,\,Z =  \begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}

\end{align}$$


- Rotation about $x,y,z$-axis : 

$$\begin{align}
RX(\theta)=  \exp \left[-\frac{i\theta}{2}  X \right] = \begin{bmatrix}
\cos (\theta/2) & -i\sin(\theta/2) \\
-i\sin(\theta/2) & \cos(\theta/2)
\end{bmatrix}

\end{align}$$

$$\begin{align}

RY(\theta) =\exp \left[-\frac{i\theta}{2}  Y \right] \,\,\, \,\,\,\,\,\,\,\,\,RZ(\theta) =\exp \left[-\frac{i\theta}{2}  Z \right] 

\end{align}$$

<br>



## 3. Controlled gate

Qubit이 2개 이상일 때는 여러 개의 qubit에 동시에 작용하는 logic gate가 존재한다. 그 중 controlled gate에서는 하나의 qubit의 상태에 따라 다른 qubit에 가해지는 operator가 바뀐다.

위에서 예시로 든 $A$ gate를 이용하여 controlled gate를 만들어 보자.







<br>

---

2025.06.00 최예성 작성




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


$$\begin{align}


\end{align}$$
<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/18/images/circuit.svg" width="550px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">From R. A. Marcus (1965).</figcaption>
</figure>
