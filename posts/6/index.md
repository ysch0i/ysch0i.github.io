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





# Fermi’s Golden Rule I


계속 튀어나오는 Fermi’s golden rule. 근데 $V(t)$ 가 작을 때 밖에 못쓴다.


## 1. Situation



해밀토니안이 $H=H_0+V(t)$ 로 표현될 때, $V(t)$가 아래와 같이 변화하는 상황을 가정하자.

- case 1 : $V(t)=VH(t)$
- case 2 : $V(t)=V\cos(\omega t)H(t)$

여기서 $H(t)$는 Heaviside step function이다.

$$
\begin{equation}
H(t) \stackrel{\text{def}}{=} \begin{cases}
    1\hphantom{-\sqrt{-}} & \text{if } t\geq 0,\\
    0 & \text{if } t <0,
  \end{cases}
\end{equation}
$$

위의 두가지 case에서 pertubation $V(t)$ 에 의해 전자가 전이될 때 transfer rate $k$ 에 대해 알아보자.

<br>

## 2. General Formulation


임의의 state는 $H_0$ 의 eigenstate의 superposition으로 나타낼 수 있다.

$$
\begin{equation}
\ket{\psi(x,0)} = \sum_ic_i\ket{\phi_i}
\end{equation}
$$

Pertubation이 없을 때, 시간에 따라 $\psi$는

$$
\begin{equation}
\ket{\psi(x,t)} = \sum_ic_ie^{-iE_it/\hbar}\ket{\phi_i}
\end{equation}
$$

로 변화한다. 그러나, pertubation이 있다면 $c$는 시간에 따라 변화한다.

$$
\begin{align}
\ket{\psi(x,t)} &= \sum_ic_i(t)e^{-iE_it/\hbar}\ket{\phi_i} \\
&= \sum_ic_i(t)e^{-i\omega_it}\ket{\phi_i}
\end{align}
$$

1st order (time-dependent) pertubation theory에 의해 $c(t)$는

$$
\begin{equation}
\frac{\partial c_k(t)}{\partial t} = -\frac{i}{\hbar}\sum_ic_i^{(0)}(t)e^{-i\omega_{ik}t}V_{ki}(t)
\end{equation}
$$

로 표현된다. 여기서 $\omega_{ik}=\omega_i−\omega_k$, $V_{ki}(t) = \braket{\phi_k|V(t)|\phi_i}=\braket{k|V(t)|i}$ 이다.

만약, $t=0$ 에서 전자가 $l$ state에만 존재한다면 $c(t)$ 는 더욱 간단해진다.

$$
\begin{equation}
\frac{\partial c_k(t)}{\partial t}  = -\frac{i}{\hbar}e^{-i\omega_{lk}t}V_{kl}(t)
\end{equation}
$$

$$
\begin{equation}
c_k(t) = -\frac{i}{\hbar} \int_{-\infty}^t \mathrm{d} t' \,e^{-i\omega_{lk}t'}V_{kl}(t')
\end{equation}
$$

또한, 우리가 구하고자 하는 transfer rate $(k_{l\rightarrow k})$ 는 $c_k(t)$ 로부터 얻을 수 있다.

$$
\begin{equation}
k_{l \rightarrow k} = \frac{\partial P_k}{\partial t} = \frac{\partial}{\partial t} |c_k(t)|^2
\end{equation}
$$

<br>

## 3. Case 1


이제 계산만 하면 된다. $V(t)=VH(t)$일 때,

$$
\begin{align}
c_k(t) &= -\frac{i}{\hbar} \int_{-\infty}^t \mathrm{d} t' \,e^{-i\omega_{lk}t'}V_{kl}(t') \\
&= -\frac{i}{\hbar}V_{kl}\int_0^t \mathrm{d}t' \, e^{-i\omega_{lk}t'} \\
&= -\frac{i}{\hbar}V_{kl} \frac{e^{i\omega_{kl}t}-1}{\omega_{kl}} \\
&= -\frac{it}{\hbar}V_{kl}e^{i\omega_{kl}t/2}\text{sinc}\left( \frac{\omega_{kl}t}{2}\right)
\end{align}
$$

이다. 여기서 $\text{sinc}(x)=\sin(x)/x$ 이다.

따라서 $k$는 아래와 같이 나타난다.

$$
\begin{align}
P_k(t) = |c_k(t)|^2 &= \frac{|V_{kl}|^2}{\hbar^2}t^2\text{sinc}^2\left(\frac{\omega_{kl}t}{2}\right) \\
&= \frac{2\pi|V_{kl}|^2}{\hbar^2}t\delta(\omega_{kl})
\end{align}
$$

$$
\begin{align}
k = \frac{\partial P_k}{\partial t} = \frac{2\pi}{\hbar^2}|V_{kl}|^2 \delta(\omega_k - \omega_l) = \frac{2\pi}{\hbar}|V_{kl}|^2 \delta(E_k - E_l)
\end{align}
$$

where, $δ(x)$ is Dirac delta function. 이를 Fermi’s golden rule이라 한다.

<br>

## 4. Case 2


여기도 열심히 계산을 해보자. $V(t)=V\cos(\omega t)H(t)$일 때,

$$
\begin{equation}
\cos (\omega t) = \frac{e^{i\omega t} + e^{-i\omega t}}{2}
\end{equation}
$$

이므로,

$$
\begin{align}
c_k(t) &= -\frac{i}{2\hbar}V_{kl}\int_0^t \mathrm{d}t' \, e^{-i(\omega_{lk}+\omega)t'} + e^{-i(\omega_{lk}-\omega)t'} \\
&= -\frac{it}{2\hbar}V_{kl}\left[e^{i(\omega_{kl}+\omega)t/2}\text{sinc}\left( \frac{(\omega_{kl}+\omega)t}{2}\right) + e^{i(\omega_{kl}-\omega)t/2}\text{sinc}\left( \frac{(\omega_{kl}-\omega)t}{2}\right)\right]
\end{align}
$$

가 된다. 따라서 $k$는 아래와 같이 나타난다.

$$
\begin{align}
P_k(t) = |c_k(t)|^2 = \frac{\pi|V_{kl}|^2}{\hbar^2}t\left[\delta(\omega_{kl}+\omega) + \delta(\omega_{kl}-\omega)\right]
\end{align}
$$

$$
\begin{align}
k = \frac{\pi}{\hbar}|V_{kl}|^2 \left[\delta(E + E_{kl}) + \delta(E - E_{kl})\right]
\end{align}
$$

만약, $E_k>E_l$ 이라면, $\delta (E−E_{kl})$ 는 absorption을 의미하고, $\delta (E+E_{kl})$는 stimulated emission을 의미한다.

<br>

## References



$^1$ D. J. Griffiths, and D. F. Schroeter, *Introduction to Quantum Mechanics*, Third edition (Cambridge University Press, Cambridge ; New York, NY, 2018).

$^2$ A. Tokmakoff, *Time Dependent Quantum Mechanics and Spectroscopy* (2024).

<br>

---

2024.11.06 최예성 작성

<footer class="site-footer"></footer>


</div>