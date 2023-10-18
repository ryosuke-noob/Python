from collections import deque

n, q = map(int,input().split())
A = [deque() for _ in range(n)]
args = [[] for i in range(0,q)]
for i in range(0,q):
    args[i] = list(map(int, input().split()))
for i in range(0,q):
    if args[i][0] == 0:
            A[args[i][1]].append(args[i][2])
    elif args[i][0] == 1:
         length = len(A[args[i][1]])
         if length == 0:
            continue
         print(A[args[i][1]][0])
    else:
        length = len(A[args[i][1]])
        if length == 0:
            continue
        A[args[i][1]].popleft()
