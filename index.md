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

# 예성 블로그~


<div style="display: flex; align-items: flex-start; gap: 20px;">
  
  <!-- 왼쪽: 사진 (테두리 있음) -->
  <img src="https://ysch0i.github.io/images/yeseong2.jpeg"  width="150" style="border: 2px solid #ccc; border-radius: 8px;" />

  <!-- 오른쪽: 테두리 없는 표 (셀 간의 테두리 제거) -->
  <table style="border-collapse: collapse; font-size: 14px;">
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">이름</td>
      <td style="padding: 4px 8px; border: none;">최예성 / Yeseong Choi / 崔睿成 / <a href="https://orcid.org/0009-0004-7409-1352" target="_blank"><img src="https://ysch0i.github.io/images/ORCID-iD_icon_vector.svg" alt="ORCID iD" style="width: 16px; height: 16px; vertical-align: text-bottom;" /> 0009-0004-7409-1352</a></td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">얼굴</td>
      <td style="padding: 4px 8px; border: none;">왼쪽 혹은 <a href="https://ysch0i.github.io/images/yeseong.jpg">증명사진</a> </td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">연락처</td>
      <td style="padding: 4px 8px; border: none;"><a href="mailto:yeseong@snu.ac.kr">yeseong@snu.ac.kr</a></td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">생일</td>
      <td style="padding: 4px 8px; border: none;">2002.05.08</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">평균 위치</td>
      <td style="padding: 4px 8px; border: none;">대전</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">소속</td>
      <td style="padding: 4px 8px; border: none;">
        한국과학기술원 <a href="https://www.m-design-lab.net/">엠디자인 연구실</a>
      </td>
    </tr>
  </table>

</div>

<br>


예성 블로그에 오신 것을 환영합니다. 이 블로그는 저의 일상과 관심 분야를 담고 있습니다.


<br>

<img src="https://ysch0i.github.io/images/namd.svg" width="550px" style="display: block; margin: 0 auto;"/>

<br>
<br>

---

2025.05.13 마지막 수정

<div id="footer"></div>
<script>
  fetch('https://ysch0i.github.io/footer.html')
    .then(res => res.text())
    .then(html => {
      document.getElementById('footer').innerHTML = html;
    });
</script>

</div>

