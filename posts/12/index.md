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


# Density Matrix


수정중

## References



$^1$ R. P. Feynman, *Statistical Mechanics: A Set of Lectures*, 19. printing (Addison-Wesley, Reading, Mass., 1996).

$^2$ R. P. Feynman, A. R. Hibbs, and D. F. Styer, *Quantum Mechanics and Path Integrals*, Emended ed (Dover publ, Mineola, 2010).

$^3$ Y. Baek, "Statistical Mechanics: Lecture Notes" (2024).

$^4$ Y. Jung, "Applied Computational Chemistry: Lecture Notes" (2023).

<br>

---

2024.12.26 최예성 작성.

<footer class="site-footer"></footer>


</div>