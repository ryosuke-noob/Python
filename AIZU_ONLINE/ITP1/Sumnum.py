while(1):
    arg = input()
    if arg[0] == '0':
        break
    sum = 0
    for c in arg:
        sum += int(c)
    print(sum)
