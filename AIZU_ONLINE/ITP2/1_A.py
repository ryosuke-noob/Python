A = []
q = int(input())
for i in range(0,q):
    args = map(int, input().split())
    for arg in args:
        if arg == 0:
            # add element x at the end of A
            A.append(next(args))
        elif arg == 1:
            # print num's element
            print(A[next(args)])
        elif arg == 2:
            # delete the last element of A
            A.pop()

# mapもイテレータであるためnext()で取り出すことができる