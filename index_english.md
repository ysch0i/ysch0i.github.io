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



# Yeseong's Blog~


<div style="display: flex; align-items: flex-start; gap: 20px;">
  
  <!-- 왼쪽: 사진 (테두리 있음) -->
  <img src="https://ysch0i.github.io/images/yeseong2.jpeg"  width="150" style="border: 2px solid #ccc; border-radius: 8px;" />

  <!-- 오른쪽: 테두리 없는 표 (셀 간의 테두리 제거) -->
  <table style="border-collapse: collapse; font-size: 14px;">
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">Name</td>
      <td style="padding: 4px 8px; border: none;">Yeseong Choi</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">Portrait</td>
      <td style="padding: 4px 8px; border: none;">Left or <a href="https://ysch0i.github.io/images/yeseong.jpg">ID picture</a> </td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">Contact</td>
      <td style="padding: 4px 8px; border: none;"><a href="mailto:yeseong@snu.ac.kr">yeseong@snu.ac.kr</a></td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">Birth</td>
      <td style="padding: 4px 8px; border: none;">2002.05.08</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">Average position</td>
      <td style="padding: 4px 8px; border: none;">Daejeon, Republic of Korea</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border: none;">Affiliation</td>
      <td style="padding: 4px 8px; border: none;">
        <a href="https://www.m-design-lab.net/">M-design Laboratory</a>, Korea Advanced Institute of Science and Technology
      </td>
    </tr>
  </table>

</div>

<br>


Welcome to Yeseong's blog. This blog contains my daily life and areas of interest.


<br>

<img src="https://ysch0i.github.io/images/namd.svg" width="550px" style="display: block; margin: 0 auto;"/>

<br>
<br>

---

Last modified on May 13, 2025

<footer class="site-footer"></footer>











</div>

