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







# Fermi's Golden Rule II

Fermi's Golden Rule을 다른 방식으로 표현해보자.




## 1. Interaction Picture

표기의 편의성을 위해 interaction picture를 사용한다. 자세한 내용은 별도의 문서에서 설명할 예정이다. 여기서는 간단히만 알아보자.

전체 Hamiltonian을 time-indepent한 부분과 time-dependent한 부분으로 나눠보자.

$$\begin{align}
H = H_0 + V(t)
\end{align}$$

그리고, 아래와 같이 wavefunction과 operator를 정의한다. (편의를 위해 $t_0= 0$ 이라 두겠다.)

$$\begin{align}
\ket{\psi_I(t)} \stackrel{\text{def}}{=} e^{iH_0t/\hbar} \ket{\psi(t)}
\end{align}$$

$$\begin{align}
A_I(t) \stackrel{\text{def}}{=} e^{iH_0t/\hbar} A \,e^{-iH_0t/\hbar}
\end{align}$$

그러면 $A$의 expectation value를 아래와 같이 표현할 수 있다.

$$\begin{align}
\braket{A}_t &= \braket{\psi(t) \,| \,A \,|\, \psi(t)} \\
&= \braket{e^{-iH_0t/\hbar} \,\psi_I(t) \,|\, A\, | \, e^{-iH_0t/\hbar}\, \psi_I(t)  } \\
&= \braket{\psi_I(t) \,| \,e^{iH_0t/\hbar} A \,e^{-iH_0t/\hbar} \,|\, \psi_I(t)} \\
&= \braket{\psi_I(t) \,| \,A_I \,|\, \psi_I(t)}
\end{align}$$

<br>

## 2. Introduce Correlation Function

식 (1)을 모든 state로 확장해보자. 시스템이 초기에 $l$ state에서 평형을 이루고 있다면,

$$\begin{align}
k = \frac{2\pi}{\hbar} \sum_{k,l} p_l |V_{kl}|^2\delta(E_k - E_l)
\end{align}$$

여기서,
$$\begin{align}
\delta(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \mathrm{d} k \, e^{ikx}
\end{align}$$
이므로, 식 (9)를 이어서 써보면

$$\begin{align}

k &= \frac{1}{\hbar^2} \sum_{k,l} p_l  \int_{-\infty}^{\infty} \mathrm{d}t \, e^{i(E_k - E_l)t/\hbar} \braket{l|V|k} \braket{k|V|l} \\
&= \frac{1}{\hbar^2} \sum_{k,l} p_l  \int_{-\infty}^{\infty} \mathrm{d}t \,  \braket{l|V|k} \braket{k|e^{iE_kt/\hbar}Ve^{-i E_lt/\hbar}|l} \\

&= \frac{1}{\hbar^2} \sum_{k,l} p_l  \int_{-\infty}^{\infty} \mathrm{d}t \,  \braket{l|V|k} \braket{k|e^{iH_0t/\hbar}Ve^{-i H_0t/\hbar}|l} \\

&= \frac{1}{\hbar^2} \sum_{k,l} p_l  \int_{-\infty}^{\infty} \mathrm{d}t \,  \braket{l|V_I(0)|k} \braket{k|V_I(t)|l} \\ 

&= \frac{1}{\hbar^2} \sum_{l} p_l  \int_{-\infty}^{\infty} \mathrm{d}t \,  \braket{l\,|\,V_I(0)V_I(t)\,|\,l} 


\end{align}$$

여기서,
$$\begin{align}
p_l = \frac{e^{-\beta E_l}}{\text{Tr}\left[e^{-\beta H}\right]}
\end{align}$$

이므로, 이를 식 (15)에 대입하면


$$\begin{align}
k &= \frac{1}{\hbar^2\,\text{Tr}\left[e^{-\beta H}\right]} \int_{-\infty}^{\infty} \mathrm{d}t \, \text{Tr}\left[e^{-\beta H} V_I(0)V_I(t)\right] \\
&= \frac{1}{\hbar^2} \int_{-\infty}^{\infty} \mathrm{d}t \, \braket{V_I(0)V_I(t)}
\end{align}$$


따라서 Fermi's golden rule이 $V_I$의 time-autocorrelation function으로 표현된다. 

<br>




## References

<sup>1</sup> A. Tokmakoff, *Time Dependent Quantum Mechanics and Spectroscopy* (2024).



<br>

---
2024.11.14 최예성 작성

<footer class="site-footer"></footer>


</div>