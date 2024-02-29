import random


def play_game():
    user_win = 0
    computer_win = 0
    draw = 0

    while True:
        user = input("가위, 바위, 보 중에서 선택하세요 : ").lower()

        if user not in ['가위', '바위', '보', 'rock', 'scissor', 'paper']:
            print("유효한 입력이 아닙니다.")
            continue

        computer = random.choice(['가위', '바위', '보'])
        print(f"사용자: {user}, 컴퓨터: {computer}")

        if (user in ['가위', 'scissor'] and computer in ['보', 'paper']) or \
           (user in ['바위', 'rock'] and computer in ['가위', 'scissor']) or \
           (user in ['보', 'paper'] and computer in ['바위', 'rock']):
            print("사용자 승리!")
            user_win += 1
        elif user == computer:
            print("무승부!")
            draw += 1
        else:
            print("컴퓨터 승리!")
            computer_win += 1

        play_again = input("다시 하시겠습니까? (y/n): ")
        if play_again.lower() == "y":
            continue
        elif play_again.lower() == "n":
            break
        else:
            break

    print("게임 종료")
    print(f"승: {user_win}")
    print(f"패: {computer_win}")
    print(f"무: {draw}")


play_game()
