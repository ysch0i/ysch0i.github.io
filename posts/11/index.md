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


# Marcus–Hush–Chidsey Theory


Marcus 이론의 전기화학 버전. 전기화학 교과서로 많이 사용되는 A. J. Bard (2022) 에서는 Gerischer Model 이라고 부른다.


## 1. Marcus 이론



Marcus 이론에서 전자전달 속도 상수는 아래와 같이 나타난다.

$$
\begin{align}	\displaystyle	k = \frac{2\pi|H_{if}|^2}{\hbar} \frac{1}{(4\pi\lambda k_\text{B}T)^{1/2}} \exp\left(-\frac{(\lambda+\Delta G^\circ)^2}{4\lambda k_\text{B}T}\right)\end{align}
$$

여기서 $H_{if}$는 초기 상태와 최종 상태의 전자 커플링, $\Delta G^\circ$는 전자전달 반응의 깁스 자유에너지 변화, $\lambda$는 재배열에너지이다.

<br>

## 2. 전기화학 시스템



식 (1) 은 두 화학종 간에 전자를 주고 받을 때 적용되는 수식이다. 

$$
\begin{align}
\ce{D} + \ce{A} \rightleftarrows \ce{D+} + \ce{A-}
\end{align}
$$

그러나 전기화학 시스템에서는 전극과 화학종 간에 전자를 주고받는다.

$$
\begin{align}
\text{O}_\text{(aq)} + ne^-_\text{(electrode)} \rightleftarrows \text{R}_\text{(aq)}
\end{align}
$$

이 때, 전극의 전자는 화학종과 달리 연속적인 에너지 분포를 가진다 (Fermi-Dirac 분포). 따라서 전자의 에너지에 따른 전자전달을 모두 고려해주어야 한다.

이해를 돕기 위해 일반적인 Marcus 이론의 PES를 살펴보자.

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/11/images/as.png" width="550px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">From R. A. Marcus (1965).</figcaption>
</figure>


이처럼 반응물 (왼쪽 PES), 생성물 (오른쪽 PES)에 해당하는 PES가 한개씩 존재하고, 전자전달 속도는 식 (1)로 표현된다.

그러나 전기화학 반응에서의 PES는 아래와 같이 바뀐다.

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/11/images/asdf.png" width="550px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">From Y. Zeng (2014).</figcaption>
</figure>




전자의 에너지가 연속적이기 때문에 반응물 $(\text{O}_\text{(aq)} + ne^-_\text{(electrode)})$ 에 해당하는 왼쪽 PES가 연속적으로 나타난다. 따라서 각각의 반응물 PES에 대해 $\Delta G^\ddagger$가 달라져 속도상수가 달라지므로 이를 평균해주어야 한다.

이 때, 전자의 에너지에 따라 재배열에너지는 바뀌지 않는다고 가정한다 (PES가 위아래로 평행이동 한다고 가정).

<br>

## 3. Notation


Potential of an Electrode 글에서 우리는 퍼텐셜을 아래와 같이 정의했었다.

$$
\begin{align}E \left( \text{vs} \,\,E_\text{ref}\right) &= -\frac{\overline{\mu}_\text{e}-\overline{\mu}_\text{e}^\text{ref}}{F} \\&= -\frac{\mathbf{E_F}-\mathbf{E_F}^\text{ref}}{e}\end{align}
$$

또한, 반응의 자유에너지 변화를

$$
\begin{align}\Delta_\text{rxn} G^0_\text{mol} &= nF\left(E - E^0\right)\end{align}
$$

로 나타낼 수 있었다.

앞으로 몰당 자유에너지가 아니라 입자당 자유에너지를 사용하자. 그럼 식 (5), (6) 으로부터

$$
\begin{align}\Delta_\text{rxn} G^0 &= -n\left(\mathbf{E_F} - \mathbf{E_F^0}\right)\end{align}
$$

