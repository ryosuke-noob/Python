a, b, c, d, e, f = input().split()
casea = d+b+c+e+d
caseb = a+d+f+c+a
casec = a+b+f+e+a
cased = a+e+f+b+a
casee = a+c+f+d+a
casef = b+d+e+c+b
q = int(input())
for _ in range(0,q):
    up, front = input().split()
    arg = up + front
    if arg in casea:
        print(a)
    if arg in caseb:
        print(b)
    if arg in casec:
        print(c)
    if arg in cased:
        print(d)
    if arg in casee:
        print(e)
    if arg in casef:
        print(f)