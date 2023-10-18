n, m = map(int, input().split())
a = [[0] * m for i in range(0,n)]
b = [0] * m
ans = [0] * n
for i in range(0,n):
    arg = map(int , input().split())
    j = 0
    for x in arg:
        a[i][j] += x
        j += 1
for j in range(0,m):
    b[j] = int(input())
# print(a)
# print(b)

for i in range(0,n):
    for j in range(0,m):
        ans[i] += a[i][j] * b[j]
    print(ans[i])