from collections import deque

N = int(input())

packets = []
while True:
    packet = int(input())
    if packet == -1:  # 입력의 끝을 나타내는 -1이 입력될 때까지 반복
        break
    packets.append(packet)
