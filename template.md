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

내용을 써보자.


<br>

---

2025.06.11 최예성 작성
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