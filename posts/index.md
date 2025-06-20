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


# 글


## 2025


[19.](https://ysch0i.github.io/posts/19/) Fourier Transform with Quantum Computer II

[18.](https://ysch0i.github.io/posts/18/) Quantum Logic Gate

[17.](https://ysch0i.github.io/posts/17/) 다시 Github으로 

[16.](https://ysch0i.github.io/posts/16/) Fourier Transform with Quantum Computer I

[15.](https://ysch0i.github.io/posts/15/) Density Matrix II

[14.](https://ysch0i.github.io/posts/14/) 뭔가 이렇게 6년이 반복될듯



## 2024

[13.](https://ysch0i.github.io/posts/12/) Density Matrix I

[12.](https://ysch0i.github.io/posts/13/) Marcus Theory Formalism

[11.](https://ysch0i.github.io/posts/11/) Marcus–Hush–Chidsey Theory

[10.](https://ysch0i.github.io/posts/10/) Green Function

[9.](https://ysch0i.github.io/posts/9/) Fermi’s Golden Rule II

[8.](https://ysch0i.github.io/posts/8/) Scattering State

[7.](https://ysch0i.github.io/posts/7/) Born–Oppenheimer Approximation

[6.](https://ysch0i.github.io/posts/6/) Fermi’s Golden Rule I

[5.](https://ysch0i.github.io/posts/5/) Time-dependent Pertubation

[4.](https://ysch0i.github.io/posts/4/) Basic Formulas

[3.](https://ysch0i.github.io/posts/3/) Potential of an Electrode

[2.](https://ysch0i.github.io/posts/2/GammaFunction) Gamma function

[1.](https://ysch0i.github.io/posts/1/Start) 블로그 시작


---

<div id="footer"></div>
<script>
  fetch('https://ysch0i.github.io/footer.html')
    .then(res => res.text())
    .then(html => {
      document.getElementById('footer').innerHTML = html;
    });
</script>


</div>