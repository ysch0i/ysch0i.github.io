# Hamiltonian of Diabatic Picture



## 1. Basis

$$\begin{align}


\ket{\psi} = \left[\sum_n \ket{0}\ket{n}\bra{n}\bra{0} + \ket{1}\ket{n}\bra{n}\bra{1}\right] \ket{\psi}

\end{align}$$


where $\ket{0}$, $\ket{1}$ are electronic wavefunction, and $\ket{n}$ is nuclei wavefunction. 

$$\begin{align}

\text{Tr} (A) &= \sum_n \bra{n}\braket{0|A|0}\ket{n} + \bra{n}\braket{1|A|1}\ket{n} \\
&= \sum_n \bra{n}\braket{0|A|0} + \braket{1|A|1}\ket{n} \\
&\stackrel{\text{def}}{=} \text{Tr}_n \left[ \braket{0|A|0} + \braket{1|A|1}  \right]

\end{align}$$

<br>




## 2. Hamiltonian

$$\begin{align}

H = H_0 \ket{0}\bra{0} + H_1 \ket{1}\bra{1} + \Delta \left( \ket{0}\bra{1} + \ket{1}\bra{0} \right)

\end{align}$$

where $H_0$ and $H_1$ are nuclei Hamiltonian for electronic state $\ket{0}$, $\ket{1}$, respectively. And $\Delta$ is small, constant electronic coupling (Condon approximation). 

<br>

## 3. Rate constant in Golden Rule Limit

Recall rate constant is independent of $\lambda$.

$$\begin{align}
kQ &= \frac{1}{2} \int_{-\infty}^{\infty} \mathrm{d}t \, c_{ff}(t + i\lambda \hbar) \\
&= \frac{1}{2}  \int_{-\infty}^{\infty}\mathrm{d}t \, \text{Tr} \left[ e^{-(\beta-\lambda) H} F e^{-\lambda H} e^{iHt/\hbar} F e^{-iHt/\hbar}   \right]
\end{align}$$

where $Q$ is partition function of reactant $\left(e^{-\beta H} \ket{0}\bra{0} \right)$ and

$$\begin{align}
F = \frac{i}{\hbar} \left[  H, \ket{1}\bra{1}  \right] = \frac{i\Delta}{\hbar} (\ket{0}\bra{1} - \ket{1}\bra{0})
\end{align}$$

Let's define a correlation function.

$$\begin{align}
c(t) \stackrel{\text{def}}{=} \text{Tr}_n \left[  e^{-\beta H_0} e^{iH_0t/\hbar} e^{-iH_1t/\hbar}   \right]
\end{align}$$

then,

$$\begin{align}
c(t + i\lambda\hbar) &= \text{Tr}_n \left[  e^{-\beta H_0} e^{-\lambda H_0t/\hbar}  e^{iH_0t/\hbar} e^{-iH_1t/\hbar} e^{\lambda H_1}  \right] \\

&= \text{Tr}_n \left[  e^{-\lambda H_0} e^{iH_0t/\hbar}  e^{-(\beta-\lambda)H_1} e^{-iH_1t/\hbar}   \right]
\end{align}$$

Now calculate Eq. (7)

$$\begin{align}

\text{Tr}_n &\braket{0 | e^{-(\beta-\lambda) H} F e^{-\lambda H} e^{iHt/\hbar} F e^{-iHt/\hbar} | 0} \\ 
&= -\frac{\Delta^2}{\hbar^2} \, \text{Tr}_n \braket{0 | e^{-(\beta-\lambda) H} (\ket{0}\bra{1} - \ket{1}\bra{0}) e^{-\lambda H} e^{iHt/\hbar} (\ket{0}\bra{1} - \ket{1}\bra{0}) e^{-iHt/\hbar} | 0} \\
&= \frac{\Delta^2}{\hbar^2} \, \text{Tr}_n \left[ e^{-(\beta-\lambda) H_0}  e^{-\lambda H_1} e^{iH_1t/\hbar} e^{-iH_0t/\hbar} \right] \\
&= \frac{\Delta^2}{\hbar^2} \, \text{Tr}_n \left[ e^{-(\beta-\lambda) H_0}  e^{-iH_0t/\hbar} e^{-\lambda H_1} e^{iH_1t/\hbar}    \right] \\
&= \frac{\Delta^2}{\hbar^2}\, c(-t + i(\beta-\lambda)\hbar)

\end{align}$$

Similary,

$$\begin{align}

\text{Tr}_n \braket{1 | e^{-(\beta-\lambda) H} F e^{-\lambda H} e^{iHt/\hbar} F e^{-iHt/\hbar} | 1} = \frac{\Delta^2}{\hbar^2}\, c(t + i\lambda\hbar)

\end{align}$$

since
$$\begin{align}
\braket{0|e^H|0} = e^{H_0} + \mathcal{O}(\Delta)
\end{align}$$

$$\begin{align}
\braket{0|e^H|1} = \mathcal{O}(\Delta)
\end{align}$$

$$\begin{align}
\braket{1|e^H|1} = e^{H_1} + \mathcal{O}(\Delta)
\end{align}$$

Then,

$$\begin{align}
kQ &= \frac{\Delta^2}{2\hbar^2} \int_{-\infty}^\infty \mathrm{d}t \,c(t + i\lambda\hbar) + c(-t + i(\beta-\lambda)\hbar) \\
&= \frac{\Delta^2}{2\hbar^2} \int_{-\infty}^\infty \mathrm{d}t \,c(t + i\lambda\hbar) + c(t + i(\beta-\lambda)\hbar) 
\end{align}$$

Since $c(t+i\lambda\hbar)$ is analytic and integral converges, 

$$\begin{align}
\int_{-\infty}^\infty \mathrm{d}t \,c(t + i\lambda\hbar)
\end{align}$$

is independent of the shift in imaginary time shift $i\lambda\hbar$ (cf. Cauchy's integral theorem). Therefore,

$$\begin{align}
kQ &= \frac{\Delta^2}{\hbar^2}  \int_{-\infty}^\infty \mathrm{d}t \,c(t + i\lambda\hbar)
\end{align}$$

<br>

## References

<sup>1</sup> J. E. Lawrence, and D. E. Manolopoulos, “Analytic continuation of Wolynes theory into the Marcus inverted regime,” [J. Chem. Phys.](https://doi.org/10.1063/1.5002894) **148**, 102313 (2017).





<br>

---
2024.11.16 최예성 작성

