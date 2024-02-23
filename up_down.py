import random


def up_down():
    while True:
        random_number = random.randint(1, 100)
        num = ""
        step = 0

        while num != random_number:
            try:
                num = int(input("숫자를 입력하세요: "))
                if 1 > num or num > 100:
                    print("유효한 범위 내의 숫자를 입력해주세요 (1 ~ 100)")
                    continue
            except:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")
                continue

            step += 1

            if num < random_number:
                print("업!")
            elif num > random_number:
                print("다운!")
            else:
                print(f"정답입니다! {random_number}이었습니다.")
                print(f"시도 횟수: {step}")

        while True:
            play_again = input("다시 하시겠습니까? (y/n): ")
            if play_again.lower() == "y":
                print(f"이전 게임 플레이어 최고 시도 횟수: {step}")
                break
            elif play_again.lower() == "n":
                break
            else:
                print("유효한 입력이 아닙니다.")
                continue

        if play_again.lower() == "n":
            print("게임을 종료합니다")
            break


up_down()
