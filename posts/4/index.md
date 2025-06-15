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



# Basic Formulas


맨날 쓰는데 왜 자꾸 까먹지?

양자역학을 처음부터 설명할 자신은 없다. 그건 뒤로 미루고, 대신 학부 2학년 수준에서 글을 써보고자 한다. 아래의 공식은 증명없이 사용할 예정이다.

## 1. Harmonic Oscillator



Creation operator $(a_+)$ and annihilation operator $(a_−)$

$$
\begin{equation}
a_\pm \stackrel{\text{def}}{=} \frac{1}{\sqrt{2\hbar m\omega}}(\mp ip + m\omega x)
\end{equation}
$$

$$
\begin{equation}
x = \sqrt{\frac{\hbar}{2m\omega }}(a_+ + a_-); \,\,\,\,\,\,\,\,\,\,
p = i\sqrt{\frac{\hbar m\omega }{2}}(a_+ - a_-)
\end{equation}
$$

$$
\begin{equation}[a_-, \,a_+] = 1\end{equation}
$$

$$
\begin{equation}
H = \hbar \omega  \left( a_+a_- + \frac{1}{2}   \right)
\end{equation}
$$

$$
\begin{equation}
\psi_n(x) = \left(\frac{m\omega }{\pi\hbar}  \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi) e^{-\xi^2/2}; \,\,\,\, \xi \stackrel{\text{def}}{=} \sqrt{\frac{m\omega }{\hbar}}x
\end{equation}
$$

where, $H_n(ξ)$ is Hermite polynomial.

<br>

## 2. Time-independent Pertubation Theory



Define Hamiltonian

$$
\begin{equation} H = H_0 + \lambda H^′\end{equation}
$$

Time-independent Schrödinger equation

$$
\begin{equation}H\psi_n = E_n\psi_n\end{equation}
$$

and let,

$$
\begin{align}
\psi_n &= \psi_n^{(0)} + \lambda \psi_n^{(1)} + \lambda^2 \psi_n^{(2)} + \cdots \\
E_n &= E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots
\end{align}
$$

then,

$$
\begin{equation}(H_0+\lambda H')(\psi_n^{(0)} + \lambda \psi_n^{(1)} + \cdots) =(E_n^{(0)} + \lambda E_n^{(1)} + \cdots) (\psi_n^{(0)} + \lambda \psi_n^{(1)} + \cdots)\end{equation}
$$

$\lambda$의 power를 기준으로 나누면,

$\lambda^0$ terms:

$$
\begin{equation}H_0 \psi_n^{(0)} = E_n^{(0)}\psi_n^{(0)}\end{equation}
$$

$\lambda^1$ terms:

$$
\begin{equation}H'\psi_n^{(0)} + H_0\psi_n^{(1)} = E_n^{(1)}\psi_n^{(0)} + E_n^{(0)} \psi_n^{(1)}\end{equation}
$$

$\lambda^2$ terms:

$$
\begin{equation}H'\psi_n^{(1)} + H_0\psi_n^{(2)} = E_n^{(2)}\psi_n^{(0)} + E_n^{(1)} \psi_n^{(1)} + E_n^{(0)} \psi_n^{(2)}\end{equation}
$$

이 때,

$$
\begin{equation}
E_n^{(1)} = \braket{\psi_n^{(0)} | H' | \psi_n^{(0)}}
\end{equation}
$$

$$
\begin{equation}
\psi_n^{(1)} = \sum_{m \neq n} \frac{\braket{\psi_m^{(0)} | H' | \psi_n^{(0)}}}{E_n^{(0)} - E_m^{(0)}} \psi_m^{(0)}
\end{equation}
$$

$$
\begin{equation}
E_n^{(2)} = \sum_{m \neq n} \frac{|\braket{\psi_m^{(0)} | H' | \psi_n^{(0)}}|^2}{E_n^{(0)} - E_m^{(0)}}
\end{equation}
$$

<br>

## 3. Fourier Transform



General

$$
\begin{equation}F(\xi) = \int_{-\infty}^\infty \mathrm{d}x \, f(x)e^{-i2\pi\xi x}\end{equation}
$$

$$
\begin{equation}f(x) = \int_{-\infty}^\infty \mathrm{d}\xi \,F(\xi) e^{i2\pi\xi x}\end{equation}
$$

Time domain $\leftrightarrow$ Frequency domain

$$
\begin{equation}F(\omega) = \int_{-\infty}^\infty \mathrm{d}t \,f(t)e^{-i\omega t}\end{equation}
$$

$$
\begin{equation}
f(t) = \frac{1}{2\pi}\int_{-\infty}^\infty \mathrm{d}\omega \,F(\omega) e^{i\omega t}
\end{equation}
$$

Position space $\leftrightarrow$ Momentum space

$$
\begin{equation}
\phi(p,t) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^\infty \mathrm{d}x \,\psi(x,t) e^{-ipx/\hbar}
\end{equation}
$$

$$
\begin{equation}
\psi(x,t) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^\infty \mathrm{d}p \,\phi(p,t) e^{ipx/\hbar}
\end{equation}
$$


<br>


## References


$^1$ D. J. Griffiths, and D. F. Schroeter, *Introduction to Quantum Mechanics*, Third edition (Cambridge University Press, Cambridge ; New York, NY, 2018).

$^2$ S. Blundell, and K. M. Blundell, *Concepts in Thermal Physics*, 2nd ed (Oxford university press, Oxford, 2010).

<br>

---

2024.05.13 최예성 작성

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