<head>
  <meta charset="UTF-8" />
  <link rel="stylesheet" href="https://ysch0i.github.io/style.css" />
  <script>
    window.onload = function() {
      fetch('https://ysch0i.github.io/header_english.html')
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


# Guestbook

<div id="cusdis_thread"
  data-host="https://cusdis.com"
  data-app-id="ba6ab1bb-9ca6-4f9e-aa64-20655316acce"
  data-page-id="guestbook"
  data-page-url="https://ysch0i.github.io/guestbook_english"
  data-page-title="Guestbook"
></div>
<script async defer src="https://cusdis.com/js/cusdis.es.js"></script>


<script>
window.addEventListener('load', function () {
    let iframe = document.querySelector("#cusdis_thread iframe");
    if (iframe) {
        let observer = new MutationObserver(() => {
            let scrollHeight = iframe.contentWindow.document.body.scrollHeight;
            iframe.style.height = scrollHeight + "px";
        });
        observer.observe(iframe.contentWindow.document.body, { childList: true, subtree: true });
    }
});
</script>





<br>

---

<footer class="site-footer"></footer>


</div>