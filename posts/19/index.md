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


# Fourier Transform with Quantum Computer II

퀀텀 컴퓨터 잘되면 좋겠다.


## 1. Basis transform with qubit


[Fourier Transform with Quantum Computer I](https://ysch0i.github.io/posts/16/) 에서 우리는 아래와 같은 basis transform을 해야 한다는 것을 알았다.

$$\begin{align}
\ket{k} \mapsto \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} \omega_N^{jk} \ket{j}
\end{align}$$

$$\begin{align}
\ket{k} &\mapsto 
\frac{1}{\sqrt{N}} \left(\ket{0} + e^{i2\pi [0.k_n]} \ket{1}      \right) \otimes \left(\ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1}      \right) \otimes \cdots \otimes \left(\ket{0} + e^{i2\pi [0.k_1 k_2 \cdots k_n]  } \ket{1}      \right)
\end{align}$$

여기서 $\omega_N = e^{i2\pi/N}$, $k$는 $0$부터 $N-1$까지의 범위를 가지는 정수, $k_j$는 0 또는 1이며 아래의 식을 만족한다.

$$\begin{align}
(k)_{10} = (k_1 k_2 \cdots k_n)_2
\end{align}$$

$$\begin{align}
k &= 2^{n-1} k_1 + 2^{n-2} k_2 +  \cdots + k_n \\ 

&= \sum_{m=1}^n 2^{n-m} k_m
\end{align}$$

$\ket{k} = \ket{k_1k_2 \cdots k_n} = \ket{k_1} \otimes \ket{k_2} \otimes \cdots \otimes \ket{k_n}$이므로 이를 식 (2)에 대입하면, 

$$\begin{align}
\ket{k_1} \otimes \ket{k_2} & \otimes \cdots \otimes \ket{k_n} \\
&\mapsto 
\frac{1}{\sqrt{N}} \left(\ket{0} + e^{i2\pi [0.k_n]} \ket{1}      \right) \otimes \left(\ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1}      \right) \otimes \cdots \otimes \left(\ket{0} + e^{i2\pi [0.k_1 k_2 \cdots k_n]  } \ket{1}      \right)
\end{align}$$

가 된다. 따라서 basis transform을 qubit의 관점에서 보면,


$$\begin{align}
\ket{k_1} \mapsto \ket{0} + e^{i2\pi [0.k_n]} \ket{1} 
\end{align}$$

$$\begin{align}
\ket{k_2} \mapsto \ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1} 
\end{align}$$

$$\cdots$$

$$\begin{align}
\ket{k_n} \mapsto \ket{0} + e^{i2\pi [0.k_1 k_2 \cdots k_n] } \ket{1}    
\end{align}$$

가 된다(정규화 상수 생략). 즉, 우리는 퀀텀 컴퓨터 회로를 통해 첫 번째 qubit을 식 (8)로, $\cdots$ $n$ 번째 qubit을 식 (10)으로 변환해야 한다.

하지만, 식 (8)-(10)의 변환은 어렵다. 따라서 quantum Fourier transform 에서는 아래와 같은 변환을 한 뒤, SWAP gate로 순서를 뒤집는다.

$$\begin{align}
\ket{k_1} \mapsto \ket{0} + e^{i2\pi [0.k_1 k_2 \cdots k_n] } \ket{1}    



\end{align}$$

$$\begin{align}
\ket{k_2} \mapsto \ket{0} + e^{i2\pi [0.k_1 k_2 \cdots k_{n-1}] } \ket{1}   
\end{align}$$

$$\cdots$$

$$\begin{align}
\ket{k_n} \mapsto \ket{0} + e^{i2\pi [0.k_n]} \ket{1} 
\end{align}$$


<br>

## 2. 회로 설계

먼저, 식 (13)의 변환은 쉽다. 잘 안보인다면 $k_n$에 0, 1을 대입해보면 된다. 

$k_n = 0$이면,

$$\begin{align}
\ket{0} &\mapsto \ket{0} + e^{i2\pi [0.0]} \ket{1} \\
&= \ket{0} + \ket{1}
\end{align}$$

$k_n = 1$이면,

$$\begin{align}
\ket{1} &\mapsto \ket{0} + e^{i2\pi [0.1]} \ket{1} \\
&= \ket{0} + e^{i2\pi 2^{-1}} \ket{1} \\
&= \ket{0} + e^{i\pi} \ket{1} \\
&= \ket{0} - \ket{1}

