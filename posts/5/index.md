<head>
  <meta charset="UTF-8" />
  <link rel="stylesheet" href="https://ysch0i.github.io/style.css" />
  <script>
    window.onload = function() {
      fetch('https://ysch0i.github.io/header.html')
        .then(response => response.text())
        .then(data => {
          document.getElementById('header').innerHTML = data;
        });
    };
  </script>
</head>

<div class="centered-container">

<div id="header"></div>



<br>




# Time-dependent Pertubation Theory

Quantum dynamics의 시작



## 1. 우리가 보려는 것

System Hamiltonian $H = H_0$의 eigenstate를 안다고 가정하자. 그럼 임의의 state는 $H_0$의 eigenstate의 superposition으로 나타낼 수 있다.

$$\begin{align}
\ket{\psi(x,0)} = \sum_ic_i\ket{\phi_i};\,\,\,\,\,\,\, \ket{\psi(x,t)} = \sum_ic_i(t)\ket{\phi_i}
\end{align}$$

Schrödinger equation

$$\begin{equation}
i\hbar\frac{\partial}{\partial t} \ket{\psi} = H_0 \ket{{\psi}}
\end{equation}$$
에 (1)을 대입하면,

$$\begin{equation}
i\hbar \sum_i \left(\frac{\partial}{\partial t}c_i(t)\right) \ket{\phi_i} = \sum_i c_i(t)E_i\ket{\phi_i}
\end{equation}$$
따라서
$$\begin{equation}
c_i(t) = c_i e^{-iE_it/\hbar}
\end{equation}$$
를 얻는다. 여기서 전자가 $i$ state의 존재할 확률은 시간에 따라 변하지 않음을 알 수 있다.

$$\begin{equation}
P_i(t) = |c_i(t)|^2 = |c_i|^2
\end{equation}$$

즉, 서로 다른 state 간의 전자 전이가 발생하지 않는다(steady-state). 

그러나, 원래의 system에 pertubation $V(t)$가 작용한다면 상황이 달라진다. 시스템의 Hamiltonian이 $H=H_0 + V(t)$로 바뀌더라도, $H_0$의 eigenstate는 complete set을 이루므로 임의의 state는 전의 예시와 비슷한 형태로 쓰여진다.

$$\begin{equation}
\ket{\psi(x,t)} = \sum_ic_i(t)\ket{\phi_i}
\end{equation}$$

Purtubation $V(t)$가 존재하므로 $c_i(t)$를 (4)와 동일하게 쓸 수는 없지만 (4)와 비슷하게 쓸 수는 있다. 

$$\begin{equation}
c_i(t) = b_i(t) e^{-iE_it/\hbar}
\end{equation}$$

Pertubation $V(t)$가 작을수록 $b_i(t)$는 $c_i$에 가까워질 것이다. 

한편, 이제는 $P_i$가 시간과 독립적이지 않다.
$$\begin{equation}
P_i(t) = |c_i(t)|^2 = |b_i(t)|^2
\end{equation}$$
즉, pertubation이 존재하면 두 state 간의 전자 전이가 발생한다. 우리가 보려는 것은 바로 이 전자 전이이다.

<br>



## 2. Two-state Model

이제, pertubation에 따라 어떠한 전자 전이가 발생하는지 알아보자. 단순화를 위해 two-state model을 사용하자. 

Unpertubated Hamiltonian $H_0$가 두 orthonormal eigenstate $\ket{\phi_a}$, $\ket{\phi_b}$를 가지고, Hamiltonian이 $H = H_0 + V(t)$로 나타난다고 가정하자. 그럼 임의의 state는 아래와 같이 표현된다.

$$\begin{equation}
\ket{\psi(x,t)} = b_a(t)e^{-iE_at/\hbar} \ket{\phi_a} + b_b(t)e^{-iE_bt/\hbar} \ket{\phi_b}
\end{equation}$$

전체  Schrödinger equation (2)에 (9)를 대입하면,

