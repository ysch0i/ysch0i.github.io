# Exact Reaction Rate Coefficient

## 1. Describing Reaction

$$\begin{align}
k = \frac{1}{2\pi\hbar Q} \int_0^\infty \mathrm{d}E \, e^{-\beta E} |T(E)|^2
\end{align}$$

where $Q$ is reactant partition function, and

$$\begin{align}
|T(E)|^2 = 2\pi\hbar \frac{m}{p} \braket{\psi_p|F(s)|\psi_p}
\end{align}$$

Note that $\braket{\psi_p|F(s)|\psi_p}$ is independent of $s$ and $p^2 = 2mE$. Then,

$$\begin{align}
kQ &= \int_0^\infty \mathrm{d}E \, e^{-\beta E}\frac{m}{p} \braket{\psi_p|F|\psi_p} \\
&= \int_0^\infty \mathrm{d}E \, \frac{m}{p} \braket{\psi_p|e^{-(\beta - \lambda) E}Fe^{-\lambda E}|\psi_p} \,\,\,\,(\text{indep of }\lambda)\\
&= \int_0^\infty \mathrm{d}p \,\braket{\psi_p|e^{-(\beta - \lambda) H}Fe^{-\lambda H}|\psi_p} \\
\end{align}$$

since
$$\begin{align}
\ket{\psi_p} = \Omega_+ \ket{p} = \lim_{t\rightarrow\infty} e^{-iHt/\hbar} e^{iH_0t/\hbar}
\end{align}$$

then

$$\begin{align}
kQ &= \int_{-\infty}^\infty \mathrm{d}p \,\braket{p|\Omega_+^\dag e^{-(\beta - \lambda) H}Fe^{-\lambda H}\Omega_+|p}h(p) \\
&=\int_{-\infty}^\infty \mathrm{d}p \,\braket{p|\Omega_+^\dag e^{-(\beta - \lambda) H}Fe^{-\lambda H}\Omega_+ h(p) |p} \\
&= \text{Tr} \left[ \Omega_+^\dag e^{-(\beta - \lambda) H}Fe^{-\lambda H}\Omega_+ h(p)  \right] \\
&= \text{Tr} \left[  e^{-(\beta - \lambda) H}Fe^{-\lambda H}\Omega_+ h(p) \Omega_+^\dag \right]
\end{align}$$

<br>

## 2. Projection Operator

$h(p)$ is momentum projection operator. However, position projection operator is easier to handle. 

$$\begin{align}
\text{Claim)} \,\,\,\,\,\,h(p) = \lim_{t\rightarrow\infty} e^{-iH_0t/\hbar} h(s-x) e^{iH_0t/\hbar}
\end{align}$$

note that $p$ and $x$ are operator, and $s$ is constant.

First, left hand side

$$\begin{align}
\braket{x|h(p)|x'} &= \int_{-\infty}^\infty \mathrm{d}p\braket{x|p} h(p) \braket{p|x'} \\
&= \frac{1}{2\pi\hbar} \int_{0}^\infty \mathrm{d}p \,e^{ip(x-x')/\hbar}
\end{align}$$

Next, right hand side

$$\begin{align}
\braket{x| e^{-iH_0t/\hbar} h(s-x) e^{iH_0t/\hbar}|x' } = \int_{-\infty}^\infty \mathrm{d}x'' \braket{x |e^{-iH_0t/\hbar} | x'' } h(s-x'') \braket{x'' |e^{iH_0t/\hbar} |x'}
\end{align}$$

since free-particle propagator is,

$$\begin{align}
\braket{x|e^{-iH_0t/\hbar}|x'} = \left(\frac{m}{2\pi i\hbar t}\right)^{1/2} e^{im(x-x')^2/(2\hbar t)}
\end{align}$$

therefore

$$\begin{align}
 \braket{x| e^{-iH_0t/\hbar} h(s-x) e^{iH_0t/\hbar}|x' }  &= \frac{m}{2\pi \hbar t} \int_{-\infty}^\infty \mathrm{d}x''\, e^{im[(x-x'')^2 - (x''-x')^2]/(2\hbar t)} h(s-x'') \\
