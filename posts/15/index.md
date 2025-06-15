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


# Density Matrix II

Density matrix III도 써야할 듯.

## 1. 서론

양자역학에서 ensemble이란 incoherent한 상태의 superposition이다. 우리는 [density matrix I](https://ysch0i.github.io/posts/12)에서 phase randomize (postulate of random phases)를 통해 ensemble을 만들 수 있다는 것을 알았다. 즉, 

$$
\begin{align}\ket{\psi} &= \sum_n c_n \ket{\phi_n}\end{align}
$$

에서 $\ket{\phi_n}$ 들을 dephasing 시켜 ensemble을 만든다. 여기서 $\ket{\phi_n}$는 Hamiltonian의 eigenstate이다. 


근데, 식 (1) 처럼만 쓰면 $\ket{\phi_n}$들이 coherent state인지, incoherent state 인지 알 방법이 없다. 일반적으로 식 (1) 같이 쓰면 $\ket{\phi_n}$들은 coherent state 이여서 $\ket{\psi}$는 coherent state 의 superposition이 된다. 따라서 ensemble을 명확히 표기하기 위해 density matrix를 이용한다.


<br>


## 1. Ensemble

우리의 목표는 state 1 $(\psi^{(1)})$, state 2 $(\psi^{(1)})$, ... state $N$ $(\psi^{(N)})$을 이용해 ensemble을 만드는 것이다. Ensemble average는 아래와 같이 표현된다.

$$\begin{align}
\braket{A} = \frac{1}{N} \sum_{\lambda = 1}^N \braket{\psi^{(\lambda)} | A | \psi^{(\lambda)}}\end{align}
$$

[Density matrix I](https://ysch0i.github.io/posts/12)의 식 (14)를 이용하면,

$$\begin{align}
\braket{A} =\frac{1}{N}\left[ \sum_n \braket{\varphi_n | A \hat{\rho}^{(1)} | \varphi_n} + \cdots + \sum_n \braket{\varphi_n | A \hat{\rho}^{(N)} | \varphi_n}   \right]\end{align}
$$

으로 표현할 수 있다. 여기서 

$$\begin{align}
\braket{\varphi_{n'} | \hat{\rho}^{(\lambda)} | \varphi_n} = (c^{(\lambda)}_n)^* c^{(\lambda)}_{n'}\end{align}
$$


$$
\begin{align}\ket{\psi^{(\lambda)}} = \sum_n c_n^{(\lambda)} \ket{\varphi_n}\end{align}
$$

이다. 이 때, 전체 density matrix를

$$\begin{align}
\hat{\rho} \stackrel{\text{def}}{=} \sum_{\lambda=1}^N \hat{\rho}^{(\lambda)}\end{align}
$$

로 정의하면, ensemble average는

$$\begin{align}
\braket{A} &= \frac{1}{N}\sum_n \braket{\varphi_n | A \sum_{\lambda=1}^N \hat{\rho}^{(\lambda)} | \varphi_n} \\
&= \frac{1}{N}\sum_n \braket{\varphi_n | A \hat{\rho} | \varphi_n} \\
&= \frac{1}{N}\text{Tr} \, \hat{\rho} A
\end{align}$$

로 표현할 수 있다. 이처럼 density matrix formalism 을 이용하면 각 state의 density matrix의 합으로 ensemble을 표현할 수 있다 (식 (6)). 

식 (6)을 조금 다른 방식으로 표현해보자. 식 (4)를 식 (6)에 대입하면,

$$\begin{align}
\hat{\rho} &= \sum_{\lambda = 1}^N \sum_{k,l} (c^{(\lambda)}_l)^* c^{(\lambda)}_{k} \ket{\varphi_k} \bra{\varphi_l} \\
&= \sum_{\lambda = 1}^N \ket{\psi^{(\lambda)}} \bra{\psi^{(\lambda)}}
\end{align}$$

를 얻는다. 따라서 $\hat{\rho}$가 hermitian임을 알 수 있다.


그 다음부터는 [Density matrix I](https://ysch0i.github.io/posts/12)와 똑같다. Density matrix가 hermitian 이므로 어떤 orthonomal basis set으로 대각화 할 수 있고, postulate of random phase를 통해 Hamiltonian의 eigenfuction을 basis set으로 사용할 수 있다. 

$$\begin{align}
\tilde{\rho} \stackrel{\text{def}}{=} \hat{\rho}/N = \sum_i w_i \ket{i}\bra{i} 
\end{align}$$

$$\begin{align}
\sum_i w_i = 1
\end{align}$$

$$\begin{align}
w_i \geq 0
\end{align}$$

or

$$\begin{align}
\tilde{\rho} = \sum_i |c_i|^2 \ket{\phi_n} \bra{\phi_n} 
\end{align}$$



<br>




## 2. Pure state

Ensemble과 구분짓기 위해 각 state $(\psi^{(\lambda)})$를 pure state라 한다. Ensemble과 pure state 모두 density matrix의 형태로 표현할 수 있다. 그러면 density matrix가 주어졌을 때, 이게 pure state인지 ensemble인지 어떻게 구별할까?

Pure state와 ensemble의 normalized density matrix $(\tilde{\rho}= \hat{\rho}/N)$를 살펴보자. 

Pure state의 경우 식 (11)을 이용하면, normalized density matrix는

$$\begin{align}
\tilde{\rho} = \ket{\psi} \bra{\psi}
\end{align}$$

로 쓸 수 있다. 따라서,

$$\begin{align}
\tilde{\rho}^2 = \ket{\psi} \braket{\psi | \psi} \bra{\psi} = \tilde{\rho}
\end{align}$$

가 성립한다. 그러나 ensemble의 경우 식 (17)이 성립하지 않는다. 증명은 간단하므로 생략하겠다. 따라서 식 (17)의 만족 여부를 통해 pure state인지 ensemble인지 구별할 수 있다.

간단한 예시를 살펴보자. 

$$\begin{align}
\ket{\psi^{(1)}} &= \frac{1}{\sqrt{2}} \ket{0} + \frac{1}{\sqrt{2}} \ket{1} \\
\ket{\psi^{(2)}} &= \frac{1}{\sqrt{2}} \ket{0} - \frac{1}{\sqrt{2}} \ket{1}
\end{align}$$

일 때,

$$\begin{align}
\tilde{\rho}^{(1)} &= \begin{bmatrix}
1/2 & 1/2 \\
1/2 & 1/2
\end{bmatrix} \\
\tilde{\rho}^{(2)} &= \begin{bmatrix}
1/2 & -1/2 \\
-1/2 & 1/2
\end{bmatrix} \\
\tilde{\rho} &= \begin{bmatrix}
1/2 & 0 \\
0 & 1/2
\end{bmatrix}
\end{align}$$

이므로 $(\tilde{\rho}^{(\lambda)})^2 = \tilde{\rho}^{(\lambda)}$ 이지만, $\tilde{\rho}^2 \neq \tilde{\rho}$ 이다.


<br>



## 3. Time evolution

Density matrix의 time evolution은 간단하지만 헷갈릴 만한 부분이 있어서 정리해보았다. 식 (11) 으로부터 $\hat{\rho}(t)$를 아래와 같이 정의한다.


$$\begin{align}
\hat{\rho}(t) &\stackrel{\text{def}}{=} \sum_{\lambda = 1}^N \ket{\psi^{(\lambda)}(t)} \bra{\psi^{(\lambda)}(t)} \\
&= \sum_{\lambda = 1}^N e^{-iHt/\hbar} \ket{\psi^{(\lambda)}} \bra{\psi^{(\lambda)}} e^{iHt/\hbar} \\
&= e^{-iHt/\hbar} \hat{\rho} e^{iHt/\hbar}

\end{align}$$

여기서, 아래와 같이 quantum Liouville operator를 정의하기도 한다.


$$\begin{align}
iL A \stackrel{\text{def}}{=} \frac{1}{i\hbar} [A, H]
\end{align}$$

이를 이용하면 식 (25)를

$$\begin{align}
\hat{\rho}(t) &= e^{-iHt/\hbar} \hat{\rho} e^{iHt/\hbar} \\
&= e^{-itL} \hat{\rho}

\end{align}$$

로 변형할 수 있다. 식 (28)의 증명은 어렵지 않으니 생략한다. 

일반적으로 Heisenberg picture에서 operator의 time evolution은

$$\begin{align}
A(t) = e^{iHt/\hbar} A e^{-iHt/\hbar}
\end{align}$$
로 표현된다. Density matrix의 time evolution 식 (27) 과 부호가 다름에 유의하자.



<br>



## References


<sup>1</sup> R. P. Feynman, *Statistical Mechanics: A Set of Lectures*, 19. printing (Addison-Wesley, Reading, Mass., 1996).



<sup>2</sup> M. E. Tuckerman, *Statistical Mechanics: Theory and Molecular Simulation*, 2nd ed (Oxford university press, Oxford, 2023).


<sup>3</sup> Y. Baek, "Statistical Mechanics: Lecture Notes" (2024).

<br>

---

2025.06.15 최예성 작성




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