를 얻는다. 

이는 전자의 에너지가 $\mathbf{E_F}$ 일 때의 자유에너지 변화이다. 그럼 만약 전자의 에너지가 $\mathbf{E}$ 라면 자유에너지 변화는

$$
\begin{align}\Delta_\text{rxn} G^0 \left(\mathbf{E}\right) &= -n\left(\mathbf{E} - \mathbf{E_F^0}\right)\end{align}
$$

로 표현된다.


<br>

## 4. Marcus–Hush–Chidsey 이론


$n=1$ 인 상황을 보도록 하자. 식 (1), (8) 에 의해 전기화학 시스템에서 에너지가 $\mathbf{E}$ 인 전자가 전이될 때 전자전달 속도 상수는

$$
\begin{align}    \displaystyle    k(\mathbf{E}) = \frac{2\pi|H_{if}(\mathbf{E})|^2}{\hbar} \frac{1}{(4\pi\lambda k_\text{B}T)^{1/2}} \exp\left(-\frac{(\mathbf{E} - \mathbf{E^0_F}-\lambda)^2}{4\lambda k_\text{B}T}\right)\end{align}
$$

로 나타난다. 이 때, 전자가 각 에너지 준위를 점유할 확률은 Fermi-Dirac 분포를 따른다. 

$$
\begin{align}\overline{n}_\mathbf{E}^\text{FD} = \frac{1}{1+\exp((\mathbf{E}-\mathbf{E_F})/k_\text{B}T)}
\end{align}
$$

따라서 전체 속도 상수는

$$
\begin{align}    k &= \int_{-\infty}^{\infty} \mathrm{d}\mathbf{E} \,  \frac{k(\mathbf{E})}{1+\exp((\mathbf{E}-\mathbf{E_F})/k_\text{B}T)} \\    &= \frac{2\pi/\hbar}{(4\pi\lambda k_\text{B}T)^{1/2}} \int_{-\infty}^{\infty} \mathrm{d}\mathbf{E} \,   \frac{|H_{if}(\mathbf{E})|^2}{1+\exp((\mathbf{E}-\mathbf{E_F})/k_\text{B}T)}\exp\left(-\frac{(\mathbf{E} - \mathbf{E^0_F}-\lambda)^2}{4\lambda k_\text{B}T}\right)\end{align}
$$

가 된다. 여기서 $H_{if}(\mathbf{E})$ 가 $\mathbf{E}$ 에 무관하다고 가정하자. 

(아니 근데 이 가정이 말이 됨? 그리고 Density of State는 어디감? 정말 엄청난 근사를 한 식이지만, 뭐 지금 나오는 논문들이 다 이 식을 쓰는데.... 쩔 수 있나.) 

그리고, $k^\infty \equiv 2\pi|H_{if}|^2/\hbar$ 로 정의하면

$$
\begin{align}    k &= \frac{k^\infty}{(4\pi\lambda k_\text{B}T)^{1/2}} \int_{-\infty}^{\infty} \mathrm{d}\mathbf{E} \,   \frac{1}{1+\exp((\mathbf{E}-\mathbf{E_F})/k_\text{B}T)}\exp\left(-\frac{(\mathbf{E} - \mathbf{E^0_F}-\lambda)^2}{4\lambda k_\text{B}T}\right) \\    &= \frac{k^\infty}{(4\pi\lambda k_\text{B}T)^{1/2}}  \int_{-\infty}^{\infty} \mathrm{d}z \, \frac{1}{1+\exp( z/k_\text{B}T)} \exp\left(-\frac{(z+\mathbf{E_F} - \mathbf{E^0_F}-\lambda)^2}{4\lambda k_\text{B}T}\right) \\\end{align}
$$

여기서 

