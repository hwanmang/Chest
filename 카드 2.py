from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])

while (len(queue) > 1):
    queue.popleft()
    card = queue.popleft()
    queue.append(card)

print(queue[0])


# from collections import deque

# N = int(input())
# queue = deque(range(1, N + 1))

# while len(queue) > 1:
#     queue.popleft()
#     queue.append(queue.popleft())

# print(queue[0])