&= \frac{m}{2\pi \hbar t} e^{im(x+x')(x-x')/(2\hbar t)} \int_{-\infty}^s \mathrm{d}x''\, e^{-imx''(x-x')/(\hbar t)}
\end{align}$$

$$\begin{align}
p = \frac{m(s-x'')}{t}
\end{align}$$

$$\begin{align}
\braket{x| e^{-iH_0t/\hbar} h(s-x) e^{iH_0t/\hbar}|x' }  &= e^{im(x+x')(x-x')/(2\hbar t)} \braket{x|h(p)|x'}
\end{align}$$

$$\begin{align}
\lim_{t\rightarrow\infty} \braket{x| e^{-iH_0t/\hbar} h(s-x) e^{iH_0t/\hbar}|x' }  &= \braket{x|h(p)|x'}
\end{align}$$

complete.

<br>

## 3. Simplify


$$\begin{align}
\Omega_+ h(p) \Omega_+^\dag &= \lim_{t\rightarrow\infty} e^{-iHt/\hbar} e^{iH_0t/\hbar}e^{-iH_0t/\hbar} h(s-x) e^{iH_0t/\hbar}e^{-iH_0t/\hbar}e^{iHt/\hbar} \\
&= \lim_{t\rightarrow\infty} e^{-iHt/\hbar}  h(s-x) e^{iHt/\hbar} \\
&= \lim_{t\rightarrow\infty} e^{-iHt/\hbar} (1- h(x-s)) e^{iHt/\hbar}
\end{align}$$

$$\begin{align}
\text{Tr}\left[ e^{-(\beta - \lambda) H}Fe^{-\lambda H}  \right] &= \int_{-\infty}^\infty \mathrm{d}p \braket{\psi_p | e^{-(\beta - \lambda) H}Fe^{-\lambda H} | \psi_p } \\
&= \int_{-\infty}^\infty \mathrm{d}p \, e^{-\beta p^2 /(2m)} \braket{\psi_p | F | \psi_p } \\
&= 0
\end{align}$$

$$\begin{align}
kQ &= \text{Tr} \left[  e^{-(\beta - \lambda) H}Fe^{-\lambda H}\Omega_+ h(p) \Omega_+^\dag \right] \\
&= -\lim_{t\rightarrow\infty} \text{Tr}\left[  e^{-(\beta - \lambda) H}Fe^{-\lambda H}    e^{-iHt/\hbar}  h(x-s) e^{iHt/\hbar} \right]
\end{align}$$

$k$ is independent of $\lambda$ and $s$. Caution : it's only $t\rightarrow\infty$.

<br>

## 4. Defining Correlation Function

$$\begin{equation}
c_{fs}(t) = \text{Tr} \left[ e^{-\beta H} F  e^{iHt/\hbar} h e^{-iHt/\hbar}   \right]
\end{equation}$$

$$\begin{equation}
c_{ss}(t) = \text{Tr} \left[ e^{-\beta H} h  e^{iHt/\hbar} (1-h) e^{-iHt/\hbar}   \right]
\end{equation}$$

$$\begin{equation}
c_{ff}(t) = \text{Tr} \left[ e^{-\beta H} F  e^{iHt/\hbar} F e^{-iHt/\hbar}   \right]
\end{equation}$$

It's flux-side, side-side, flux-flux correlation function, respectively.

Then,

$$\begin{align}
c_{fs}(t + i\lambda\hbar) &= \text{Tr} \left[ e^{-\beta H} F  e^{iH(t + i\lambda\hbar)/\hbar} h e^{-iH(t + i\lambda\hbar)/\hbar}   \right] \\
&= \text{Tr} \left[ e^{-\beta H} F e^{-\lambda H}  e^{iHt/\hbar} h e^{-iHt/\hbar}  e^{\lambda H} \right] \\
&= \text{Tr} \left[ e^{-(\beta-\lambda) H} F e^{-\lambda H}  e^{iHt/\hbar} h e^{-iHt/\hbar}   \right]
\end{align}$$

Therefore, $k$ can be written using correlation function.

$$\begin{align}
kQ &= -\lim_{t\rightarrow\infty} c_{fs}(-t + i\lambda\hbar)
\end{align}$$

and it't independent of $\lambda$. ($t\rightarrow\infty$ only)

<br>


## 5. Properties of Correlation Function

Derivatives

$$\begin{align}
\frac{\mathrm{d}}{\mathrm{d}t} c_{fs}(t + i\lambda\hbar) &= \frac{\mathrm{d}}{\mathrm{d}t} \text{Tr} \left[ e^{-(\beta-\lambda) H} F e^{-\lambda H}  e^{iHt/\hbar} h e^{-iHt/\hbar}   \right] 
\\
&= \text{Tr} \left[ e^{-(\beta-\lambda) H} F e^{-\lambda H}  e^{iHt/\hbar} \frac{i}{\hbar} Hh e^{-iHt/\hbar}   \right] + \text{Tr} \left[ e^{-(\beta-\lambda) H} F e^{-\lambda H}  e^{iHt/\hbar} h \frac{-i}{\hbar}He^{-iHt/\hbar}   \right]  \\
&= \text{Tr} \left[ e^{-(\beta-\lambda) H} F e^{-\lambda H}  e^{iHt/\hbar} \frac{i}{\hbar}[H,h] e^{-iHt/\hbar}   \right] \\
&= \text{Tr} \left[ e^{-(\beta-\lambda) H} F e^{-\lambda H}  e^{iHt/\hbar} F e^{-iHt/\hbar}   \right] \\
&= c_{ff}(t + i\lambda\hbar)
\end{align}$$

Similary

$$\begin{align}
\frac{\mathrm{d}}{\mathrm{d}t} c_{ss}(t + i\lambda\hbar) = c_{fs}(t + i\lambda\hbar)
\end{align}$$

Complex conjugate

$$\begin{align}
c_{ff}^*(t+i\lambda\hbar) &= c_{ff}(-t+i\lambda\hbar) \\
&= \text{Tr} \left[ e^{-(\beta-\lambda) H} F e^{-\lambda H}  e^{-iHt/\hbar} F e^{iHt/\hbar}   \right] \\
&= \text{Tr} \left[ e^{iHt/\hbar} F e^{-iHt/\hbar}e^{-\lambda H}   F  e^{-(\beta-\lambda) H}   \right] \\
&= \text{Tr} \left[ e^{-\lambda H} F e^{-(\beta-\lambda) H}  e^{iHt/\hbar} F e^{-iHt/\hbar}   \right] \\
&= c_{ff}(t+i(\beta-\lambda)\hbar)
\end{align}$$

Similary

$$\begin{align}
c_{ss}^*(t+i\lambda\hbar) &= c_{ss}(-t+i\lambda\hbar) = c_{ss}(t + i(\beta-\lambda)\hbar)
\end{align}$$

Therefore, for special case $\lambda = \beta/2$ :

$c_{ss}(t+i\beta\hbar/2)$ and $c_{ff}(t+i\beta\hbar/2)$ are real and even function for real $t$, and by Eq (41), $c_{fs}(t+i\beta\hbar/2)$ is real and odd for real $t$ as follows. Also, $c_{fs}(i\beta\hbar/2) = 0$.

Now, let's generlize for arbitrary $\lambda$.

$$\begin{align}
\frac{\mathrm{d}}{\mathrm{d}t} c_{ss}(-t+i\lambda\hbar) &= -c_{fs}(-t+i\lambda\hbar)\\
&= \frac{\mathrm{d}}{\mathrm{d}t} c_{ss}(t + i(\beta-\lambda)\hbar) \\
&= c_{fs}(t+i(\beta-\lambda)\hbar)
\end{align}$$


Recall Eq (35),

$$\begin{align}
\lim_{t\rightarrow\infty} c_{fs}(-t + i\lambda\hbar)
\end{align}$$

is independent of $\lambda$.

<br>

## 6. Rate Coefficient 

$$\begin{align}
kQ &= -\lim_{t\rightarrow\infty} c_{fs}(-t + i\lambda\hbar) \\
&= -\lim_{t\rightarrow\infty} c_{fs}(-t + i (\beta-\lambda) \hbar) \\
&= \lim_{t\rightarrow\infty} c_{fs}(t + i\lambda\hbar) 
\end{align}$$

for any $\lambda$. Further,

$$\begin{align}
\frac{1}{2} \int_{-\infty}^\infty \mathrm{d} t\, c_{ff}(t+i\lambda\hbar) &= \frac{1}{2} \int_{-\infty}^\infty \mathrm{d} t\, \frac{\mathrm{d}}{\mathrm{d}t}c_{fs}(t+i\lambda\hbar) \\
&= \frac{1}{2} \left[\lim_{t\rightarrow\infty} c_{fs}(t + i\lambda\hbar) - \lim_{t\rightarrow-\infty} c_{fs}(t + i\lambda\hbar)\right] \\
&= \frac{1}{2} \left[\lim_{t\rightarrow\infty} c_{fs}(t + i\lambda\hbar) - \lim_{t\rightarrow\infty} c_{fs}(-t + i\lambda\hbar)\right] \\
&= \lim_{t\rightarrow\infty} c_{fs}(t + i\lambda\hbar) \\
&= kQ
\end{align}$$


$$\begin{align}
\therefore kQ = \lim_{t\rightarrow\infty} c_{fs}(t + i\lambda\hbar)= \frac{1}{2} \int_{-\infty}^\infty \mathrm{d} t\, c_{ff}(t+i\lambda\hbar)
\end{align}$$

for any $0\leq\lambda\leq \beta$.







Note that,

$$\begin{align}
c_{fs}(t) \neq c_{fs}(t+i\lambda\hbar)
\end{align}$$

$$\begin{align}
c_{ff}(t) \neq c_{ff}(t+i\lambda\hbar)
\end{align}$$

Only,

$$\begin{align}
\lim_{t\rightarrow\infty}c_{fs}(t) =\lim_{t\rightarrow\infty} c_{fs}(t+i\lambda\hbar)
\end{align}$$

$$\begin{align}
\int_{-\infty}^\infty \mathrm{d} t\,  c_{ff}(t) = \int_{-\infty}^\infty \mathrm{d} t\, c_{ff}(t+i\lambda\hbar)
\end{align}$$



<br>

## References
<sup>1</sup> D. E. Manolopoulos, “Chemical Reaction Dynamics,” [David Manolopoulos Research Group: Chemical Dynamics](http://manolopoulos.chem.ox.ac.uk/) (2008).


<br>

---
2024.11.15 최예성 작성