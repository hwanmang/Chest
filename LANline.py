k, n = map(int, input().split())
# lan = []
# for _ in range(k):
#     lan.append(int(input()))
lan = [int(input()) for _ in range(k)]
start = 1
end = max(lan)

# 이분탐색
while (start <= end):
    mid = (start+end)//2
    cnt = 0
    for i in lan:
        cnt += i//mid
    if cnt >= n:  # 자른 개수가 많으면 -> 더 크게잘라야함
        start = mid+1
    else:
        end = mid-1
print(end)
