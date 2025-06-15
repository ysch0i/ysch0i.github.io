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


# Density Matrix



여러분이 알고 있는 그 density matrix 가 맞나??

## 1. Partition Function



통계역학을 공부하면서 이런 말을 들어본 적 있을 것이다.

"시스템의 partition function을 안다면 시스템의 모든 거시적 성질을 아는 것이다.”

그래서 통계역학 문제를 풀 때 가장 먼저 하는 일은 partition function을 구하는 일이다.

먼저 partition function을 구하고, connection to thermodynamics을 이용해 thermodynamic potential을 구하고, potential을 편미분하여 원하는 물리량을 구한다. 이게 통계역학 문제를 푸는 일반적인 방법이다.

예를 들어, 단원자 이상기체의 압력을 구하고 싶다고 하자.

먼저, 어떤 ensemble을 사용할 지 결정한다. 무난하게 canonical ensemble $(N,V,T)$ 를 사용하자. 아 그리고 고전역학을 사용해서 문제를 풀자. Partition function의 중요성을 얘기하는 부분이므로 자세한 계산은 생략한다.

Partiton function은

$$
\begin{align}Z &= \frac{1}{h^{3N}N!} \int \mathrm{d}\mathbf{r}^N\,\mathrm{d}\mathbf{p}^N \, e^{-\beta H(\mathbf{r}^N,\mathbf{p}^N)} \\&= \frac{V^N}{h^{3N}N!} \left( \frac{2\pi m}{\beta}  \right)^{3/2}

\end{align}
$$

로 나타난다. 그럼 canonical ensemble의 thermodynamic potential인 Helmholtz free energy $F$ 는 

$$
\begin{align}F &= -k_\text{B}T \ln Z \\&= k_\text{B}T \ln N! - Nk_\text{B}T\ln\left[ V \left(\frac{2\pi m k_\text{B}T}{h^2} \right)^{3/2}  \right]

\end{align}
$$

로 나타난다. 마지막으로 $F$ 를 $V$ 로 편미분하여 압력을 구한다.

$$
\begin{align}P = -\left( \frac{\partial F}{\partial V} \right)_{N,T}= \frac{Nk_\text{B}T}{V}\end{align}
$$

<br>

## 2. Density Matrix and Operator



Density matrix는 양자 통계역학에서 partition function과 같은 역할을 한다. 즉, 시스템의 density matrix를 알고 있다면 시스템에 대한 모든 걸 아는 것이다. 

조금 더 엄밀하게 말하면, 양자 통계역학에서는 parition function을 아는 것만으로는 충분하지 않다. 시스템의 density matrix는 partition function 보다 더 많은 정보를 가지고 있다. 그 내용을 한번 알아보자. 

전체 System은 Hamiltonian eigenstate $\phi_n$ 의 superposition으로 표현할 수 있다.

$$
\begin{align}\psi &= \sum_n \ket{\phi_n} \braket{\phi_n \,| \,\psi} \\&= \sum_n c_n \ket{\phi_n}\end{align}
$$

그리고 어떤 물리량 $A$ 의 expectation value를 구해보자.