$$\begin{equation}
i\hbar\left(\dot{b_a}e^{-iE_at/\hbar} \ket{\phi_a} + \dot{b_b}e^{-iE_bt/\hbar} \ket{\phi_b}           \right) = b_a(t)e^{-iE_at/\hbar} V(t) \ket{\phi_a} + b_b(t)e^{-iE_bt/\hbar} V(t)\ket{\phi_b}
\end{equation}$$

여기서 양변에 각각 $\bra{\phi_a}$와 $\bra{\phi_b}$를 취하면,

$$\begin{align}
\dot{b_a}(t) &= -\frac{i}{\hbar} \left[  b_a(t)V_{aa} + b_b V_{ab} e^{-i(E_b-E_a)t/\hbar}   \right] \\
\dot{b_b}(t) &= -\frac{i}{\hbar} \left[  b_b(t)V_{bb} + b_a V_{ba} e^{-i(E_a-E_b)t/\hbar}   \right]
\end{align}$$

를 얻는다. 여기서 $V_{ab} = \braket{\phi_a | V(t) | \phi_b}$ 이다. 

일반적으로, $V(t)$의 diagonal term은 0이므로, 위의 식을 간단하게 표현할 수 있다. 

$$\begin{align}
\dot{b_a}(t) &= -\frac{i}{\hbar} b_b V_{ab} e^{-i(E_b-E_a)t/\hbar}   \\
\dot{b_b}(t) &= -\frac{i}{\hbar} b_a V_{ba} e^{-i(E_a-E_b)t/\hbar}   
\end{align}$$

여기까지는, 어떠한 근사도 사용하지 않았다.

<br>

## 3. 1st order Purtubation Theory

만약, $V(t)$가 매우 작다면 시간에 따라 $b(t)$는 시간에 따라 크게 변화하지 않을 것이다. 또한, $t=0$에서 전자는 $\ket{\phi_a}$에 있다고 하자.

$$\begin{equation}
b_a(0) = 1 \stackrel{\text{def}}{=} b_a^{(0)}(t); \,\,\,\,\,\,b_b(0) = 0 \stackrel{\text{def}}{=} b_b^{(0)}(t)
\end{equation}$$


그러면, 식 (13)과 (14)를 아래와 같이 근사할 수 있다.

$$\begin{align}
\dot{b_a}^{(1)} (t) &\simeq -\frac{i}{\hbar} b_b^{(0)} (t) V_{ab} e^{-i(E_b-E_a)t/\hbar} = 0  \\
\dot{b_b}^{(1)}(t) &\simeq -\frac{i}{\hbar} b_a^{(0)} (t) V_{ba} e^{-i(E_a-E_b)t/\hbar}   = -\frac{i}{\hbar}V_{ba} e^{-i(E_a-E_b)t/\hbar}
\end{align}$$

따라서 

$$\begin{align}
b_a^{(1)}(t) &\simeq 1  \\
b_b^{(1)}(t) &\simeq -\frac{i}{\hbar} \int_{-\infty}^t \mathrm{d}t' \, V_{ba} e^{-i(E_a-E_b)t'/\hbar}   
\end{align}$$

가 된다. 이를 1st order time-dependent purtubation theory라 한다.


<br>

## 4. Generalization

Two-state model을 확장해보자.


$$\begin{align}

\frac{\partial b_{k}^{(1)}(t) }{\partial t} &\simeq -\frac{i}{\hbar} \sum_i b_i^{(0)} (t) V_{ki} e^{-i(E_i-E_k)t/\hbar}

\\
b_{k\neq l}^{(1)}(t) &\simeq -\frac{i}{\hbar} \sum_k\int_{-\infty}^t \mathrm{d}t' \, b_k^{(0)}(t) V_{kl} e^{-i(E_l-E_k)t'/\hbar}   
\end{align}$$

<br>


## References

<sup>1</sup> D. J. Griffiths, and D. F. Schroeter, *Introduction to Quantum Mechanics*, Third edition (Cambridge University Press, Cambridge ; New York, NY, 2018).



<br>

---
2024.05.17 최예성 작성

<footer class="site-footer"></footer>


</div>