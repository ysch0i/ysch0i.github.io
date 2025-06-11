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


# 제목

<div id="utterances-comments"></div>

내용을 써보자.


<script>
  const utterancesScript = document.createElement('script');
  utterancesScript.src = 'https://utteranc.es/client.js';
  utterancesScript.repo = 'ysch0i/ysch0i.github.io';
  utterancesScript.setAttribute('issue-term', 'pathname');
  utterancesScript.setAttribute('theme', 'github-light');
  utterancesScript.setAttribute('label', 'comment');
  utterancesScript.crossOrigin = 'anonymous';
  utterancesScript.async = true;

  document.getElementById('utterances-comments').appendChild(utterancesScript);
</script>



<br>

---

2025.06.11 최예성 작성
<div id="footer"></div>
<script>
  fetch('https://ysch0i.github.io/footer.html')
    .then(res => res.text())
    .then(html => {
      document.getElementById('footer').innerHTML = html;
    });
</script>
</div>