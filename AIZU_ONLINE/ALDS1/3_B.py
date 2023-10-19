from collections import deque

n, q = map(int, input().split())
Q = deque()
for i in range(n):
    lst = list(input().split())
    Q.append([lst[0], int(lst[1])])

sum_time = 0
qlen = len(Q)
while qlen > 0:
    lst = Q.popleft()
    if lst[1] <= q:
        print(lst[0], sum_time + lst[1])
        qlen -= 1
        sum_time += lst[1]
    else:
        Q.append(lst)
        lst[1] -= q
        sum_time += q
