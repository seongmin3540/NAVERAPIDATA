# 프로젝트 개요
- 해당 프로젝트에서는 네이버 API를 활용하여 API에 대한 이해도를 높임과 동시에 데이터를 시각화함.

# 프로젝트 기본 구조
📂 my_project/

├── 📁 scripts/ → 데이터 크롤링 및 분석 코드 (필요조건 X)

├── 📁 static/ → 시각화 관련 파일 (JS, CSS) + 필요 icon

├── 📁 templates/ → 웹 페이지 템플릿 (HTML, Jinja2)

├── 📄 app.py → Flask 웹 서버 (backend)

└── 📄 requirements.txt → 프로젝트 설명 + 필요한 패키지 목록

# 프로젝트 주요 기능
1. 네이버 검색어 데이터 수집 (네이버 검색 API)  
2. 웹 대시보드 구현 (Flask + HTML/CSS + JS)

# 개인 desktop 에서 실행시 
1. app.py 실행
2. http://127.0.0.1:5000 접속

# 배포
- Flask(API 서버)는 Render, Railway, Heroku 등에 배포  
- Netlify는 정적 HTML, CSS, JS 파일만 배포  
- Netlify 프론트엔드에서 Flask 서버 URL로 API 요청 전송  

