import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = int(input())

    if a > 0:
        # (-a, a)의 튜플 형태로 push하여 pop할 때 1번째 인덱스만 출력하도록
        heapq.heappush(heap, (-a, a))
    elif a == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
