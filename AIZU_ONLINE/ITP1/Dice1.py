a, b, c, d, e, f = map(int, input().split())
command = input()
for ch in command:
    if ch == 'N':
        tmp = a
        a = b
        b = f
        f = e
        e = tmp
    elif ch == 'S':
        tmp = a
        a = e
        e = f
        f = b
        b = tmp
    elif ch == 'E':
        tmp = a
        a = d
        d = f
        f = c
        c = tmp
    elif ch == 'W':
        tmp = a
        a = c
        c = f
        f = d
        d = tmp
print(a)