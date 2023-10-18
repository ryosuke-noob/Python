r, c = map(int, input().split())
grid = [[0] * (c + 1) for i in range(0,r + 1)]
sum = 0
for i in range(0, r):
    arg = map(int, input().split())
    j = 0
    for k in arg:
        grid[i][j] += k
        grid[r][j] += k
        grid[i][c] += k
        sum += k
        j += 1
grid[r][c] += sum
for i in range(0,r+1):
    for j in range(0, c+1):
        print(grid[i][j],end='')
        if j != c:
            print(' ', end='')
    print('')
