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



# Scattering State



터널링 연습벽을 보고 생각나서 정리해본다. 




<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/8/images/1.png" width="550px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">틀방에 있는 터널링 연습 벽.</figcaption>
</figure>





## 1. Scattering vs Bound



Scattering state와 bound state의 정의부터 알아보자. 편의를 위해 1차원에서 설명한다.

$$
\begin{align}
\begin{cases}    E < V(\pm \infty) & \Rightarrow \text{bound state}\\    E > V(-\infty) \text{ or } V(+\infty) & \Rightarrow \text{scattering state}  \end{cases}
\end{align}
$$

이를 그림으로 나타내면 아래와 같다.

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/8/images/2.png" width="700px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">From D. J. Griffiths (2018).</figcaption>
</figure>


즉, bound state에서는 입자가 potential에 trap되어 있어 $x = \pm \infty$에서 입자를 발견할 확률이 0에 수렴하지만, scattering state에서는 그렇지 않다. 

Scattering state와 bound state를 나누는 이유는 그들의 특성이 다르기 때문이다. 우리가 양자역학을 배울 때 다루는 대부분의 state는 bound state 이다. 예를 들어 harmonic potential이나 infinite potential wall 또는 Hydrogen atom을 생각해보자. 이들의 eigenstate는 normalizable 하고 양자수가 불연속적인데, 이것이 bound state의 특징이다.