$$
\begin{align}
\braket{\psi | A | \psi} &= \sum_{n,n'} c_n^* c_{n'} \braket{\phi_n | A | \phi_{n'}} 
\end{align}
$$

여기서 density matrix가 아래와 같이 정의된다.

$$
\begin{align}
\rho_{n'n} \stackrel{\text{def}}{=} c_n^* c_{n'}
\end{align}
$$

또한, density matrix를 이용해 density operator $\hat{\rho}$ 역시 정의할 수 있다. Density operator는 아래와 같은 조건을 만족시키도록 정의한다.

$$
\begin{align}
\braket{\phi_{n'} | \hat{\rho} | \phi_n} \stackrel{\text{def}}{=} \rho_{n'n}
\end{align}
$$

그럼 $A$ 의 expectation value를 조금 더 간단하게 나타낼 수 있다.

$$
\begin{align}
\braket{\psi | A | \psi} &= \sum_{n,n'}\braket{\phi_n | A | \phi_{n'}} \rho_{n'n} \\&= \sum_{n,n'}\braket{\phi_n | A | \phi_{n'}} \braket{\phi_{n'} | \hat{\rho} | \phi_n} \\&= \sum_{n}\braket{\phi_n | A \sum_{n'}|  \phi_{n'}} \braket{\phi_{n'} | \hat{\rho} | \phi_n} \\&= \sum_n \braket{\phi_n |A\hat{\rho} | \phi_n} \\&= \text{Tr}\, \rho A

\end{align}
$$

여기서 trace란 임의의 complete basis set $\left\{ \chi_k \right\}$ 에 대해 다음을 의미한다.

$$
\begin{align}

\text{Tr} \,O = \begin{cases}\displaystyle    \sum_k \braket{\chi_k | O | \chi_k} &  \text{for discrete basis}\\ \displaystyle    \int \mathrm{d}k  \braket{\chi_k | O | \chi_k}  & \text{for continuous basis}  \end{cases}
\end{align}
$$

여담이지만, trace는 교환이 성립하기 때문에 trace 값은 basis에 의존하지 않는다. 

$$
\begin{align}
\text{Tr } \left[ U^\dagger A U \right] = \text{Tr } \left[A U U^\dagger \right] = \text{Tr }A
\end{align}
$$

Density matrix와 density operator는 각각 식 (9), (10) 으로 정의되지만, 저 형태로는 잘 쓰이지 않는다. 식을 조금 변형해보자.

식 (9)를 보면 density matrix가 hermitian임을 알 수 있다.

$$
\begin{align}
\rho_{n'n}^* &= \left(c_n^* c_{n'}\right)^* \\&= c_n c_{n'}^* \\&= \rho_{nn'}
\end{align}
$$

따라서 어떤 complete orthonormal basis set $\left\{ \ket{i} \right\}$ 과 실수 eigenvalue $\left\{ w_i \right\}$ 를 이용해 density matrix를 대각화 할 수 있다.

$$
\begin{align}
\hat{\rho} = \sum_i w_i \ket{i} \bra{i}
\end{align}
$$

그럼 신기한 성질을 2가지 얻는데, 식 (15)에서 $A = 1$ 이라면

$$
\begin{align}
\text{Tr } \rho = \sum_i w_i = \braket{\psi|\psi} = 1
\end{align}
$$

을 얻고, $A = \ket{i'} \bra{i'}$ 이라면

$$
\begin{align}
\text{Tr } \rho A &= w_{i'} \\&= \braket{\psi | i'} \braket{i' | \psi} = |\braket{i' | \psi}|^2 \geq 0
\end{align}
$$

얻는다. 즉, $\displaystyle \sum_i w_i = 1$, $w_{i} \geq 0$ 이므로 $w_i$를 system이 $\ket{i}$ state에 있을 확률이라고 해석할 수 있다.

<br>

## 3. 양자 통계역학



이제 양자 통계역학에서 ensemble을 만드는 방법에 대해 알아보자. (이렇게 해도 되나.. 싶다.) 앞에서 얻은 $w_i$가 system이  $\ket{i}$ state에 있을 확률이라는 사실을 이용한다.

고전적인 통계역학에서도 그렇듯이 일반적으로 ensemble을 만들 때는 system의 각 state를 Hamiltonian의 eigenstate로 잡는다. 

$$
\begin{align}\psi &= \sum_n c_n \ket{\phi_n}\end{align}
$$

여기서 $|c_n|^2$은 system이 $\ket{\phi_n}$ state에 존재할 확률이므로, 뭔가 $w_i$와 연관될 것 같은 느낌이 든다. 만약 density operator가

$$
\begin{align}
\hat{\rho} = \sum_n |c_n|^2 \ket{\phi_n} \bra{\phi_n}
\end{align}
$$

으로 표현될 수 있다면 둘 사이의 관계가 명확해질 것이다. 또한, ensemble을 만들기도 용이하다.

Density operator를 식 (26)으로 표현하기 위해서는 energy eigenstate가 density matrix를 대각화시킬 수 있어야 한다. 다시말해, 식 (9)에서 

$$
\begin{align}\rho_{n'n} = c_n^* c_{n'} = 0 \text{    if } n \neq n'\end{align}
$$

이어야 한다. 여기서 약간 tricky한게 들어오는데.. 먼저, 양자 통계역학에서는 (비록 microcanonical ensemble 일지라도) 시스템이 완전히 고립되어 있지 않다고 가정한다. 즉, 아주 작은 pertubation이 항상 존재하고, 그 pertubation에 의해 energy eigenstate의 phase가 교란된다. 두 번째로, 어떤 물리량을 측정할 때에는 energy eigenstate의 phase가 회전하는 time-scale보다 긴 시간이 필요하다고 가정한다. 

설명을 더 명확히 하기 위해 수식을 사용해보자. 위에서 말한 phase란 아래와 같다.

$$
\begin{align}
\ket{\phi_n(t)} = e^{-iE_nt/\hbar}\ket{\phi_n(0)}
\end{align}
$$

$$
\begin{align}
\therefore c_n(t) = e^{-iE_nt/\hbar} c_n(0)
\end{align}
$$

그리고, 측정에는 시간이 필요하므로 식 (27) 보다 대각화의 조건이 완화된다.

$$
\begin{align}\rho_{n'n} &= \overline{c_n^* c_{n'}} \\&= \overline{c_n^*(0) c_{n'}(0)} \cdot \overline{e^{-i(E_{n'} - E_n)t/\hbar}} \end{align}
$$

