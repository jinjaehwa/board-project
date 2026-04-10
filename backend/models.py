from app import db
from flask_login import UserMixin

# 회원 테이블
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)  # 아이디
    password = db.Column(db.String(200), nullable=False)              # 비밀번호
    posts = db.relationship('Post', backref='author', lazy=True)

# 게시글 테이블
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)                 # 제목
    content = db.Column(db.Text, nullable=False)                      # 내용
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))         # 작성자