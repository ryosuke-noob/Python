n, m, l = map(int, input().split())
a = [[0] * m for i in range(0,n)]
b = [[0] * l for i in range(0,m)]
c = [[0] * l for i in range(0,n)]
for i in range(0,n):
    arg = map(int, input().split())
    j = 0
    for x in arg:
        a[i][j] += x
        j += 1
for i in range(0,m):
    arg = map(int, input().split())
    j = 0
    for x in arg:
        b[i][j] += x
        j += 1
for i in range(0,n):
    for j in range(0,l):
        for k in range(0,m):
            c[i][j] += a[i][k] * b[k][j]

for i in range(0,n):
    for j in range(0, l):
        print(c[i][j],end='')
        if j != l-1:
            print(' ', end='')
    print('')