while(1):
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for i in range(0, h):
        for j in range(0, w):
            if i%2 == j%2:
                print('#', end="")
            else:
                print('.', end="")
        print('')
    print('')