while 1:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    count = 0
    for i in range(1, min(n + 1, int(x / 3 + 1))):
        for j in range(i + 1, min(n + 1, int(x / 2 + 1))):
            if i + j > x:
                break
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    # print(i, j, k)
                    count += 1
                    break
    print(count)
