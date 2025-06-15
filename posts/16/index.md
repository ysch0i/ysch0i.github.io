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


# Fourier Transform with Quantum Computer I

오! 퀀텀컴퓨터. 이 글에서는 퀀텀컴퓨터 회로를 다루지 않는다. 

## 1. Discrete Fourier transform

평소 우리가 자주 쓰는 Fouier transform 은 아래와 같은 적분 형태이다.

$$\begin{align}
F(\xi) = \int_{-\infty}^\infty \mathrm{d}x \, f(x)e^{-i2\pi\xi x}
\end{align}$$

그러나, numerical 하게 Fourier transform을 하기 위해선 아래와 같이 discretization을 해야 한다.

$$\begin{align}
\xi_k &= \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j e^{-i2\pi jk/N} \\
&= \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j \omega_N^{-jk}
\end{align}$$

이를 discrete Fourier transform 이라 한다. 

그런데 화나게도 quantum Fouier transform에서는 phase의 부호를 바꿔버린다.

$$\begin{align}
\xi_k &= \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j \omega_N^{jk}
\end{align}$$

앞으로 식 (4)를 Fourier transform라 부르겠다. 


간단한 예시로, 길이가 3인 vector의 Fourier transform은 다음과 같이 행렬로 나타낼 수 있다.

$$\begin{align}
\begin{bmatrix}
\xi_0 \\ \xi_1 \\ \xi_2
\end{bmatrix}  =\frac{1}{\sqrt{3}} \begin{bmatrix}
1 & 1 & 1 \\
1 & \omega & \omega^2 \\
1 & \omega^2 & \omega^4

\end{bmatrix} \begin{bmatrix}
x_0 \\
x_1 \\
x_2
\end{bmatrix} = \frac{1}{\sqrt{3}}\begin{bmatrix}
x_0 + x_1 + x_2\\
x_0 + \omega x_1 + \omega^2 x_2\\
x_0 + \omega^2 x_1 + \omega^4 x_2
\end{bmatrix} 
\end{align}$$

여기서, $\omega = \omega_3 = e^{i2\pi/3}$ 이다.


<br>

## 2. Basis transform

식 (5)를 basis transform의 관점에서 생각해 보자. 임의의 vector는 아래와 같이 basis vector의 합으로 나타낼 수 있다.


$$\begin{align}
\begin{bmatrix}
x_0 \\
x_1 \\
x_2
\end{bmatrix} = x_0 \ket{0} + x_1 \ket{1} + x_2 \ket{2}
\end{align}$$

그리고 아래와 같은 basis transform을 생각해보자.


$$\begin{align}
\ket{0} \mapsto \frac{1}{\sqrt{3}}(\ket{0} + \ket{1} + \ket{2})
\end{align}$$

$$\begin{align}
\ket{1} \mapsto \frac{1}{\sqrt{3}}(\ket{0} + \omega\ket{1} + \omega^2\ket{2})
\end{align}$$

$$\begin{align}
\ket{2} \mapsto \frac{1}{\sqrt{3}}(\ket{0} + \omega^2\ket{1} + \omega^4\ket{2})
\end{align}$$


그러면,

$$\begin{align}
x_0 \ket{0} + x_1 \ket{1} + x_2 \ket{2} &\mapsto \frac{1}{\sqrt{3}} \left[ x_0 (\ket{0} + \ket{1} + \ket{2}) + x_1 (\ket{0} + \omega\ket{1} + \omega^2\ket{2}) + x_2 (\ket{0} + \omega^2\ket{1} + \omega^4\ket{2}) \right]\\
&= \frac{1}{\sqrt{3}} \left[(x_0 + x_1 + x_2) \ket{0} + (x_0 + \omega x_1 + \omega^2 x_2)\ket{1} + (x_0 + \omega^2 x_1 + \omega^4 x_2) \ket{2} \right]
\end{align}$$


$$\begin{align}\begin{bmatrix}
x_0 \\
x_1 \\
x_2
\end{bmatrix} \mapsto\frac{1}{\sqrt{3}}
\begin{bmatrix}
x_0 + x_1 + x_2\\
x_0 + \omega x_1 + \omega^2 x_2\\
x_0 + \omega^2 x_1 + \omega^4 x_2
\end{bmatrix} = \begin{bmatrix}
\xi_0 \\ \xi_1 \\ \xi_2
\end{bmatrix}
\end{align}$$

가 된다. 

따라서 식 (7)-(9)의 basis transform을 Fourier transform이라 생각할 수 있다. 이를 일반화하면 아래와 같다.

$$\begin{align}
\ket{k} \mapsto \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} \omega_N^{jk} \ket{j}
\end{align}$$


<br>



## 3. Quantum algorithm


식 (13)에서 $j$는 $0$부터 $N-1$까지의 범위를 가지는 정수이다. 이를 이진법으로 표현하면,

$$\begin{align}
(j)_{10} = (j_1 j_2 \cdots j_n)_2
\end{align}$$

$$\begin{align}
j &= 2^{n-1} j_1 + 2^{n-2} j_2 +  \cdots + j_n \\ 

&= \sum_{l=1}^n 2^{n-l} j_l
\end{align}$$

가 된다. 여기서 $2^n = N$ 이고 $j_l$는 0 또는 1이다. 그리고, 마찬가지로 basis도 이진법으로 표현해보자.


