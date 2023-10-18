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
        if A[args[i][1]]:
            length = len(A[args[i][1]])
            if length == 0:
                print('')
                continue
            for i, num in enumerate(A[args[i][1]]):
                print(num, end='')
                if i != length - 1:
                    print(' ', end='')
        print('')            
    else:
        if A[args[i][1]]:
            if A[args[i][2]]:
                if len(A[args[i][1]]) == 1:
                    A[args[i][2]].append(A[args[i][1]][0])
                elif len(A[args[i][2]]) == 1:
                    A[args[i][1]].appendleft(A[args[i][2]][0])
                    A[args[i][2]] = A[args[i][1]]
                else:
                    A[args[i][2]].extend(A[args[i][1]])
            else:
                A[args[i][2]] = A[args[i][1]]
            A[args[i][1]] = deque()
