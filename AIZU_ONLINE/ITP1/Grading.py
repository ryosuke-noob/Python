while 1:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    score = m + f
    if m == -1 or f == -1:
        print('F')
    elif score < 30:
        print('F')
    elif score < 50:
        if r < 50:
            print('D')
        else:
            print('C')
    elif score < 65:
        print('C')
    elif score < 80:
        print('B')
    else:
        print('A')
