from collections import deque

n = int(input())
Q = deque()
for i in range(n):
    lst = list(input().split())
    cmd = lst[0]
    if len(lst) == 2:
        key = lst[1]

    if cmd == "insert":
        Q.appendleft(key)
    elif cmd == "delete":
        if key in Q:
            Q.remove(key)
    elif cmd == "deleteFirst":
        Q.popleft()
    else:
        Q.pop()
print(*Q)