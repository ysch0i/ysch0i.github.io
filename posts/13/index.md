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


# Marcus Theory Formalism



여기서 말하고 싶은 것은 Marcus 이론, 더 넓게는 전자전달 이론이 사용하는 일반적인 형식이다. Marcus 이론의 물리적 의미, 해석, 유도는 다른 글에서 다룬다.

## 1. Potential Energy Surface



우리는 화학을 배울 때 아래 그림과 같은 potential energy surface (PES) 를 자주 접한다.

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/13/images/as.png" width="550px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">From R. A. Marcus (1965).</figcaption>
</figure>


근데 여기서 $x$축과 $y$축이 정확히 뭘까? 우리는 대략적으로만 알고 있다. $x$축은 reaction coordinate 이고, $y$축은 free energy 이다.

그러나 그것만으로는 부족하다. 실험 또는 계산을 해서 PES를 그리고, PES로부터 원하는 물리량을 끄집어 내기 위해서는 조금 더 정량적인 정의가 필요하다.

<br>

## 2. Energy Gap Coordinate



모두들 화학 1을 공부할 때 $\ce{NaCl}$이 형성되는 과정의 PES를 본 적이 있을 것이다. 

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/13/images/1.png" width="550px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">From 완자 화학 I.</figcaption>
</figure>



이때 사용한 reaction coordinate $\xi$ 은 두 입자 사이의 거리 $R$ 이다. 

$$
\begin{align}\xi = R = |\mathbf{r}_\text{Na} -\mathbf{r}_\text{Cl}| \end{align}
$$

이처럼 우리는 시스템의 각 입자의 Cartesian coordinate을 통해 reaction coordinate을 정의할 수 있었다.

복잡한 시스템이라고 다를 건 없다. 시스템이 $N$개의 핵을 포함한 경우 다음과 같이 Cartesian coordinate의 함수로 reaction coordinate을 정의한다.

$$
\begin{align}\xi_\alpha = f_\alpha(\mathbf{r}^N) \,\, (\alpha = 1, 2, \cdots)\end{align}
$$

여기서 $\alpha$가 붙은 이유는 reaction coordinate을 다차원으로 잡을 수도 있기 때문이다. 이제 우리가 해야할 것은 반응을 편리하게 기술할 수 있는 적절한 $f$를 찾는 것이다.

$f$를 정하는 방법은 수 없이 많지만, 전자전달 이론에서는 일반적으로 아래와 같이 정의되는 energy gap coordinate을 사용한다.

$$
\begin{align}\xi \stackrel{\text{def}}{=} \Delta E (\mathbf{r}^N) = E_\text{product} (\mathbf{r}^N) - E_\text{reactant}(\mathbf{r}^N)\end{align}
$$

즉, nuclear coordinate가 동일할 때 생성물과 반응물의 에너지 차이인 vertical energy gap을 reaction coordinate으로 정의하는 것이다.

<br>

## 3. Free Energy



이제 $y$축을 어떻게 정의하는지 알아보자. 

화학반응을 기술할 때 canonical ensemble $(N,V,T)$ 을 많이 사용하므로, 우리가 자연스럽게 떠올릴 수 있는 free energy는 Helmholtz free energy $F$ 이다. (Gibbs 미안..)

Helmholtz free energy를 구하려면 일단 partition function $Z$ 부터 구해야 하니께... 구해봅시다.

$$
\begin{align}Z_i = \frac{1}{h^{3N}} \int  \mathrm{d}\mathbf{r}^N\,\mathrm{d}\mathbf{p}^N \, e^{-\beta H_i(\mathbf{r}^N,\mathbf{p}^N)}\end{align}
$$

첨자 $i$는 상태를 의미한다 (반응물 or 생성물).

여기서 reaction coordinate이 $X$인 애들만 모아보자. Reaction coordinate은 1차원 이므로 $\xi = X$인 nuclear coordinate은 많을 것이다. 그 애들의 partition function을 $Z(X)$라 정의하면,

$$
\begin{align}Z_i(X) \stackrel{\text{def}}{=} \frac{1}{h^{3N}} \int  \mathrm{d}\mathbf{r}^N\,\mathrm{d}\mathbf{p}^N \, \delta(X-\Delta E (\mathbf{r}^N)) e^{-\beta H_i(\mathbf{r}^N,\mathbf{p}^N)}\end{align}
$$

