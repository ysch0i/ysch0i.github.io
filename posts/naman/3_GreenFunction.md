# Green Function

양자역학에 Green function을 도입해보자.

## Recap

이 글은 아래의 문서를 기반으로 작성되었다.
- Scattering State
  

<br>

## 1. Linear Differential Equation

Green function은 선형 미분방정식을 풀기 위해 도입되었다. 

$$\begin{align}
Ly(x) = f(x)
\end{align}$$

Define Green function $G(x,s)$ as follows

$$\begin{align}
LG(x,s) = \delta(x-s)
\end{align}$$

Then,

$$\begin{align}
L\left( \int \mathrm{d}s\, G(x,s)f(s)  \right) &= \int \mathrm{d}s\, LG(x,s) f(s) \\
&= \int \mathrm{d} s\, \delta(x-s) f(s) \\
&= f(x)
\end{align}$$

$$\begin{align}
\therefore y(x) = \int \mathrm{d} s \, G(x,s) f(s)
\end{align}$$

Using Green function, we can find solution of differential equation.

<br>

## 2. Application : Scattering state

Recall notation

$$\begin{align}
H = H_0 + V = \frac{p^2}{2m} + V(x)
\end{align}$$


$$\begin{align}
H\ket{\psi_p} = E \ket{\psi_p}
\end{align}$$

$$\begin{align}
\frac{p^2}{2m} &\stackrel{\text{def}}{=} E
\end{align}$$

Rearrange Schrödinger equation.

$$\begin{align}
(E-H_0) \ket{\psi_p} = V\ket{\psi_p}
\end{align}$$

Then,

$$\begin{align}
\ket{\psi_p} = \ket{p} + \lim_{\epsilon \rightarrow \infty} (E + i\epsilon - H_0)^{-1} V \ket{\psi_p}
\end{align}$$

since $\ket{p}$ is eigenstate of $H_0$. 

If inverse operator is unfamiliar, 

$$\begin{align}
f(A) = \sum_{n = 0}^\infty \frac{f^{(n)}(0)}{n!} A^n
\end{align}$$

where $A$ is operator.

Also, why we introduce $\epsilon$? It is to avoid situations where the denominator becomes zero in future calculations (cf. Residue theorem). However, since I will not be performing direct calculations, I will omit a detailed explanation.

Next, multiplicate $\bra{x}$ to Eq (11)

$$\begin{align}
\braket{x|\psi_p} = \psi_p(x) &= \braket{x|p} + \braket{x | \lim_{\epsilon\rightarrow0} (E + i\epsilon - H_0)^{-1} V | \psi_p  } \\
&=  \phi_p(x) + \int_{-\infty}^\infty \mathrm{d}x'  \braket{x|\lim_{\epsilon\rightarrow0} (E + i\epsilon - H_0)^{-1} |x' } V(x') \psi_p(x')
\end{align}$$

Therefore, Green function is defined as follows

$$\begin{align}
G_0^+ (x,x') \stackrel{\text{def}}{=} \lim_{\epsilon\rightarrow0} \braket{x| (E + i\epsilon - H_0)^{-1} |x' }
\end{align}$$

The "+" is attached to the Green's function because, in reality, it represents the limit where $\epsilon$ approaches $0^+$. However, as noted above, it is not important for the discussion going forward.

Note that $G_0^+ (x,x')$ is function, not operator. Then, let's define Green operator. I don't particularly like using operator symbols, but I will use them only in Eq (16).

$$\begin{align}
\hat{G}_0^+  \stackrel{\text{def}}{=} \lim_{\epsilon\rightarrow0}\, (E + i\epsilon - \hat{H}_0)^{-1} 
\end{align}$$

And, similary define $G^+$

$$\begin{align}
G^+  \stackrel{\text{def}}{=} \lim_{\epsilon\rightarrow0}\, (E + i\epsilon - H)^{-1} 
\end{align}$$

Since
$$\begin{align}
(G_0^+)^{-1} = (G^+)^{-1} + V
\end{align}$$

then,

$$\begin{align}
G^+V = G_0^+V + G^+VG_0^+V
\end{align}$$

$$\begin{align}
(1+G^+V)(1-G_0^+V) = 1
\end{align}$$

Now, recall Eq (11)

$$\begin{align}
\ket{\psi_p} = \ket{p} + G_0^+ V \ket{\psi_p} 
\end{align}$$

$$\begin{align}
(1-G_0^+V)\ket{\psi_p} = \ket{p}
\end{align}$$

Using Eq (20)

$$\begin{align}
\ket{\psi_p} &= (1+G^+V)\ket{p} \\
&= (1-G^+(E-H)) \ket{p} \\
&= \lim_{\epsilon\rightarrow0} \left[ 1- (E+i\epsilon-H)^{-1} (E+i\epsilon - H -i\epsilon)  \right]\ket{p} \\
&= \lim_{\epsilon\rightarrow0} \,(i\epsilon) (E+i\epsilon-H)^{-1}  \ket{p} \\
&= \lim_{\epsilon\rightarrow0} \frac{\epsilon}{\hbar} \int_0^\infty \mathrm{d}t \, e^{i(E+i\epsilon-H)t/\hbar} \ket{p} \\
&= \lim_{\epsilon\rightarrow0} \frac{\epsilon}{\hbar} \int_0^\infty \mathrm{d}t \, e^{-\epsilon t/\hbar} e^{-iHt/\hbar} e^{iH_0t/\hbar}\ket{p} \\
&= \lim_{\epsilon\rightarrow0}  \int_0^\infty \mathrm{d}x \,e^{-x} e^{-iHx/\epsilon} e^{iH_0t/\epsilon}   \ket{p} \\
&= \lim_{t\rightarrow\infty}  \int_0^\infty \mathrm{d}x \,e^{-x} e^{-iHt/\hbar} e^{iH_0t/\hbar}   \ket{p} \\
&= \lim_{t\rightarrow\infty} e^{-iHt/\hbar} e^{iH_0t/\hbar}   \ket{p} 

\end{align}$$

And, Let's define Møller operator

$$\begin{align}
\Omega_+ \stackrel{\text{def}}{=} \lim_{t\rightarrow\infty} e^{-iHt/\hbar} e^{iH_0t/\hbar}
\end{align}$$

Therefore,

$$\begin{align}
\ket{\psi_p} = \Omega_+ \ket{p}
\end{align}$$

Let us examine two important properties of the Møller operator.

The first important property is the physical meaning of the Møller operator. It is an operator that sends a state infinitely into the past under the Hamiltonian $H_0$, and then brings it back to the original time under the Hamiltonian $H$.

The second important property is the normalization and orthogonality of $\ket{\psi_p}$.


$$\begin{align}
\braket{\psi_{p'} | \psi_p} &= \braket{p' | \Omega^\dag_+ \Omega_+ | p } \\
&= \lim_{t\rightarrow\infty} \braket{p' |e^{-iH_0t/\hbar} e^{iHt/\hbar}e^{-iHt/\hbar} e^{iH_0t/\hbar}| p} \\
&= \braket{p'|p} = \delta(p'-p)

\end{align}$$

<br>

## References
<sup>1</sup> D. E. Manolopoulos, “Chemical Reaction Dynamics,” [David Manolopoulos Research Group: Chemical Dynamics](http://manolopoulos.chem.ox.ac.uk/) (2008).


<br>

---
2024.11.14 최예성 작성