$$\begin{align}
\ket{j} = \ket{j_1 j_2 \cdots j_n} &= \ket{j_1} \ket{j_2} \cdots \ket{j_n} \\ &= \ket{j_1} \otimes \ket{j_2} \otimes \cdots \otimes \ket{j_n}
\end{align}$$

이를 식 (16), (18)을 식 (13)에 대입하면 

$$\begin{align}
\ket{k} \mapsto \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} \omega_N^{jk}\ket{j}&=    \frac{1}{\sqrt{N}} \sum_{j_1, \cdots, j_n }^{0, 1} \omega_N^{k\sum_{l=1}^n 2^{n-l} j_l} \ket{j_1} \otimes \cdots \otimes \ket{j_n} \\
&= \frac{1}{\sqrt{N}} \sum_{j_1, \cdots, j_n }^{0, 1} \left(\omega_N^{2^{n-1}j_1 k} \ket{j_1} \right) \otimes \left(\omega_N^{2^{n-2}j_2 k} \ket{j_2} \right) \otimes \cdots \otimes \left(\omega_N^{j_n k} \ket{j_n} \right) \\
&= \frac{1}{\sqrt{N}} \left(\ket{0} + \omega_N^{2^{n-1}k} \ket{1}      \right) \otimes \left(\ket{0} + \omega_N^{2^{n-2}k} \ket{1}      \right) \otimes \cdots \otimes \left(\ket{0} + \omega_N^{k} \ket{1}      \right) \\
&=\frac{1}{\sqrt{N}} \bigotimes_{l=1}^n \left(\ket{0} + \omega_N^{2^{n-l}k} \ket{1}   \right)
\end{align}$$

를 얻을 수 있다. 여기서 $k$도 $0$부터 $N-1$까지의 범위를 가지는 정수이므로 $j$와 같이 이진법으로 변환하자.

$$\begin{align}
(k)_{10} = (k_1 k_2 \cdots k_n)_2
\end{align}$$

$$\begin{align}
k &= 2^{n-1} k_1 + 2^{n-2} k_2 +  \cdots + k_n \\ 

&= \sum_{m=1}^n 2^{n-m} k_m
\end{align}$$

그럼, 식 (22)에서 

$$\begin{align}
\omega_N^{2^{n-l}k} &= \omega_N^{2^{n-l}\sum_{m=1}^n 2^{n-m} k_m} \\

&= \exp \left[ i2\pi \sum_{m=1}^n 2^{n-l-m} k_m   \right]
\end{align}$$

이 된다. 그리고 아래와 같은 노테이션을 사용하자. 

$$\begin{align}
[0.k_1k_2 \cdots k_n] = \frac{k_1}{2} + \frac{k_2}{2^2} + \cdots + \frac{k_n}{2^n}
\end{align}$$

만약 $l = 1$이면,

$$\begin{align}
\omega_N^{2^{n-1}k} 
&= \exp \left[ i2\pi \sum_{m=1}^n 2^{n-1-m} k_m   \right] \\
&= e^{i2\pi 2^{n-2}k_1} \cdots e^{i2\pi k_{n-1}} e^{{i2\pi k_n/2}} \\
&= e^{i2\pi k_n/2} \\
&= e^{i2\pi [0.k_n]}
\end{align}$$

만약 $l = 2$이면,

$$\begin{align}
\omega_N^{2^{n-2}k} 
&= e^{i2\pi k_{n-1}/2} e^{i2\pi k_n/2^2} \\
&= e^{i2\pi [0.k_{n-1}k_n]}
\end{align}$$

$l = n$이면,

$$\begin{align}
\omega_N^{k} 
&= e^{i2\pi [0.k_1 k_2 \cdots k_n]  }
\end{align}$$

이 된다. 마지막으로 식 (32), (34), (35)를 식 (22)에 대입하면,

$$\begin{align}
\ket{k} &\mapsto \frac{1}{\sqrt{N}} \bigotimes_{l=1}^n \left(\ket{0} + \omega_N^{2^{n-l}k} \ket{1}   \right) \\
&= \frac{1}{\sqrt{N}} \left(\ket{0} + e^{i2\pi [0.k_n]} \ket{1}      \right) \otimes \left(\ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1}      \right) \otimes \cdots \otimes \left(\ket{0} + e^{i2\pi [0.k_1 k_2 \cdots k_n]  } \ket{1}      \right)
\end{align}$$

를 얻는다. 

수식은 여기서 끝이다. 이제 식 (37)을 만들 수 있는 quantum computer 회로를 설계하면 된다. 여기까지만 보면 식 (37)의 의미가 잘 보이지 않지만 구현된 회로를 보면 무슨 느낌인지 알 것이다. 회로 구현은 Fourier Transform with Quantum Computer II 에서 다룰 예정이다.


<br>

## References

<sup>1</sup> L. Ruiz-Perez, and J. C. Garcia-Escartin, “Quantum arithmetic with the quantum Fourier transform,” [Quantum Inf Process](https://doi.org/10.1007/s11128-017-1603-1) **16**, 152 (2017).

<sup>2</sup> D. Camps, R. Van Beeumen, and C. Yang, “Quantum Fourier transform revisited,” [Numerical Linear Algebra App](https://doi.org/10.1002/nla.2331) **28**, e2331 (2021).

<sup>3</sup> Y. M. Rhee, "Quantum Fourier Transform" (2025).


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