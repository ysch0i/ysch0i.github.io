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



# Born–Oppenheimer Approximation



최근 영화로 대중성이 생긴 Julius Robert Oppenheimer. 그가 박사학위를 받은 지 5개월 후, 지도교수 Max Born과 함께 발표한 Born–Oppenheimer approximation에 대해 알아보자. [원문](https://doi.org/10.1002%2Fandp.19273892002)을 읽어보진 못했다. 독일어라.

## 1. 결과



Born–Oppenheimer approximation은 total wavefunction (spatial part only)에서 전자의 wavefunction과 핵의 wavefunction을 분리하여 다룰 수 있다고 가정하는 것이다. 따라서 total wavefunction을 아래와 같이 쓸 수 있다.

$$
\begin{equation}\psi(r, R) = \chi(R)\,\phi(r; R)\end{equation}
$$

여기서 $\psi$ 는 total wavefunction, $\chi$, $\phi$ 는 각각 핵과 전자의 wavefunction이다. 이와 같은 분리가 가능한 이유는 핵이 전자에 비해 1000배 이상 무거워, 전자가 핵에 비해 훨씬 빠르게 움직이기 때문이다. 이런 상황에서 전자는 핵의 움직임에 즉각적으로 반응하고, 이로 인해 핵의 위치가 고정된 상태에서 전자의 움직임을 다룰 수 있다. 즉, 핵과 전자의 움직임을 나누어서 생각할 수 있다.

<br>

## 2. Hamiltonian



우리는 한 분자에 대한 spatial wavefunction을 보고 있다. 그 분자에 대한 Hamiltonian은 아래와 같이 표현된다. 상수는 쓰기 귀찮으니까 생략하자 (use atomic units).

$$
\begin{align}H &= T_\text{nuc}  + V_\text{nuc-nuc}  + V_\text{nuc-el} +T_\text{el}  + V_\text{el-el} \\&= -\frac{1}{2} \sum_{n} \frac{\nabla_n^2}{M_n} + \sum_{m<n} \frac{Z_mZ_n}{|R_m - R_n|} - \sum_{n, i} \frac{Z_n}{|R_n - r_i|}  - \frac{1}{2} \sum_{i} \nabla_i^2 + \sum_{i<j} \frac{1}{|r_i - r_j|} 
\end{align}
$$

<br>

## 3. 정성적 설명



1절에 이어 설명을 조금 덧붙여보자. 전자가 핵의 움직임에 즉각적으로 반응한다는 것은, 전자가 핵의 움직임을 자연스럽게 따라간다는 것이다. 따라서 핵의 좌표 (nuclear coordinates)가 조금 변화했을 때 전자의 wavefunction도 핵의 좌표를 따라 조금 변화해야 된다. 느꼈겠지만 “자연스럽게”, “조금”이라는 표현에는 모호함이 있다. 이런 모호함을 해결하기 위해 electronic states를 생각해보자.

“조금” 변하는 wavefunction을 상상하기 힘들다면, 반대로 급격하게 변하는 wavefunction을 상상해보자. Wavefunction이 급격하게 변하면 그 wavefunction이 가지는 물리량이 급격하게 변할 것이라고 예상할 수 있고, 이는 wavefunction의 state가 변했다고 생각할 수 있다 (전자-전이). 즉, wavefunction이 “자연스럽게”, “조금” 변화한다는 것은 wavefunction의 state가 바뀌지 않음을 의미한다. (내가 나중에 다룰지도 모르겠지만, 이렇게 핵의 좌표에 대해 즉각적이고 자연스럽게 반응하는 전자의 wavefunction을 basis로 사용하는 것을 adiabatic picture (regime) 라고도 한다.)

정리하자면 Born–Oppenheimer approximation (보다 엄밀하게는 adiabatic approximation)에서 가정하는 것은 **핵의 움직임이 전자-전이를 유발하지 않는다**는 것이다. 같은 맥락에서, 전자의 wavefunction이 급격하게 변하지 않으면서 핵의 움직임을 따라가므로 전자의 wavefunction을 staionary state라고 볼 수 있다. 다시 말해, 핵의 움직임에 비해 전자는 빠르게 평형에 도달한다. 따라서 고정된 핵 좌표 $R$ 에 대해 전자의 wavefunction을 구해도 된다.

$R=R_\text{fix}$ 로 고정한다면 식 (3)에서 $T_\text{nuc}$ 항이 사라진다. 이 때, 남은 Hamiltonian을 electronic Hamiltonian $(H_\text{el})$ 이라 하고, $H_\text{el}$ 의 eigenfunction을 전자의 wavefunction $(\phi)$ 이라 하자. 여기서 $H_\text{el}$ 은 고정된 핵의 좌표에 의존하고, $\phi$ 는 $r$ 에 대한 함수이자 $R_\text{fix}$ 에 의존하는 functional이므로 아래와 같이 표기한다. $R_\text{fix}$ 은 변수가 아닌 parameter이므로 $\phi$ 가 $R_\text{fix}$ 에 대한 함수가 아님에 유의하자.

$$
\begin{equation}H_\text{el} = H_\text{el}(R_\text{fix})\end{equation}
$$

$$
\begin{equation}\phi = \phi(r;R_\text{fix})\end{equation}
$$

그러면 전자에 대한 Schrödinger equation은 아래와 같이 표현된다 (time-independent).

$$
\begin{equation}H_\text{el} (R_\text{fix})\, \phi(r;R_\text{fix}) = E_\text{el}(R_\text{fix})\, \phi(r;R_\text{fix})\end{equation}
$$

where,

$$
\begin{equation}H_\text{el} (R_\text{fix})  = V_\text{nuc-nuc} +  V_\text{nuc-el} +T_\text{el}  + V_\text{el-el} \end{equation}
$$

이렇게 전자의 wavefunction과 $E_\text{el}(R_\text{fix})$ 을 얻을 수 있다. 여기서 $E_\text{el}$ 은 핵의 좌표 $R$ 에 대한 함수이고 전자는 핵에 비해 매우 빠르게 평형에 도달하므로, $E_\text{el}$ 은 핵이 느끼는 effective potential이 된다. 이를 potential energy surface (PES) 라고도 한다.

이제 다시 변수 $R$ 을 도입하여 핵의 움직임에 대해 생각해보자. 핵은 위에서 구한 PES 에서 움직이므로 핵에 대한 Schrödinger equation은 아래와 같이 표현된다 (time-independent).

$$
\begin{equation}[T_\text{nuc} + E_\text{el}(R)] \,\chi(R) = E\,\chi(R)\end{equation}
$$

끝으로, 식 (6)과 (8)에서 얻은 wavefunction의 곱이 total wavefunction이 된다.

$$
\begin{equation}\psi(r, R) = \chi(R)\,\phi(r; R)\end{equation}
$$

<br>


## 4. 정량적 설명



핵의 움직임이 전자 전이를 유발하지 않으므로, 서로 다른 electronic state 간의 coupling이 없어야 한다 ([Time-dependent Pertubation](https://ysch0i.github.io/posts/5) 참고). 이러한 조건이 어떻게 수식으로 표현되는지 알아보자.

우선 식 (6)으로 돌아가자. 식 (6)에서 얻은 전자의 wavefunction $\{ϕ(r;R)\}$ 은 electronic Hilbert space를 span하므로 total wavefunction을 아래와 같이 쓸 수 있다.

$$
\begin{align}
\psi(r, R) &= \sum_{a}\chi_a(R)\,\phi_a(r;R) \\
\ket{\psi} &= \sum_a \ket{\chi_a} \ket{\phi_a}
\end{align}
$$

여기서 $a$ 는 전자의 state를 의미한다. 이후 분자에 대한 Schrödinger equation을 풀어보자.

$$
\begin{equation}H\,\psi(r, R) = E\,\psi(r, R)\end{equation}
$$

$$
\begin{align}
 E\sum_a \ket{\chi_a} \ket{\phi_a} &= \left[ T_\text{nuc} + H_\text{el}(R)  \right]\,\sum_a \ket{\chi_a} \ket{\phi_a} \\
 &= \sum_a \left[  -\frac{1}{2}\sum_n \frac{1}{M_n}\nabla_n^2(\ket{\chi_a} \ket{\phi_a})  + E_{\text{el},a} \ket{\chi_a} \ket{\phi_a} \right]
\end{align}
$$

식 (14) 양변에 $\bra{\phi_b}$ 를 곱하면,

$$
\begin{align}
 E\ket{\chi_b} = E_{\text{el},b} \ket{\chi_b} + \sum_a -\frac{1}{2}\sum_n \frac{1}{M_n}\bra{\phi_b} \nabla_n^2(\ket{\chi_a} \ket{\phi_a})
\end{align}
$$

를 얻는다. 우변의 두 번째 항을 조금 더 풀어써보자.

$$
\begin{equation}
\nabla_n^2 \ket{\chi_a} \ket{\phi_a} = \ket{\phi_a} \nabla_n^2 \ket{\chi_a}  +2\,\nabla_n\ket{\chi_a}\nabla_n  \ket{\phi_a}  + \ket{\chi_a}\nabla_n^2  \ket{\phi_a}
\end{equation}
$$

이므로,

$$
\begin{align}
-\frac{1}{2}\sum_n \frac{1}{M_n}\bra{\phi_b} \nabla_n^2(\ket{\chi_a} \ket{\phi_a}) &= -\frac{1}{2} \sum_n \frac{1}{M_n} \left[ \delta_{ba} \nabla_n^2 \ket{\chi_a} + 2\braket{\phi_b|\nabla_n|\phi_a} \nabla_n \ket{\chi_a} + \braket{\phi_b|\nabla_n^2|\phi_a} \ket{\chi_a}  \right] \\
&= \delta_{ba} T_\text{nuc} \ket{\chi_a} -\frac{1}{2} \sum_n \frac{1}{M_n} \left[ 2\braket{\phi_b|\nabla_n|\phi_a} \nabla_n  + \braket{\phi_b|\nabla_n^2|\phi_a}   \right]\ket{\chi_a}
\end{align}
$$

를 얻는다. 여기서 다음과 같은 operator를 정의해보자.

$$
\begin{equation}
\Theta_{ba} \stackrel{\text{def}}{=} -\frac{1}{2} \sum_n \frac{1}{M_n} \left[ 2\braket{\phi_b|\nabla_n|\phi_a} \nabla_n  + \braket{\phi_b|\nabla_n^2|\phi_a}   \right]
\end{equation}
$$

이를 nonadiabaticity operator라 한다. Nonadiabaticity operator를 이용하면 식 (15)를 다음과 같이 간단히 표현할 수 있다.

$$
\begin{equation}
 E\ket{\chi_b} = E_{\text{el},b} \ket{\chi_b} + T_\text{nuc} \ket{\chi_b} + \Theta_{bb} \ket{\chi_b}+ \sum_{a\neq b} \Theta_{ba} \ket{\chi_a}
\end{equation}
$$

이항하여 정리하면,

$$
\begin{equation}\left[ T_\text{nuc} + \Theta_{bb} + E_{\text{el},b} - E\right] \chi_b(R)=- \sum_{a\neq b} \Theta_{ba} \,\chi_a(R)\end{equation}
$$

여기서 서로 다른 전자 state에 대한 nonadiabaticity operator $\Theta_{ba}$ 를 0으로 가정한다. 이것이 Born–Oppenheimer approximation이다. 그러면 핵에 대한 Schrödinger equation을 얻는다.

$$
\begin{equation}\left[ T_\text{nuc} + \Theta_{bb} + E_{\text{el},b} \right] \chi_b(R)=E\,\chi_b(R)\end{equation}
$$

따라서 하나의 전자 state $b\,$에 대한 전자 wavefunction $\phi_b(r;R)$ 과 핵 wavefunction $\chi_b(R)$ 의 곱은 전체 Schrödinger equation (12)를 만족하기 때문에 전체 wavefunction을 핵과 전자 wavefunction의 곱으로 표현할 수 있다.

$$
\begin{equation}\psi_b(r, R) = \chi_b(R)\,\phi_b(r; R)\end{equation}
$$

$$
\begin{equation}H\,\psi_b(r, R) = E\,\psi_b(r, R)\end{equation}
$$

또한, 서로 다른 전자 state에 대해 coupling이 없기 때문에 핵의 움직임이 전자 전이를 유발하지 않는다.

$$
\begin{equation}\Theta_{ab} \approx 0 \,\,\,\,\,\,\,\text{  if  } a\neq b\end{equation}
$$


<br>

## References



$^1$ V. May, and O. Kühn, *Charge and Energy Transfer Dynamics in Molecular Systems*, Fourth edition (Wiley-VCH, Weinheim, Germany, 2023).

<br>

---

2024.11.08 최예성 작성



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