from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# 비밀키 - 로그인 세션 암호화할 때 씀
app.config['SECRET_KEY'] = 'mysecretkey'

# DB 설정 (SQLite - 설치 필요 없음)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///board.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from routes import *

if __name__ == '__main__':
    app.run(debug=True)