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

<div id="header"></div>

<br>



# Gamma Function


내가 좋아하는 Gamma functon


## 1. Definition

Gamma function은 아래와 같이 정의된다.

$$\begin{equation}
\Gamma(x) \stackrel{\text{def}}{=} \int_0^\infty \mathrm{d}z\, z^{x-1}e^{-z} \,\,\,\,\,\, (x>0)
\end{equation}$$
부분적분을 이용하면

$$\begin{align}
\Gamma(x) &= \left[ -z^{x-1}e^{-z}  \right]_0^\infty + (x-1)\int_0^\infty \mathrm{d}z\,  z^{x-2}e^{-z} \\
&= (x-1) \int_0^\infty \mathrm{d}z\,  z^{x-2}e^{-z} \\
&= (x-1) \Gamma(x-1)
\end{align}$$

특별히, $x$가 자연수라면
$$\begin{equation}
\Gamma(x) = (x-1)(x-2) \cdots \Gamma(1)
\end{equation}$$

여기서
$$\begin{equation}
\Gamma(1) = \int_0^\infty \mathrm{d}z\, e^{-z} = 1
\end{equation}$$

이므로, gamma function은 아래와 같이 표현된다.

$$\begin{equation}
\Gamma(x) = (x-1)(x-2) \cdots (1) = (x-1)!
\end{equation}$$

<br>


## 2. Application
양자역학에서는 아래와 같은 형태의 적분이 많이 등장한다.
$$\begin{equation}
\int_0^\infty \mathrm{d}x \, x^ne^{-ax^2}
\end{equation}$$

Gamma function을 활용하면 이를 손쉽게 계산할 수 있다. 예를 들어 $n = 2$ 인 경우

$$\begin{align}
\int_0^\infty \mathrm{d}x \, x^2e^{-ax^2} &= \frac{1}{2a^{3/2}}\int_0^\infty \mathrm{d}u \, \sqrt{u} e^{-u} \\
&= \frac{1}{2a^{3/2}}\times \Gamma\left(\frac{3}{2}\right) 
= \frac{1}{4a^{3/2}}\times \Gamma\left(\frac{1}{2}\right)
\end{align}$$

여기서
$$\begin{equation}
\Gamma\left(\frac{1}{2}\right) = \int_0^\infty \mathrm{d}z\, z^{-1/2}e^{-z} = 2\int_0^\infty\mathrm{d}u\,e^{-u^2} = \sqrt{\pi}
\end{equation}$$
이므로, 아래를 얻을 수 있다.

$$\begin{equation}
\int_0^\infty \mathrm{d}x \, x^2e^{-ax^2} = \frac{\sqrt
\pi}{4a^{3/2}}
\end{equation}$$

<br>

## References

<sup>1</sup> D. A. McQuarrie, *Mathematics for Physical Chemistry: Opening Doors* (Univ. Science Books, Sausalito, Calif, 2008).




<br>

---
2024.05.04 최예성 작성


© 2024 Yeseong Choi. All rights reserved.
