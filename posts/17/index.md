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


# 다시 Github으로 

아무래도 난 github이 제일 편하다. 노션은 음... 정이 안간다.


이번에 다시 github으로 오면서 방명록과 댓글 기능을 만들었다.


<br>

방명록은 누구나 작성할 수 있도록 cusdis를 이용해 만들었다. 로그인 없이 작성할 수 있다.

이메일을 넣는 칸이 있는데, 여기 이메일을 넣어도 내가 볼 수는 없다. 왜 있는걸까.


<br>

댓글 기능도 cusdis를 이용해 만들고 싶었지만, 아쉽게도 cusdis는 페이지 1개까지만 무료라고 한다. 

그래서 댓글 기능은 utterances를 이용해 만들었다. Utterances는 github 계정이 있어야만 댓글을 작성할 수 있다. 




<br>

---

2025.06.16 최예성 작성




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