여기서 pertubation에 의해 phase가 randomized 되므로 $E_n = E_{n'}$ 이더라도 $\rho_{n'n} = 0$ 이 된다. 즉, energy eigenstate가 density matrix를 대각화시킨다.

그럼 이제 식 (26)을 사용하여 여러 ensemble을 정의할 수 있다.

Microcanonical ensemble은 모든 state를 발견할 확률이 같으므로 density operator는 

$$
\begin{align}\hat{\rho}_E \stackrel{\text{def}}{=} \sum_{E\leq E_n \leq E+\delta E} \ket{\phi_n} \bra{\phi_n}\end{align}
$$

로 정의된다. 식 (22)와 달리 양자 통계역학에서는 주로 density operator를 nomalization 시키지 않는다. 대신, density operator의 trace가 partition function과 같아진다. 이를 통해 density operator가 partition function보다 많은 정보를 갖고 있음을 알 수 있다.

$$
\begin{align}\text{Tr }\hat{\rho}_E = \Omega (E)\end{align}
$$

다음으로 canonical ensemble을 만들어보자. Canonical ensemble에서 system이 에너지가 $E_n$인 state에 있을 확률은 $e^{-\beta E_n}$에 비례하므로

$$
\begin{align}\hat{\rho}_\beta &\stackrel{\text{def}}{=} \sum_{n} e^{-\beta E_n}\ket{\phi_n} \bra{\phi_n} \\&= \sum_{n} e^{-\beta H}\ket{\phi_n} \bra{\phi_n} \\&= e^{-\beta H}\sum_{n} \ket{\phi_n} \bra{\phi_n} \\&= e^{-\beta H}\end{align}
$$

로 density operator가 정의된다. 마찬가지로, density operator의 trace가 partition function이 된다.

$$
\begin{align}\text{Tr }\hat{\rho}_\beta = Z(T)\end{align}
$$

이외에도 density matrix에 대해 더 할말이 많다. 이 글은 여기서 멈추고 density matrix II를 만들어야겠다.

<br>

## 4. Hartree-Fock



그래도 여긴 화학부라, 많은 분들이 density matrix를 RHF Hartree-Fock의 Roothann Equation에서 처음 접했을 것이다.

Hartree-Fock equation의 eigenstate의 spatial part를 $\ket{\psi_a}$라 하자. LCAO를 이용해 계산을 한다면 $\ket{\psi_a}$를 Atomic orbital $\ket{\chi_\nu}$ 의 선형결합으로 표현한다.

$$
\begin{align}\ket{\psi_a} = \sum_\nu C_{\nu a} \ket{\chi_\nu}\end{align}
$$

이때, density matrix는 아래와 같이 정의된다.

$$
\begin{align}P_{\mu\nu} \stackrel{\text{def}}{=} 2 \sum_a^{N/2} C_{\mu a} C_{\nu a}^*\end{align}
$$

다시 우리가 정의한 density matrix를 보자. Density operator가 

$$
\begin{align}
\hat{\rho} = \sum_i w_i \ket{i} \bra{i}
\end{align}
$$

로 주어진다면, 임의의 orthonormal basis $\left\{ \ket{v_n} \right\}$에 대한 density matrix는

$$
\begin{align}
\rho_{mn} = \sum_i w_i \braket{v_m| i} \braket{i|v_n}
\end{align}
$$

로 나타난다. 이 때, 

$$
\begin{align}
\ket{i} &= \sum_n \ket{v_n} \braket{v_n|i} \\&\stackrel{\text{def}}{=} \sum_n C_{ni} \ket{v_n}
\end{align}
$$

이라 하면,

$$
\begin{align}
\rho_{mn} = \sum_i w_i C_{mi} C_{ni}^*
\end{align}
$$

를 얻는다.

식 (40)이랑 식 (45)가 뭔가 비슷하지 않나? 아님 말고.

<br>

## References



$^1$ R. P. Feynman, *Statistical Mechanics: A Set of Lectures*, 19. printing (Addison-Wesley, Reading, Mass., 1996).

$^2$ R. P. Feynman, A. R. Hibbs, and D. F. Styer, *Quantum Mechanics and Path Integrals*, Emended ed (Dover publ, Mineola, 2010).

$^3$ Y. Baek, "Statistical Mechanics: Lecture Notes" (2024).

$^4$ Y. Jung, "Applied Computational Chemistry: Lecture Notes" (2023).

<br>

---

2024.12.26 최예성 작성.

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