$$
\begin{align}
\braket{\psi_n | \psi_{n'}} = \delta_{n,n'}
\end{align}
$$

$$
\begin{align}
1 = \sum_n \ket{\psi_n} \bra{\psi_n}
\end{align}
$$

$$
\begin{align}
\psi = \sum_n \ket{\psi_n} \braket{\psi_n | \psi}
\end{align}
$$

그러나 scattering state는 그렇지 않다. Scattering state의 대표적인 예시인 free particle을 생각해보면 양자수 $k$가 연속적인 값을 가질 수 있음을 알 수 있다.

$$
\begin{align}
\braket{x | \psi_k} = \psi_k(x) \propto e^{ikx}
\end{align}
$$

또한, $\ket{\psi_k}$가 normalizable 하지도 않다. 따라서 scattering state는 Kronecker delta가 아닌 delta function을 이용해 orthonormality를 만들고, $\sum$ 대신 $\int$을 이용하여 closure relation을 만든다.

$$
\begin{align}
\braket{\psi_k | \psi_{k'}} = \delta(k-k')
\end{align}
$$

$$
\begin{align}
1 = \int \mathrm{d}k \ket{\psi_k} \bra{\psi_k}
\end{align}
$$

$$
\begin{align}
\psi = \int \mathrm{d}k \ket{\psi_k} \braket{\psi_k | \psi}
\end{align}
$$

그럼 터널링을 볼 때 왜 scattering state를 사용할까? 물론 bound state에서도 터널링을 볼 수 있지만, bound state는 터널링의 flux를 만들지 못한다. 따라서 터널링을 기술할때에는 scattering state의 도입이 필수적이다. 

<br>

## 2. Notation


Define Hamiltonian.

$$
\begin{align}
H = H_0 + V = \frac{p^2}{2m} + V(x)
\end{align}
$$

Note that $p$ and $x$ are operator.

Define eigenstate.

$$
\begin{align}
H\ket{\psi_p} = E \ket{\psi_p}
\end{align}
$$

$$
\begin{align}
\frac{p^2}{2m} &\stackrel{\text{def}}{=} E
\end{align}
$$

Note that momentum of state $\ket{\psi_p}$ is not $p$, since it’s not free-particle.

여기서 $V(x)$가 $x = \pm \infty$ 에서 0으로 수렴한다고 가정하자. 아래 그림과 같은 일반적인 터널링 시스템을 상상하면 된다. 

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/8/images/3.png" width="550px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">From 김지환 교수님 양자화학 ppt (2023).</figcaption>
</figure>


그림에서는 입자가 a/b 구역의 경계에서 반사될 확률을 $|r|^2$, 입자가 c 구역으로 투과될 확률을 $|t|^2$으로 설정했었다. 이와 비슷하게 나는 입자가 potential wall의 어디서든 반사되어 $x = -\infty$에 도달할 확률을 $|R|^2$, potential wall을 투과화여 $x = +\infty$에 도달할 확률을 $|T|^2$이라 하겠다. $R$ 과 $T$ 는 당연히 시스템의 총 에너지 $E$의 함수일 것이다. 따라서 boundary condition은 아래와 같이 나타난다. 

Boundary conditions.

$$
\begin{align}
\psi_p(x\rightarrow -\infty) = \phi_p(x) + \phi_{-p}(x) R(E)
\end{align}
$$

$$
\begin{align}
\psi_p(x\rightarrow \infty) =\phi_p(x)T(E)
\end{align}
$$

where $\phi_p(x) = \braket{x|p}$ (free-particle eigenstate).

<br>

## 3. Probability Current



이제 우리는 $x=-\infty$ 에서 출발한 입자가 potential wall을 터널링해 $x =+\infty$ 에 도달하는 flux를 보고자 한다.

$h$ : Heaviside step function or projection operator.

$$
\begin{equation}
h(t) \stackrel{\text{def}}{=} \begin{cases}
    1\hphantom{-\sqrt{-}} & \text{if } x\geq s,\\
    0 & \text{if } x <s,
  \end{cases}
\end{equation}
$$

Recall Heisenberg picture of operator.

$$
\begin{align}
F(s) &\stackrel{\text{def}}{=} \frac{\mathrm{d}}{\mathrm{d}t} h(x-s) = \frac{i}{\hbar} \left[ H, h(x-s) \right]
\end{align}
$$

Let’s simplify

$$
\begin{align}
\left[  \frac{\mathrm{d}^2}{\mathrm{d}x^2} , h(x-s) \right] \psi &= \frac{\mathrm{d}^2}{\mathrm{d}x^2} (h(x-s)\psi) - h(x-s) \frac{\mathrm{d}^2}{\mathrm{d}x^2} \psi \\
&= \psi \frac{\mathrm{d}^2}{\mathrm{d}x^2} h(x-s) + 2 \left( \frac{\mathrm{d}}{\mathrm{d}x} \psi \right)\left( \frac{\mathrm{d}}{\mathrm{d}x} h(x-s) \right) \\
&= \psi \frac{\mathrm{d}}{\mathrm{d}x} \delta(x-s) + 2 \delta(x-s) \frac{\mathrm{d}}{\mathrm{d}x} \psi \\
&= \frac{\mathrm{d}}{\mathrm{d}x} (\delta(x-s)\psi) + \delta(x-s) \frac{\mathrm{d}}{\mathrm{d}x} \psi \\
&= \left(  \frac{\mathrm{d}}{\mathrm{d}x} \delta(x-s)  + \delta(x-s) \frac{\mathrm{d}}{\mathrm{d}x} \right)\psi
\end{align}
$$

Therefore,

$$
\begin{align}
F(s) = -\frac{i\hbar}{2m} \left[  \frac{\mathrm{d}}{\mathrm{d}x} \delta(x-s)  + \delta(x-s) \frac{\mathrm{d}}{\mathrm{d}x}   \right]
\end{align}
$$

Then,

$$
\begin{align}
\braket{\psi|F(s)|\psi} &= -\frac{i\hbar}{2m} \left[ \int_{-\infty}^{\infty} \mathrm{d}x \,  \psi^*(x) \delta (x-s) \frac{\mathrm{d}}{\mathrm{d}x}\psi(x)  + \int_{-\infty}^{\infty} \mathrm{d}x \,  \psi^*(x) \frac{\mathrm{d}}{\mathrm{d}x}(\delta (x-s) \psi(x) ) \right] \\
&=  -\frac{i\hbar}{2m} \left[ \int_{-\infty}^{\infty} \mathrm{d}x \,  \psi^*(x) \delta (x-s) \frac{\mathrm{d}}{\mathrm{d}x}\psi(x)  - \int_{-\infty}^{\infty} \mathrm{d}x \,  \left(\frac{\mathrm{d}}{\mathrm{d}x} \psi^*(x) \right)\delta (x-s) \psi(x)  \right] \\
&= -\frac{i\hbar}{2m} \left[  \psi^*(s,t) \frac{\partial \psi(s,t)}{\partial s} - \frac{\partial \psi^*(s,t)}{\partial s} \psi(s,t) \right]
\end{align}
$$

$\braket{\psi|F(s)|\psi}$ satisfies following properties.

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{d}t}P_{ab} = \int_a^b \mathrm{d}x \, \frac{\partial}{\partial t} |\psi|^2 = \braket{\psi|F(a)|\psi} - \braket{\psi|F(b)|\psi}
\end{align}
$$

$$
\begin{align}
\frac{\partial}{\partial x} \braket{\psi|F(x)|\psi} = -\frac{\partial}{\partial t} |\psi(x,t)|^2
\end{align}
$$

Proof is not hard, so I’ll skip (cf. Griffiths Problem 1.14).

Therefore, physical meaning of $\braket{\psi|F(s)|\psi}$ is probability current. And, since $\ket{\psi_p}$ is eigenstate of Hamiltonian,

$$
\begin{align}
\frac{\partial}{\partial x} \braket{\psi_p|F(x)|\psi_p} &= -\frac{\partial}{\partial t} |\psi_p(x,t)|^2 \\
&= -\frac{\partial}{\partial t} |e^{-iHt/\hbar} \psi_p(x,0)|^2 \\
&= 0
\end{align}
$$

Therefore, $\braket{\psi|F(s)|\psi}$ intependent of $s$.

Now, let’s pick $s→\infty$, by Eq (13)

$$
\begin{align}
\braket{\psi|F(s)|\psi} &= \braket{p|F(s)|p} |T(E)|^2 \\
&= -\frac{i\hbar}{2m} \left[ \phi_p^*(s) \frac{\mathrm{d}}{\mathrm{d}s} \phi_p(s) - \phi_p(s) \frac{\mathrm{d}}{\mathrm{d}s} \psi_p^*(s) \right] |T(E)|^2 \\
&= -\frac{i\hbar}{2m} \frac{1}{2\pi\hbar} \left[  e^{-ips/\hbar}  \frac{\mathrm{d}}{\mathrm{d}s} e^{ips/\hbar} -  e^{ips/\hbar}  \frac{\mathrm{d}}{\mathrm{d}s} e^{-ips/\hbar}  \right] |T(E)|^2 \\
&= \frac{1}{2\pi\hbar} \frac{p}{m} |T(E)|^2
\end{align}
$$

<br>

## References

$^1$ D. J. Griffiths, and D. F. Schroeter, *Introduction to Quantum Mechanics*, Third edition (Cambridge University Press, Cambridge ; New York, NY, 2018).

$^2$ D. E. Manolopoulos, “Chemical Reaction Dynamics,” [David Manolopoulos Research Group: Chemical Dynamics](http://manolopoulos.chem.ox.ac.uk/) (2008).


<br>


---

2024.11.13 최예성 작성

2024.12.25 rev1


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