를 얻는다. 이로부터 시스템이 $\xi = X$에 있을 확률을 구할 수 있다.

$$
\begin{align}
P_i(X) &= \frac{Z_i(X)}{Z(X)} \\&= \frac{\int  \mathrm{d}\mathbf{r}^N\,\mathrm{d}\mathbf{p}^N \, \delta(X-\Delta E (\mathbf{r}^N)) e^{-\beta H_i(\mathbf{r}^N,\mathbf{p}^N)}}{\int  \mathrm{d}\mathbf{r}^N\,\mathrm{d}\mathbf{p}^N \, e^{-\beta H_i(\mathbf{r}^N,\mathbf{p}^N)}} \\&= \braket{\delta(X-\Delta E (\mathbf{r}^N))}\end{align}
$$

$\braket{}$은 ensemble average를 의미한다. 이제 우리가 원하는 Helmholtz free energy를 구하자. 

$$
\begin{align}F_i = -k_\text{B}T \ln Z_i\end{align}
$$

근데 얘는 reaction coordinate의 함수가 아니므로 $y$축으로 쓸 수 없다. 따라서 다음과 같이 reaction coordinate이 $X$인 애들의 Helmholtz free energy $F(X)$ 를 정의하자. 이를 Landau free energy 혹은 free energy function 이라고도 한다.

$$
\begin{align}F_i(X) &\stackrel{\text{def}}{=} -k_\text{B}T \ln Z_i(X) \\&= -k_\text{B}T \ln P_i(X) + F_i\end{align}
$$

이게 바로 우리가 찾던 $y$축이다.

<br>

## 4. Linear Free Energy Relation



근데, 우리가 찾은 $y$축은 신기한 성질을 가지고 있다. 바로 linear free energy relation 이다.

$$
\begin{align}F_\text{product} (X) = F_\text{reactant} (X) + X\end{align}
$$

이걸 처음 보면 다들 띠용... 할거다. 이럼 $x$축이랑 $y$축이랑 같은 거 아닌가??? 고민은 일단 뒤로 미루고, 이걸 증명하는건 간단하니 먼저 해보자. 편의상 반응물을 1, 생성물을 2라 쓰겠다.

$$
\begin{align}Z_2(X) &= \frac{1}{h^{3N}} \int  \mathrm{d}\mathbf{r}^N\,\mathrm{d}\mathbf{p}^N \, \delta(X-\Delta E (\mathbf{r}^N)) e^{-\beta H_2(\mathbf{r}^N,\mathbf{p}^N)} \\&= \frac{1}{h^{3N}} \int  \mathrm{d}\mathbf{r}^N\,\mathrm{d}\mathbf{p}^N \, \delta(X-\Delta E (\mathbf{r}^N)) e^{-\beta (\Delta E(\mathbf{r}^N) + H_1)} \\&= \frac{1}{h^{3N}} \int  \mathrm{d}\mathbf{r}^N\,\mathrm{d}\mathbf{p}^N \, \delta(X-\Delta E (\mathbf{r}^N)) e^{-\beta (X + H_1)} \\&= \frac{e^{-\beta X}}{h^{3N}} \int  \mathrm{d}\mathbf{r}^N\,\mathrm{d}\mathbf{p}^N \, \delta(X-\Delta E (\mathbf{r}^N)) e^{-\beta H_1} \\&= e^{-\beta X} Z_1(X)\end{align}
$$

$$
\begin{align}\therefore F_2(X) &= -\frac{1}{\beta} \ln Z_2(X) \\&= -\frac{1}{\beta} \left[ -\beta X + \ln Z_1(X)  \right] \\&= F_1(X) + X\end{align}
$$

다시 띠용..한 부분으로 돌아오자. 일단 글을 처음부터 끝까지 쭉 다시 읽어보자. 아직도 띠용..이라면 내가 달아놓은 reference들을 읽어보자. 잘 생각해보면 순환논리는 없다. 

그래도 모르겠으면.. 그냥 받아들이시길.

