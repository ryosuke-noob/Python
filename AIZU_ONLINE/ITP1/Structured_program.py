n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0:
        print('', i, end='')
    elif i % 10 == 3:
        print('', i, end='')
    else:
        tmp = i
        while(i / 10 != 0):
            i = int(i/10)
            if i % 10 == 3:
                print('', tmp, end='')
                break
print('')