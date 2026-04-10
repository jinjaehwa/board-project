# 게시판 프로젝트

파이썬 Flask를 이용해서 만든 게시판입니다.
로그인 기능과 게시글 CRUD 기능을 구현했습니다.

## 사용 기술

- Python, Flask
- HTML, CSS, JavaScript
- SQLite

## 기능

- 회원가입, 로그인, 로그아웃
- 게시글 작성, 수정, 삭제, 조회
- 삭제 시 확인 팝업
- 글자수 실시간 표시

## 파일 구조

```
board_project/
├── frontend/
│   ├── templates/
│   │   ├── base.html          # 공통 레이아웃
│   │   ├── auth/
│   │   │   ├── login.html     # 로그인 페이지
│   │   │   └── register.html  # 회원가입 페이지
│   │   └── post/
│   │       ├── index.html     # 글 목록 페이지
│   │       ├── write.html     # 글쓰기 페이지
│   │       ├── post_detail.html # 글 상세보기 페이지
│   │       └── edit.html      # 글 수정 페이지
│   └── static/
│       ├── css/
│       │   └── style.css      # 스타일시트
│       └── js/
│           └── main.js        # 자바스크립트
├── backend/
│   ├── app.py                 # Flask 앱 설정
│   ├── models.py              # DB 모델
│   └── routes.py              # 페이지 라우팅
├── .gitignore
└── README.md
```

## 실행 방법

pip install flask flask-sqlalchemy flask-login pymysql
python -c "from app import app, db; app.app_context().push(); db.create_all()"
python app.py

http://127.0.0.1:5000 접속