$$
\begin{align}\mathbf{E_F} - \mathbf{E^0_F} &= \left(\mathbf{E_F}-\mathbf{E_F}^\text{ref}\right) - \left(\mathbf{E_F^0}-\mathbf{E_F}^\text{ref}\right) \\&= -e\left(E - E^0  \right) \\&= -e\eta\end{align}
$$

이므로

$$
\begin{align}    k &=  \frac{k^\infty}{(4\pi\lambda k_\text{B}T)^{1/2}}  \int_{-\infty}^{\infty} \mathrm{d}z \, \frac{1}{1+\exp( z/k_\text{B}T)} \exp\left(-\frac{(z-\lambda -e\eta)^2}{4\lambda k_\text{B}T}\right) \\    &= \frac{k^\infty}{(4\pi\lambda k_\text{B}T)^{1/2}}  \int_{-\infty}^{\infty} \mathrm{d}z \, \frac{1}{1+\exp( z/k_\text{B}T)} \exp\left(-\frac{(z-\lambda - e\eta)^2}{4\lambda k_\text{B}T}\right) \end{align}
$$

를 얻는다. 여기서 $\eta$ 는 과전압이다.

이렇게 우리는 전기화학 시스템에서의 속도 상수를 식 (19)로 얻을 수 있다. 식을 통해 알 수 있듯이 속도 상수는 과전압 $\eta$, $k^\infty (= k(\eta = -\infty))$, 재배열에너지 $\lambda$ 의 함수이다.


<br>

## 4. 도식화


뭐 여기까지만 해도 상관없지만 재미를 위해 식 (19)를 도식화 해보기로 하자. 

확산에 의한 전류는 무시하기로 하고, 전극 표면에서 $\ce{O}$ 와 $\ce{R}$ 의 농도가 같다고 가정하자. 그럼 전류는

$$
\begin{align}
i(\eta) = FAC\left[ k_\text{ox}(\eta) - k_\text{red}(\eta)  \right]
\end{align}
$$

로 표현된다. 여기서 $F$는 패더레이 상수, $A$는 전극의 표면적, $C$는 전극 표면에서 화학종의 농도이다. 

$k$를 표현할 때 Butler-Volmer model을 사용한 경우와 Marcus–Hush–Chidsey 이론을 사용한 경우를 비교해보자.

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/11/images/mhc_fit.png" width="550px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">내가 Matlab으로 계산함.</figcaption>
</figure>


오 C. E. D. Chidsey (1991) 에서 봤던 그림이랑 똑같다..!!!

Butler-Volmer model을 사용하면 과전압이 커질 때 전류의 크기가 발산하지만, Marcus–Hush–Chidsey 이론을 사용하면 과전압이 커질 때 전류의 크기가 수렴함을 볼 수 있다.

또한, Marcus–Hush–Chidsey 이론에서는 Marcus inverted region이 나타나지 않는다.

<br>

## References



$^1$ R. A. Marcus, “On the Theory of Electron‐Transfer Reactions. VI. Unified Treatment for Homogeneous and Electrode Reactions,” [J. Chem. Phys.](https://doi.org/10.1063/1.1696792) **43**, 679–701 (1965).

$^2$ C. E. D. Chidsey, “Free Energy and Temperature Dependence of Electron Transfer at the Metal-Electrolyte Interface,” [Science](https://doi.org/10.1126/science.251.4996.919) **251**, 919–922 (1991).

$^3$ Y. Zeng, R. B. Smith, P. Bai, and M. Z. Bazant, “Simple formula for Marcus–Hush–Chidsey kinetics,” [J. Electroanal. Chem.](https://doi.org/10.1016/j.jelechem.2014.09.038) **735**, 77–83 (2014).

$^4$ A. J. Bard, L. R. Faulkner, and H. S. White, *Electrochemical Methods: Fundamentals and Applications*, Third edition (Wiley, Hoboken, NJ, USA Chichester, West Sussex, UK, 2022).


<br>


---

2024.12.23 최예성 작성

<footer class="site-footer"></footer>


</div>