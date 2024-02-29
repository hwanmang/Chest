# 필수 라이브러리
'''
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
'''
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)
# DB 기본 코드

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(10000), nullable=False)

    def __repr__(self):
        return f'{self.username} {self.title} 추천 by {self.username}'


with app.app_context():
    db.create_all()

game_flow = {
    'user_win': 0,
    'computer_win': 0,
    'draw': 0
}


@app.route("/")
def home():
    name = '양승조'
    motto = "행복해서 웃는게 아니라 웃어서 행복합니다."

    context = {
        "name": name,
        "motto": motto,
    }
    return render_template('motto.html', data=context)


@app.route("/music/")
def music():
    song_list = Song.query.all()
    return render_template('music.html', data=song_list)


@app.route("/music/<username>")
def render_music_filter(username):
    filter_list = Song.query.filter_by(username=username).all()
    return render_template('music.html', data=filter_list)


@app.route("/iloveyou/<name>/")
def iloveyou(name):
    motto = f"{name}야 난 너뿐이야!"

    context = {
        'name': name,
        'motto': motto,
    }
    return render_template('motto.html', data=context)


@app.route("/music/create")
def music_create():
    # form에서 보낸 데이터 받아오기
    username_receive = request.args.get("username")
    title_receive = request.args.get("title")
    artist_receive = request.args.get("artist")
    image_url_receive = request.args.get("image_url")

    # 데이터를 DB에 저장하기
    song = Song(username=username_receive, title=title_receive,
                artist=artist_receive, image_url=image_url_receive)
    db.session.add(song)
    db.session.commit()
    return redirect(url_for('render_music_filter', username=username_receive))


@app.route('/game/')
def game():
    return render_template('game.html', game_flow=game_flow)


@app.route('/game/play/', methods=['POST'])
def game_play():
    choice = request.form.get('choice')
    computer_choice = random.choice(['가위', '바위', '보'])
    result = ""

    if (choice in ['가위', 'scissor'] and computer_choice in ['보', 'paper']) or \
        (choice in ['바위', 'rock'] and computer_choice in ['가위', 'scissor']) or \
            (choice in ['보', 'paper'] and computer_choice in ['바위', 'rock']):
        game_flow['user_win'] += 1
        result = "사용자 승리!"
    elif choice == computer_choice:
        game_flow['draw'] += 1
        result = "무승부!"
    else:
        game_flow['computer_win'] += 1
        result = "컴퓨터 승리!"

    return render_template('game.html', choice=choice, computer_choice=computer_choice, result=result, game_flow=game_flow)


if __name__ == "__main__":
    app.run(debug=True)
