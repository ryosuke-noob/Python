q = int(input())
m = {}
for _ in range(q):
    args = input().split()
    cmd = int(args[0])
    key = str(args[1])
    if cmd == 0:
        x = int(args[2])
        m[key] = x
    if cmd == 1:
        print(m[key])
    # print('[',*m,']')
