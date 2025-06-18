# Reaction Rate Coefficient Formulas

책마다, 논문마다 notation이 달라서 정리해본다.

<br>
David E. Manolopoulos : Chemical Reaction Dynamics (Lecture note)
  
$$\begin{equation}
k(T) = \frac{1}{2\pi\hbar Q_r(T)} \int_0^\infty \mathrm{d}E e^{-\beta E}N(E)
\end{equation}$$
$$\begin{equation}
Q_r(T) = \frac{1}{\Lambda(T)} = \left( \frac{2\pi m k_\text{B}T}{h^2} \right)^{1/2} = \left( \frac{m}{2\pi\beta\hbar^2}  \right)^{1/2}
\end{equation}$$

$$\begin{equation}
N(E) = |T(E)|^2
\end{equation}$$

$$\begin{equation}
F = \frac{i}{\hbar} [H,h]
\end{equation}$$


$$\begin{equation}
c_{fs}(t) = \text{Tr} \left[ e^{-\beta H/2} F e^{-\beta H/2} e^{iHt/\hbar} h e^{-iHt/\hbar}   \right]
\end{equation}$$

$$\begin{equation}
c_{ss}(t) = \text{Tr} \left[ e^{-\beta H/2} h e^{-\beta H/2} e^{iHt/\hbar} (1-h) e^{-iHt/\hbar}   \right]
\end{equation}$$

$$\begin{equation}
c_{ff}(t) = \text{Tr} \left[ e^{-\beta H/2} F e^{-\beta H/2} e^{iHt/\hbar} F e^{-iHt/\hbar}   \right]
\end{equation}$$

$$\begin{equation}
k(T)Q_r(T) = \lim_{t \rightarrow \infty} \frac{\mathrm{d}}{\mathrm{d}t}c_{ss}(t) = \lim_{t \rightarrow \infty} c_{fs}(t) = \int_0^\infty \mathrm{d}t \, c_{ff}(t)
\end{equation}$$



<br>

*J. Chem. Phys.* 110, 5307–5317 (1999) [DOI](https://doi.org/10.1063/1.478425)

$$\begin{equation}
k = \Delta^2 \int_{-\infty}^{\infty} \mathrm{d}t\braket{e^{iH_1t/\hbar}e^{-iH_2t/\hbar}}
\end{equation}$$

$$\begin{equation}
\braket{...} = \frac{\text{Tr}[... e^{-\beta H_1}]}{\text{Tr}[e^{-\beta H_1}]}
\end{equation}$$

<br>

## References


<sup>1</sup> D. E. Manolopoulos, “Chemical Reaction Dynamics,” [David Manolopoulos Research Group: Chemical Dynamics](http://manolopoulos.chem.ox.ac.uk/) (2008).

<sup>2</sup> Y. Georgievskii, C.-P. Hsu, and R. A. Marcus, “Linear response in theory of electron transfer reactions as an alternative to the molecular harmonic oscillator model,” [J. Chem. Phys.](https://doi.org/10.1063/1.478425) **110**, 5307–5317 (1999).

<br>

---
2024.11.12 최예성 작성