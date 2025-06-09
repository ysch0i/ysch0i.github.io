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
  <style>
    iframe[data-cusdis-iframe] {
      height: 1000px !important; /* 댓글 수에 따라 조절 */
      overflow: visible !important;
      width: 100% !important;
      border: none;
    }
  </style>
</head>

<div class="centered-container">

<div id="header"></div>



<br>


# 방명록

<div id="cusdis_thread"
  data-host="https://cusdis.com"
  data-app-id="ba6ab1bb-9ca6-4f9e-aa64-20655316acce"
  data-page-id="guestbook"
  data-page-url="https://ysch0i.github.io/guestbook"
  data-page-title="Guestbook"
></div>
<script async defer src="https://cusdis.com/js/cusdis.es.js"></script>










<br>

---

<footer class="site-footer"></footer>


</div>