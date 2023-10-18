while True:
    str = input()
    if str == "-":
        break
    length = len(str)
    m = int(input())
    start = 0
    for i in range(0,m):
        h = int(input())
        start = (start + h) % length
    print(str[start:], end='')
    print(str[:start])