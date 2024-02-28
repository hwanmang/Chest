from flask import Flask, render_template, request
import random

app = Flask(__name__)

game_flow = {
    'user_win': 0,
    'draw': 0,
    'computer_win': 0
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    result = ""

    computer_choice = random.choice(['가위', '바위', '보'])
    choice = request.form.get('choice')
    if (choice in ['가위', 'scissor'] and computer_choice in ['보', 'paper']) or \
        (choice in ['바위', 'rock'] and computer_choice in ['가위', 'scissor']) or \
            (choice in ['보', 'paper'] and computer_choice in ['바위', 'rock']):
        result = "사용자 승리!"
        game_flow['user_win'] += 1
    elif choice == computer_choice:
        result = "무승부!"
        game_flow['draw'] += 1
    else:
        result = "컴퓨터 승리!"
        game_flow['computer_win'] += 1
    return render_template('index.html', choice=choice, computer_choice=computer_choice,
                           game_flow=game_flow, result=result)


if __name__ == '__main__':
    app.run()