\end{align}$$

따라서 식 (13)의 변환은 

$$\begin{align}
\begin{bmatrix}
a \\
b 
\end{bmatrix} \mapsto \begin{bmatrix}
a+b \\
a-b
\end{bmatrix}
\end{align}$$

이다. 이게 뭘까? 바로 Hadamard gate 이다. 따라서 $n$ 번째 qubit의 변환은 Hadamard gate 하나로 표현된다 (앞으로 정규화 상수 생략).

$$\begin{align}
H \ket{k_n} = \ket{0} + e^{i2\pi [0.k_n]} \ket{1} 
\end{align}$$



<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/circuit1.svg" width="150px" style="display: block; margin: 0 auto;" />
</figure>


다음으로 $n-1$ 번째 qubit을 변환해보자. 


$$\begin{align}
\ket{k_{n-1}} \mapsto \ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1} 
\end{align}$$

일단 먼저 Hadamard gate를 통과시키면,

$$\begin{align}
H \ket{k_{n-1}} = \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} 
\end{align}$$

가 된다. 이제

$$\begin{align}
 \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} \mapsto \ket{0} + e^{i2\pi [0.k_{n-1}k_n]} \ket{1} 
\end{align}$$

을 해주면 된다. 앞에서와 마찬가지로 $k_n$에 0, 1을 대입해보자. 

$k_n = 0$이면,

$$\begin{align}
 \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} \mapsto \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} 
\end{align}$$


아무 변화가 없다. $k_n = 1$이면,

$$\begin{align}
 \ket{0} + e^{i2\pi [0.k_{n-1}]} \ket{1} &\mapsto \ket{0} + e^{i2\pi [0.k_{n-1}1]} \ket{1} \\
 &= \ket{0} + e^{i2\pi ([0.k_{n-1}] + 2^{-2})} \ket{1} \\
&= \ket{0} + e^{i2\pi[0.k_{n-1}]} e^{i2\pi / 2^2} \ket{1} \\
\end{align}$$

즉, 식 (28)의 변환은 $\ket{1}$에 $e^{i2\pi / 2^2}$ 가 곱해지므로 아래와 같은 행렬 $R_2$로 표현할 수 있다.

$$\begin{align}
R_2 = \begin{bmatrix}
1 & 0 \\
0 & e^{i2\pi / 2^2}
\end{bmatrix}

\end{align}$$


식 (25), (28)을 종합하면, $n-1$ 번째 qubit은 $n$ 번째 qubit이 $\ket{0}$이면, 아무런 변화가 없고, $n$ 번째 qubit이 $\ket{1}$이면, $R_2$ gate가 가해진다. 이게 뭘까? 바로 controlled gate 이다. 

따라서 식 (23)의 Hadamard gate, 식 (24)의 controlled gate 를 종합하면 $n-1$ 번째 qubit의 변환은 아래와 같이 표현된다 ($n$ 번째 qubit의 변환도 같이 표현).

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/circuit2.svg" width="300px" style="display: block; margin: 0 auto;" />
</figure>


이렇게 계속 반복하면 된다. 예들 들어 qubit이 3개라면 

<figure style="text-align: center;">
  <img src="https://ysch0i.github.io/posts/19/images/circuit3.svg" width="450px" style="display: block; margin: 0 auto;" />
</figure>

가 된다. 마지막으로 SWAP gate을 통해 qubit의 순서를 반대로 바꿔주면 quantum Fourier transform 회로가 완성된다.





## 3. 





<br>

## References

<sup>1</sup> L. Ruiz-Perez, and J. C. Garcia-Escartin, “Quantum arithmetic with the quantum Fourier transform,” [Quantum Inf Process](https://doi.org/10.1007/s11128-017-1603-1) **16**, 152 (2017).

<sup>2</sup> D. Camps, R. Van Beeumen, and C. Yang, “Quantum Fourier transform revisited,” [Numerical Linear Algebra App](https://doi.org/10.1002/nla.2331) **28**, e2331 (2021).


<sup>3</sup> M. A. Nielsen, and I. L. Chuang, *Quantum Computation and Quantum Information*, 10th anniversary edition (Cambridge university press, Cambridge, 2010).


<br>

---

2025.06.21 최예성 작성




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