아 그리고 내가 위에서 굳이 언급하진 않았는데, 우리가 구한 PES는 diabatic PES이다. Diabatic picture와 adiabatic picture에 대해 아직 다루지 않아서 이걸 말하기는 애매했다. 추후 별도의 글에서 다룰 예정.

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/13/images/asd.png" width="550px" style="display: block; margin: 0 auto;" />
  <figcaption style="margin-top: 8px; font-size: 0.9em; color: #555;">From J. Blumberger (2015).</figcaption>
</figure>

<br>


## 5. Reorganization Energy



반응물의 재배열에너지는 reaction coordinate이 반응물 평형 상태로부터 생성물 평형 상태로 변할 때 반응물 free energy 차이로 정의한다. 생성물의 재배열에너지도 비슷하게 정의된다.

반응물 평형 상태, 생성물 평형 상태의 reaction coordinate을 각각 $X_1$, $X_2$ 라 하면,

$$
\begin{align}\lambda_1 \stackrel{\text{def}}{=} F_1(X_2) - F_1(X_1) \\\lambda_2 \stackrel{\text{def}}{=} F_2(X_1) - F_2(X_2)\end{align}
$$

정의에서 알 수 있듯이, 재배열에너지는 뭔가 free energy curve의 curvature과 연관되어 있을 것 같은 느낌이 든다. 다음 절에서 자세히 알아보자.

<br>

## 6. Marcus Theory



Marcus 이론에서는 식 (8)에서본 $P(X)$가 Gaussian 분포를 따른다고 가정한다. 왜 이런 가정을 했는지는 이 글에서 다루지 않는다.

$$
\begin{align}P_i(X) &= \braket{\delta(X-\Delta E (\mathbf{r}^N))}  \\&\simeq \frac{1}{\sqrt{2\pi\sigma_i^2}}\exp \left[ -(X-X_i)^2 / 2\sigma_i^2  \right]\end{align}
$$

따라서 free energy는 이차함수의 형태를 가진다.

$$
\begin{align}F_i(X) = \frac{k_\text{B}T}{2\sigma_i^2}\left(X-X_i\right)^2 + F_i + \frac{k_\text{B}T}{2} \ln 2\pi\sigma_i^2\end{align}
$$

식 (12), (21), (22), (25)를 연립하면 다음 관계를 얻을 수 있다. 단순 계산이므로 과정은 생략한다.

$$
\begin{align}\lambda &\stackrel{\text{def}}{=} \lambda_1 = \lambda_2 \\&= \frac{X_1 - X_2}{2} = \frac{1}{2k_\text{B}T}\sigma_i^2\end{align}
$$

$$
\begin{align}\Delta F = \frac{X_1 + X_2}{2}\end{align}
$$

결과가 매우 신기하군. 

<br>



## References


$^1$ R. A. Marcus, “Electrostatic Free Energy and Other Properties of States Having Nonequilibrium Polarization. I,” [J. Chem. Phys.](https://doi.org/10.1063/1.1742724) **24**, 979–989 (1956).

$^2$ R. A. Marcus, “On the Theory of Oxidation‐Reduction Reactions Involving Electron Transfer. I,” [J. Chem. Phys.](https://doi.org/10.1063/1.1742723) **24**, 966–978 (1956).

$^3$ R. A. Marcus, “On the Theory of Electron‐Transfer Reactions. VI. Unified Treatment for Homogeneous and Electrode Reactions,” [J. Chem. Phys.](https://doi.org/10.1063/1.1696792) **43**, 679–701 (1965).

$^4$ J. Blumberger, “Recent Advances in the Theory and Molecular Simulation of Biological Electron Transfer Reactions,” [Chem. Rev.](https://doi.org/10.1021/acs.chemrev.5b00298) **115**, 11191–11238 (2015).

$^5$ M. Tachiya, “Relation between the electron-transfer rate and the free energy change of reaction,” [J. Phys. Chem.](https://doi.org/10.1021/j100357a005) **93**, 7050–7052 (1989).

$^6$ D. V. Matyushov, “Reorganization energy of electron transfer,” [Phys. Chem. Chem. Phys.](https://doi.org/10.1039/D2CP06072H) **25**, 7589–7610 (2023).

<br>

---

2024.12.25 최예성 작성

<footer class="site-footer"></footer>


</div>