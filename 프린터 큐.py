from collections import deque

for tc in range(int(input())):  # 테스트케이스 수만큼
    n, m = map(int, input().split())  # 문서 개수, 궁금한 문서가 몇 번째에 놓여있는지
    data = list(map(int, input().split()))  # 중요도
    q = deque(data)  # 큐에 중요도 삽입
    count = 0  # 몇 번째로 인쇄되는지 count할 변수
    while q:
        max_value = max(q)  # 큐의 원소들 중 가장 큰 값
        now = q.popleft()  # 큐에서 삭제된 가장 왼쪽 원소
        m -= 1             # 큐에서 원소가 삭제되면 index가 앞으로 밀림

        if now == max_value:  # 만약 삭제된 값이 max 값이라면
            count += 1       # 인쇄 순서 증가시켜줌
            if m < 0:        # 만약 index가 0보다 작다면 (궁금한 원소라면)
                print(count)  # 순서 출력
                break

        if now != max_value:  # 만약 삭제된 값이 max 값이 아니라면
            q.append(now)    # 큐의 맨 오른쪽에 다시 삽입
            if m < 0:          # 만약 index가 0보다 작다면
                m = len(q) - 1  # 큐의 길이에서 1을 뺀 수로 index 지정
