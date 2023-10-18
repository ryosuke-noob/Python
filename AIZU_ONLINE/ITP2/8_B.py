from bisect import bisect_left, bisect_right, insort_left

q = int(input())
m = {}
for _ in range(q):
    args = input().split()
    cmd = int(args[0])
    if cmd == 0:
        key = str(args[1])
        x = int(args[2])
        m[key] = x
    if cmd == 1:
        key = str(args[1])
        if key in m:
            print(m[key])
        else:
            print(0)
    if cmd == 2:
        key = str(args[1])
        if key in m:
            del m[key]
    if cmd == 3:
        l = str(args[1])
        r = str(args[2])
        
